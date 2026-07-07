---
title: "Webhooks"
parent: "Referência da API"
nav_order: 100
layout: "doc"
permalink: "/api/webhooks/"
description: "É um método de ampliar ou alterar o comportamento de uma página da Web, ou aplicação da Web, com callbacks personalizados."
source: "webhook.html"
---

# WEBHOOK

É um método de ampliar ou alterar o comportamento de uma página da Web, ou aplicação da Web, com callbacks personalizados.

Endpoints relacionados a configuração dos webhooks.

<a id="entrega-de-webhooks"></a>

#### Entrega de webhooks

A entrega dos webhooks é feita via HTTPS POST, utilizando o Merchant Token em base64 como autenticação. Ou seja, será enviado o parâmetro Authorization: base64(merchantToken).

🚧 É importante que essa validação seja feita afim de evitar ataques de spoofing.

O body da requisição é descrito no objeto [`WebhookCall`](#webhookcall).

<a id="requisitos-para-url-webhook"></a>

#### Requisitos para URL Webhook

**Utilização obrigatória de HTTPS:**
 Para garantir a segurança, apenas URLs iniciadas com "https://" serão aceitas. Endereços "http://" são recusados.

**Certificado válido e atualizado:**
 O endereço deve possuir um certificado SSL válido. Certificados expirados ou autoassinados podem comprometer o funcionamento do webhook.

**Acessibilidade pública:**
 Assegure-se de que seu endpoint seja acessível publicamente. Caso contrário, isso afetará a entrega.

**Resposta em tempo hábil:**
 Nosso sistema necessita estabelecer conexão com ele. O webhook deverá responder em até 30 segundos com status HTTP 2xx.

**Categoria de domínio:**
 Temos categorias de URL liberadas por padrão:

- Business and Economy
- Educational Institutions
- Financial Services
- Health and Medicine
- Shopping
- Motor Vehicles

Para demais categorias, é necessário a abertura de uma solicitação para realizarmos a liberação de regras internas (Este possui um SLA de até 15 dias).

O site abaixo pode ser usado de suporte para validação da categoria de sua URL: 

 [https://urlfiltering.paloaltonetworks.com/query](https://urlfiltering.paloaltonetworks.com/query)

<a id="post-webhook-bulk"></a>

### `POST` /webhook/bulk

**Versão** `v1.0`

<a id="requisição-http"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_WEBHOOK}}/v1/webhook/bulk
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_WEBHOOK}}/v1/Webhook/Bulk")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["merchantId"] = "{{merchantId}}"
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n  \"email\": \"ggabriellyalinemartins@webin.com.br\",\r\n  \"webhooks\": [\r\n    {\r\n      \"targetUrl\": \"https://typedwebhook.tools/webhook/1ffe334f-d284-4f48-bee7-4598c1cda210\",\r\n      \"eventType\": 1 \r\n    },\r\n    {\r\n      \"targetUrl\": \"https://typedwebhook.tools/webhook/1ffe334f-d284-4f48-bee7-4598c1cda210\",\r\n      \"eventType\": 2 \r\n    }\r\n  ]\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "https://webhook-dev.safrapay.com.br/v1/Webhook/Bulk"

