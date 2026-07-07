# Templates e Convenções

Este documento descreve **como as páginas desta documentação são estruturadas**,
para que novas páginas ou edições sigam o mesmo padrão. Toda a documentação foi
gerada por conversão do dump HTML do portal de desenvolvedores da SafraPay
(`.data/developers-hml.safrapay.com.br`) para Markdown.

> **Não oficial.** Veja o [`README.md`](README.md) para o aviso completo.

## Estrutura de diretórios (site Jekyll)

```
docs/safrapay/
├── _config.yml            # configuração do Jekyll
├── _data/
│   └── navigation.yml     # menu lateral (ordem das seções e páginas)
├── _layouts/
│   ├── default.html       # esqueleto da página (sidebar + conteúdo)
│   ├── doc.html           # layout de página de documentação
│   └── home.html          # layout da página inicial
├── _includes/
│   └── nav.html           # renderiza o menu a partir de navigation.yml
├── assets/css/style.css   # estilo (autossuficiente, tema claro/escuro)
├── index.md               # página inicial / visão geral
├── guias/                 # guias conceituais
├── api/                   # referência da API (endpoints)
├── referencia/            # tabelas de referência (endpoints, enums, variáveis)
├── README.md              # como usar/construir o site
└── TEMPLATES.md           # este arquivo
```

As três seções de conteúdo espelham o menu lateral:

| Diretório | Seção no menu | Conteúdo |
| --- | --- | --- |
| `guias/` | Guias | Material conceitual (primeiros passos, antifraude, integrações…). |
| `api/` | Referência da API | Uma página por recurso, contendo os endpoints. |
| `referencia/` | Referência | Tabelas geradas: índice de endpoints, enumeradores, variáveis. |

## Front matter (obrigatório em toda página)

Todas as páginas começam com um bloco YAML:

```yaml
---
title: "Autenticação"            # título exibido e usado no <title>
parent: "Referência da API"      # seção (Guias | Referência da API | Referência)
nav_order: 10                    # ordem dentro da seção
layout: "doc"                    # doc (conteúdo) ou home (página inicial)
permalink: "/api/autenticacao/"  # URL canônica no site publicado
description: "..."               # resumo (usado em SEO e nos cards)
source: "authentication.html"    # página original do portal (rastreabilidade)
---
```

> **Liquid desativado no corpo.** O `_config.yml` define `render_with_liquid: false`
> para as páginas, de modo que marcadores como `{{ENDPOINT_GATEWAY}}` apareçam
> **literalmente**. O menu ainda funciona porque layouts/includes sempre passam
> por Liquid.

## Template de página de endpoint (`api/`)

Cada operação da API segue este padrão. Os títulos das subseções (`Requisição
HTTP`, `Cabeçalho`, `Requisição`, `Resposta`…) vêm do portal e podem variar
conforme o endpoint.

````markdown
<a id="post-merchant-auth"></a>

### `POST` /merchant/auth

**Versão** `v2.0`

<a id="requisição-http"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/merchant/auth
```

> Exemplo de requisição

```ruby
# exemplo em ruby
```
```python
# exemplo em python
```
```bash
# exemplo em curl
```
```javascript
// exemplo em javascript
```

> O comando acima retorna um JSON estruturado assim:

```json
{ "accessToken": "...", "success": true }
```

Texto descritivo do que o endpoint faz.

#### Cabeçalho

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| Authorization | string | Sim | Chave de acesso à API. |

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| accessToken | string | Token JWT usado nas próximas requisições. |
````

Elementos do template:

- **Âncora explícita `<a id="…">`** antes de cada título (ver *Âncoras* abaixo).
- **Título do endpoint** = `` `MÉTODO` /caminho `` (o método vem em `code`).
- **Versão** logo abaixo, quando o portal informa.
- **Bloco `http`** com a linha da requisição (base como `{{ENDPOINT_GATEWAY}}`).
- **Exemplos multi-linguagem** em blocos com a linguagem correta (`ruby`,
  `python`, `bash`, `javascript`, `php`, `json`, `xml`…), precedidos por uma
  citação `>` com o rótulo original.
- **Tabelas** para cabeçalhos, parâmetros/corpo e resposta.

## Template de página de guia (`guias/`)

Guias são texto corrido com títulos, tabelas, listas e blocos de código —
mesmas regras de conversão, sem a obrigatoriedade da estrutura de endpoint.

## Páginas de referência (`referencia/`) — geradas

| Página | Origem | Formato |
| --- | --- | --- |
| `endpoints.md` | varredura das páginas `api/` | Tabela `Método · Caminho · Recurso`, com link para cada endpoint. |
| `enumeradores.md` | `_inventory.json → enums` | Uma seção por enum, com tabela `Valor · Nome · Descrição`. |
| `variaveis.md` | `_inventory.json → variaveis` | Tabela `Variável · Descrição` dos marcadores `{{...}}`. |

## Âncoras e links internos

Para que os links funcionem **igualmente no GitHub e no Jekyll/kramdown** (que
geram âncoras automáticas diferentes):

- Cada título (h2–h6) recebe uma âncora explícita `<a id="slug"></a>`.
- O `slug` é gerado por: minúsculas → remover pontuação → colapsar espaços,
  `/`, `_` e `-` em um único `-`. Duplicatas recebem sufixo `-1`, `-2`, …
- Links entre páginas usam caminhos relativos com extensão `.md`
  (ex.: `../guias/antifraude.md#device-fingerprint`); o plugin
  `jekyll-relative-links` os converte em URLs no site publicado.
- Fragmentos de origem que não correspondem a nenhum título são reduzidos a um
  link para a página (sem âncora), evitando links quebrados.

## Convenções de conteúdo

- Idioma do conteúdo: **português** (fiel ao portal).
- Valores monetários das APIs são em **centavos** (ex.: `15550` = R$ 155,50).
- IDs de transação são **UUIDs**.
- Colchetes literais em texto são escapados (`\[`, `\]`) para não virarem links.
- Imagens do portal **não** fazem parte do dump e foram omitidas.

## Regenerando a documentação

As páginas são geradas a partir do dump por scripts Python ad hoc (não
versionados). Ao reprocessar, mantenha o front matter, as âncoras explícitas e
a estrutura de diretórios descritos aqui, e valide os links internos ao final.
