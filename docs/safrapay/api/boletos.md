---
title: "Boletos"
parent: "Referência da API"
nav_order: 50
layout: "doc"
permalink: "/api/boletos/"
description: "Antes da utilização da API de geração de cobranças por boleto bancários, é necessário acionar o Executivo Comerial da conta para habilitar/contratar o serviço de boleto no banco."
source: "bankslip.html"
---

# BOLETOS

<a id="habilitação-de-boleto"></a>

## Habilitação de Boleto

Antes da utilização da API de geração de cobranças por boleto bancários, é necessário acionar o Executivo Comerial da conta para habilitar/contratar o serviço de boleto no banco.

<a id="informações-importante"></a>

## Informações importante

Ao gerar o Boleto via API, a data de vencimento pode ser definida no momento da requisição.

<a id="criação-de-cobrança-por-boleto"></a>

## Criação de cobrança por boleto

Este endpoint é responsável pela criação de uma nova cobrança com o meio de pagamento **Boleto Bancário**.

<a id="post-charge-boleto"></a>

### `POST` /charge/boleto

**Versão** `v2.0`

<a id="requisição-http"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}v2/charge/boleto
```

> Exemplo de requisição

```ruby
require "uri"
require "json"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/charge/boleto")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "charge": {
    "deadline": "2021-06-22",
    "customer": {
      "name": "Jorge Felipe",
      "email": "jorginho.felps@email.com.br",
      "entityType": 1,
      "documentType": 1,
      "document": "38000266350",
      "Address": {
        "street": "Av das dores",
        "number": "99",
        "neighborhood": "Vila Mança",
        "city": "Rio de Janeiro",
        "state": "RJ",
        "country": "BR",
        "zipCode": "212240080"
      },
      "phone": {
        "countryCode": "55",
        "areaCode": "21",
        "number": "999999999",
        "type": 5
      }
    },
    "transactions": [
      {
        "amount": 1000,
        "instructions": "Pagamento até o vencimento"
      }
    ],
    "source": 7
  }
})

response = https.request(request)
puts response.read_body
```

```python
import requests
import json

url = "{{ENDPOINT_GATEWAY}}/v2/charge/boleto"

