# safrapay

## Quick Reference

**SafraPay** integration workspace. The versioned deliverable is `openapi/openapi.yaml` — an **UNOFFICIAL** OpenAPI 3.1 spec for the SafraPay API, split into `openapi/{paths,components/schemas,components/security-schemes}/` following [Redocly's own multi-file convention](https://github.com/Redocly/openapi-starter) (with the security schemes dir kept kebab-case) — plus the tooling to work with it.

```bash
mise install                             # toolchain: python 3.12, jq, yq, node 22
mise run setup                           # create .env + install requirements.txt into .venv
.venv/bin/python3 script.py              # run Python scripts (always via .venv)
npm install                              # once, installs @redocly/cli + orval + tsx
npm run lint                             # OpenAPI lint (redocly.yaml points at openapi/openapi.yaml)
```

## Architecture

- **`openapi/`** — the only versioned source. OpenAPI 3.1 spec (56 paths, 12 tag groups), reverse-engineered from the SafraPay developer portal, split into `openapi.yaml` (entrypoint: info/servers/tags + `$ref` maps), `paths/` (one file per path, filename = path with `/`→`_`, braces kept verbatim), `components/schemas/` (one file per `components.schemas` entry), `components/security-schemes/` (one file per `components.securitySchemes` entry — dir name kebab-case by request, the OpenAPI keyword itself stays `securitySchemes`). This is what the repo delivers. Built with `tools/split_openapi.py <source.yaml>` (one-off migration script, safe to rerun against a flat snapshot if the tree ever needs rebuilding).
- **`generated/`** — build output, **git-ignored** entirely, regenerate on demand: `generated/docs/index.html` (static HTML API reference, `npm run docs:build`) and `generated/node/` (Node/TS client, `npm run generate:client` — bundles the spec then runs Orval; plain `fetch`-based functions, no custom mutator, no baked-in base URL). There is no generated Python client.
- **Python scripts** — process files and call the SafraPay API. Ad hoc and **not versioned**; deps in `requirements.txt`, run via `.venv/bin/python3`.
- **Secrets vs. environment** — `.env` (real, ignored) holds secrets; `.env.hml`/`.env.prd` (versioned) hold only non-sensitive endpoints; `.env.example` documents the secrets.
- **`.data/`** — git-ignored scratch dump for raw inputs (holds PII). Not part of the deliverable; do not treat its contents as project structure and never commit it.

## Conventions

- Tools and virtualenv always via **mise**; Python always via `.venv/bin/python3`; node tooling always via the root `package.json` (`npm run <script>`), not raw `npx` one-offs.
- New secret variables: document them in `.env.example` (no value); URLs/environment go in `.env.hml`/`.env.prd`.
- SafraPay transaction IDs are UUIDs; API monetary values are in **cents** (e.g. `15550` = R$ 155.50).

## Workflow

- Non-trivial tasks (new script, spec changes): start in **Plan mode** and agree on the approach before implementing.
- When editing the spec, preserve the existing structure (tags, `operationId`, servers) and validate afterward.
- A schema referencing another schema uses a relative file `$ref` (e.g. `./CardBrand.yaml`), never `#/components/schemas/X` — that only resolves within a single file, and these are split across `openapi/components/schemas/*.yaml`. Same idea for a path referencing a schema: `../components/schemas/X.yaml`.
- Break large changes into small, verifiable chunks.

## Verification

Run after any relevant change to the spec:

```bash
yq . openapi/openapi.yaml > /dev/null                              # 1. entrypoint parses as YAML
for f in openapi/paths/*.yaml openapi/components/schemas/*.yaml openapi/components/security-schemes/*.yaml; do
  yq . "$f" > /dev/null || echo "BROKEN: $f"
done                                                                # 2. every split file parses
npx @redocly/cli bundle openapi/openapi.yaml -o /dev/null          # 3. every cross-file $ref resolves (yq alone won't catch a dangling ref)
npm run lint                                                        # 4. OpenAPI lint
.venv/bin/python3 -c "import ast,sys; ast.parse(open(sys.argv[1]).read())" <script>  # 5. Python compiles
npx tsx tests/generated_node/smoke.ts                               # 6. after `npm run generate:client`, if the Node client shape changed
```

Scripts that hit the API: run against **homologation** (`.env.hml`), never production, when testing.

## Deep Dive (read on demand)

- SafraPay auth: `POST /v2/merchant/auth` (MerchantToken) → `accessToken` JWT (~30 min) as `Bearer`; refresh via `POST /v2/refreshtoken`.
- Servers: `https://payment.safrapay.com.br` (prod), `https://payment-hml.safrapay.com.br` (homologation).

## Critical rules

- **IMPORTANT: NEVER** commit, log, or send to external services the contents of `.env` (secrets) or `.data/` (customer PII). Both are git-ignored — keep it that way.
- **IMPORTANT:** `openapi/openapi.yaml` is **unofficial** (reverse-engineered). Do not state SafraPay guarantees based on it.
- **YOU MUST** test API calls against homologation before production; payment/refund side effects are real money.

## Learnings

<!-- Living section — update after corrections and reviews. Format: YYYY-MM-DD: learning. -->

- 2026-07-07: the `openapi/` split was first built ad hoc (top-level `schemas/`+`security-schemas/`, prefix-grouped path files), then rebuilt to follow Redocly's own `openapi-starter` convention (`components/schemas/`, `components/securitySchemes/`, one file per path) — then the security-schemes dir was renamed back to kebab-case (`components/security-schemes/`) by explicit request, landing on a hybrid: Redocly's nesting/path-filename convention, but kebab-case for that one directory. The OpenAPI keyword itself (`components.securitySchemes` in the YAML) is unaffected either way — only the directory name changed.
- 2026-07-07: Orval's plain-`fetch` output (no custom mutator) does not account for per-operation `servers:` overrides — it only ever emits the raw OpenAPI path template. Chargeback's operations (and v1 Autenticação) have a `servers:` override adding a `/chargeback` path prefix on top of the host; callers of the generated client must add that prefix manually. A mutator that varies the base path per operation would fix this but was judged not worth the added complexity for a spec/tooling workspace with no shared consuming app (unlike `web-app/packages/api`, which has one).

## Gotchas

- `.data/` is fully git-ignored; new files there are not tracked by default. `.claude/` is versioned except `.claude/settings.local.json` (personal permission overrides, gitignored).
