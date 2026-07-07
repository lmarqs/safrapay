---
title: "Chargeback"
parent: "Guias"
nav_order: 30
layout: "doc"
permalink: "/guias/chargeback/"
description: "A Chargeback API foi desenvolvida para suportar o gerenciamento do ciclo de disputas de transações de pagamento, permitindo que os estabelecimentos integrem seu"
source: "chargeback.html"
---

# Documentação — Chargeback API

---

<a id="introdução"></a>

## Introdução

A **Chargeback API** foi desenvolvida para suportar o gerenciamento do ciclo de disputas de transações de pagamento, permitindo que os estabelecimentos integrem seus sistemas aos processos de consulta, acompanhamento e tratamento de chargebacks de forma estruturada e escalável.

Por meio desta API, é possível:

- Recuperar informações sobre transações contestadas;
- Identificar o status de cada disputa;
- Acessar os dados necessários para análise;
- Executar as ações aplicáveis dentro do fluxo operacional de chargeback, incluindo etapas relacionadas à defesa da contestação.

Esta documentação apresenta os endpoints disponíveis, os modelos de requisição e resposta, as regras de negócio associadas ao processo, bem como o fluxo de defesa e os prazos operacionais que devem ser observados para o correto tratamento das disputas.

---

<a id="base-url"></a>

## Base URL

| Ambiente | URL |
| --- | --- |
| Sandbox | `https://payment-hml.safrapay.com.br/chargeback` |
| Produção | `https://payment.safrapay.com.br/chargeback` |

---

<a id="autenticação"></a>

## Autenticação

A API exige autenticação do **GATEWAY API**. *(Autenticação > Gateway API)*

---

<a id="fluxo-de-consulta-e-defesa-de-disputas"></a>

## Fluxo de Consulta e Defesa de Disputas

A API disponibiliza um fluxo estruturado para que o time de TI do estabelecimento acompanhe o ciclo completo das disputas, desde a consulta até o envio da defesa, de forma padronizada, rastreável e dentro dos prazos operacionais definidos.

<a id="objetivo-do-fluxo"></a>

### Objetivo do Fluxo

Permitir que os sistemas do cliente:

1. Consultem as disputas abertas e seus respectivos detalhes.
2. Identifiquem o status, prazo e motivo de cada contestação.
3. Preparem a defesa com base nas evidências exigidas.
4. Enviem a resposta à disputa dentro da janela de processamento estabelecida.

---

<a id="1-autenticação"></a>

### 1. Autenticação

Todos os endpoints da API requerem autenticação. Antes de realizar qualquer requisição, é necessário obter um **token de acesso** válido.

> Para gerar o token, consulte o fluxo de autenticação em: **Autenticação > Gateway API**.

---

<a id="2-consulta-de-disputas"></a>

### 2. Consulta de Disputas

O estabelecimento pode consultar disputas de duas formas:

1. **Sumário de Disputas**
  - `GET /v1/disputes/summary` → Retorna uma lista de disputas com filtros por status, categoria e período.
2. **Totais de Disputas**
  - `GET /v1/disputes/total` → Retorna o total de disputas abertas e finalizadas, organizadas por status.

<a id="status-da-disputa"></a>

#### Status da Disputa

| Status | Descrição |
| --- | --- |
| `Pending` | Disputa aguardando ação do estabelecimento. |
| `UnderAnalysis` | Disputa em análise pelo Safrapay ou pelo Emissor. |
| `Completed` | Disputa finalizada, com um resultado definido. |

---

<a id="3-análise-e-detalhamento-da-disputa"></a>

### 3. Análise e Detalhamento da Disputa

`GET /v1/disputes/{disputeId}` → Retorna todas as informações da disputa, incluindo:

- **Categoria** (`category`) → Motivo da disputa (Fraud, Authorization, etc.).
- **Estágio da Análise** (`analysisStage`) → Indica quem está avaliando (Safrapay ou Emissor).
- **Prazo** (`deadline`) → Disputas têm **15 dias corridos** para resposta. Após esse prazo, avançam automaticamente para débito.
- **Conclusão** (`conclusion`) → Aplicável apenas para disputas `Completed`:
  - `Gain` → O EC ganhou a disputa.
  - `Due` → O EC perdeu a disputa.
  - `Contested` → O EC contestou o débito.

---

<a id="4-tomada-de-decisão-pelo-ec"></a>

### 4. Tomada de Decisão pelo EC

**Aceitar o débito:**

- `POST /v1/disputes/{disputeId}/debts/accept` → Confirma a aceitação do débito e encerra a disputa.

**Reapresentar a disputa (contestação):**

- `POST /v1/disputes/second-presentment` → Envia documentos para contestar o chargeback.

<a id="regras-para-anexos-na-reapresentação"></a>

#### Regras para Anexos na Reapresentação

| Critério | Valor |
| --- | --- |
| Formato | `.pdf` |
| Tamanho Máximo | `2MB` |

> ⚠️ **Atenção:** O nome dos arquivos enviados **não deve conter caracteres especiais** (ex.: `ç`, `ã`, `@`, `#`, `&`). Arquivos fora desse padrão serão rejeitados pelo portal.

---

<a id="5-finalização-da-disputa"></a>

### 5. Finalização da Disputa

Uma disputa é considerada finalizada quando seu status atinge `Completed`. O resultado pode ser consultado pelo campo `conclusion`:

| Valor | Significado |
| --- | --- |
| `Gain` | A disputa foi decidida a favor do estabelecimento. |
| `Due` | A disputa foi decidida a favor do portador do cartão, gerando débito ao EC. |
| `Contested` | A disputa foi contestada e aguarda análise da bandeira. |

> Caso o EC discorde do resultado, é possível acionar o time de suporte pelos canais oficiais disponibilizados pelo Banco Safra.

---

<a id="resumo-do-fluxo"></a>

### Resumo do Fluxo

| Etapa | Descrição |
| --- | --- |
| 1. Autenticação | Obtenha o token de acesso antes de qualquer requisição. |
| 2. Consulta de Disputas | Recupere o sumário ou os totais das disputas do estabelecimento. |
| 3. Detalhes da Disputa | Acesse informações completas de uma disputa específica. |
| 4. Decisão do EC | Aceite o débito via `debts/accept` ou conteste via `second-presentment` (anexo `.pdf` até 2MB). |
| 5. Finalização | A disputa é encerrada com status `Completed` ou `UnderAnalysis`. Verifique `conclusion` e acione o suporte se necessário. |

> ⏱️ **Prazo de Resposta:** O EC tem **15 dias corridos** para tomar uma decisão. Após esse prazo, o débito é aplicado automaticamente.

---

<a id="api-reference"></a>

## API Reference

<a id="autenticação-1"></a>

### Autenticação

Todos os endpoints da API requerem autenticação. O token deve ser enviado no header `Authorization` em todas as requisições.

<a id="gerar-token-de-autenticação"></a>

#### Gerar Token de Autenticação

```bash
POST /v1/merchant/auth
```

Gera um par de tokens — acesso (`access_token`) e atualização (`refresh_token`) — a partir do token de comerciante fornecido pelo Safrapay.

> **Renovação:** Utilize o `refresh_token` para obter um novo `access_token` sem necessidade de reautenticação completa.

<a id="códigos-de-status"></a>

##### Códigos de Status

| Código | Status | Descrição |
| --- | --- | --- |
| `200` | OK | Token gerado com sucesso. |
| `400` | Bad Request | Parâmetros inválidos ou ausentes. |
| `401` | Unauthorized | Token de comerciante inválido ou expirado. |
| `500` | Internal Server Error | Erro interno no servidor. |

---

<a id="disputas"></a>

## Disputas

<a id="consultar-disputa-sumário"></a>

### Consultar Disputa (Sumário)

```bash
GET /v1/disputes/summary
```