payload="{\r\n  \"email\": \"ggabriellyalinemartins@webin.com.br\",\r\n  \"webhooks\": [\r\n    {\r\n      \"targetUrl\": \"https://typedwebhook.tools/webhook/1ffe334f-d284-4f48-bee7-4598c1cda210\",\r\n      \"eventType\": 1 \r\n    },\r\n    {\r\n      \"targetUrl\": \"https://typedwebhook.tools/webhook/1ffe334f-d284-4f48-bee7-4598c1cda210\",\r\n      \"eventType\": 2 \r\n    }\r\n  ]\r\n}"
headers = {
  'merchantId': '{{merchantId}}',
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST 'https://webhook-dev.safrapay.com.br/v1/Webhook/Bulk' \
--header 'merchantId: {{merchantId}}' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "email": "ggabriellyalinemartins@webin.com.br",
  "webhooks": [
    {
      "targetUrl": "https://typedwebhook.tools/webhook/1ffe334f-d284-4f48-bee7-4598c1cda210",
      "eventType": 1 
    },
    {
      "targetUrl": "https://typedwebhook.tools/webhook/1ffe334f-d284-4f48-bee7-4598c1cda210",
      "eventType": 2 
    }
  ]
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("merchantId", "{{merchantId}}");
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"email":"ggabriellyalinemartins@webin.com.br","webhooks":[{"targetUrl":"https://typedwebhook.tools/webhook/1ffe334f-d284-4f48-bee7-4598c1cda210","eventType":1},{"targetUrl":"https://typedwebhook.tools/webhook/1ffe334f-d284-4f48-bee7-4598c1cda210","eventType":2}]});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://webhook-dev.safrapay.com.br/v1/Webhook/Bulk", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "webhooks": [
        {
            "eventType": "ChargeCreated",
            "webhookId": "df007e3d-ebb5-46d1-80bc-a9815b1f32e6",
            "status": "Active",
            "targetUrl": "https://typedwebhook.tools/webhook/1ffe334f-d284-4f48-bee7-4598c1cda210",
            "creationDate": "2021-06-14 22:19:32Z",
            "email": "ggabriellyalinemartins@webin.com.br"
        },
        {
            "eventType": "ChargeUpdated",
            "webhookId": "9deffbef-0a79-456c-8a41-f60dd9f125ba",
            "status": "Active",
            "targetUrl": "https://typedwebhook.tools/webhook/1ffe334f-d284-4f48-bee7-4598c1cda210",
            "creationDate": "2021-06-14 22:19:32Z",
            "email": "ggabriellyalinemartins@webin.com.br"
        }
    ],
    "success": true,
    "errors": [],
    "traceKey": "202415f4-1e6f-4c74-b47d-eb5020adfcc2"
}
```

O endpoint responsável por criar uma notificação webhook.

<a id="requisição"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| email | string | Sim | Email para contingência de entrega do webhook. |
| webhooks | array | Sim | Representa um evento de interesse para acionar as notificações. |
| webhooks.targetUrl | string | Sim | URL onde a solicitação foi feita. Verificar [`Requisitos da URL`](webhooks.md#requisitos-para-url-webhook). |
| webhooks.eventType | EventTypeEnum | Sim | [Representam todos os eventos existentes.](../guias/primeiros-passos.md#eventtype) |
| webhook.customHeaders | array | Não | Lista de objetos contendo parâmetros e valores a serem enviados nos cabeçalhos do Webhook. |
| webhook.customHeaders.param | string | Não | Nome do cabeçalho a ser definido no cabeçalho da solicitação. |
| webhook.customHeaders.value | string | Não | Valor do cabeçalho para definir no parâmetro de solicitação. |

<a id="resposta"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| webhooks | array | Representa um evento de interesse acionando as notificações. |
| webhooks.eventType | string | Representa o tipo de evento. |
| webhook.webhookId | string | O ID único do Webhook. |
| webhook.status | string | [O status do Webhook](../guias/primeiros-passos.md#webhookstatus). |
| webhook.targetUrl | string | URL onde a solicitação foi feita. |
| webhook.creationDate | string | Data de criação do Webhook. |
| webhook.email | string | Email para contato. |
| webhook.customHeaders | array | Lista de objetos contendo parâmetros e valores que foram enviados nos cabeçalhos do Webhook. |
| webhook.customHeaders.param | string | Nome do cabeçalho definido no cabeçalho da solicitação. |
| webhook.customHeaders.value | string | Valor do cabeçalho definido no parâmetro da solicitação. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Não |
| errors.message | string | Não |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | Use o Merchant Token para gerar o `accessToken` do ENDPOINT_GATEWAY. |

<a id="body-raw"></a>

#### BODY Raw

```http
{
"email": "ggabriellyalinemartins@webin.com.br",
"webhooks": [
{
"targetUrl": "https://typedwebhook.tools/webhook/1ffe334f-d284-4f48-bee7-4598c1cda210",
"eventType": 1
},
{
"targetUrl": "https://typedwebhook.tools/webhook/1ffe334f-d284-4f48-bee7-4598c1cda210",
"eventType": 2
}
]
}
```

<a id="get-webhook"></a>

### `GET` /webhook

**Versão** `v1.0`

<a id="requisição-http-1"></a>

#### Requisição HTTP

```http
GET {{ENDPOINT_WEBHOOK}}/v1/webhook
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_WEBHOOK}}/v1/Webhook?pageSize=10&currentPage=1")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Get.new(url)
request["merchantId"] = "{{merchantId}}"
request["Authorization"] = "Bearer {{accessToken}}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_WEBHOOK}}/v1/Webhook?pageSize=10&currentPage=1"

