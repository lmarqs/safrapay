---
title: "Taxas"
parent: "Referência da API"
nav_order: 60
layout: "doc"
permalink: "/api/taxas/"
description: "As taxas que serão utilizadas nas transações do gateway."
source: "taxes.html"
---

# Taxas

As taxas que serão utilizadas nas transações do gateway.

<a id="post-tax"></a>

### `POST` /tax

**Versão** `v2.0`

<a id="requisição-http"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/tax
```

> Exemplo de requisição (`Plano de Taxas`)

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/tax")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n  \"acquirer\": 999,\r\n  \"name\": \"Plano de Taxa\",\r\n  \"parentTax\": \"b265018d-b935-5de5-85cf-d805be8ba5cf\",\r\n  \"taxes\": [\r\n    {\r\n        \"paymentType\": 2,\r\n        \"isInInstallment\": false,\r\n        \"upsellAnticipationTax\": 1.0,\r\n        \"upsellTax\": 1.0,\r\n        \"cardBrand\": 2,\r\n        \"priority\": 1\r\n    }\r\n  ],\r\n  \"aditumProduct\": 1\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/tax"

payload="{\r\n  \"acquirer\": 999,\r\n  \"name\": \"Plano de Taxa\",\r\n  \"parentTax\": \"b265018d-b935-5de5-85cf-d805be8ba5cf\",\r\n  \"taxes\": [\r\n    {\r\n        \"paymentType\": 2,\r\n        \"isInInstallment\": false,\r\n        \"upsellAnticipationTax\": 1.0,\r\n        \"upsellTax\": 1.0,\r\n        \"cardBrand\": 2,\r\n        \"priority\": 1\r\n    }\r\n  ],\r\n  \"aditumProduct\": 1\r\n}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/tax' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "acquirer": 999,
  "name": "Plano de Taxa",
  "parentTax": "b265018d-b935-5de5-85cf-d805be8ba5cf",
  "taxes": [
    {
        "paymentType": 2,
        "isInInstallment": false,
        "upsellAnticipationTax": 1.0,
        "upsellTax": 1.0,
        "cardBrand": 2,
        "priority": 1
    }
  ],
  "aditumProduct": 1
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"acquirer":999,"name":"Plano de Taxa","parentTax":"b265018d-b935-5de5-85cf-d805be8ba5cf","taxes":[{"paymentType":2,"isInInstallment":false,"upsellAnticipationTax":1,"upsellTax":1,"cardBrand":2,"priority":1}],"aditumProduct":1});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/tax", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> Exemplo de requisição (`Taxa Base`)

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/tax")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n  \"acquirer\": 999,\r\n  \"name\": \"Taxa Base\",\r\n  \"taxes\": [\r\n    {\r\n        \"paymentType\": 2,\r\n        \"isInInstallment\": false,\r\n        \"anticipationTax\": 1.0,\r\n        \"taxPercentage\": 1.0,\r\n        \"cardBrand\": 2,\r\n        \"priority\": 1\r\n    }\r\n  ],\r\n  \"aditumProduct\": 1,\r\n  \"mccs\": [\r\n      \"763\"\r\n  ],\r\n  \"receivableMode\": 1\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/tax"

payload="{\r\n  \"acquirer\": 999,\r\n  \"name\": \"Taxa Base\",\r\n  \"taxes\": [\r\n    {\r\n        \"paymentType\": 2,\r\n        \"isInInstallment\": false,\r\n        \"anticipationTax\": 1.0,\r\n        \"taxPercentage\": 1.0,\r\n        \"cardBrand\": 2,\r\n        \"priority\": 1\r\n    }\r\n  ],\r\n  \"aditumProduct\": 1,\r\n  \"mccs\": [\r\n      \"763\"\r\n  ],\r\n  \"receivableMode\": 1\r\n}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/tax' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "acquirer": 999,
  "name": "Taxa Base",
  "taxes": [
    {
        "paymentType": 2,
        "isInInstallment": false,
        "anticipationTax": 1.0,
        "taxPercentage": 1.0,
        "cardBrand": 2,
        "priority": 1
    }
  ],
  "aditumProduct": 1,
  "mccs": [
      "763"
  ],
  "receivableMode": 1
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"acquirer":999,"name":"Taxa Base","taxes":[{"paymentType":2,"isInInstallment":false,"anticipationTax":1,"taxPercentage":1,"cardBrand":2,"priority":1}],"aditumProduct":1,"mccs":["763"],"receivableMode":1});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/tax", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

> Resposta (`Plano de Taxas`)

```json
{
    "taxes": {
        "id": "27dcaa67-ec5e-4975-97fe-6396534506a4",
        "isActive": true,
        "acquirer": "Simulator",
        "name": "Plano de Taxa",
        "parentTax": "b265018d-b935-4de6-75cf-d805be8ba5cf",
        "taxes": [
            {
                "paymentType": "Credit",
                "isInInstallment": false,
                "upsellAnticipationTax": 1.0,
                "upsellTax": 1.0,
                "cardBrand": "MasterCard",
                "priority": 1
            }
        ],
        "aditumProduct": "Ecommerce",
        "receivableMode": "Default",
        "mccs": [
            "763"
        ]
    },
    "success": true,
    "errors": [],
    "traceKey": "427c9a57-3225-4f6f-9590-b60f13f57d02"
}
```

> Resposta (`Taxa Base`)

```json
{
    "taxes": {
        "id": "b265018d-b936-7de5-85cf-d805be8ba5cf",
        "isActive": true,
        "acquirer": "Simulator",
        "name": "Taxa Base",
        "taxes": [
            {
                "paymentType": "Credit",
                "isInInstallment": false,
                "taxPercentage": 1.0,
                "anticipationTax": 1.0,
                "cardBrand": "MasterCard",
                "priority": 1
            }
        ],
        "aditumProduct": "Ecommerce",
        "receivableMode": "Default",
        "mccs": [
            "763"
        ]
    },
    "success": true,
    "errors": [],
    "traceKey": "91ce694e-4e7d-48ed-9cc4-ace6e68fd787"
}
```

Endpoint responsável por criar um novo plano de taxas. Esse plano de taxas será utilizado pelo gateway para identificar adquirente a processar uma transação especifica. O gateway utiliza a propriedade `priority` para priorizar cada taxa, sendo a prioridade mais alta `1`.

Exemplo:

A `LOJA_EXEMPLO` suporta as adquirentes `ADQ_A` e `ADQ_B`, sendo que a `ADQ_B` é tem uma taxa mais baixa para transações de crédito a vista Elo. Nesse caso, a taxa da `ADQ_B` para crédito a vista deve ter `priority 1` enquanto a `ADQ_A` tem prioridade `priority 2`.

Em suma, o plano de taxas pode ser utilizado como uma ferramenta flexível de priorização e roteamento de transações.

<a id="requisição"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| acquirer | int | Sim | [O ID da adquirente.](../guias/primeiros-passos.md#acquirercode). |
| name | string | Sim | O nome da adquirente. |
| parentTax | string | Não | O ID de uma outra taxa, usado para venda. |
| taxes | array(object) | Sim | Lista de taxas para o comerciante, definida por cada adquirente. |
| taxes.paymentType | string | Sim | [Tipo de transação.](../guias/primeiros-passos.md#paymenttype) |
| taxes.isInInstallment | bool | Sim | Se a estratégia está relacionada a um tipo de transação instalado ou não. |
| taxes.installmentRange | object | Sim | Informalções da faixa de parcelamento, em um crédito tributário, de 2 a 6x ou de 7 a 12x. |
| taxes.installmentRange.minimum | int | Sim | Parcela mínima. |
| taxes.installmentRange.maximum | int | Sim | Parcela máxima. |
| taxes.taxPercentage | float | Sim | Percentual de taxa definido pelo adquirente. Pode ser nulo se o plano de taxas tiver taxa pai. |
| taxes.anticipationTax | float | Sim | Define a percentagem a cobrar quando o valor é antecipado. Pode ser nulo se o plano de taxas tiver taxa parental. |
| taxes.upsellAnticipationTax | float | Sim | Upsell antecipado, usado para cobrança do parceiro e recebimento do valor pela antecipação da transação. Precisa ser preenchido quando houver ParentTax. |
| taxes.upsellTax | number | Sim | A porcentagem do parceiro a ser cobrada e somará `ParentTax.TaxPercentage` ou `ParentTax.UpsellTax` se `parenttax` tiver pai. |
| taxes.cardBrand | int | Sim | [A bandeira do cartão à qual o imposto se aplica.](../guias/primeiros-passos.md#cardbrand). |
| taxes.priority | int | Sim | É um número inteiro positivo, cujo valor mais alto é 1. |
| virtualAcquirerId | string | Não | Campo opcional referent ao adquirente virtual. Usado em casos onde o comércio age como sub comércio. |
| aditumProduct | int | Sim | É produto relacionado ao plano de taxas. |
| receivableMode | int | Sim | Modo de recebimento configurado para o plano de taxa. |
| mccs | array(string) | Não | Código de Categoria do comerciante (MCC) é um número de 4 dígitos listado na ISO 18245 para serviços financeiro de varejo. MCC é usado para classificar o negócio pelo tipo de bens ou serviços que é ofertado. |

<a id="resposta"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| acquirer | int | [O ID da adquirente.](../guias/primeiros-passos.md#acquirercode). |
| name | string | O nome da adquirente. |
| taxes | Taxes | Lista de taxas para o comerciante, definida por cada adquirente. |
| taxes.paymentType | string | [Tipo de transação.](../guias/primeiros-passos.md#paymenttype). |
| taxes.isInInstallment | bool | Se a estratégia está relacionada a um tipo de transação instalado ou não. |
| taxes.installmentRange | array | Define faixa de parcelamento, em um crédito tributário, de 2 a 6x ou de 7 a 12x. |
| taxes.taxPercentage | number | Percentual de taxa definido pelo adquirente. Pode ser nulo se o plano de taxas tiver taxa pai. |
| taxes.anticipationTax | number | define a percentagem a cobrar quando o valor é antecipado. Pode ser nulo se o plano de taxas tiver taxa parental |
| taxes.upsellTax | number | A porcentagem do parceiro a ser cobrada e somará `ParentTax.TaxPercentage` ou `ParentTax.UpsellTax` se `parenttax` tiver pai. |
| taxes.cardBrand | int | [A bandeira do cartão à qual o imposto se aplica.](../guias/primeiros-passos.md#cardbrand). |
| taxes.priority | int | É um número inteiro positivo, cujo valor mais alto é 1. |
| aditumProduct | int | É produto relacionado ao plano de taxas. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

<a id="body-raw"></a>

#### BODY Raw

***Plano de Taxas***

```http
{
"acquirer": 999,
"name": "Plano de Taxa",
"parentTax": "b265018d-b935-5de5-85cf-d805be8ba5cf",
"taxes": [
{
"paymentType": 2,
"isInInstallment": false,
"upsellAnticipationTax": 1.0,
"upsellTax": 1.0,
"cardBrand": 2,
"priority": 1
},
{
"paymentType": 2,
"isInInstallment": true,
"installmentRange": {
"minimum": 2,
"maximum": 6
},
"upsellAnticipationTax": 1.0,
"upsellTax": 1.0,
"cardBrand": 2,
"priority": 1
},
{
"paymentType": 2,
"isInInstallment": true,
"installmentRange": {
"minimum": 7,
"maximum": 12
},
"upsellAnticipationTax": 1.0,
"upsellTax": 1.0,
"cardBrand": 2,
"priority": 1
}
],
"aditumProduct": 1
}
```

***Taxa Base***

```http
{
"acquirer": 999,
"name": "Taxa Base",
"taxes": [
{
"paymentType": 2,
"isInInstallment": false,
"anticipationTax": 1.0,
"taxPercentage": 1.0,
"cardBrand": 2,
"priority": 1
},
{
"paymentType": 2,
"isInInstallment": true,
"installmentRange": {
"minimum": 2,
"maximum": 6
},
"anticipationTax": 1.0,
"taxPercentage": 1.0,
"cardBrand": 2,
"priority": 1
},
{
"paymentType": 2,
"isInInstallment": true,
"installmentRange": {
"minimum": 7,
"maximum": 12
},
"anticipationTax": 1.0,
"taxPercentage": 1.0,
"cardBrand": 2,
"priority": 1
}
],
"aditumProduct": 1,
"mccs": [
"763"
],
"receivableMode": 1
}
```

<a id="get-tax"></a>

### `GET` /tax

**Versão** `v2.0`

<a id="requisição-http-1"></a>

#### Requisição HTTP

```http
GET {{ENDPOINT_GATEWAY}}/v2/tax
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/tax")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/tax"