**Descrição:** Lista as disputas por status (Análise, Pendentes e Concluídas).

**Endpoint:**

```handlebars
{{gatewayAPI}}/v1/disputes/summary?Status=UnderAnalysis&CreatedDate.gte={{DataInicial}}&CreatedDate.lte={{DataFinal}}&Limit=100&Page=1
```

**CURL Request:**

```bash
curl -X GET \
  "http://{{gatewayAPI}}/v1/disputes/summary?Status=UnderAnalysis&CreatedDate.gte={{DataInicial}}&CreatedDate.lte={{DataFinal}}&Limit=100&Page=1&Nsu=123&Category=XX" \
  -H "Accept: application/json"
```

<a id="parâmetros-de-query"></a>

#### Parâmetros de Query

| Nome | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| `Status` | string | Sim | Status da disputa (`Pending`, `UnderAnalysis`, `Completed`). |
| `Nsu` | string | Não | Número sequencial único da transação. |
| `Category` | string | Não | `Authorization`, `ConsumerDisputes`, `ProcessingError`, `Fraud`, `RetrievalRequest`. |
| `CreatedDate.Gte` | date | Sim | Retorna registros com data de criação >= data informada. |
| `CreatedDate.Lte` | date | Sim | Retorna registros com data de criação <= data informada. |
| `Page` | integer | Sim | Número da página a ser retornada. |
| `Limit` | integer | Sim | Quantidade de itens retornados por página. |
| `Errors` | array | Sim | Lista de erros. Array vazio em caso de sucesso. |

<a id="códigos-de-status-1"></a>

#### Códigos de Status

| Código | Descrição |
| --- | --- |
| `200` | Sumário retornado com sucesso. |
| `400` | Parâmetros inválidos. |
| `401` | Falha na autenticação. |
| `500` | Erro no servidor. |

<a id="response-200-ok"></a>

#### Response `200 OK`

```json
{
  "pagination": {
    "first": 1,
    "last": 10,
    "previous": 2,
    "next": 4,
    "page": 3,
    "isFirst": false,
    "isLast": false,
    "totalElements": 750
  },
  "data": [
    {
      "disputeId": "000010527200157418652024061800",
      "merchantCode": "21",
      "cycleId": 1,
      "cycle": "1ª Chargeback",
      "nsu": 20012212154,
      "categoryId": 1,
      "category": "Reversal Fee Colect",
      "transactionPaymentMethod": "CRÉDITO PARCELADO C/ JUROS",
      "deadline": 12,
      "brandDescription": "Mastercard",
      "createdDate": "2024-10-10",
      "value": 15,
      "analysisStage": "AwaitingSafrapay",
      "conclusion": "Gain",
      "status": "Pending"
    }
  ],
  "success": true,
  "errors": [{ "errorCode": 0, "message": "string", "field": "string" }],
  "traceKey": "9f624100-ca4c-4461-86ea-a11da428f81e"
}
```

<a id="response-400-bad-request"></a>

#### Response `400 Bad Request`

```json
{
  "success": false,
  "errors": [{ "errorCode": 400, "message": "O campo 'Limit' é obrigatório", "field": "Limit" }],
  "traceKey": "ad4e7e6f-f0db-4ad6-abdc-01eb0e6fa65b"
}
```

<a id="estrutura-de-resposta-campos-raiz"></a>

#### Estrutura de Resposta — Campos Raiz

| Nome | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| `success` | boolean | Sim | `true` para requisição bem-sucedida. |
| `errors` | array | Sim | Lista de erros. Array vazio em sucesso. |
| `traceKey` | string | Sim | Identificador único para rastreamento e auditoria. |
| `data` | object | Sim | Detalhes completos da disputa. |

<a id="estrutura-de-data"></a>

#### Estrutura de `data[]`