payload={}
headers = {
  'merchantId': '{{merchantId}}',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request GET '{{ENDPOINT_WEBHOOK}}/v1/Webhook?pageSize=10&currentPage=1' \
--header 'merchantId: {{merchantId}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("merchantId", "{{merchantId}}");
myHeaders.append("Authorization", "Bearer {{accessToken}}");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("{{ENDPOINT_WEBHOOK}}/v1/Webhook?pageSize=10&currentPage=1", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "webhooks": [
        {
            "eventType": "ChargeCreated",
            "webhookId": "7e768876-042c-4c47-a712-37f56aa7ead7",
            "status": "Active",
            "targetUrl": "https://typedwebhook.tools/webhook/1ffe334f-d284-4f48-bee7-4598c1cda210",
            "creationDate": "2021-06-23 20:39:01Z",
            "email": "ggabriellyalinemartins@webin.com.br"
        },
        {
            "eventType": "ChargeUpdated",
            "webhookId": "807a0ac2-832c-44f1-bb67-f706c43528e8",
            "status": "Active",
            "targetUrl": "https://typedwebhook.tools/webhook/1ffe334f-d284-4f48-bee7-4598c1cda210",
            "creationDate": "2021-06-23 20:39:01Z",
            "email": "ggabriellyalinemartins@webin.com.br"
        }
    ],
    "total": 2,
    "success": true,
    "errors": [],
    "traceKey": "22f9281e-d12e-4e22-977b-bcf5451679a1"
}
```

O endpoint responsável por obter notificações webhook.

<a id="requisição-1"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| pageSize | int | Sim | Quantidade de webhooks por página. |
| currentPage | int | Sim | Página atual da consulta. |

<a id="resposta-1"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| webhooks | array | Representa um evento de interesse. |
| webhooks.eventType | string | Representa o tipo de evento. |
| webhook.webhookId | string | O ID único do Webhook. |
| webhook.status | string | O status do Webhook. |
| webhook.targetUrl | string | URL onde a solicitação foi feita. |
| webhook.creationDate | string | Data de criação do Webhook. |
| webhook.email | string | Email para contato. |
| webhook.customHeaders | array | Lista de objetos contendo parâmetros e valores que foram enviados nos cabeçalhos do Webhook. |
| webhook.customHeaders.param | string | Nome do cabeçalho definido no cabeçalho da solicitação. |
| webhook.customHeaders.value | string | Valor do cabeçalho definido no parâmetro da solicitação. |
| total | int | Indica quantos Webhooks foram encontrados na consulta. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Não |
| errors.message | string | Não |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | Use o Merchant Token para gerar o `accessToken` do ENDPOINT_GATEWAY. |

| PARAMS | - |
| --- | --- |
| **pageSize** | {{pageSize}} |
| -- | A quantidade de itens por página. |
| **currentPage** | {{currentPage}} |
| -- | A página atual. |

<a id="put-webhook-cancel-webhookid"></a>

### `PUT` /Webhook/Cancel/{webhookId}

**Versão** `v1.0`

<a id="requisição-http-2"></a>

#### Requisição HTTP

```http
PUT {{ENDPOINT_WEBHOOK}}/v1/Webhook/Cancel/{webhookId}
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_WEBHOOK}}/v1/Webhook/Cancel/{{webhookId}}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Put.new(url)
request["merchantId"] = "{{merchantId}}"
request["Authorization"] = "Bearer {{accessToken}}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_WEBHOOK}}/v1/Webhook/Cancel/{{webhookId}}"