payload = json.dumps({
  "charge": {
    "deadline": "2021-06-22",
    "customer": {
      "name": "Jorge Felipe",
      "email": "jorginho.felps@email.com.br",
      "entityType": 1,
      "documentType": 1,
      "document": "38000266350",
      "Address": {
        "street": "Av das dores",
        "number": "99",
        "neighborhood": "Vila Mança",
        "city": "Rio de Janeiro",
        "state": "RJ",
        "country": "BR",
        "zipCode": "212240080"
      },
      "phone": {
        "countryCode": "55",
        "areaCode": "21",
        "number": "999999999",
        "type": 5
      }
    },
    "transactions": [
      {
        "amount": 1000,
        "instructions": "Pagamento até o vencimento"
      }
    ],
    "source": 7
  }
})
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/charge/boleto' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "charge": {
        "deadline": "2021-06-22",
        "customer": {
            "name": "Jorge Felipe",
            "email": "jorginho.felps@email.com.br",
            "entityType": 1,
            "documentType": 1,
            "document": "38000266350",
            "Address": {
                "street": "Av das dores",
                "number": "99",
                "neighborhood": "Vila Mança",
                "city": "Rio de Janeiro",
                "state": "RJ",
                "country": "BR",
                "zipCode": "212240080"
            },
            "phone": {
                "countryCode": "55",
                "areaCode": "21",
                "number": "999999999",
                "type": 5
            }
        },
        "transactions": [
            {
                "amount": 1000,
                "instructions": "Pagamento até o vencimento"
            }
        ],
        "source": 7
    }
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "charge": {
    "deadline": "2021-06-22",
    "customer": {
      "name": "Jorge Felipe",
      "email": "jorginho.felps@email.com.br",
      "entityType": 1,
      "documentType": 1,
      "document": "38000266350",
      "Address": {
        "street": "Av das dores",
        "number": "99",
        "neighborhood": "Vila Mança",
        "city": "Rio de Janeiro",
        "state": "RJ",
        "country": "BR",
        "zipCode": "212240080"
      },
      "phone": {
        "countryCode": "55",
        "areaCode": "21",
        "number": "999999999",
        "type": 5
      }
    },
    "transactions": [
      {
        "amount": 1000,
        "instructions": "Pagamento até o vencimento"
      }
    ],
    "source": 7
    "metadata": [
      {
        "key": "metadata.0.key",
        "value": "metadata.0.value"
      }
    ]
  }
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/charge/boleto", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "charge": {
        "id": "0b2edbfb-4770-43f6-afa8-af30d7ff8fc5",
        "chargeStatus": "PreAuthorized",
        "transactions": [
            {
                "aditumNumber": "0000000421     ",
                "transactionId": "0000000000094",
                "digitalLine": "03399000378200000000000009401019686590000001000",
                "barcode": "03396865900000020009000381000000000000940101",
                "bankSlipId": "0000000000094",
                "deadline": "2021-06-22T00:00:00",
                "paymentType": "Boleto",
                "amount": 1000,
                "transactionStatus": "PendingPayment",
                "bankIssuerId": "Santander",
                "bankErrorMessage": "00000 - Título registrado em cobrança",
                "bankErrorCode": "0",
                "creationDateTime": "2021-06-18T23:37:14.6061259Z",
                "bankSlipUrl": "/v2/charge/0b2edbfb-4770-43f6-afa8-af30d7ff8fc5/boleto/0000000000094",
                "virtualAcquirerId": "df61a4d2-d04c-4575-8713-26d6dbd50560"
            }
        ]
    },
    "success": true,
    "errors": [],
    "traceKey": "e280c533-4327-4d4f-b2b3-a78ac75a1fb9"
}
```

O Endpoint responsável por criar uma nova cobrança em boleto.

<a id="requisição"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| charge.merchantChargeId | string | Não | ID de cobrança definido pelo sistema do comerciante. |
| charge.sessionId | string | Não | ID da sessão criada pelo servidor do site do cliente e usada durante a visita de um determinado usuário. |
| charge.deadline | string | Sim | Vencimento do boleto. |
| charge.smartCheckoutId | string | Não | ID Smart Checkout, se aplicável. |
| charge.customerId | string | Não | ID do cliente que foi adicionado anteriormente para o comerciante. |
| charge.customer | - | Sim | Dados do comprador. |
| charge.customer.name | string | Sim | Nome completo do comprador. |
| charge.customer.email | string | Sim | E-mail do comprador. |
| charge.customer.entityType | int | Sim | **[Se é pessoa física ou jurídica](../guias/primeiros-passos.md#entitytype).** |
| charge.customer.documentType | documentType | Sim | **[Tipo do documento do comprador](../guias/primeiros-passos.md#documenttype).** |
| charge.customer.document | string | Sim | Documento do comprador. |
| charge.customer.phone | object | Sim | Telefone do comprador. |
| charge.customer.phone.countryCode | string | Sim | Código do país. |
| charge.customer.phone.areaCode | string | Sim | Código de área. |
| charge.customer.phone.number | string | Sim | Número do Telefone. |
| charge.customer.phone.type | PhoneType | Sim | **[Tipo do telefone](../guias/primeiros-passos.md#phone).** |
| charge.customer.address | object | Não | Endereço do comprador. |
| charge.customer.address.street | string | Sim | Rua. |
| charge.customer.address.number | string | Sim | Número. |
| charge.customer.address.neighborhood | string | Sim | Bairro. |
| charge.customer.address.city | string | Sim | Cidade. |
| charge.customer.address.state | string | Sim | Estado. |
| charge.customer.address.country | string | Sim | País. |
| charge.customer.address.zipCode | string | Sim | CEP. |
| charge.customer.address.complement | string | Sim | Complemento. |
| charge.transactions | - | Sim | Uma ou várias transações a serem realizadas dentro da cobrança. |
| charge.transactions.amount | int | Sim | Valor em centavos do boleto. |
| charge.transactions.fine.startDate | string | Sim | Data de início que multa começará a contar. |
| charge.transactions.fine.amount | int | Sim | Valor a ser pago após a data de vencimento. |
| charge.transactions.fine.interest | int | Sim | Os juros financeiros representam um valor em porcentagem que será calculado todos os dias após a data de vencimento. |
| charge.transactions.discount.type | int | Sim | **[Tipo de desconto](../guias/primeiros-passos.md#discounttype).** |
| charge.transactions.discount.amount | int | Sim | Valor em centavos ou porcentagem com base no tipo de desconto. |
| charge.transactions.discount.deadline | string | Sim | Data limite em que o desconto pode ser aplicado. |
| charge.transactions.instructions | string | Não | Instruções de 255 caracteres a serem adicionadas no boleto bancário. |
| charge.source | int | Sim | **[Define a fonte de cobrança](../guias/primeiros-passos.md#paymentsource).** |
| charge.origin | string | Não | Uma propriedade que o cliente pode usar para identificar a origem da cobrança, como nome do fornecedor ou identificador. |
| charge.metadata | array(object) | Não | Entradas coletadas para iniciação do evento. |
| charge.metadata.key | string | Não | O nome da chave (campo) |
| charge.metadata.value | string | Não | O valor da chave. |

<a id="resposta"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| charge.merchantChargeId | string | ID de cobrança definido pelo sistema do comerciante. |
| charge.id | string | O ID da cobrança. |
| charge.chargeStatus | string | Indica o status da cobrança. |
| charge.transactions.aditumNumber | string | Número transacional. |
| charge.transactions.transactionId | string | Número Sequencial Único (NSU) da autorização, caso o pagamento seja aprovado pelo Emissor. |
| charge.transactions.digitalLine | string | Uma linha de transmissão que usa apenas código binário para recepção e emissão. |
| charge.transactions.barcode | string | O código de barras do boleto. |
| charge.transactions.bankSlipId | string | O ID do boleto. |
| charge.transactions.deadline | string | Data de vencimento do boleto. |
| charge.transactions.paymentType | string | Tipo de pagamento. |
| charge.transactions.amount | int | Valor a pagar do boleto. |
| charge.transactions.transactionStatus | string | Indica o status da transação. |
| charge.transactions.bankIssuerId | string | O nome do banco. |
| charge.transactions.bankErrorMessage | string | A mensagem de erro enviada do banco. |
| charge.transactions.bankErrorCode | string | O código do erro enviado do banco. |
| charge.transactions.creationDateTime | string | A data de criação da cobrança. |
| charge.transactions.bankSlipUrl | string | O url da cobrança. |
| charge.transactions.fine.startDate | string | Data de início que multa começará a contar. |
| charge.transactions.fine.amount | int | Valor a ser pago após a data de vencimento. |
| charge.transactions.fine.interest | int | Os juros financeiros representam um valor em porcentagem que será calculado todos os dias após a data de vencimento. |
| charge.transactions.discount.type | int | **[Tipo de desconto](../guias/primeiros-passos.md#discounttype).** |
| charge.transactions.discount.amount | int | Valor em centavos ou porcentagem com base no tipo de desconto. |
| charge.transactions.discount.deadline | string | Data limite em que o desconto pode ser aplicado. |
| charge.transactions.virtualAcquirerId | string | O adquirente virtual da taxa sobre boleto bancário. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

<a id="body-raw"></a>

#### BODY Raw

```http
{
    "charge": {
        "deadline": "2021-06-22",
        "customer": {
            "name": "Yago Sebastião Lima",
            "email": "yagosebastiaolima@archosolutions.com.br",
            "entityType": 1,
            "documentType": 1,
            "document": "38000266350",
            "Address": {
                "street": "RUA ALEKRIN",
                "number": "99",
                "neighborhood": "Parque Residencial Nova Fronteira",
                "city": "Gurupi",
                "state": "BA",
                "country": "BR",
                "zipCode": "212211150"
            },
            "phone": {
                "countryCode": "55",
                "areaCode": "21",
                "number": "999999999",
                "type": 5
            }
        },
        "transactions": [
            {
                "amount": 1000,
                "instructions": "Pagamento até o vencimento",
            }
        ],
        "source": 7
    }
}
```

<a id="baixando-o-boleto-bancário-em-pdf"></a>

## Baixando o boleto bancário em PDF

<a id="get-charge-chargeid-boleto-transactionid"></a>

### `GET` /charge/{{chargeId}}/boleto/{{transactionId}}

**Versão** `v2.0`

<a id="requisição-http-1"></a>

#### Requisição HTTP

```http
GET {{ENDPOINT_GATEWAY}}/v2/charge/{{chargeId}}/boleto/{{{transactionId}}
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/charge/{{chargeId}}/boleto/{{transactionId}}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/charge/{{chargeId}}/boleto/{{transactionId}}"

payload={}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location -g --request GET '{{ENDPOINT_GATEWAY}}/v2/charge/{{chargeId}}/boleto/{{transactionId}}' \
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

fetch("{{ENDPOINT_GATEWAY}}/v2/charge/{{chargeId}}/boleto/{{transactionId}}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

O Endpoint responsável por gerar um arquivo em .pdf com os dados do boleto.

<a id="requisição-1"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| chargeId | string | Sim | O ID da cobrança. |
| transactionId | string | Sim | Número Sequencial Único (NSU) da autorização, caso o pagamento seja aprovado pelo Emissor. |

<a id="resposta-1"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| Boleto | PDF | Resposta retorna um boleto em .pdf. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

| PARAMS | - |
| --- | --- |
| **chargeId** | {{chargeId}} |
| -- | O ID da cobrança. |
| **transactionId** | {{transactionId}} |
| -- | O ID da transação. |