| Nome | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| `disputeId` | string | Sim | Identificador único da disputa. |
| `merchantCode` | string | Sim | Código do comerciante. |
| `cycleId` | integer | Sim | ID do ciclo da disputa. |
| `cycle` | string | Sim | Nome do ciclo atual. |
| `nsu` | integer | Sim | NSU da transação contestada. |
| `categoryId` | integer | Sim | ID da categoria. |
| `category` | string | Sim | Nome da categoria. |
| `transactionPaymentMethod` | string | Sim | Método de pagamento. |
| `deadline` | integer | Não | Prazo. Apenas quando `status` for `Pending`. |
| `brandDescription` | string | Sim | Bandeira do cartão. |
| `createdDate` | date | Sim | Data de criação (`YYYY-MM-DD`). |
| `value` | decimal | Sim | Valor da disputa. |
| `analysisStage` | string | Sim | Estágio. Apenas quando `status` for `UnderAnalysis`. |
| `conclusion` | string | Sim | Conclusão. Apenas quando `status` for `Completed`. |
| `status` | string | Sim | Status atual da disputa. |

<a id="estrutura-de-errors"></a>

#### Estrutura de `errors[]`

| Nome | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| `errors[].errorCode` | integer | Sim | Código do erro. |
| `errors[].message` | string | Sim | Mensagem descritiva do erro. |
| `errors[].field` | string | Não | Campo relacionado ao erro. |

<a id="estrutura-de-pagination"></a>

#### Estrutura de `pagination`

| Nome | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| `first` | integer | Sim | Número da primeira página. |
| `last` | integer | Sim | Número da última página. |
| `previous` | integer | Não | Página anterior. |
| `next` | integer | Não | Próxima página. |
| `page` | integer | Sim | Página atual. |
| `isFirst` | boolean | Sim | `true` se for a primeira página. |
| `isLast` | boolean | Sim | `true` se for a última página. |
| `totalElements` | integer | Sim | Total de disputas retornadas. |

---

<a id="totais-de-disputas"></a>

### Totais de Disputas

```bash
GET /v1/disputes/total
```

**Descrição:** Recupera os totais de disputas por status.

**Endpoint:**

```handlebars
{{gatewayAPI}}/v1/disputes/total?RequestDate.gte={{DataInicial}}&RequestDate.lte={{DataFinal}}
```

**CURL Request:**

```bash
curl --request GET \
  '{{gatewayAPI}}/v1/disputes/total?RequestDate.gte={{DataInicial}}&RequestDate.lte={{DataFinal}}' \
  --header 'Accept: application/json'
```

<a id="parâmetros-de-query-1"></a>

#### Parâmetros de Query

| Nome | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| `RequestDate.Gte` | date | Sim | Data inicial. Retorna registros com data >= informada. |
| `RequestDate.Lte` | date | Sim | Data final. Retorna registros com data <= informada. |

<a id="códigos-de-status-2"></a>

#### Códigos de Status

| Código | Descrição |
| --- | --- |
| `200` | Totais retornados com sucesso. |
| `400` | Parâmetros inválidos. |
| `401` | Falha na autenticação. |
| `500` | Erro no servidor. |

<a id="response-200-ok-1"></a>

#### Response `200 OK`

```json
{
  "data": {
    "opened": {
      "total":            { "quantity": 0, "value": 0.00 },
      "underAnalysis":    { "quantity": 0, "value": 0.00 },
      "awaitingDocument": { "quantity": 0, "value": 0.00 },
      "inContestation":   { "quantity": 0, "value": 0.00 }
    },
    "completed": {
      "total":     { "quantity": 0, "value": 0.00 },
      "gain":      { "quantity": 0, "value": 0.00 },
      "due":       { "quantity": 0, "value": 0.00 },
      "contested": { "quantity": 0, "value": 0.00 }
    }
  },
  "success": true,
  "errors": [],
  "traceKey": "fd4472c1-1b2d-4718-8210-7a578a683c4f"
}
```

<a id="response-400-bad-request-1"></a>

#### Response `400 Bad Request`