payload={}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request GET '{{ENDPOINT_GATEWAY}}/v2/tax' \
--header 'Authorization: Bearer {{accessToken}}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/tax", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "taxes": [
        {
            "id": "f7b04a26-1cd8-4bc0-ae89-e9b7254817eb",
            "isActive": true,
            "acquirer": "Simulator",
            "name": "Plano de Taxa Teste",
            "parentTax": "7833d91f-57f5-4ee6-8862-f390b698fdc2",
            "taxes": [
                {
                    "paymentType": "Credit",
                    "isInInstallment": false,
                    "upsellAnticipationTax": 1.0,
                    "upsellTax": 1.0,
                    "cardBrand": "MasterCard",
                    "priority": 1
                }
            ],
            "aditumProduct": "Ecommerce",
            "receivableMode": "Default"
        }
    ],
    "success": true,
    "errors": [],
    "traceKey": "6aa471e4-dc69-4c1a-a64d-749a9791eaf3"
}
```

Endpoint responsável por obter todas as taxas cadastradas por um comerciante.

<a id="requisição-1"></a>

#### Requisição

Enviar a requisição http com a autorização no header.

<a id="resposta-1"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| id | string | O ID da taxa. |
| isActive | bool | Se a taxa está ativa ou não. |
| acquirer | int | [O ID da adquirente.](../guias/primeiros-passos.md#acquirercode). |
| name | string | O nome da adquirente. |
| parentTax | string | O ID de uma outra taxa, usado para venda. |
| taxes | Taxes | Lista de taxas para o comerciante, definida por cada adquirente. |
| taxes.paymentType | string | [Tipo de transação.](../guias/primeiros-passos.md#paymenttype) |
| taxes.isInInstallment | bool | Se a estratégia está relacionada a um tipo de transação instalado ou não. |
| taxes.installmentRange | array | Define faixa de parcelamento, em um crédito tributário, de 2 a 6x ou de 7 a 12x. |
| taxes.upsellTax | number | A porcentagem do parceiro a ser cobrada e somará `ParentTax.TaxPercentage` ou `ParentTax.UpsellTax` se `parenttax` tiver pai. |
| taxes.cardBrand | int | [A bandeira do cartão à qual o imposto se aplica.](../guias/primeiros-passos.md#cardbrand). |
| taxes.priority | int | É um número inteiro positivo, cujo valor mais alto é 1. |
| aditumProduct | int | É produto relacionado ao plano de taxas. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

<a id="put-tax"></a>

### `PUT` /tax

**Versão** `v2.0`

<a id="requisição-http-2"></a>

#### Requisição HTTP

```http
PUT {{ENDPOINT_GATEWAY}}/v2/tax
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/tax")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n  \"taxes\": [\r\n    {\r\n        \"id\": \"f7b04a26-1cd0-4bc9-ae89-e9b7254817eb\",\r\n        \"isActive\": true,\r\n        \"acquirer\": 999,\r\n        \"name\": \"Plano de Taxa\",\r\n        \"parentTax\": \"7833d91f-47f5-5ee7-8862-f390b698fdc2\",\r\n        \"taxes\": [\r\n            {\r\n                \"paymentType\": 2,\r\n                \"isInInstallment\": false,\r\n                \"upsellAnticipationTax\": 1.0,\r\n                \"upsellTax\": 1.0,\r\n                \"cardBrand\": 2,\r\n                \"priority\": 1\r\n            }\r\n        ],\r\n        \"aditumProduct\": 1,\r\n        \"receivableMode\": 1\r\n    }\r\n  ]\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/tax"