payload={}
headers = {
  'merchantId': '{{merchantId}}',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location -g --request PUT '{{ENDPOINT_WEBHOOK}}/v1/Webhook/Cancel/{{webhookId}}' \
--header 'merchantId: {{merchantId}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("merchantId", "{{merchantId}}");
myHeaders.append("Authorization", "Bearer {{accessToken}}");

var requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("{{ENDPOINT_WEBHOOK}}/v1/Webhook/Cancel/{{webhookId}}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "success": true,
    "errors": [],
    "traceKey": "9563608b-408b-4a21-bb22-ced4d2eb1d81"
}
```

O endpoint responsável por cancelar notificação webhook por ID.

<a id="requisição-2"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| webhookId | string | Sim | O ID único do Webhook. |

<a id="resposta-2"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Não |
| errors.message | string | Não |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | Use o Merchant Token para gerar o `accessToken` do ENDPOINT_GATEWAY. |

<a id="webhookcall"></a>

#### `WebhookCall`

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| ChargeId | string | Sim | ID da cobrança. |
| MerchantId | string | Sim | ID do estabelecimento. |
| Nsu | string | Sim | Código da cobrança criado pela Safrapay, **não utilizado pelo e-commerce**. |
| CustomerId | string | Sim | ID do comprador. |
| ShippingAddress | Address | Condicional | Endereço de entrega. Presente se houver entrega configurada no checkout / link de pagamento. |
| Source | PaymentSource | Sim | [Origem da cobrança](../guias/primeiros-passos.md#paymentsource). |
| SmartCheckoutId | string | Sim | ID do checkout / link de pagamentos. |
| Transactions | WebhookTransaction | Sim | Informações das transações na cobrança. |
| ChargeStatus | ChargeStatus | Sim | Status atualizado da cobrança. |

<a id="webhooktransaction"></a>

#### `WebhookTransaction`

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| Card | ShortCard | Condicional | Dados não sensíveis do cartão. Presente se a transação foi de cartão de crédito / débito. |
| SoftDescriptor | string | Sim | Descrição no extrato bancário do comprador. |
| TransactionStatus | TransactionStatus | Sim | [Status atualizado da transação](../guias/primeiros-passos.md#transactionstatus). |
| IsApproved | bool | Sim | Se a transação está aprovada. |
| PaymentType | PaymentType | Sim | [Tipo de pagamento da transação](../guias/primeiros-passos.md#paymenttype). |
| InstallmentNumber | int | Condicional | Numero de parcelas na transação. Presente se a transação foi parcelada. |
| InstallmentType | InstallmentType | Sim | [Tipo de parcelamento da transação](../guias/primeiros-passos.md#installmenttype). |
| AcquirerCode | AcquirerCode | Sim | [Adquirente que autorizou a transação](../guias/primeiros-passos.md#acquirercode). |
| Amount | int | Sim | Valor da transação em centavos. |
| IsCapture | bool | Sim | Se a transação foi capturada. |
| IsRecurrency | bool | Sim | Se a transação é recorrente. |
| IsCanceled | bool | Sim | Se a transação foi cancelada. |
| TransactionId | string | Sim | Número Sequencial Único (NSU) da autorização, caso o pagamento seja aprovado pelo Emissor. |
| MerchantOrderId | string | Opcional | ID da cobrança definido pelo integrador. Se não utilizado, a Safrapay atribui valor aleatório. |
| CreationDateTime | string | Sim | Data da criação da transação no formato DD/MM/AAAA HH:MM:SS. |
| CaptureDateTime | string | Sim | Data da captura da transação no formato DD/MM/AAAA HH:MM:SS. |
| CancelStatus | CancelStatus | Condicional | [Status do cancelamento. Presente se a transação foi cancelada](../guias/primeiros-passos.md#cancelstatus). |