```json
{
  "success": false,
  "errors": [{ "errorCode": 400, "message": "Campo Lte é obrigatório", "field": "RequestDate.Lte" }],
  "traceKey": "0460eb0a-715e-4a3f-9c87-413def28279b"
}
```

<a id="estrutura-de-dataopened-e-datacompleted"></a>

#### Estrutura de `data.opened` e `data.completed`

| Nome | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| `total.quantity` | integer | Sim | Qtd total de disputas. |
| `total.value` | decimal | Sim | Valor total das disputas. |
| `underAnalysis.quantity` | integer | Sim | Qtd em análise. |
| `underAnalysis.value` | decimal | Sim | Valor em análise. |
| `awaitingDocument.quantity` | integer | Sim | Qtd aguardando documento. |
| `awaitingDocument.value` | decimal | Sim | Valor aguardando documento. |
| `inContestation.quantity` | integer | Sim | Qtd em contestação. |
| `inContestation.value` | decimal | Sim | Valor em contestação. |
| `gain.quantity` | integer | Sim | Qtd de disputas ganhas. |
| `gain.value` | decimal | Sim | Valor das disputas ganhas. |
| `due.quantity` | integer | Sim | Qtd de disputas vencidas. |
| `due.value` | decimal | Sim | Valor das disputas vencidas. |

> **Notas:** `opened` = disputas em andamento · `completed` = disputas finalizadas.

---

<a id="detalhes-da-disputa"></a>

### Detalhes da Disputa

```bash
GET /v1/disputes/{disputeId}
```

**Descrição:** Retorna os detalhes de uma disputa pelo identificador informado.

**Endpoint:** `{{gatewayAPI}}/v1/disputes/{{disputeId}}`

<a id="parâmetros-de-path"></a>

#### Parâmetros de Path

| Nome | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| `disputeId` | string | Sim | ID da disputa. |

<a id="códigos-de-status-3"></a>

#### Códigos de Status

| Código | Descrição |
| --- | --- |
| `200` | Detalhes retornados com sucesso. |
| `400` | Parâmetros inválidos. |
| `401` | Falha na autenticação. |
| `404` | Disputa não encontrada. |
| `500` | Erro no servidor. |

<a id="response-200-ok-2"></a>

#### Response `200 OK`

```json
{
  "data": {
    "aging": 2,
    "cycle": "1º Chargeback",
    "status": "Completed",
    "createdDate": "2026-03-16T00:00:00",
    "arn": "10000000511520400014195",
    "category": { "id": 4, "description": "Fraude" },
    "merchant": { "merchantCode": 1000471, "corporateName": "TESTE PAC EMP2" },
    "transaction": {
      "nsu": "020018678955",
      "authorization": "502538",
      "brandCode": "AMEX",
      "transactionPaymentMethodCode": "CP07",
      "cardPan": "374245*****1005",
      "date": "2025-07-23T00:00:00",
      "valor": 10.00
    },
    "reasonCode": {
      "code": "4755",
      "description": "Autorizacao solicitada nao foi obtida ou nao aprovada"
    },
    "steps": [
      {
        "sequence": 3,
        "description": "Concluido",
        "startDate": "2026-03-18T00:00:00",
        "endDate": "2026-03-18T00:00:00",
        "comment": "Teste API Cliente"
      },
      {
        "sequence": 2,
        "description": "Pendente - Em análise Safrapay",
        "startDate": "2026-03-16T00:00:00",
        "endDate": "2026-03-16T00:00:00",
        "comment": ""
      }
    ]
  }
}
```

<a id="response-400-bad-request-2"></a>

#### Response `400 Bad Request`

```json
{
  "success": false,
  "errors": [{
    "errorCode": 400,
    "message": "The field disputeId must be a string or array type with a minimum length of '30'.",
    "field": "disputeId"
  }],
  "traceKey": "87eafaeb-f9b3-465b-aeec-1715a450017b"
}
```

<a id="estrutura-de-data-1"></a>

#### Estrutura de `data`

