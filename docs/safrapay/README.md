# Documentação da API SafraPay (não oficial)

Documentação de referência da **API SafraPay**, reconstruída por engenharia
reversa do portal de desenvolvedores (ambiente de homologação,
`developers-hml.safrapay.com.br`) e convertida para Markdown organizado como um
site **Jekyll**.

> ⚠️ **Não oficial.** Este material é uma referência interna de integração e
> **não constitui garantia contratual**. Em caso de divergência, o portal
> oficial da SafraPay prevalece.

## Como navegar

- Comece por **[`index.md`](index.md)** (visão geral, ambientes, autenticação).
- **Guias** conceituais em [`guias/`](guias/).
- **Referência da API** (endpoints) em [`api/`](api/).
- **Referência rápida** (índice de endpoints, enumeradores, variáveis) em
  [`referencia/`](referencia/).

O arquivo é totalmente navegável como Markdown direto no GitHub — os links
internos são relativos e resolvem sem build.

## Como construir o site localmente

O toolchain é gerenciado por **mise** (Ruby incluso). A partir da raiz do repo:

```bash
mise install            # instala ruby (e demais ferramentas)
mise run docs:setup     # instala bundler + gems em docs/safrapay
mise run docs:serve     # serve em http://localhost:4000 (com live reload)
# ou
mise run docs:build     # gera o site estático em docs/safrapay/_site
```

Os três tasks executam dentro de `docs/safrapay/` usando o `Gemfile` local.

## Estrutura

```
docs/safrapay/
├── _config.yml   _data/   _layouts/   _includes/   assets/
├── index.md          # visão geral
├── guias/            # guias conceituais
├── api/              # referência da API (endpoints)
├── referencia/       # tabelas: endpoints, enumeradores, variáveis
├── README.md         # este arquivo
└── TEMPLATES.md      # estrutura das páginas e convenções
```

## Manutenção

A estrutura das páginas, o front matter e as convenções de âncoras/links estão
documentados em **[`TEMPLATES.md`](TEMPLATES.md)**. As páginas foram geradas a
partir do dump HTML original; ao regenerá-las, preserve esse padrão e valide os
links internos.

## Origem dos dados

- Fonte: dump do portal em `.data/developers-hml.safrapay.com.br` (não versionado).
- Cada página registra a origem no campo `source` do front matter.
- Imagens do portal não faziam parte do dump e foram omitidas.
