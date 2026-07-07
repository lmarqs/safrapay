# safrapay-integration

**SafraPay** integration workspace.

The versioned artifact of this repo is **`openapi/openapi.yaml`** — an **UNOFFICIAL** OpenAPI 3.1 spec for the SafraPay API, generated from the developer-portal documentation, plus the tooling to work with it.

> ⚠️ The spec is **unofficial** (reverse-engineered from the homologation docs). Treat it as a reference, not as a contract guaranteed by SafraPay.

## What's here

```
.
├── openapi/               # SafraPay API OpenAPI 3.1 spec (unofficial) — the deliverable
│   ├── openapi.yaml           # entrypoint: info/servers/tags + $ref maps into paths/ and components/
│   ├── paths/                  # one file per path (e.g. v2_charge_{chargeId}.yaml) — Redocly's own multi-file convention
│   └── components/
│       ├── schemas/             # one file per components.schemas entry
│       └── security-schemes/    # one file per components.securitySchemes entry
├── redocly.yaml            # Redocly CLI config (lint rules, code-sample languages)
├── package.json            # npm scripts: lint, docs:build (HTML reference), generate:client (Orval)
├── orval.config.ts         # Orval config — generates generated/node/ from the bundled spec
├── generated/               # build output — git-IGNORED entirely, regenerate on demand
│   ├── node/                  # Orval-generated TS/fetch client (`npm run generate:client`)
│   └── docs/                  # Redocly-built static HTML API reference (`npm run docs:build`)
├── mise.toml               # Toolchain (python 3.12, jq, yq, node 22) + tasks
├── requirements.txt        # Python deps (pypdf, openpyxl, requests, python-dotenv) — ad hoc scripts only
├── .env.example             # Template for SECRETS (no values) — versioned
├── .env.hml/.env.prd        # Per-environment endpoints/URLs (non-sensitive) — versioned
├── .env                      # Real secrets — git-IGNORED
└── .data/                     # Scratch dump for raw inputs (PII) — git-IGNORED, not a deliverable
```

`.data/` is an unstructured scratch area — drop any raw input there. It is git-ignored and holds customer PII, so **never** commit it. Ad-hoc Python scripts (run via `.venv/bin/python3`) are not versioned either.

## Prerequisites

- [mise](https://mise.jdx.dev/) — manages the tools and the virtualenv.

## Setup

```bash
mise install        # installs python 3.12, jq, yq, node 22
mise run setup      # creates .env from the template + installs requirements.txt into .venv
```

`mise run setup` copies `.env.example` → `.env` (if it doesn't exist yet) and runs `pip install -r requirements.txt` in `.venv`.

## Environments and variables

| File | Contents | Versioned? |
|---|---|---|
| `.env` | Real secrets | ❌ ignored |
| `.env.example` | Template that **documents** which secrets exist | ✅ |
| `.env.hml` | Homologation (sandbox) endpoints/URLs | ✅ |
| `.env.prd` | Production endpoints/URLs | ✅ |

Usage: load `.env.hml` **or** `.env.prd` (environment) **+** `.env` (secrets).

## SafraPay API — authentication

1. `POST /v2/merchant/auth` with the *MerchantToken* in the `Authorization` header.
2. Use the returned `accessToken` (JWT, ~30 min) as `Authorization: Bearer <accessToken>`.
3. Refresh with `POST /v2/refreshtoken`.

Servers: `https://payment.safrapay.com.br` (production) and `https://payment-hml.safrapay.com.br` (homologation). The spec covers Gateway, Charges, Payment Links, Checkout, Bank Slips, Fees, Protected Card, Recurrence, Chargeback, Webhook, and the local TEF Agent.

## Working with the spec

```bash
npm install                # once, installs @redocly/cli + orval + tsx
npm run lint                # OpenAPI lint (redocly.yaml picks up openapi/openapi.yaml)
npm run docs:build          # builds a static HTML API reference into generated/docs/index.html
npm run generate:client     # bundles the spec, then regenerates the Node/TS client into generated/node/
npx tsx tests/generated_node/smoke.ts   # smoke-tests the generated client
```

There's no generated Python client — the only generated client is the Node/TS one via Orval (`generated/node/`), which exports one plain `fetch`-based function per operation plus a `getXxxUrl()` helper. It has no built-in base URL: prepend the right host (`.env.hml`/`.env.prd`) yourself, and note that Chargeback's operations need an extra `/chargeback` path segment on top of the host (see that operation's `servers:` override under `openapi/paths/`).

## 🔒 Sensitive data

`.env` holds **secrets** and `.data/` holds **customer PII**. Both are git-ignored — **never** version them, print them to logs, or send them to external services.