| Nome | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| `data.aging` | integer | Sim | Idade da disputa (dias decorridos). |
| `data.deadline` | integer | Sim | Prazo para resolução. |
| `data.cycle` | string | Sim | Nome do ciclo da disputa. |
| `data.status` | string | Sim | Status atual (`Pending`, `Closed`, etc.). |
| `data.createdDate` | date | Sim | Data de criação (`YYYY-MM-DD`). |
| `data.arn` | string | Sim | Número ARN da transação. |

<a id="estrutura-de-datacategory"></a>

#### Estrutura de `data.category`

| Nome | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| `data.category.id` | integer | Sim | ID da categoria. |
| `data.category.description` | string | Sim | Descrição da categoria. |

<a id="estrutura-de-datamerchant"></a>

#### Estrutura de `data.merchant`

| Nome | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| `data.merchant.merchantCode` | integer | Sim | Código do comerciante. |
| `data.merchant.corporateName` | string | Sim | Nome corporativo do EC. |

<a id="estrutura-de-datatransaction"></a>

#### Estrutura de `data.transaction`

| Nome | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| `data.transaction.nsu` | string | Sim | NSU da transação. |
| `data.transaction.authorization` | string | Sim | Código de autorização. |
| `data.transaction.brandCode` | string | Sim | Bandeira do cartão. |
| `data.transaction.transactionPaymentMethodCode` | string | Sim | Código do método de pagamento. |
| `data.transaction.cardPan` | string | Sim | PAN mascarado (PCI DSS). Formato: `************1234`. |
| `data.transaction.date` | date | Sim | Data da transação (`YYYY-MM-DD`). |
| `data.transaction.valor` | decimal | Sim | Valor total da transação. |

<a id="estrutura-de-datareasoncode"></a>

#### Estrutura de `data.reasonCode`

| Nome | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| `data.reasonCode.code` | string | Sim | Código do motivo da disputa. |
| `data.reasonCode.description` | string | Sim | Descrição legível do motivo. |

<a id="estrutura-de-datasteps-histórico-da-disputa"></a>

#### Estrutura de `data.steps` *(histórico da disputa)*

| Nome | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| `data.steps.[x].sequence` | integer | Sim | Número de ordem do passo. |
| `data.steps.[x].description` | string | Sim | Descrição do status/evento. |
| `data.steps.[x].startDate` | date | Sim | Data de início (`YYYY-MM-DD`). |
| `data.steps.[x].endDate` | date | Sim | Data de término (`YYYY-MM-DD`). |
| `data.steps.[x].comment` | string | Não | Comentário adicional. |

---

<a id="acatar-débito-da-disputa"></a>

### Acatar Débito da Disputa

```bash
POST /v1/disputes/{disputeId}/debts/accept
```

**Descrição:** Aceita o débito de uma disputa especificada.

<a id="parâmetros-de-path-1"></a>

#### Parâmetros de Path

| Nome | Local | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- | --- |
| `disputeId` | path | string | Sim | ID da disputa. |

<a id="códigos-de-status-4"></a>

#### Códigos de Status

| Código | Descrição |
| --- | --- |
| `204` | Débito aceito com sucesso. |
| `400` | Parâmetros inválidos. |
| `401` | Falha na autenticação. |
| `500` | Erro no servidor. |

<a id="response-200-ok-3"></a>

#### Response `200 OK`

```json
{
  "success": true,
  "errors": [],
  "traceKey": "de162330-ee49-44a7-a9ef-073b207e39b7"
}
```

---

<a id="criar-representação-secundária"></a>

### Criar Representação Secundária

```bash
POST /v1/disputes/second-presentment
```

**Descrição:** Cria uma representação secundária rejeitando o débito.

<a id="códigos-de-status-5"></a>

#### Códigos de Status

| Código | Descrição |
| --- | --- |
| `204` | Segunda apresentação criada com sucesso. |
| `400` | Parâmetros inválidos. |
| `401` | Falha na autenticação. |
| `500` | Erro no servidor. |