payload="{\r\n  \"taxes\": [\r\n    {\r\n        \"id\": \"f7b04a26-1cd0-4bc9-ae89-e9b7254817eb\",\r\n        \"isActive\": true,\r\n        \"acquirer\": 999,\r\n        \"name\": \"Plano de Taxa\",\r\n        \"parentTax\": \"7833d91f-47f5-5ee7-8862-f390b698fdc2\",\r\n        \"taxes\": [\r\n            {\r\n                \"paymentType\": 2,\r\n                \"isInInstallment\": false,\r\n                \"upsellAnticipationTax\": 1.0,\r\n                \"upsellTax\": 1.0,\r\n                \"cardBrand\": 2,\r\n                \"priority\": 1\r\n            }\r\n        ],\r\n        \"aditumProduct\": 1,\r\n        \"receivableMode\": 1\r\n    }\r\n  ]\r\n}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request PUT '{{ENDPOINT_GATEWAY}}/v2/tax' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "taxes": [
    {
        "id": "f7b04a26-1cd0-4bc9-ae89-e9b7254817eb",
        "isActive": true,
        "acquirer": 999,
        "name": "Plano de Taxa",
        "parentTax": "7833d91f-47f5-5ee7-8862-f390b698fdc2",
        "taxes": [
            {
                "paymentType": 2,
                "isInInstallment": false,
                "upsellAnticipationTax": 1.0,
                "upsellTax": 1.0,
                "cardBrand": 2,
                "priority": 1
            }
        ],
        "aditumProduct": 1,
        "receivableMode": 1
    }
  ]
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"taxes":[{"id":"f7b04a26-1cd0-4bc9-ae89-e9b7254817eb","isActive":true,"acquirer":999,"name":"Plano de Taxa","parentTax":"7833d91f-47f5-5ee7-8862-f390b698fdc2","taxes":[{"paymentType":2,"isInInstallment":false,"upsellAnticipationTax":1,"upsellTax":1,"cardBrand":2,"priority":1}],"aditumProduct":1,"receivableMode":1}]});

var requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/tax", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "taxes": [
        {
            "id": "f7b04a26-1cd0-4bc9-ae89-e9b7254817eb",
            "isActive": true,
            "acquirer": "Simulator",
            "name": "Plano de Taxa",
            "parentTax": "7833d91f-47f5-5ee7-8862-f390b698fdc2",
            "taxes": [
                {
                    "paymentType": "Credit",
                    "isInInstallment": false,
                    "upsellAnticipationTax": 1.0,
                    "upsellTax": 1.0,
                    "cardBrand": "MasterCard",
                    "priority": 1
                }
            ],
            "aditumProduct": "Ecommerce",
            "receivableMode": "Default"
        }
    ],
    "success": true,
    "errors": [],
    "traceKey": "ac17ebe6-3f8f-4a2f-ad54-d2d13a173dee"
}
```

O Endpoint responsável por atualizar as taxas.

<a id="requisição-2"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| taxes | array(object) | Sim | Dados de taxas a serem atualizadas. |
| taxes.id | string | Sim | O ID da taxa. |
| taxes.isActive | bool | Sim | Se a taxa está ativa ou não. |
| taxes.acquirer | int | Sim | [O ID da adquirente.](../guias/primeiros-passos.md#acquirercode). |
| taxes.name | string | Sim | O nome da adquirente. |
| taxes.parentTax | string | Sim | O ID de uma outra taxa, usado para venda. |
| taxes.taxes | array(object) | Sim | Lista de taxas para o comerciante, definida por cada adquirente. |
| taxes.taxes.paymentType | string | Sim | [Tipo de transação.](../guias/primeiros-passos.md#paymenttype) |
| taxes.taxes.isInInstallment | bool | Sim | Se a estratégia está relacionada a um tipo de transação instalado ou não. |
| taxes.taxes.installmentRange | object | Sim | Define faixa de parcelamento, em um crédito tributário, de 2 a 6x ou de 7 a 12x. |
| taxes.taxes.installmentRange.minimum | int | Sim | Parcela mínima. |
| taxes.taxes.installmentRange.maximum | int | Sim | Parcela máxima. |
| taxes.taxes.upsellTax | number | Sim | A porcentagem do parceiro a ser cobrada e somará `ParentTax.TaxPercentage` ou `ParentTax.UpsellTax` se `parenttax` tiver pai. |
| taxes.taxes.cardBrand | int | Sim | [A bandeira do cartão à qual o imposto se aplica.](../guias/primeiros-passos.md#cardbrand). |
| taxes.taxes.priority | int | Sim | É um número inteiro positivo, cujo valor mais alto é 1. |
| taxes.virtualAcquirerId | string | Não | Campo opcional referent ao adquirente virtual. Usado em casos onde o comércio é age como sub comércio. |
| taxes.aditumProduct | int | Sim | É produto relacionado ao plano de taxas. |
| taxes.receivableMode | int | Sim | Modo de recebimento configurado para o plano de taxa. |
| taxrs.mccs | array(string) | Não | Código de Categoria do comerciante (MCC) é um número de 4 dígitos listado na ISO 18245 para serviços financeiro de varejo. MCC é usado para classificar o negócio pelo tipo de bens ou serviços que é ofertado. |

<a id="resposta-2"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| id | string | O ID da taxa. |
| isActive | bool | Se a taxa está ativa ou não. |
| acquirer | int | [O ID da adquirente.](../guias/primeiros-passos.md#acquirercode). |
| name | string | O nome da adquirente. |
| parentTax | string | O ID de uma outra taxa, usado para venda. |
| taxes | Taxes | Lista de taxas para o comerciante, definida por cada adquirente. |
| taxes.paymentType | string | [Tipo de transação.](../guias/primeiros-passos.md#paymenttype) |
| taxes.isInInstallment | bool | Se a estratégia está relacionada a um tipo de transação instalado ou não. |
| taxes.installmentRange | array | Define faixa de parcelamento, em um crédito tributário, de 2 a 6x ou de 7 a 12x. |
| taxes.upsellTax | number | A porcentagem do parceiro a ser cobrada e somará `ParentTax.TaxPercentage` ou `ParentTax.UpsellTax` se `parenttax` tiver pai. |
| taxes.cardBrand | int | [A bandeira do cartão à qual o imposto se aplica.](../guias/primeiros-passos.md#cardbrand). |
| taxes.priority | int | É um número inteiro positivo, cujo valor mais alto é 1. |
| aditumProduct | int | É produto relacionado ao plano de taxas. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

<a id="body-raw-1"></a>

#### BODY Raw

```http
{
"taxes": [
{
"id": "f7b04a26-1cd0-4bc9-ae89-e9b7254817eb",
"isActive": true,
"acquirer": 999,
"name": "Plano de Taxa",
"parentTax": "7833d91f-47f5-5ee7-8862-f390b698fdc2",
"taxes": [
{
"paymentType": 2,
"isInInstallment": false,
"upsellAnticipationTax": 1.0,
"upsellTax": 1.0,
"cardBrand": 2,
"priority": 1
}
],
"aditumProduct": 1,
"receivableMode": 1
}
]
}
```

<a id="delete-tax-taxplanid"></a>

### `DELETE` /tax/{taxPlanId}

**Versão** `v2.0`

<a id="requisição-http-3"></a>

#### Requisição HTTP

```http
DELETE {{ENDPOINT_GATEWAY}}/v2/tax/{taxPlanId}
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/tax/{{taxPlanId}}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/tax/{{taxPlanId}}"

