#!/usr/bin/env python3
"""One-off migration: split the monolithic openapi.yaml into openapi/{paths,components}.

Follows Redocly's own multi-file convention (github.com/Redocly/openapi-starter),
with one deliberate deviation (kebab-case security schemes dir, per explicit request):
paths/<path with '/'->'_', braces kept>.yaml, components/schemas/<Name>.yaml,
components/security-schemes/<Name>.yaml, all referenced from openapi/openapi.yaml
via whole-file $refs (no JSON-pointer fragments).

Usage: .venv/bin/python3 tools/split_openapi.py <source.yaml>
Writes the openapi/ tree next to this repo's root. Does not touch the source file.
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "openapi"

SCHEMA_REF_RE = re.compile(r"^#/components/schemas/(.+)$")


# PyYAML's own (YAML 1.1) resolver is more lenient than the other YAML parsers this
# repo actually feeds (yq/go-yaml for validation, redocly's js-yaml for lint/bundle,
# snakeyaml in Orval's generated-client toolchain): it happily leaves e.g. '09' or
# '01234567891' unquoted because *its* implicit-int regex rejects them, but those other
# parsers' regexes accept them and silently reinterpret as a number, dropping leading
# zeros. Force-quote anything that looks numeric (or a YAML 1.1 bool/null keyword) so the
# round-trip is safe across all consumers, not just PyYAML itself.
_LOOKS_NUMERIC_RE = re.compile(r"^[+-]?[0-9]+(\.[0-9]+)?$")
_YAML_KEYWORDS = {
    "true", "false", "null", "yes", "no", "on", "off", "~",
}


def _str_presenter(dumper, data):
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    if _LOOKS_NUMERIC_RE.match(data) or data.lower() in _YAML_KEYWORDS:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="'")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


yaml.add_representer(str, _str_presenter, Dumper=yaml.SafeDumper)


def dump(obj):
    return yaml.safe_dump(obj, sort_keys=False, allow_unicode=True, default_flow_style=False, width=100000)


def rewrite_refs(node, replacement_prefix):
    """Recursively rewrite '#/components/schemas/X' refs to '<replacement_prefix>X.yaml'."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "$ref" and isinstance(v, str):
                m = SCHEMA_REF_RE.match(v)
                if m:
                    node[k] = f"{replacement_prefix}{m.group(1)}.yaml"
                    continue
            rewrite_refs(v, replacement_prefix)
    elif isinstance(node, list):
        for v in node:
            rewrite_refs(v, replacement_prefix)


def path_filename(path):
    """'/v2/charge/{chargeId}' -> 'v2_charge_{chargeId}' (Redocly starter convention)."""
    return path.strip("/").replace("/", "_")


def main():
    if len(sys.argv) != 2:
        sys.exit(f"usage: {sys.argv[0]} <source-openapi.yaml>")
    src = Path(sys.argv[1])
    data = yaml.safe_load(src.read_text())

    (OUT / "paths").mkdir(parents=True, exist_ok=True)
    (OUT / "components" / "schemas").mkdir(parents=True, exist_ok=True)
    (OUT / "components" / "security-schemes").mkdir(parents=True, exist_ok=True)

    # --- schemas ---
    schema_names = list(data["components"]["schemas"].keys())
    for name in schema_names:
        schema = data["components"]["schemas"][name]
        rewrite_refs(schema, "./")
        (OUT / "components" / "schemas" / f"{name}.yaml").write_text(dump(schema))

    # --- security schemes (dir is kebab-case per explicit request; the OpenAPI
    # keyword itself, components.securitySchemes, stays camelCase in the YAML) ---
    scheme_names = list(data["components"]["securitySchemes"].keys())
    for name in scheme_names:
        scheme = data["components"]["securitySchemes"][name]
        (OUT / "components" / "security-schemes" / f"{name}.yaml").write_text(dump(scheme))

    # --- paths, one file per path ---
    source_paths = list(data["paths"].keys())
    filenames = [path_filename(p) for p in source_paths]
    if len(set(filenames)) != len(filenames):
        dupes = {f for f in filenames if filenames.count(f) > 1}
        sys.exit(f"path_filename collision(s): {dupes}")

    for path in source_paths:
        item = data["paths"][path]
        rewrite_refs(item, "../components/schemas/")
        (OUT / "paths" / f"{path_filename(path)}.yaml").write_text(dump(item))

    # --- root entrypoint ---
    root = {}
    for key in ("openapi", "info", "externalDocs", "servers", "tags"):
        if key in data:
            root[key] = data[key]

    root["paths"] = {
        path: {"$ref": f"./paths/{path_filename(path)}.yaml"}
        for path in source_paths
    }

    components = {}
    for key in data["components"].keys():
        if key == "schemas":
            components["schemas"] = {
                name: {"$ref": f"./components/schemas/{name}.yaml"} for name in schema_names
            }
        elif key == "securitySchemes":
            components["securitySchemes"] = {
                name: {"$ref": f"./components/security-schemes/{name}.yaml"} for name in scheme_names
            }
    root["components"] = components

    if "security" in data:
        root["security"] = data["security"]

    (OUT / "openapi.yaml").write_text(dump(root))

    print(f"Wrote {len(schema_names)} schemas, {len(scheme_names)} security schemes, "
          f"{len(source_paths)} path files -> {OUT}")


if __name__ == "__main__":
    main()