payload={}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location -g --request DELETE '{{ENDPOINT_GATEWAY}}/v2/tax/{{taxPlanId}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");

var requestOptions = {
  method: 'DELETE',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/tax/{{taxPlanId}}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "taxPlanId": "27dcaa67-ec3e-4974-97fe-6396534506a4",
    "success": true,
    "errors": [],
    "traceKey": "6f3490df-6afd-45db-8f72-d5aac3d6d2c5"
}
```

O Endpoint responsável por deletar as taxas de um comerciante.

<a id="parâmetros-de-rota"></a>

#### Parâmetros de rota

| Parâmetro | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| taxPlanId | string | Sim | O ID da taxa. |

<a id="resposta-3"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| taxPlandId | string | O ID da taxa. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

<a id="put-tax-activate-taxplanid"></a>

### `PUT` /tax/Activate/{{taxPlanId}}

**Versão** `v2.0`

<a id="requisição-http-4"></a>

#### Requisição HTTP

```http
PUT {{ENDPOINT_GATEWAY}}/v2/tax/Activate/{taxPlanId}
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/tax/Activate/{{taxPlanId}}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/tax/Activate/{{taxPlanId}}"

payload={}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location -g --request PUT '{{ENDPOINT_GATEWAY}}/v2/tax/Activate/{{taxPlanId}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");

var requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/tax/Activate/{{taxPlanId}}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "taxPlanId": "27dcaa67-ec5e-6994-97fe-6396534506a4",
    "success": true,
    "errors": [],
    "traceKey": "af7e0261-6412-483f-bec3-6525aa184df2"
}
```

O Endpoint responsável por ativar as taxas de um comerciante.

<a id="parâmetros-de-rota-1"></a>

#### Parâmetros de rota

| Parâmetro | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| taxPlanId | string | Sim | O ID da taxa. |

<a id="resposta-4"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| taxPlandId | string | O ID da taxa. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |
