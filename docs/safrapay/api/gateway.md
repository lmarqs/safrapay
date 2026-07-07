---
title: "Pagamentos (Gateway)"
parent: "Referência da API"
nav_order: 20
layout: "doc"
permalink: "/api/gateway/"
description: "Infraestrutura tecnológica para integrar a sua loja na internet com todos os meios de pagamentos. Isto é: com as bandeiras de cartão de crédito e débito e com b"
source: "gateway.html"
---

# PAGAMENTOS

Infraestrutura tecnológica para integrar a sua loja na internet com todos os meios de pagamentos. Isto é: com as bandeiras de cartão de crédito e débito e com bancos.

<a id="compradores"></a>

## Compradores

Os clientes que serão cadastrados no sistema para serem relacionados a suas transações futuras.

<a id="post-customer"></a>

### `POST` /customer

**Versão** `v2.0`

<a id="requisição-http"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/customer
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/customer")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n  \"customer\": {\r\n    \"name\": \"Yago Sebastião Lima\",\r\n    \"email\": \"yagosebastiaolima@archosolutions.com.br\",\r\n    \"entityType\": 1,\r\n    \"documentType\": 1,\r\n    \"document\": \"78112482802\",\r\n    \"phone\": {\r\n      \"countryCode\": \"55\",\r\n      \"areaCode\": \"21\",\r\n      \"number\": \"999999999\",\r\n      \"type\": 5\r\n    }\r\n  }\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/customer"

payload="{\r\n  \"customer\": {\r\n    \"name\": \"Yago Sebastião Lima\",\r\n    \"email\": \"yagosebastiaolima@archosolutions.com.br\",\r\n    \"entityType\": 1,\r\n    \"documentType\": 1,\r\n    \"document\": \"78112482802\",\r\n    \"phone\": {\r\n      \"countryCode\": \"55\",\r\n      \"areaCode\": \"21\",\r\n      \"number\": \"999999999\",\r\n      \"type\": 5\r\n    }\r\n  }\r\n}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/customer' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "customer": {
    "name": "Yago Sebastião Lima",
    "email": "yagosebastiaolima@archosolutions.com.br",
    "entityType": 1,
    "documentType": 1,
    "document": "78112482802",
    "phone": {
      "countryCode": "55",
      "areaCode": "21",
      "number": "999999999",
      "type": 5
    }
  }
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"customer":{"name":"Yago Sebastião Lima","email":"yagosebastiaolima@archosolutions.com.br","entityType":1,"documentType":1,"document":"78112482802","phone":{"countryCode":"55","areaCode":"21","number":"999999999","type":5}}});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/customer", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "customer": {
        "id": "ffede3ee-37ab-47bb-9981-d4d14697d67a",
        "name": "Yago Sebastião Lima",
        "email": "yagosebastiaolima@archosolutions.com.br",
        "entityType": "IndividualMerchant",
        "documentType": "Cpf",
        "document": "78112482802",
        "gender": "Undefined",
        "phone": {
            "countryCode": "55",
            "areaCode": "21",
            "number": "999999999",
            "type": "Mobile"
        }
    },
    "success": true,
    "errors": [],
    "traceKey": "496e22bd-0690-489c-a88f-9c1fd4e64d62"
}
```

O Endpoint responsável por criar um novo comprador.

<a id="requisição"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| customer | object | Sim | Dados do comprador. |
| customer.name | string | Sim | Nome completo do comprador. |
| customer.email | string | Sim | E-mail do comprador. |
| customer.entityType | entityType | Sim | Se é pessoa física ou jurídica |
| customer.documentType | documentType | Sim | Tipo do documento do comprador. |
| customer.document | string | Sim | Documento do comprador. |
| customer.birthday | date | Não | Data de nascimento do comprador. |
| customer.gender | Gender | Não | Gênero do comprador. |
| customer.phone | object | Sim | Telefone do comprador. |
| customer.phone.countryCode | string | Sim | Código do país. |
| customer.phone.areaCode | string | Sim | Código de área. |
| customer.phone.number | string | Sim | Número do Telefone. |
| customer.phone.type | PhoneType | Sim | Tipo do telefone. |
| customer.address | object | Não | Endereço do comprador. |
| customer.address.street | string | Sim | Rua. |
| customer.address.number | string | Sim | Número. |
| customer.address.neighborhood | string | Sim | Bairro. |
| customer.address.city | string | Sim | Cidade. |
| customer.address.state | string | Sim | Estado. |
| customer.address.country | string | Sim | País. |
| customer.address.zipCode | string | Sim | CEP. |
| customer.address.complement | string | Sim | Complemento. |
| customer.bankAccounts | object | Não | Contas do comprador. |
| customer.bankAccounts.bankCode | string | Sim | Código do banco. |
| customer.bankAccounts.bankName | string | Não | Nome do banco. |
| customer.bankAccounts.branch | string | Não | Filial. |
| customer.bankAccounts.branchCheckDigit | string | Não | Dígito de verificação da filial. |
| customer.bankAccounts.account | string | Não | Conta bancária. |
| customer.bankAccounts.accountCheckDigit | string | Não | Dígito de verificação da conta bancária. |
| customer.bankAccounts.type | int | Sim | Tipo de conta. |
| customer.bankAccounts.isActive | bool | Sim | Se a conta está ativa ou não. |
| customer.isActive | bool | Não | Se o usuário é ativo ou não. |

<a id="resposta"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| id | string | O ID do comprador |
| name | string | Nome completo do comprador. |
| email | string | E-mail do comprador. |
| entityType | entityType | Se é pessoa física ou jurídica. |
| documentType | documentType | Tipo do documento do comprador. |
| document | string | Documento do comprador. |
| birthday | date | Data de nascimento do comprador. |
| gender | Gender | Gênero do comprador. |
| phone | object | Telefone do comprador. |
| phone.countryCode | string | Código do país. |
| phone.areaCode | string | Código de área. |
| phone.number | string | Número do Telefone. |
| phone.type | PhoneType | Tipo do telefone |
| address | object | Endereço do comprador. |
| address.street | string | Rua. |
| address.number | string | Número. |
| address.neighborhood | string | Bairro. |
| address.city | string | Cidade. |
| address.state | string | Estado. |
| address.country | string | País. |
| address.zipCode | string | CEP. |
| address.complement | string | Complemento. |
| bankAccounts | object | Contas do comprador. |
| bankAccounts.bankCode | string | Código do banco. |
| bankAccounts.bankName | string | Nome do banco. |
| bankAccounts.branch | string | Filial. |
| bankAccounts.branchCheckDigit | string | Dígito de verificação da filial. |
| bankAccounts.account | string | Conta bancária. |
| bankAccounts.accountCheckDigit | string | Dígito de verificação da conta bancária. |
| bankAccounts.type | int | Tipo de conta. |
| bankAccounts.isActive | bool | Se a conta está ativa ou não. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| errors.field | string | Qual campo da requisição está com erro. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

<a id="body-raw"></a>

#### BODY Raw

```http
{
"customer": {
"name": "Yago Sebastião Lima",
"email": "yagosebastiaolima@archosolutions.com.br",
"entityType": 1,
"documentType": 1,
"document": "78112482802",
"phone": {
"countryCode": "55",
"areaCode": "21",
"number": "999999999",
"type": 5
}
}
}
```

<a id="put-customer"></a>

### `PUT` /customer

**Versão** `v2.0`

<a id="requisição-http-1"></a>

#### Requisição HTTP

```http
PUT {{ENDPOINT_GATEWAY}}/v2/customer
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/customer")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n  \"customer\": {\r\n    \"id\": \"ffede3ee-37ab-47bb-9981-d3d14697d67z\",\r\n    \"name\": \"Yago Sebastião Lima\",\r\n    \"email\": \"yagosebastiaolima@archosolutions.com.br\",\r\n    \"entityType\": 1,\r\n    \"documentType\": 1,\r\n    \"document\": \"38000266350\",\r\n    \"phone\": {\r\n      \"countryCode\": \"55\",\r\n      \"areaCode\": \"21\",\r\n      \"number\": \"999999999\",\r\n      \"type\": 5\r\n    }\r\n  }\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/customer"

payload="{\r\n  \"customer\": {\r\n    \"id\": \"ffede3ee-37ab-47bb-9981-d3d14697d67z\",\r\n    \"name\": \"Yago Sebastião Lima\",\r\n    \"email\": \"yagosebastiaolima@archosolutions.com.br\",\r\n    \"entityType\": 1,\r\n    \"documentType\": 1,\r\n    \"document\": \"38000266350\",\r\n    \"phone\": {\r\n      \"countryCode\": \"55\",\r\n      \"areaCode\": \"21\",\r\n      \"number\": \"999999999\",\r\n      \"type\": 5\r\n    }\r\n  }\r\n}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request PUT '{{ENDPOINT_GATEWAY}}/v2/customer' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "customer": {
    "id": "ffede3ee-37ab-47bb-9981-d3d14697d67z",
    "name": "Yago Sebastião Lima",
    "email": "yagosebastiaolima@archosolutions.com.br",
    "entityType": 1,
    "documentType": 1,
    "document": "38000266350",
    "phone": {
      "countryCode": "55",
      "areaCode": "21",
      "number": "999999999",
      "type": 5
    }
  }
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"customer":{"id":"ffede3ee-37ab-47bb-9981-d3d14697d67z","name":"Yago Sebastião Lima","email":"yagosebastiaolima@archosolutions.com.br","entityType":1,"documentType":1,"document":"38000266350","phone":{"countryCode":"55","areaCode":"21","number":"999999999","type":5}}});

var requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/customer", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "updatedCustomer": {
        "id": "ffede3ee-37ab-47bb-9981-d3d14697d67z",
        "name": "Yago Sebastião Lima",
        "email": "yagosebastiaolima@archosolutions.com.br",
        "entityType": "IndividualMerchant",
        "documentType": "Cpf",
        "document": "78112482802",
        "gender": "Undefined",
        "phone": {
            "countryCode": "55",
            "areaCode": "21",
            "number": "999999999",
            "type": "Mobile"
        }
    },
    "success": true,
    "errors": [],
    "traceKey": "33d8aa2b-5b89-4f5f-a1ca-74b759658edf"
}
```

O Endpoint responsável por atualizar um comprador existente por seu ID. Todas as informações do comprador substituirão as existentes na base de dados, exceto o ID do comprador, que permanecerá o mesmo.

<a id="requisição-1"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| customer | object | Sim | Dados do comprador. |
| customer.id | string | O ID do comprador. |   |
| customer.name | string | Sim | Nome completo do comprador. |
| customer.email | string | Sim | E-mail do comprador. |
| customer.entityType | entityType | Sim | Se é pessoa física ou jurídica. |
| customer.documentType | documentType | Sim | Tipo do documento do comprador. |
| customer.document | string | Sim | Documento do comprador. |
| customer.birthday | date | Não | Data de nascimento do comprador. |
| customer.gender | Gender | Não | Gênero do comprador. |
| customer.phone | object | Sim | Telefone do comprador. |
| customer.phone.countryCode | string | Sim | Código do país. |
| customer.phone.areaCode | string | Sim | Código de área. |
| customer.phone.number | string | Sim | Número do Telefone. |
| customer.phone.type | PhoneType | Sim | Tipo do telefone. |
| customer.address | object | Não | Endereço do comprador. |
| customer.address.street | string | Sim | Rua. |
| customer.address.number | string | Sim | Número. |
| customer.address.neighborhood | string | Sim | Bairro. |
| customer.address.city | string | Sim | Cidade. |
| customer.address.state | string | Sim | Estado. |
| customer.address.country | string | Sim | País. |
| customer.address.zipCode | string | Sim | CEP. |
| customer.address.complement | string | Sim | Complemento. |
| customer.bankAccounts | object | Não | Contas do comprador. |
| customer.bankAccounts.bankCode | string | Sim | Código do banco. |
| customer.bankAccounts.bankName | string | Não | Nome do banco. |
| customer.bankAccounts.branch | string | Não | Filial. |
| customer.bankAccounts.branchCheckDigit | string | Não | Dígito de verificação da filial. |
| customer.bankAccounts.account | string | Não | Conta bancária. |
| customer.bankAccounts.accountCheckDigit | string | Não | Dígito de verificação da conta bancária. |
| customer.bankAccounts.type | int | Sim | Tipo de conta. |
| customer.bankAccounts.isActive | bool | Sim | Se a conta está ativa ou não. |
| customer.isActive | bool | Não | Se o usuário é ativo ou não. |

<a id="resposta-1"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| customer.id | string | O ID do comprador. |
| customer.name | string | Nome completo do comprador. |
| customer.email | string | E-mail do comprador. |
| customer.entityType | entityType | Se é pessoa física ou jurídica. |
| customer.documentType | documentType | Tipo do documento do comprador. |
| customer.document | string | Documento do comprador. |
| customer.birthday | date | Data de nascimento do comprador. |
| customer.gender | Gender | Gênero do comprador. |
| customer.phone | object | Telefone do comprador. |
| customer.phone.countryCode | string | Código do país. |
| customer.phone.areaCode | string | Código de área. |
| customer.phone.number | string | Número do Telefone. |
| customer.phone.type | PhoneType | Tipo do telefone. |
| customer.address | object | Endereço do comprador. |
| customer.address.street | string | Rua. |
| customer.address.number | string | Número. |
| customer.address.neighborhood | string | Bairro. |
| customer.address.city | string | Cidade. |
| customer.address.state | string | Estado. |
| customer.address.country | string | País. |
| customer.address.zipCode | string | CEP. |
| customer.address.complement | string | Complemento. |
| customer.bankAccounts | object | Contas do comprador. |
| customer.bankAccounts.bankCode | string | Código do banco. |
| customer.bankAccounts.bankName | string | Nome do banco. |
| customer.bankAccounts.branch | string | Filial. |
| customer.bankAccounts.branchCheckDigit | string | Dígito de verificação da filial. |
| customer.bankAccounts.account | string | Conta bancária. |
| customer.bankAccounts.accountCheckDigit | string | Dígito de verificação da conta bancária. |
| customer.bankAccounts.type | int | Tipo de conta. |
| customer.bankAccounts.isActive | bool | Se a conta está ativa ou não. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| errors.field | string | Qual campo da requisição está com erro. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

<a id="body-raw-1"></a>

#### BODY Raw

```http
{
"customer": {
"id": "ffede3ee-37ab-47bb-9981-d3d14697d67z",
"name": "Yago Sebastião Lima",
"email": "yagosebastiaolima@archosolutions.com.br",
"entityType": 1,
"documentType": 1,
"document": "38000266350",
"phone": {
"countryCode": "55",
"areaCode": "21",
"number": "999999999",
"type": 5
}
}
}
```

<a id="get-customer"></a>

### `GET` /customer

**Versão** `v2.0`

<a id="requisição-http-2"></a>

#### Requisição HTTP

```http
GET {{ENDPOINT_GATEWAY}}/v2/customer
```

> Exemplo de requisição (`Por ID`)

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/customer?id={{customerId}}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/customer?id={{customerId}}"

payload={}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request GET '{{ENDPOINT_GATEWAY}}/v2/customer?id={{customerId}}' \
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

fetch("{{ENDPOINT_GATEWAY}}/v2/customer?id={{customerId}}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> Exemplo de requisição (`Por Documento`)

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/customer?document={{document}}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/customer?document={{document}}"

payload={}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location -g --request GET '{{ENDPOINT_GATEWAY}}/v2/customer?document={{document}}' \
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

fetch("{{ENDPOINT_GATEWAY}}/v2/customer?document={{document}}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "customer": {
        "id": "ffede3ee-37ab-47bb-9981-d3d14697d67z",
        "name": "Yago Sebastião Lima",
        "email": "yagosebastiaolima@archosolutions.com.br",
        "entityType": "IndividualMerchant",
        "documentType": "Cpf",
        "document": "38000266350",
        "gender": "Undefined",
        "phone": {
            "countryCode": "55",
            "areaCode": "21",
            "number": "999999999",
            "type": "Mobile"
        }
    },
    "success": true,
    "errors": [],
    "traceKey": "660ba190-188c-4da9-8655-7aa61cef7d59"
}
```

O Endpoint responsável por obter um comprador com base no ID ou Documento, utilize um ou outro.

<a id="parâmetros-de-query"></a>

#### Parâmetros de query

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| id | string | Sim | O ID do comprador. |
| document | string | Não | O documento do comprador. |

<a id="resposta-2"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| customer.id | string | O ID do comprador. |
| customer.name | string | Nome completo do comprador. |
| customer.email | string | E-mail do comprador. |
| customer.entityType | entityType | Se é pessoa física ou jurídica. |
| customer.documentType | documentType | Tipo do documento do comprador. |
| customer.document | string | Documento do comprador. |
| customer.birthday | date | Data de nascimento do comprador. |
| customer.gender | Gender | Gênero do comprador. |
| customer.phone | object | Telefone do comprador. |
| customer.phone.countryCode | string | Código do país. |
| customer.phone.areaCode | string | Código de área. |
| customer.phone.number | string | Número do Telefone. |
| customer.phone.type | PhoneType | Tipo do telefone. |
| customer.address | object | Endereço do comprador. |
| customer.address.street | string | Rua. |
| customer.address.number | string | Número. |
| customer.address.neighborhood | string | Bairro. |
| customer.address.city | string | Cidade. |
| customer.address.state | string | Estado. |
| customer.address.country | string | País. |
| customer.address.zipCode | string | CEP. |
| customer.address.complement | string | Complemento. |
| customer.bankAccounts | object | Contas do comprador. |
| customer.bankAccounts.bankCode | string | Código do banco. |
| customer.bankAccounts.bankName | string | Nome do banco. |
| customer.bankAccounts.branch | string | Filial. |
| customer.bankAccounts.branchCheckDigit | string | Dígito de verificação da filial. |
| customer.bankAccounts.account | string | Conta bancária. |
| customer.bankAccounts.accountCheckDigit | string | Dígito de verificação da conta bancária. |
| customer.bankAccounts.type | int | Tipo de conta. |
| customer.bankAccounts.isActive | bool | Se a conta está ativa ou não. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| errors.field | string | Qual campo da requisição está com erro. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

| PARAMS | - |
| --- | --- |
| **Id** | {{customerId}} |
| -- | Número de identificação do comprador. |
| **Document** | {{document}} |
| -- | Número do documento do comprador. |

<a id="crédito-à-vista"></a>

## Crédito à vista

> 🛡️ **Antifraude:** Para transações com antifraude ativo, os campos `sessionId` e `remoteIp` são obrigatórios. Consulte a [documentação do Device Fingerprint e SDK SafraPay Antifraud](../guias/antifraude.md#device-fingerprint).

<a id="post-charge-authorization"></a>

### `POST` /charge/authorization

**Versão** `v2.0`

<a id="requisição-http-3"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/charge/authorization
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/charge/authorization")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n  \"remoteIp\": \"203.0.113.45\",\r\n  \"charge\": {\r\n    \"sessionId\": \"123456789\",\r\n    \"customer\": {\r\n      \"name\": \"Ester Patrícia Aparício\",\r\n      \"email\": \"eesterpatriciaaparicio@ladder.com.br\",\r\n      \"document\": \"71877920002\",\r\n      \"documentType\": 1,\r\n      \"phone\": {\r\n          \"number\": \"999999999\",\r\n          \"countryCode\": \"55\",\r\n          \"areaCode\": \"21\",\r\n          \"type\": 5\r\n      }\r\n    },\r\n    \"transactions\": [\r\n      {\r\n        \"card\": {\r\n          \"cardNumber\": \"4444585001234562\",\r\n          \"cvv\": \"123\",\r\n          \"brand\": 1,\r\n          \"cardholderName\": \"Ester Patrícia Aparício\",\r\n          \"cardholderDocument\": \"71877920002\",\r\n          \"expirationMonth\": 12,\r\n          \"expirationYear\": 2034\r\n        },\r\n        \"paymentType\": 0,\r\n        \"amount\": 1000,\r\n        \"installmentNumber\": 0,\r\n        }\r\n    ],\r\n    \"source\": 1\r\n  },\r\n  \"capture\": true\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/charge/authorization"

payload="{\r\n  \"remoteIp\": \"203.0.113.45\",\r\n  \"charge\": {\r\n    \"sessionId\": \"123456789\",\r\n    \"customer\": {\r\n      \"name\": \"Ester Patrícia Aparício\",\r\n      \"email\": \"eesterpatriciaaparicio@ladder.com.br\",\r\n      \"document\": \"71877920002\",\r\n      \"documentType\": 1,\r\n      \"phone\": {\r\n          \"number\": \"999999999\",\r\n          \"countryCode\": \"55\",\r\n          \"areaCode\": \"21\",\r\n          \"type\": 5\r\n      }\r\n    },\r\n    \"transactions\": [\r\n      {\r\n        \"card\": {\r\n          \"cardNumber\": \"4444585001234562\",\r\n          \"cvv\": \"123\",\r\n          \"brand\": 1,\r\n          \"cardholderName\": \"Ester Patrícia Aparício\",\r\n          \"cardholderDocument\": \"71877920002\",\r\n          \"expirationMonth\": 12,\r\n          \"expirationYear\": 2034\r\n        },\r\n        \"paymentType\": 0,\r\n        \"amount\": 1000,\r\n        \"installmentNumber\": 0,\r\n        }\r\n    ],\r\n    \"source\": 1\r\n  },\r\n  \"capture\": true\r\n}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/charge/authorization' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "remoteIp": "203.0.113.45",
  "charge": {
    "sessionId": "123456789",
    "customer": {
      "name": "Ester Patrícia Aparício",
      "email": "eesterpatriciaaparicio@ladder.com.br",
      "document": "71877920002",
      "documentType": 1,
      "phone": {
          "number": "999999999",
          "countryCode": 55,
          "areaCode": 11,
          "type": 5
      }
    },
    "transactions": [
      {
        "card": {
          "cardNumber": "5491670214095346",
          "cvv": "111",
          "brand": "2",
          "cardholderName": "Ester Patrícia Aparício",
          "cardholderDocument": "71877920002",
          "expirationMonth": 12,
          "expirationYear": 2029
        },
        "paymentType": 2,
        "amount": 10000,
        "installmentNumber": 1
      }
    ],
    "source": 1
  },
  "capture": true
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"remoteIp":"203.0.113.45","charge":{"sessionId":"123456789","customer":{"name":"Ester Patrícia Aparício","email":"eesterpatriciaaparicio@ladder.com.br","document":"71877920002","documentType":1,"phone":{"number":"999999999","countryCode":55,"areaCode":11,"type":5}},"transactions":[{"card":{"cardNumber":"5491670214095346","cvv":"111","brand":"2","cardholderName":"Ester Patrícia Aparício","cardholderDocument":"71877920002","expirationMonth":12,"expirationYear":2029},"paymentType":2,"amount":10000,"installmentNumber":1}],"source":1},"capture":true});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/charge/authorization", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "charge": {
        "merchantChargeId": "TASK5333",
        "id": "3e60759b-e818-4a83-a98c-883fcd609d4f",
        "nsu": "000000019",
        "customerId": "a1a5a477-f8b5-471d-ab42-765c2e4b1ad1",
        "chargeStatus": "Authorized",
        "transactions": [
            {
              "card": {
                  "id": "65327e40-37ee-4c23-9369-4845519d19b7",
                  "customerId": "a1a5a477-f8b5-471d-ab42-765c2e4b1ad1",
                  "cardNumber": "549167******0005",
                  "brand": "Mastercard",
                  "cardholderName": "Ester Patrícia Aparício",
                  "cardholderDocument": "71877920002",
                  "billingAddress": {
                      "street": "Rua Juvêncio Erudilho",
                      "number": "39",
                      "neighborhood": "Centro",
                      "city": "Gurupi",
                      "state": "BA",
                      "country": "BR",
                      "zipCode": "44002-528"
                  },
                  "isPrivateLabel": false,
                  "expirationMonth": 12,
                  "expirationYear": 2034,
                  "brandName": "Mastercard"
              },
              "isApproved": true,
              "paymentType": "Credit",
              "installmentType": "None",
              "installmentNumber": 1,
              "softDescriptor": "TASK*5333",
              "amount": 1000,
              "isCapture": true,
              "isRecurrency": false,
              "isCanceled": false,
              "transactionId": "1623709631269",
              "transactionStatus": "Captured",
              "merchantTransactionId": "TASK5333",
              "acquirer": "Simulator",
              "creationDateTime": "2021-06-14T19:27:11.3167988-03:00",
              "captureDateTime": "2021-06-14T19:27:11.3156408-03:00",
              "authorizationResponseCode": "00",
              "authorizationCode": "689020",
              "merchantAdviceCode": "01",
              "acquirerTransactionId": "ff478f2d-r569-568s-22ds-52s6742",
              "bankSlipStatus": 0
            }
        ]
    },
    "success": true,
    "errors": [],
    "traceKey": "ac0ea0e1-ad9f-412e-a0bb-4b97e9893a3f"
}
```

O Endpoint responsável por criar uma nova cobrança, contendo uma transação autorizada, usando adquirente. A cobrança não precisa ser capturada posteriormente.

<a id="requisição-2"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| charge | Object | Sim | Dados da transação. |
| charge.merchantChargeId | string | Não | O ID de cobrança definido pelo sistema do comerciante. **Não utilize espaços** no meio do identificador (ex.: `TASK5333`). Campos obrigatórios da estrutura não podem ser enviados vazios nem como string vazia `""`. |
| charge.subscriptionId | string | Não | GUID único relacionado ao subscription. |
| charge.sessionId | string | Condicional | ID da sessão criada pelo servidor do site do cliente e usada durante a visita de um determinado usuário. **Obrigatório caso utilize antifraude.** |
| charge.smartCheckoutId | string | Não | O ID do smartCheckout. |
| charge.id | string | Não | O ID da cobrança. |
| charge.chargeStatus | int | Não | Status atual da cobrança, indicando em qual estágio do processo de autorização a cobrança está. Ele reflete diretamente todos os status de transação dentro da cobrança. |
| charge.subMerchant | object | Não | Objeto com dados referente ao submerchant (Caso exista submerchant). |
| charge.subMerchant.id | string | Sim | ID do submerchant. |
| charge.subMerchant.document | string | Sim | Documento do submerchant. |
| charge.subMerchant.socialName | string | Sim | Razão social do submerchant. |
| charge.subMerchant.address | objeto | Sim | Endereço do submerchant. |
| charge.subMerchant.address.street | string | Sim | Rua. |
| charge.subMerchant.address.number | string | Sim | Número. |
| charge.subMerchant.address.neighborhood | string | Sim | Bairro. |
| charge.subMerchant.address.city | string | Sim | Cidade. |
| charge.subMerchant.address.state | string | Sim | Estado. |
| charge.subMerchant.address.country | string | Sim | País. |
| charge.subMerchant.address.zipCode | string | Sim | CEP. |
| charge.subMerchant.address.complement | string | Não | Complemento. |
| charge.customer | object | Sim | Dados do comprador. |
| charge.customer.id | string | Não | O ID do comprador. |
| charge.customer.name | string | Sim | Nome completo do comprador. |
| charge.customer.email | string | Sim | E-mail do comprador. |
| charge.customer.entityType | entityType | Não | Se é pessoa física ou jurídica. |
| charge.customer.documentType | documentType | Sim | Tipo do documento do comprador. |
| charge.customer.document | string | Sim | Documento do comprador. |
| charge.customer.birthday | date | Não | Data de nascimento do comprador. |
| charge.customer.gender | Gender | Não | Gênero do comprador. |
| charge.customer.phone | object | Sim | Telefone do comprador. |
| charge.customer.phone.countryCode | string | Sim | Código do país. |
| charge.customer.phone.areaCode | string | Sim | Código de área. |
| charge.customer.phone.number | string | Sim | Número do Telefone. |
| charge.customer.phone.type | PhoneType | Sim | Tipo do telefone. |
| charge.customer.address | object | Condicional | Endereço do comprador. **Obrigatório caso utilize antifraude.** |
| charge.customer.address.street | string | Sim | Rua. |
| charge.customer.address.number | string | Sim | Número. |
| charge.customer.address.neighborhood | string | Sim | Bairro. |
| charge.customer.address.city | string | Sim | Cidade. |
| charge.customer.address.state | string | Sim | Estado. |
| charge.customer.address.country | string | Sim | País. |
| charge.customer.address.zipCode | string | Sim | CEP. |
| charge.customer.address.complement | string | Sim | Complemento. |
| charge.customer.bankAccounts | object | Não | Contas do comprador. |
| charge.customer.bankAccounts.bankCode | string | Sim | Código do banco. |
| charge.customer.bankAccounts.bankName | string | Sim | Nome do banco. |
| charge.customer.bankAccounts.branch | string | Sim | Filial. |
| charge.customer.bankAccounts.branchCheckDigit | string | Sim | Dígito de verificação da filial. |
| charge.customer.bankAccounts.account | string | Sim | Conta bancária. |
| charge.customer.bankAccounts.accountCheckDigit | string | Sim | Dígito de verificação da conta bancária. |
| charge.customer.bankAccounts.type | int | Sim | Tipo de conta. |
| charge.customer.bankAccounts.isActive | bool | Sim | Se a conta está ativa ou não. |
| charge.customer.isActive | bool | Não | Se o comprador está ativo ou não. |
| charge.transactions | array(object) | Sim | Uma transação a ser realizada dentro da cobrança. |
| charge.transactions.card | object | Não | O Cartão a ser utilizado na transação. |
| charge.transactions.card.id | string | Não | O ID do cartão. |
| charge.transactions.card.customerId | string | Não | O ID do comprador. |
| charge.transactions.card.cardNumber | string | Sim | O número impresso na frente do cartão. |
| charge.transactions.card.cvv | string | Sim | Card Verification Value (CVV) é um recurso de segurança para transações de cartão de pagamento "cartão ausente" instituído para reduzir a incidência de fraude de cartão de crédito. Consiste em um número de 3-4 dígitos impresso no cartão. |
| charge.transactions.card.cvvMissingReason | int | Não | Razão pela qual o CVV não consta na cobrança, se necessário. Mandatório apenas para PagSeguro. |
| charge.transactions.card.brand | int | Sim | A bandeira do cartão à qual o imposto se aplica. |
| charge.transactions.card.cardholderName | string | Sim | O nome do títular do cartão. |
| charge.transactions.card.cardholderDocument | string | Sim | O documento do títular do cartão. |
| charge.transactions.card.expirationMonth | int | Sim | O Mês de expiração do cartão com 2 dígitos. |
| charge.transactions.card.expirationYear | int | Sim | O Ano de expiração do cartão com 4 dígitos. |
| charge.transactions.card.billingAddress | object | Condicional | É o endereço conectado ao cartão de crédito ou débito. As empresas usam o endereço de cobrança para verificar o uso autorizado de tal cartão. É também para onde as empresas enviam contas em papel e extratos bancários. **Obrigatório caso utilize antifraude.** |
| charge.transactions.card.billingAddress.street | string | Não | Rua. |
| charge.transactions.card.billingAddress.number | string | Não | Número. |
| charge.transactions.card.billingAddress.neighborhood | string | Não | Bairro. |
| charge.transactions.card.billingAddress.city | string | Não | Cidade. |
| charge.transactions.card.billingAddress.state | string | Não | Estado. |
| charge.transactions.card.billingAddress.country | string | Não | País. |
| charge.transactions.card.billingAddress.zipCode | string | Não | CEP. |
| charge.transactions.card.billingAddress.complement | string | Não | Complemento. |
| charge.transactions.card.isPrivateLabel | bool | Condicional | Indica se o cartão é um produto de whitelabel ou não. Whitelabel é um produto ou serviço que uma empresa produz e comercializa com outras empresas que tem interesse em utilizar o mesmo com sua marca estampada. **Obrigatório caso utilize antifraude.** |
| charge.transactions.card.brandName | string | Não | O nome da bandeira do cartão. |
| charge.transactions.card.cardToken | string | Não | Token do cartão. |
| charge.transactions.card.eci | string | Não | Código de autenticação ECI (Retornado apenas quando a transação passa pelo fluxo do 3DS). |
| charge.transactions.card.cavv | string | Não | Criptorgrama de autenticação (Retornado apenas quando a transação passa pelo fluxo do 3DS). |
| charge.transactions.card.xid | string | Não | Identificador MPI da transação autenticada. |
| charge.transactions.card.cardholderAuthenticationVersion | string | Não | Versão da autentificação retornada pelo provedor. |
| charge.transactions.card.metadata | objeto | Não | Armazena todas as credenciais relacionadas a bandeira. |
| charge.transactions.card.metadata.additionalProp1 | string | Não | Propriedade adicional. |
| charge.transactions.card.metadata.additionalProp2 | string | Não | Propriedade adicional. |
| charge.transactions.card.metadata.additionalProp3 | string | Não | Propriedade adicional. |
| charge.transactions.card.cardTransactionId | string | Não | ID para a requisição da transação do cartão. |
| charge.transactions.card.cof | bool | Não | indica se a transação é COF (Credentials On File). |
| charge.transactions.temporaryCardToken | string | Não | Token do cartão que foi gerado em um endpoint temporário de cartão. |
| charge.transactions.externalWallet | object | Não | Informações de carteira externa. |
| charge.transactions.externalWallet.type | int | Não | Indica qual carteira foi usada. |
| charge.transactions.externalWallet.payload | string | Não | Payload enviado pela carteira para processamento. |
| charge.transactions.externalWallet.billingAddress | object | Não | Endereço relacionado à conta da carteira externa. |
| charge.transactions.externalWallet.street | string | Não | Rua. |
| charge.transactions.externalWallet.number | string | Não | Número. |
| charge.transactions.externalWallet.neighborhood | string | Não | Bairro. |
| charge.transactions.externalWallet.city | string | Não | Cidade. |
| charge.transactions.externalWallet.state | string | Não | Estado. |
| charge.transactions.externalWallet.country | string | Não | País. |
| charge.transactions.externalWallet.zipCode | string | Não | CEP. |
| charge.transactions.externalWallet.complement | string | Não | Complemento. |
| charge.transactions.paymentType | int | Sim | Tipo de transação. |
| charge.transactions.amount | int | Sim | O valor do pagamento em centavos. |
| charge.transactions.installmentNumber | int | Sim | Quantidade de parcelas. Só pode ser maior que **1** se o tipo de transação for crédito. |
| charge.transactions.installmentType | int | Sim | Tipo de parcelamento da transação |
| charge.transactions.softDescriptor | string | Não | Breve descrição a ser apresentada na fatura bancária do cliente. Este campo aceita apenas strings compostas por letras (maiúsculas ou minúsculas), números e o caractere asterisco (*), **sem espaços** nem outros símbolos. Formato equivalente à expressão regular `/^[a-zA-Z0-9*]+$/`. Se nulo, ele será preenchido com um rótulo padrão definido pela Safrapay. |
| charge.transactions.merchantTransactionId | string | Não | Identificador de pedido definido pelo sistema do estabelecimento comercial. Esta propriedade é obrigatória e servirá para capturar, cancelar e consultar posteriormente a transação. **Não utilize espaços** no meio do valor. |
| charge.transactions.acquirer | int | Não | O ID da adquirente. |
| charge.transactions.firstSubscriptionCharge | bool | Não | Indica se a transação é a primeira cobrança de assinatura. |
| charge.transactions.productIds | array(string) | Não | O ID de cada produto sendo comprado pela transação. |
| charge.transactions.source | object | Não | É a origem da transação. |
| charge.transactions.source.id | string | Sim | O ID do SmartCheckout |
| charge.transactions.source.type | int | Sim | Tipo de smartCheckout. |
| charge.transactions.boardingTaxAmount | object | Não | Representa as informações sobre taxas de embarque para companhias aéreas. |
| charge.transactions.boardingTaxAmount.amount | int | Não | Valor da taxa de embarque cobrada pela companhia aérea. |
| charge.transactions.boardingTaxAmount.entryAmount | int | Não | Valor da taxa de embarque cobrada pela companhia aérea. |
| charge.transactions.acquirerKey | string | Não | Número da chave do contrato do adquirente. |
| charge.transactions.sdwo | object | Não | Dados do integrador. |
| charge.transactions.sdwo.merchantCode | string | Sim | Código do estabelecimento. |
| charge.transactions.sdwo.walletId | string | Sim | ID da carteira que será integrada. |
| charge.transactions.sdwo.mcc | string | Sim | Número MCC que será enviado na integração. |
| charge.transactions.sdwo.name | string | Não | Nome do submerchant. |
| charge.transactions.sdwo.document | string | Não | Número do documento. |
| charge.transactions.sdwo.documentType | int | Não | Tipo de documento de acordo com o número do documento. |
| charge.transactions.sdwo.addressLine | string | Sim | Linha de endereço. |
| charge.transactions.sdwo.phone | object | Sim | Informações de telefone. |
| charge.transactions.sdwo.phone.countryCode | string | Sim | Código do país. |
| charge.transactions.sdwo.phone.areaCode | string | Sim | Código de área. |
| charge.transactions.sdwo.phone.number | string | Sim | Número do Telefone. |
| charge.transactions.sdwo.phone.type | PhoneType | Não | Tipo do telefone. |
| charge.transactions.sdwo.address | object | Não | Informações de endereço. |
| charge.transactions.sdwo.address.city | string | Sim | Cidade. |
| charge.transactions.sdwo.address.state | string | Sim | Estado. |
| charge.transactions.sdwo.address.country | string | Sim | País. |
| charge.transactions.sdwo.address.zipCode | string | Sim | CEP. |
| charge.transactions.sdwo.address.complement | string | Sim | Complemento. |
| charge.transactions.sdwo.operationType | string | Não | Opcional quando vazio, por padrão o valor é "BackToBack". |
| charge.transactions.authentication | object | Não | Dados informativos para autenticação 3DS. |
| charge.transactions.authentication.xid | string | Não | MPI identificador da transação autenticada, no formato base64 (usado apenas para bandeira VISA). |
| charge.transactions.authentication.cavv | string | Não | Identificador de autenticação criptografado pela bandeira (VISA e Mastercard) no formato base64. |
| charge.transactions.authentication.eci | string | Não | Indicador que mostra se a transação foi processada com Bearer authentication. |
| charge.transactions.authentication.directoryServer | string | Não | Campo usado apenas para bandeira Elo. |
| charge.transactions.authentication.version | string | Não | Versão utilizada no 3DS. |
| charge.products | array(object) | Não | Lista com cada produto dentro da cobrança. |
| charge.products.id | string | Não | UUID do produto. |
| charge.products.amount | int | Não | Valor do produto. |
| charge.products.name | int | Não | Nome do produto. |
| charge.products.description | string | Não | Descrição do produto. |
| charge.products.membershipFee | int | Não | Taxa que o cliente paga para ter o produto. |
| charge.products.sku | string | Não | ID único definido pelo comércio para identificar o produto na nossa base de dados (Stock Keeping Unit). |
| charge.products.quantity | int | Não | Quantidade do produto no carrinho. |
| charge.products.imagesRef | array(string) | Não | Lista com URL das imagens do produto. |
| charge.products.isActive | bool | Não | Define se o produto está ativo ou não. |
| charge.source | int | Sim | Define a fonte de cobrança, por exemplo, um POS, pinpad, site de comércio eletrônico. |
| charge.origin | string | Não | Uma propriedade que o cliente pode usar para identificar a origem da cobrança, como nome do fornecedor ou identificador. |
| charge.receivers | array(object) | Não | Recebedores envolvidos na cobrança. Irá definir quem receberá a transação pela divisão do valor total da cobrança em diferentes pagamentos. |
| charge.receivers.id | string | Sim | Documento identificador. |
| charge.receivers.mdrDiscount | bool | Não | Define se terá desconto MDR. |
| charge.receivers.fixedAmountComission | float | Não | Valor fixo que o destinatário deve receber. |
| charge.receivers.chargeRemainder | bool | Não | Após processar os valores divididos para cada parte, se houver centavos que sobraram da divisão, este campo indica qual destinatário deverá receber os centavos restantes. Também pode ser definido para divisão de centavos (exemplo 100/3) ou para quando o destinatário não tiver regra especifica. |
| charge.receivers.percentageComission | float | Não | Esta comissão é calculada no topo do valor da transação. |
| charge.receivers.mdrComission | float | Não | Porcentagem relativa ao MDR calculado na liquidação. |
| charge.receivers.membershipComission | float | Não | Comissão percentual para transações de associação. |
| charge.receivers.amount | float | Não | Valor. |
| charge.metadata | object | Não | Entradas coletadas para iniciação do evento. |
| charge.metadata.key | string | Não | O nome da chave (campo) |
| charge.metadata.value | string | Não | O valor da chave. |
| charge.gatewayId | string | Não | Gateway ID criado para o cliente para uso de autorização do Safra. |
| charge.shippingAddress | object | Não | Representa as informações do endereço de envio. |
| charge.shippingAddress.country | string | Não | Código do país. |
| charge.shippingAddress.street | string | Não | Rua. |
| charge.shippingAddress.number | string | Não | Número. |
| charge.shippingAddress.complement | string | Não | Complemento. |
| charge.shippingAddress.neighborhood | string | Não | Bairro. |
| charge.shippingAddress.postalCode | string | Não | Código postal. |
| charge.shippingAddress.city | string | Não | Cidade. |
| charge.shippingAddress.state | string | Não | Estado. |
| charge.shippingSettings | array(object) | Não | Configurações adicionais de envio. |
| charge.shippingSettings.merchantId | string | Não | ID único do estabelecimento relacionado à configuração de envio. |
| charge.shippingSettings.amount | int | Não | Valor do envio. |
| charge.macAddress | string | Não | Endereço MAC (Media Access Control) do dispositivo de origem usado para identificar exclusivamente um controlador de interface de rede. |
| lateCapture | bool | Não | Informar valor "true" para uma autorização com captura tardia. Valor padrão: false. |
| capture | bool | Sim | Se a cobrança deve ou não ser capturada. |
| templateId | string | Não | TemplateId que será usado para enviar o recibo ao cliente. |
| primaryColor | string | Não | A cor primária da configuração do comerciante. |
| secondaryColor | string | Não | A cor secundária da configuração do comerciante. |
| hostname | string | Não | O hostname da configuração do comerciante. |
| merchantCode | string | Não | Código do estabelecimento definido pelo integrador. |
| remoteIp | string | Sim | **\[OBRIGATÓRIO quando antifraude ativo\]** O endereço IP do comprador. Este dado é utilizado em diversas verificações de risco (número de tentativas de pagamento, verificações baseadas em localização, detecção de uso de VPN/proxy). **Suporta IPv4.** **Exemplo:** `192.168.1.100`. Este campo complementa a implementação do Device Fingerprint. Consulte [documentação completa](../guias/antifraude.md#campo-remoteip-complemento-ao-device-fingerprint). |

<a id="resposta-3"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| merchantChargeId | string | O ID de cobrança definido pelo sistema do comerciante. |
| id | string | O ID da cobrança. |
| nsu | string | Identificador do pedido (Safrapay). |
| customerId | string | O ID do comprador. |
| chargeStatus | int | Status atual da cobrança, indicando em qual estágio do processo de autorização a cobrança está. Ele reflete diretamente todos os status de transação dentro da cobrança. |
| transactions | object | Uma transação a ser realizada dentro da cobrança. |
| transactions.card | object | O Cartão a ser utilizado na transação. |
| transactions.card.id | string | O ID do cartão. |
| transactions.card.customerId | string | O ID do comprador. |
| transactions.card.cardNumber | string | O número impresso na frente do cartão. |
| transactions.card.brand | int | A bandeira do cartão à qual o imposto se aplica. |
| transactions.card.cardholderName | string | O nome do títular do cartão. |
| transactions.card.cardholderDocument | string | O documento do títular do cartão. |
| transactions.card.billingAddress | array | É o endereço conectado ao cartão de crédito ou débito. As empresas usam o endereço de cobrança para verificar o uso autorizado de tal cartão. É também para onde as empresas enviam contas em papel e extratos bancários. |
| transactions.card.billingAddress.street | string | Rua. |
| transactions.card.billingAddress.number | string | Número. |
| transactions.card.billingAddress.neighborhood | string | Bairro. |
| transactions.card.billingAddress.city | string | Cidade. |
| transactions.card.billingAddress.state | string | Estado. |
| transactions.card.billingAddress.country | string | País. |
| transactions.card.billingAddress.zipCode | string | CEP. |
| transactions.card.billingAddress.complement | string | Complemento. |
| transactions.card.isPrivateLabel | bool | Indica se o cartão é um produto de whitelabel ou não. Whitelabel é um produto ou serviço que uma empresa produz e comercializa com outras empresas que tem interesse em utilizar o mesmo com sua marca estampada. |
| transactions.card.expirationMonth | int | O Mês de expiração do cartão com 2 dígitos. |
| transactions.card.expirationYear | int | O Ano de expiração do cartão com 4 dígitos. |
| transactions.card.fallback | bool | Uma bandeira que informa se a cobrança necessária será feita como fita magnética substituta. |
| transactions.card.brandName | string | O nome da bandeira do cartão. |
| isApproved | bool | Indica se a cobrança está aprovada. |
| paymentType | int | Tipo de transação. |
| installmentType | string | Tipo de parcelamento da transação |
| installmentNumber | int | Quantidade de parcelas. Só pode ser maior que **1** se o tipo de transação for crédito. |
| softDescriptor | string | Breve descrição a ser apresentada na fatura bancária do cliente. Este campo aceita apenas strings compostas por letras (maiúsculas ou minúsculas), números e o caractere asterisco (*), **sem espaços** nem outros símbolos. Formato equivalente à expressão regular `/^[a-zA-Z0-9*]+$/`. Se nulo, ele será preenchido com um rótulo padrão definido pela Safrapay. |
| amount | int | O valor do pagamento em centavos. |
| isCapture | bool | Indica se a cobrança foi capturada. |
| isRecurrency | bool | Indica se a cobrança é uma recorrência. |
| isCanceled | bool | Indica se a cobrança foi cancelada. |
| transactionId | string | Número Sequencial Único (NSU) da autorização, caso o pagamento seja aprovado pelo Emissor. |
| transactionStatus | string | Indica qual o status da transação. |
| merchantTransactionId | string | O ID da transação do Lojista |
| acquirer | string | O nome da adquirente. |
| creationDateTime | string | A data de criação da transação. |
| captureDateTime | string | A data de captura da transação. |
| bankSlipStatus | int | Status do boleto bancário. |
| metadata | object | Lista de informações personalizados. |
| metadata.key | string | O nome da chave (campo) |
| metadata.value | string | O valor da chave passada no campo `metadata.key`. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

<a id="body-raw-2"></a>

#### BODY Raw

```http
{
"charge": {
"merchantChargeId": "TASK5333",
"customer": {
"name": "Ester Patrícia Aparício",
"email": "eesterpatriciaaparicio@ladder.com.br",
"document": "71877920002",
"documentType": 1,
"phone": {
"number": "999999999",
"countryCode": "55",
"areaCode": "21",
"type": 5
}
},
"transactions": [
{
"card": {
"cardNumber": "4444585001234562",
"cvv": "123",
"brand": 1,
"cardholderName": "Ester Patrícia Aparício",
"cardholderDocument": "71877920002",
"billingAddress": {
"street": "Rua Juvêncio Erudilho",
"number": "39",
"neighborhood": "Centro",
"city": "Gurupi",
"state": "BA",
"country": "BR",
"zipCode": "44002-528"
},
"expirationMonth": 12,
"expirationYear": 2034
},
"paymentType": 2,
"amount": 1000,
"installmentNumber": 0,
"softDescriptor": "TASK*5333",
}
],
"source": 8
}
}
```

<a id="crédito-parcelado"></a>

## Crédito parcelado

<a id="post-charge-authorization-1"></a>

### `POST` /charge/authorization

**Versão** `v2.0`

<a id="requisição-http-4"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/charge/authorization
```

> Exemplo de requisição (Sem juros)

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/charge/authorization")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n  \"charge\": {\r\n    \"merchantChargeId\": \"TASK5333\",\r\n    \"customer\": {\r\n      \"name\": \"Ester Patrícia Aparício\",\r\n      \"email\": \"eesterpatriciaaparicio@ladder.com.br\",\r\n      \"document\": \"71877920002\",\r\n      \"documentType\": 1,\r\n      \"phone\": {\r\n          \"number\": \"999999999\",\r\n          \"countryCode\": \"55\",\r\n          \"areaCode\": \"21\",\r\n          \"type\": 5\r\n      }\r\n    },\r\n    \"transactions\": [\r\n      {\r\n        \"card\": {\r\n          \"cardNumber\": \"4444585001234562\",\r\n          \"cvv\": \"123\",\r\n          \"brand\": 1,\r\n          \"cardholderName\": \"Ester Patrícia Aparício\",\r\n          \"cardholderDocument\": \"71877920002\",\r\n          \"billingAddress\": {\r\n            \"street\": \"Rua Juvêncio Erudilho\",\r\n            \"number\": \"39\",\r\n            \"neighborhood\": \"Centro\",\r\n            \"city\": \"Gurupi\",\r\n            \"state\": \"BA\",\r\n            \"country\": \"BR\",\r\n            \"zipCode\": \"44002-528\"\r\n          },\r\n          \"expirationMonth\": 12,\r\n          \"expirationYear\": 2034\r\n        },\r\n        \"paymentType\": 2,\r\n        \"amount\": 10000,\r\n        \"installmentNumber\": 2,\r\n  \"installmentType\": 1,\r\n      \"softDescriptor\": \"TASK*5333\",\r\n     }\r\n    ],\r\n    \"source\": 8\r\n  }\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/charge/authorization"

payload="{\r\n  \"charge\": {\r\n    \"merchantChargeId\": \"TASK5333\",\r\n    \"customer\": {\r\n      \"name\": \"Ester Patrícia Aparício\",\r\n      \"email\": \"eesterpatriciaaparicio@ladder.com.br\",\r\n      \"document\": \"71877920002\",\r\n      \"documentType\": 1,\r\n      \"phone\": {\r\n          \"number\": \"999999999\",\r\n          \"countryCode\": \"55\",\r\n          \"areaCode\": \"21\",\r\n          \"type\": 5\r\n      }\r\n    },\r\n    \"transactions\": [\r\n      {\r\n        \"card\": {\r\n          \"cardNumber\": \"4444585001234562\",\r\n          \"cvv\": \"123\",\r\n          \"brand\": 1,\r\n          \"cardholderName\": \"Ester Patrícia Aparício\",\r\n          \"cardholderDocument\": \"71877920002\",\r\n          \"billingAddress\": {\r\n            \"street\": \"Rua Juvêncio Erudilho\",\r\n            \"number\": \"39\",\r\n            \"neighborhood\": \"Centro\",\r\n            \"city\": \"Gurupi\",\r\n            \"state\": \"BA\",\r\n            \"country\": \"BR\",\r\n            \"zipCode\": \"44002-528\"\r\n          },\r\n          \"expirationMonth\": 12,\r\n          \"expirationYear\": 2034\r\n        },\r\n        \"paymentType\": 2,\r\n        \"amount\": 10000,\r\n        \"installmentNumber\": 2,\r\n  \"installmentType\": 1,\r\n      \"softDescriptor\": \"TASK*5333\"\r\n      }\r\n    ],\r\n   \"source\": 8\r\n  }\r\n}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/charge/authorization' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "charge": {
    "merchantChargeId": "TASK5333",
    "customer": {
      "name": "Ester Patrícia Aparício",
      "email": "eesterpatriciaaparicio@ladder.com.br",
      "document": "71877920002",
      "documentType": 1,
      "phone": {
          "number": "999999999",
          "countryCode": "55",
          "areaCode": "21",
          "type": 5
      }
    },
    "transactions": [
      {
        "card": {
          "cardNumber": "4444585001234562",
          "cvv": "123",
          "brand": 1,
          "cardholderName": "Ester Patrícia Aparício",
          "cardholderDocument": "71877920002",
          "billingAddress": {
            "street": "Rua Juvêncio Erudilho",
            "number": "39",
            "neighborhood": "Centro",
            "city": "Gurupi",
            "state": "BA",
            "country": "BR",
            "zipCode": "44002-528"
          },
          "expirationMonth": 12,
          "expirationYear": 2034
        },
        "paymentType": 2,
        "amount": 10000,
        "installmentNumber": 2,
        "installmentType": 1,
        "softDescriptor": "TASK*5333"
      }
    ],
    "source": 8
  }
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"charge":{"merchantChargeId":"TASK5333","customer":{"name":"Ester Patrícia Aparício","email":"eesterpatriciaaparicio@ladder.com.br","document":"71877920002","documentType":1,"phone":{"number":"999999999","countryCode":"55","areaCode":"21","type":5}},"transactions":[{"card":{"cardNumber":"4444585001234562","cvv":"123","brand":1,"cardholderName":"Ester Patrícia Aparício","cardholderDocument":"71877920002","billingAddress":{"street":"Rua Juvêncio Erudilho","number":"39","neighborhood":"Centro","city":"Gurupi","state":"BA","country":"BR","zipCode":"44002-528"},"expirationMonth":12,"expirationYear":2034},"paymentType":2,"amount":10000,"installmentNumber":2,"installmentType": 1,"softDescriptor":"TASK*5333"}],"source":8}});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/charge/authorization", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "charge": {
        "merchantChargeId": "TASK5333",
        "id": "3e60759b-e818-4a83-a98c-883fcd609d4f",
        "nsu": "000000019",
        "customerId": "a1a5a477-f8b5-471d-ab42-765c2e4b1ad1",
        "chargeStatus": "Authorized",
        "transactions": [
            {
              "card": {
                  "id": "65327e40-37ee-4c23-9369-4845519d19b7",
                  "customerId": "a1a5a477-f8b5-471d-ab42-765c2e4b1ad1",
                  "cardNumber": "549167******0005",
                  "brand": "Mastercard",
                  "cardholderName": "Ester Patrícia Aparício",
                  "cardholderDocument": "71877920002",
                  "billingAddress": {
                      "street": "Rua Juvêncio Erudilho",
                      "number": "39",
                      "neighborhood": "Centro",
                      "city": "Gurupi",
                      "state": "BA",
                      "country": "BR",
                      "zipCode": "44002-528"
                  },
                  "isPrivateLabel": false,
                  "expirationMonth": 12,
                  "expirationYear": 2034,
                  "brandName": "Mastercard"
              },
              "isApproved": true,
              "paymentType": "Credit",
              "installmentType": "Merchant",
              "installmentNumber": 2,
              "softDescriptor": "TASK*5333",
              "amount": 10000,
              "isCapture": true,
              "isRecurrency": false,
              "isCanceled": false,
              "transactionId": "1623709631269",
              "transactionStatus": "Captured",
              "merchantTransactionId": "TASK5333",
              "acquirer": "Simulator",
              "creationDateTime": "2021-06-14T19:27:11.3167988-03:00",
              "captureDateTime": "2021-06-14T19:27:11.3156408-03:00",
              "authorizationResponseCode": "00",
              "authorizationCode": "689020",
              "merchantAdviceCode": "01",
              "acquirerTransactionId": "ff478f2d-r569-568s-22ds-52s6742",
              "bankSlipStatus": 0
            }
        ]
    },
    "success": true,
    "errors": [],
    "traceKey": "ac0ea0e1-ad9f-412e-a0bb-4b97e9893a3f"
}
```

O que diferencia uma transação de crédito parcelada de uma **à vista**, é o número de parcelas `InstallmentNumber` e o tipo de parcelamento `InstallmentType`. Para a realização de uma transação de crédito parcelada, precisamos adicionar e alterar os seguintes atributos em nossa requisição de [POSTCrédito à Vista](#crédito-à-vista).

<a id="alteração-em-atributos"></a>

#### Alteração em Atributos

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| charge.transactions.paymentType | int | Sim | Para uma transação parcelada, o PaymentType precisa ser do tipo **Crédito**. Para isso, iremos passar o valor 2 neste atributo. |
| charge.transactions.installmentNumber | int | Sim | Quantidade de parcelas da cobrança. |
| charge.transactions.installmentType | int | Sim | Este é o atributo que diferencia uma transação com e sem juros. Se enviado o valor **1**, a transação será parcelada pelo lojista, ou seja, sem juros. Se passado o valor **2**, a transação será parcelada pelo emissor do cartão, ou seja, com juros. Esta informação pode ser consultada em **Tipo de parcelamento da transação** |

<a id="requisição-3"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| charge | Object | Sim | Dados da transação. |
| charge.merchantChargeId | string | Não | O ID de cobrança definido pelo sistema do comerciante. **Não utilize espaços** no meio do identificador (ex.: `TASK5333`). Campos obrigatórios da estrutura não podem ser enviados vazios nem como string vazia `""`. |
| charge.subscriptionId | string | Não | GUID único relacionado ao subscription. |
| charge.sessionId | string | Não | ID da sessão criada pelo servidor do site do cliente e usada durante a visita de um determinado usuário. |
| charge.smartCheckoutId | string | Não | O ID do smartCheckout. |
| charge.id | string | Não | O ID da cobrança. |
| charge.chargeStatus | int | Não | Status atual da cobrança, indicando em qual estágio do processo de autorização a cobrança está. Ele reflete diretamente todos os status de transação dentro da cobrança. |
| charge.subMerchant | object | Não | Objeto com dados referente ao submerchant (Caso exista submerchant). |
| charge.subMerchant.id | string | Sim | ID do submerchant. |
| charge.subMerchant.document | string | Sim | Documento do submerchant. |
| charge.subMerchant.socialName | string | Sim | Razão social do submerchant. |
| charge.subMerchant.address | objeto | Sim | Endereço do submerchant. |
| charge.subMerchant.address.street | string | Sim | Rua. |
| charge.subMerchant.address.number | string | Sim | Número. |
| charge.subMerchant.address.neighborhood | string | Sim | Bairro. |
| charge.subMerchant.address.city | string | Sim | Cidade. |
| charge.subMerchant.address.state | string | Sim | Estado. |
| charge.subMerchant.address.country | string | Sim | País. |
| charge.subMerchant.address.zipCode | string | Sim | CEP. |
| charge.subMerchant.address.complement | string | Não | Complemento. |
| charge.customer | object | Sim | Dados do comprador. |
| charge.customer.id | string | Não | O ID do comprador. |
| charge.customer.name | string | Sim | Nome completo do comprador. |
| charge.customer.email | string | Sim | E-mail do comprador. |
| charge.customer.entityType | entityType | Não | Se é pessoa física ou jurídica. |
| charge.customer.documentType | documentType | Sim | Tipo do documento do comprador. |
| charge.customer.document | string | Sim | Documento do comprador. |
| charge.customer.birthday | date | Não | Data de nascimento do comprador. |
| charge.customer.gender | Gender | Não | Gênero do comprador. |
| charge.customer.phone | object | Sim | Telefone do comprador. |
| charge.customer.phone.countryCode | string | Sim | Código do país. |
| charge.customer.phone.areaCode | string | Sim | Código de área. |
| charge.customer.phone.number | string | Sim | Número do Telefone. |
| charge.customer.phone.type | PhoneType | Sim | Tipo do telefone. |
| charge.customer.address | object | Não | Endereço do comprador. |
| charge.customer.address.street | string | Sim | Rua. |
| charge.customer.address.number | string | Sim | Número. |
| charge.customer.address.neighborhood | string | Sim | Bairro. |
| charge.customer.address.city | string | Sim | Cidade. |
| charge.customer.address.state | string | Sim | Estado. |
| charge.customer.address.country | string | Sim | País. |
| charge.customer.address.zipCode | string | Sim | CEP. |
| charge.customer.address.complement | string | Sim | Complemento. |
| charge.customer.bankAccounts | object | Não | Contas do comprador. |
| charge.customer.bankAccounts.bankCode | string | Sim | Código do banco. |
| charge.customer.bankAccounts.bankName | string | Sim | Nome do banco. |
| charge.customer.bankAccounts.branch | string | Sim | Filial. |
| charge.customer.bankAccounts.branchCheckDigit | string | Sim | Dígito de verificação da filial. |
| charge.customer.bankAccounts.account | string | Sim | Conta bancária. |
| charge.customer.bankAccounts.accountCheckDigit | string | Sim | Dígito de verificação da conta bancária. |
| charge.customer.bankAccounts.type | int | Sim | Tipo de conta. |
| charge.customer.bankAccounts.isActive | bool | Sim | Se a conta está ativa ou não. |
| charge.customer.isActive | bool | Não | Se o comprador está ativo ou não. |
| charge.transactions | array(object) | Sim | Uma transação a ser realizada dentro da cobrança. |
| charge.transactions.card | object | Não | O Cartão a ser utilizado na transação. |
| charge.transactions.card.id | string | Não | O ID do cartão. |
| charge.transactions.card.customerId | string | Não | O ID do comprador. |
| charge.transactions.card.cardNumber | string | Sim | O número impresso na frente do cartão. |
| charge.transactions.card.cvv | string | Sim | Card Verification Value (CVV) é um recurso de segurança para transações de cartão de pagamento "cartão ausente" instituído para reduzir a incidência de fraude de cartão de crédito. Consiste em um número de 3-4 dígitos impresso no cartão. |
| charge.transactions.card.cvvMissingReason | int | Não | Razão pela qual o CVV não consta na cobrança, se necessário. Mandatório apenas para PagSeguro. |
| charge.transactions.card.brand | int | Sim | A bandeira do cartão à qual o imposto se aplica. |
| charge.transactions.card.cardholderName | string | Sim | O nome do títular do cartão. |
| charge.transactions.card.cardholderDocument | string | Sim | O documento do títular do cartão. |
| charge.transactions.card.billingAddress | object | Não | É o endereço conectado ao cartão de crédito ou débito. As empresas usam o endereço de cobrança para verificar o uso autorizado de tal cartão. É também para onde as empresas enviam contas em papel e extratos bancários. |
| charge.transactions.card.billingAddress.street | string | Não | Rua. |
| charge.transactions.card.billingAddress.number | string | Não | Número. |
| charge.transactions.card.billingAddress.neighborhood | string | Não | Bairro. |
| charge.transactions.card.billingAddress.city | string | Não | Cidade. |
| charge.transactions.card.billingAddress.state | string | Não | Estado. |
| charge.transactions.card.billingAddress.country | string | Não | País. |
| charge.transactions.card.billingAddress.zipCode | string | Não | CEP. |
| charge.transactions.card.billingAddress.complement | string | Não | Complemento. |
| charge.transactions.card.isPrivateLabel | bool | Não | Indica se o cartão é um produto de whitelabel ou não. Whitelabel é um produto ou serviço que uma empresa produz e comercializa com outras empresas que tem interesse em utilizar o mesmo com sua marca estampada. |
| charge.transactions.card.expirationMonth | int | Sim | O Mês de expiração do cartão com 2 dígitos. |
| charge.transactions.card.expirationYear | int | Sim | O Ano de expiração do cartão com 4 dígitos. |
| charge.transactions.card.brandName | string | Não | O nome da bandeira do cartão. |
| charge.transactions.card.cardToken | string | Não | Token do cartão. |
| charge.transactions.card.eci | string | Não | Código de autenticação ECI (Retornado apenas quando a transação passa pelo fluxo do 3DS). |
| charge.transactions.card.cavv | string | Não | Criptorgrama de autenticação (Retornado apenas quando a transação passa pelo fluxo do 3DS). |
| charge.transactions.card.xid | string | Não | Identificador MPI da transação autenticada. |
| charge.transactions.card.cardholderAuthenticationVersion | string | Não | Versão da autentificação retornada pelo provedor. |
| charge.transactions.card.metadata | objeto | Não | Armazena todas as credenciais relacionadas a bandeira. |
| charge.transactions.card.metadata.additionalProp1 | string | Não | Propriedade adicional. |
| charge.transactions.card.metadata.additionalProp2 | string | Não | Propriedade adicional. |
| charge.transactions.card.metadata.additionalProp3 | string | Não | Propriedade adicional. |
| charge.transactions.card.cardTransactionId | string | Não | ID para a requisição da transação do cartão. |
| charge.transactions.card.cof | bool | Não | indica se a transação é COF (Credentials On File). |
| charge.transactions.temporaryCardToken | string | Não | Token do cartão que foi gerado em um endpoint temporário de cartão. |
| charge.transactions.externalWallet | object | Não | Informações de carteira externa. |
| charge.transactions.externalWallet.type | int | Não | Indica qual carteira foi usada. |
| charge.transactions.externalWallet.payload | string | Não | Payload enviado pela carteira para processamento. |
| charge.transactions.externalWallet.billingAddress | object | Não | Endereço relacionado à conta da carteira externa. |
| charge.transactions.externalWallet.street | string | Não | Rua. |
| charge.transactions.externalWallet.number | string | Não | Número. |
| charge.transactions.externalWallet.neighborhood | string | Não | Bairro. |
| charge.transactions.externalWallet.city | string | Não | Cidade. |
| charge.transactions.externalWallet.state | string | Não | Estado. |
| charge.transactions.externalWallet.country | string | Não | País. |
| charge.transactions.externalWallet.zipCode | string | Não | CEP. |
| charge.transactions.externalWallet.complement | string | Não | Complemento. |
| charge.transactions.paymentType | int | Sim | Tipo de transação. |
| charge.transactions.amount | int | Sim | O valor do pagamento em centavos. |
| charge.transactions.installmentNumber | int | Sim | Quantidade de parcelas. Só pode ser maior que **1** se o tipo de transação for crédito. |
| charge.transactions.softDescriptor | string | Não | Breve descrição a ser apresentada na fatura bancária do cliente. Este campo aceita apenas strings compostas por letras (maiúsculas ou minúsculas), números e o caractere asterisco (*), **sem espaços** nem outros símbolos. Formato equivalente à expressão regular `/^[a-zA-Z0-9*]+$/`. Se nulo, ele será preenchido com um rótulo padrão definido pela Safrapay. |
| charge.transactions.merchantTransactionId | string | Não | Identificador de pedido definido pelo sistema do estabelecimento comercial. Esta propriedade é obrigatória e servirá para capturar, cancelar e consultar posteriormente a transação. **Não utilize espaços** no meio do valor. |
| charge.transactions.installmentType | int | Sim | Tipo de parcelamento da transação |
| charge.transactions.acquirer | int | Não | O ID da adquirente. |
| charge.transactions.firstSubscriptionCharge | bool | Não | Indica se a transação é a primeira cobrança de assinatura. |
| charge.transactions.productIds | array(string) | Não | O ID de cada produto sendo comprado pela transação. |
| charge.transactions.source | object | Não | É a origem da transação. |
| charge.transactions.source.id | string | Sim | O ID do SmartCheckout |
| charge.transactions.source.type | int | Sim | Tipo de smartCheckout. |
| charge.transactions.boardingTaxAmount | object | Não | Representa as informações sobre taxas de embarque para companhias aéreas. |
| charge.transactions.boardingTaxAmount.amount | int | Não | Valor da taxa de embarque cobrada pela companhia aérea. |
| charge.transactions.boardingTaxAmount.entryAmount | int | Não | Valor da taxa de embarque cobrada pela companhia aérea. |
| charge.transactions.acquirerKey | string | Não | Número da chave do contrato do adquirente. |
| charge.transactions.sdwo | object | Não | Dados do integrador. |
| charge.transactions.sdwo.merchantCode | string | Sim | Código do estabelecimento. |
| charge.transactions.sdwo.walletId | string | Sim | ID da carteira que será integrada. |
| charge.transactions.sdwo.mcc | string | Sim | Número MCC que será enviado na integração. |
| charge.transactions.sdwo.name | string | Não | Nome do submerchant. |
| charge.transactions.sdwo.document | string | Não | Número do documento. |
| charge.transactions.sdwo.documentType | int | Não | Tipo de documento de acordo com o número do documento. |
| charge.transactions.sdwo.addressLine | string | Sim | Linha de endereço. |
| charge.transactions.sdwo.phone | object | Sim | Informações de telefone. |
| charge.transactions.sdwo.phone.countryCode | string | Sim | Código do país. |
| charge.transactions.sdwo.phone.areaCode | string | Sim | Código de área. |
| charge.transactions.sdwo.phone.number | string | Sim | Número do Telefone. |
| charge.transactions.sdwo.phone.type | PhoneType | Não | Tipo do telefone. |
| charge.transactions.sdwo.address | object | Não | Informações de endereço. |
| charge.transactions.sdwo.address.city | string | Sim | Cidade. |
| charge.transactions.sdwo.address.state | string | Sim | Estado. |
| charge.transactions.sdwo.address.country | string | Sim | País. |
| charge.transactions.sdwo.address.zipCode | string | Sim | CEP. |
| charge.transactions.sdwo.address.complement | string | Sim | Complemento. |
| charge.transactions.sdwo.operationType | string | Não | Opcional quando vazio, por padrão o valor é "BackToBack". |
| charge.transactions.authentication | object | Não | Dados informativos para autenticação 3DS. |
| charge.transactions.authentication.xid | string | Não | MPI identificador da transação autenticada, no formato base64 (usado apenas para bandeira VISA). |
| charge.transactions.authentication.cavv | string | Não | Identificador de autenticação criptografado pela bandeira (VISA e Mastercard) no formato base64. |
| charge.transactions.authentication.eci | string | Não | Indicador que mostra se a transação foi processada com Bearer authentication. |
| charge.transactions.authentication.directoryServer | string | Não | Campo usado apenas para bandeira Elo. |
| charge.transactions.authentication.version | string | Não | Versão utilizada no 3DS. |
| charge.products | array(object) | Não | Lista com cada produto dentro da cobrança. |
| charge.products.id | string | Não | UUID do produto. |
| charge.products.amount | int | Não | Valor do produto. |
| charge.products.name | int | Não | Nome do produto. |
| charge.products.description | string | Não | Descrição do produto. |
| charge.products.membershipFee | int | Não | Taxa que o cliente paga para ter o produto. |
| charge.products.sku | string | Não | ID único definido pelo comércio para identificar o produto na nossa base de dados (Stock Keeping Unit). |
| charge.products.quantity | int | Não | Quantidade do produto no carrinho. |
| charge.products.imagesRef | array(string) | Não | Lista com URL das imagens do produto. |
| charge.products.isActive | bool | Não | Define se o produto está ativo ou não. |
| charge.source | int | Sim | Define a fonte de cobrança, por exemplo, um POS, pinpad, site de comércio eletrônico. |
| charge.origin | string | Não | Uma propriedade que o cliente pode usar para identificar a origem da cobrança, como nome do fornecedor ou identificador. |
| charge.receivers | array(object) | Não | Recebedores envolvidos na cobrança. Irá definir quem receberá a transação pela divisão do valor total da cobrança em diferentes pagamentos. |
| charge.receivers.id | string | Sim | Documento identificador. |
| charge.receivers.mdrDiscount | bool | Não | Define se terá desconto MDR. |
| charge.receivers.fixedAmountComission | float | Não | Valor fixo que o destinatário deve receber. |
| charge.receivers.chargeRemainder | bool | Não | Após processar os valores divididos para cada parte, se houver centavos que sobraram da divisão, este campo indica qual destinatário deverá receber os centavos restantes. Também pode ser definido para divisão de centavos (exemplo 100/3) ou para quando o destinatário não tiver regra especifica. |
| charge.receivers.percentageComission | float | Não | Esta comissão é calculada no topo do valor da transação. |
| charge.receivers.mdrComission | float | Não | Porcentagem relativa ao MDR calculado na liquidação. |
| charge.receivers.membershipComission | float | Não | Comissão percentual para transações de associação. |
| charge.receivers.amount | float | Não | Valor. |
| charge.metadata | object | Não | Entradas coletadas para iniciação do evento. |
| charge.metadata.key | string | Não | O nome da chave (campo) |
| charge.metadata.value | string | Não | O valor da chave. |
| charge.gatewayId | string | Não | Gateway ID criado para o cliente para uso de autorização do Safra. |
| charge.shippingAddress | object | Não | Representa as informações do endereço de envio. |
| charge.shippingAddress.country | string | Não | Código do país. |
| charge.shippingAddress.street | string | Não | Rua. |
| charge.shippingAddress.number | string | Não | Número. |
| charge.shippingAddress.complement | string | Não | Complemento. |
| charge.shippingAddress.neighborhood | string | Não | Bairro. |
| charge.shippingAddress.postalCode | string | Não | Código postal. |
| charge.shippingAddress.city | string | Não | Cidade. |
| charge.shippingAddress.state | string | Não | Estado. |
| charge.shippingSettings | array(object) | Não | Configurações adicionais de envio. |
| charge.shippingSettings.merchantId | string | Não | ID único do estabelecimento relacionado à configuração de envio. |
| charge.shippingSettings.amount | int | Não | Valor do envio. |
| charge.macAddress | string | Não | Endereço MAC (Media Access Control) do dispositivo de origem usado para identificar exclusivamente um controlador de interface de rede. |
| lateCapture | bool | Não | Informar valor "true" para uma autorização com captura tardia. Valor padrão: false. |
| capture | bool | Sim | Se a cobrança deve ou não ser capturada. |
| templateId | string | Não | TemplateId que será usado para enviar o recibo ao cliente. |
| primaryColor | string | Não | A cor primária da configuração do comerciante. |
| secondaryColor | string | Não | A cor secundária da configuração do comerciante. |
| hostname | string | Não | O hostname da configuração do comerciante. |
| merchantCode | string | Não | Código do estabelecimento definido pelo integrador. |
| remoteIp | string | Sim | **\[OBRIGATÓRIO quando antifraude ativo\]** O endereço IP do comprador. Este dado é utilizado em diversas verificações de risco (número de tentativas de pagamento, verificações baseadas em localização, detecção de uso de VPN/proxy). **Suporta IPv4.** **Exemplo:** `192.168.1.100`. Este campo complementa a implementação do Device Fingerprint. Consulte [documentação completa](../guias/antifraude.md#campo-remoteip-complemento-ao-device-fingerprint). |

#### BODY Raw

```http
{
"charge": {
"merchantChargeId": "TASK5333",
"customer": {
"name": "Ester Patrícia Aparício",
"email": "eesterpatriciaaparicio@ladder.com.br",
"document": "71877920002",
"documentType": 1,
"phone": {
"number": "999999999",
"countryCode": "55",
"areaCode": "21",
"type": 5
}
},
"transactions": [
{
"card": {
"cardNumber": "4444585001234562",
"cvv": "123",
"brand": 1,
"cardholderName": "Ester Patrícia Aparício",
"cardholderDocument": "71877920002",
"billingAddress": {
"street": "Rua Juvêncio Erudilho",
"number": "39",
"neighborhood": "Centro",
"city": "Gurupi",
"state": "BA",
"country": "BR",
"zipCode": "44002-528"
},
"expirationMonth": 12,
"expirationYear": 2034
},
"paymentType": 2,
"amount": 10000,
"installmentNumber": 2,
"installmentType": 1,
"softDescriptor": "TASK*5333",
}
],
"source": 8
}
}
```

<a id="com-juros"></a>

### Com Juros

> Exemplo de requisição (Com juros)

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/charge/authorization")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n  \"charge\": {\r\n    \"merchantChargeId\": \"TASK5333\",\r\n    \"customer\": {\r\n      \"name\": \"Ester Patrícia Aparício\",\r\n      \"email\": \"eesterpatriciaaparicio@ladder.com.br\",\r\n      \"document\": \"71877920002\",\r\n      \"documentType\": 1,\r\n      \"phone\": {\r\n          \"number\": \"999999999\",\r\n          \"countryCode\": \"55\",\r\n          \"areaCode\": \"21\",\r\n          \"type\": 5\r\n      }\r\n    },\r\n    \"transactions\": [\r\n      {\r\n        \"card\": {\r\n          \"cardNumber\": \"4444585001234562\",\r\n          \"cvv\": \"123\",\r\n          \"brand\": 1,\r\n          \"cardholderName\": \"Ester Patrícia Aparício\",\r\n          \"cardholderDocument\": \"71877920002\",\r\n          \"billingAddress\": {\r\n            \"street\": \"Rua Juvêncio Erudilho\",\r\n            \"number\": \"39\",\r\n            \"neighborhood\": \"Centro\",\r\n            \"city\": \"Gurupi\",\r\n            \"state\": \"BA\",\r\n            \"country\": \"BR\",\r\n            \"zipCode\": \"44002-528\"\r\n          },\r\n          \"expirationMonth\": 12,\r\n          \"expirationYear\": 2034\r\n        },\r\n        \"paymentType\": 2,\r\n        \"amount\": 10000,\r\n        \"installmentNumber\": 2,\r\n  \"installmentType\": 2,\r\n      \"softDescriptor\": \"TASK*5333\"\r\n      }\r\n    ],\r\n    \"source\": 8\r\n  }\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/charge/authorization"

payload="{\r\n  \"charge\": {\r\n    \"merchantChargeId\": \"TASK5333\",\r\n    \"customer\": {\r\n      \"name\": \"Ester Patrícia Aparício\",\r\n      \"email\": \"eesterpatriciaaparicio@ladder.com.br\",\r\n      \"document\": \"71877920002\",\r\n      \"documentType\": 1,\r\n      \"phone\": {\r\n          \"number\": \"999999999\",\r\n          \"countryCode\": \"55\",\r\n          \"areaCode\": \"21\",\r\n          \"type\": 5\r\n      }\r\n    },\r\n    \"transactions\": [\r\n      {\r\n        \"card\": {\r\n          \"cardNumber\": \"4444585001234562\",\r\n          \"cvv\": \"123\",\r\n          \"brand\": 1,\r\n          \"cardholderName\": \"Ester Patrícia Aparício\",\r\n          \"cardholderDocument\": \"71877920002\",\r\n          \"billingAddress\": {\r\n            \"street\": \"Rua Juvêncio Erudilho\",\r\n            \"number\": \"39\",\r\n            \"neighborhood\": \"Centro\",\r\n            \"city\": \"Gurupi\",\r\n            \"state\": \"BA\",\r\n            \"country\": \"BR\",\r\n            \"zipCode\": \"44002-528\"\r\n          },\r\n          \"expirationMonth\": 12,\r\n          \"expirationYear\": 2034\r\n        },\r\n        \"paymentType\": 2,\r\n        \"amount\": 10000,\r\n        \"installmentNumber\": 2,\r\n  \"installmentType\": 2,\r\n      \"softDescriptor\": \"TASK*5333\"\r\n      }\r\n    ],\r\n    \"source\": 8\r\n  }\r\n}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/charge/authorization' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "charge": {
    "merchantChargeId": "TASK5333",
    "customer": {
      "name": "Ester Patrícia Aparício",
      "email": "eesterpatriciaaparicio@ladder.com.br",
      "document": "71877920002",
      "documentType": 1,
      "phone": {
          "number": "999999999",
          "countryCode": "55",
          "areaCode": "21",
          "type": 5
      }
    },
    "transactions": [
      {
        "card": {
          "cardNumber": "4444585001234562",
          "cvv": "123",
          "brand": 1,
          "cardholderName": "Ester Patrícia Aparício",
          "cardholderDocument": "71877920002",
          "billingAddress": {
            "street": "Rua Juvêncio Erudilho",
            "number": "39",
            "neighborhood": "Centro",
            "city": "Gurupi",
            "state": "BA",
            "country": "BR",
            "zipCode": "44002-528"
          },
          "expirationMonth": 12,
          "expirationYear": 2034
        },
        "paymentType": 2,
        "amount": 10000,
        "installmentNumber": 2,
        "installmentType": 2,
        "softDescriptor": "TASK*5333"
      }
    ],
    "source": 8
  }
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"charge":{"merchantChargeId":"TASK5333","customer":{"name":"Ester Patrícia Aparício","email":"eesterpatriciaaparicio@ladder.com.br","document":"71877920002","documentType":1,"phone":{"number":"999999999","countryCode":"55","areaCode":"21","type":5}},"transactions":[{"card":{"cardNumber":"4444585001234562","cvv":"123","brand":1,"cardholderName":"Ester Patrícia Aparício","cardholderDocument":"71877920002","billingAddress":{"street":"Rua Juvêncio Erudilho","number":"39","neighborhood":"Centro","city":"Gurupi","state":"BA","country":"BR","zipCode":"44002-528"},"expirationMonth":12,"expirationYear":2034},"paymentType":2,"amount":10000,"installmentNumber":2,"installmentType": 2,"softDescriptor":"TASK*5333"}],"source":8}});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/charge/authorization", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "charge": {
        "merchantChargeId": "TASK5333",
        "id": "3e60759b-e818-4a83-a98c-883fcd609d4f",
        "nsu": "000000019",
        "customerId": "a1a5a477-f8b5-471d-ab42-765c2e4b1ad1",
        "chargeStatus": "Authorized",
        "transactions": [
            {
              "card": {
                  "id": "65327e40-37ee-4c23-9369-4845519d19b7",
                  "customerId": "a1a5a477-f8b5-471d-ab42-765c2e4b1ad1",
                  "cardNumber": "444458******4562",
                  "brand": "Visa",
                  "cardholderName": "Ester Patrícia Aparício",
                  "cardholderDocument": "71877920002",
                  "billingAddress": {
                      "street": "Rua Juvêncio Erudilho",
                      "number": "39",
                      "neighborhood": "Centro",
                      "city": "Gurupi",
                      "state": "BA",
                      "country": "BR",
                      "zipCode": "44002-528"
                  },
                  "isPrivateLabel": false,
                  "expirationMonth": 12,
                  "expirationYear": 2034,
                  "brandName": "Visa"
              },
              "isApproved": true,
              "paymentType": "Credit",
              "installmentType": "Issuer",
              "installmentNumber": 2,
              "softDescriptor": "TASK*5333",
              "amount": 10000,
              "isCapture": true,
              "isRecurrency": false,
              "isCanceled": false,
              "transactionId": "1623709631269",
              "transactionStatus": "Captured",
              "merchantTransactionId": "TASK5333",
              "acquirer": "Simulator",
              "creationDateTime": "2021-06-14T19:27:11.3167988-03:00",
              "captureDateTime": "2021-06-14T19:27:11.3156408-03:00",
              "authorizationResponseCode": "00",
              "authorizationCode": "689020",
              "acquirerTransactionId": "ff478f2d-r569-568s-22ds-52s6742",
              "bankSlipStatus": 0
            }
        ]
    },
    "success": true,
    "errors": [],
    "traceKey": "ac0ea0e1-ad9f-412e-a0bb-4b97e9893a3f"
}
```

Para realizarmos uma transação parcelada com juros, devemos alterar o campo InstallmentType para o valor **2**. Assim teremos a mesma transação acima, porém parcelada com juros.

<a id="alteração-em-atributos-1"></a>

#### Alteração em Atributos

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| charge.transactions.installmentType | int | Sim | Este é o atributo que diferencia uma transação com e sem juros. Se enviado o valor **1**, a transação será parcelada pelo lojista, ou seja, sem juros. Se passado o valor **2**, a transação será parcelada pelo emissor do cartão, ou seja, com juros. Esta informação pode ser consultada em **Tipo de parcelamento da transação** |

<a id="voucher"></a>

## Voucher

O **Voucher PAT** é um meio de pagamento vinculado ao **Programa de Alimentação do Trabalhador (PAT)**, iniciativa voltada à concessão de benefícios destinados à alimentação dos trabalhadores. Na prática, essa modalidade permite que empresas ofereçam aos seus colaboradores um benefício para uso em estabelecimentos habilitados, por meio de cartão ou credencial eletrônica aceita na rede autorizada.

No contexto transacional, o Voucher PAT é processado como uma modalidade específica de pagamento, com regras próprias de autorização e aceitação, de acordo com o arranjo e com o produto contratado.

> **⚠️ Ponto de atenção:** Mesmo quando embandeirado com Visa, Mastercard ou Elo, o cartão deve ser processado no **trilho de pagamento "Voucher"**, com regras de aceitação, autorização e liquidação próprias para benefícios.

<a id="aceitação"></a>

#### Aceitação

A aceitação depende de habilitação do estabelecimento para esse tipo de benefício. Se você ainda não é cliente, consulte o seu relacionamento comercial Safrapay e solicite a habilitação do voucher. Se você já é cliente, habilite a função em: Safra Empresas > Safrapay > Venda com cartões de benefícios.

<a id="prazo-de-liquidação"></a>

#### Prazo de liquidação

As vendas de Voucher realizadas no novo arranjo PAT serão liquidadas em **15 dias** e serão apresentadas no Extrato Safrapay.

<a id="regras-de-autorização"></a>

#### Regras de autorização

A autorização da transação depende dos seguintes critérios:

- Elegibilidade do estabelecimento, de acordo com o MCC;
- Regras do emissor/arranjo;
- Uso do trilho correto de voucher;
- Tipo de benefício;
- Saldo disponível no benefício.

<a id="mccs-compatíveis-com-o-programa-de-benefícios-pat-voucher"></a>

#### MCCs compatíveis com o programa de benefícios PAT Voucher

| MCC | Descrição |
| --- | --- |
| 5300 | Venda por atacado (Wholesale Clubs) |
| 5311 | Lojas de departamentos |
| 5411 | Mercearias / Supermercados |
| 5422 | Açougues |
| 5441 | Loja de doces |
| 5451 | Produtos de laticínios |
| 5462 | Confeitarias |
| 5499 | Alimentos variados |
| 5811 | Distribuição e produção de alimentos |
| 5812 | Restaurantes |
| 5813 | Bares, pubs e casas noturnas |
| 5814 | Lanchonetes / Fast food |
| 5815 | Produtos digitais audiovisuais |
| 5733 | Instrumentos musicais |
| 5735 | Lojas de discos |
| 5932 | Loja de antiguidades |
| 5942 | Livrarias |
| 5943 | Papelarias |
| 5994 | Banca de jornal / notícias |
| 4722 | Agências de viagens |
| 7832 | Cinemas / produções cinematográficas |
| 7841 | Lojas de vídeos |
| 7911 | Estúdios / escolas de dança |
| 7922 | Teatros / espetáculos |
| 7929 | Bandas / artistas diversos |
| 7991 | Atrações turísticas / exposições |
| 7996 | Parques / circos |
| 7998 | Aquários / zoológicos |
| 8699 | Associações culturais / sindicatos |
| 9399 | Serviços governamentais |

<a id="orientações-de-integração"></a>

### Orientações de integração

O endpoint de autorização permite registrar e processar uma cobrança do tipo Voucher, retornando o resultado da análise transacional e o status da autorização. A transação é enviada com os dados do cliente, cartão, valor da compra e identificadores da operação.

<a id="regras-de-negócio"></a>

#### Regras de negócio

1. O endpoint utilizado para esta operação deve ser o de **autorização** (`POST /v2/charge/authorization`).
2. O campo `paymentType` deve ser enviado com o valor **3** (Voucher).
3. O valor da transação deve ser informado em **centavos**.
4. Para transações Voucher PAT, o parcelamento deve seguir o padrão:
  - `installmentNumber` = `1` (sempre à vista).
  - `installmentType` = `"None"`.
5. O identificador da cobrança no estabelecimento deve ser enviado no campo `merchantChargeId`.
6. O identificador da transação no estabelecimento deve ser enviado no campo `merchantTransactionId`.
7. A transação está sujeita à validação do emissor, da bandeira e das regras do produto voucher.
8. A aprovação da transação deve ser validada pelos campos `chargeStatus` e `transactions[].isApproved`.

<a id="post-charge-authorization-2"></a>

### `POST` /charge/authorization

**Versão** `v2.0`

<a id="requisição-http-5"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/charge/authorization
```

> Exemplo de requisição

```ruby
require "uri"
require "json"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/charge/authorization")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "charge": {
    "customer": {
      "name": "Victor Barbosa",
      "email": "victor.barbosa@safra.com.br",
      "document": "57730954834",
      "documentType": 1,
      "phone": {
        "number": "972255710",
        "countryCode": 55,
        "areaCode": 11,
        "type": 5
      }
    },
    "transactions": [
      {
        "card": {
          "cardNumber": "5491670000000005",
          "cvv": "911",
          "brand": 1,
          "cardholderName": "VICTOR A BARBOSA",
          "cardholderDocument": "57730954834",
          "expirationMonth": "09",
          "expirationYear": "2029"
        },
        "paymentType": 3,
        "amount": 1500,
        "installmentNumber": 1
      }
    ],
    "source": 1
  }
})

response = https.request(request)
puts response.read_body
```

```python
import requests
import json

url = "{{ENDPOINT_GATEWAY}}/v2/charge/authorization"

payload = json.dumps({
  "charge": {
    "customer": {
      "name": "Victor Barbosa",
      "email": "victor.barbosa@safra.com.br",
      "document": "57730954834",
      "documentType": 1,
      "phone": {
        "number": "972255710",
        "countryCode": 55,
        "areaCode": 11,
        "type": 5
      }
    },
    "transactions": [
      {
        "card": {
          "cardNumber": "5491670000000005",
          "cvv": "911",
          "brand": 1,
          "cardholderName": "VICTOR A BARBOSA",
          "cardholderDocument": "57730954834",
          "expirationMonth": "09",
          "expirationYear": "2029"
        },
        "paymentType": 3,
        "amount": 1500,
        "installmentNumber": 1
      }
    ],
    "source": 1
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
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/charge/authorization' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "charge": {
    "customer": {
      "name": "Victor Barbosa",
      "email": "victor.barbosa@safra.com.br",
      "document": "57730954834",
      "documentType": 1,
      "phone": {
        "number": "972255710",
        "countryCode": 55,
        "areaCode": 11,
        "type": 5
      }
    },
    "transactions": [
      {
        "card": {
          "cardNumber": "5491670000000005",
          "cvv": "911",
          "brand": 1,
          "cardholderName": "VICTOR A BARBOSA",
          "cardholderDocument": "57730954834",
          "expirationMonth": "09",
          "expirationYear": "2029"
        },
        "paymentType": 3,
        "amount": 1500,
        "installmentNumber": 1
      }
    ],
    "source": 1
  }
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"charge":{"customer":{"name":"Victor Barbosa","email":"victor.barbosa@safra.com.br","document":"57730954834","documentType":1,"phone":{"number":"972255710","countryCode":55,"areaCode":11,"type":5}},"transactions":[{"card":{"cardNumber":"5491670000000005","cvv":"911","brand":1,"cardholderName":"VICTOR A BARBOSA","cardholderDocument":"57730954834","expirationMonth":"09","expirationYear":"2029"},"paymentType":3,"amount":1500,"installmentNumber":1}],"source":1}});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/charge/authorization", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "charge": {
        "merchantChargeId": "a2c65b4b-beb1-4216-ae91-22c6b554d0fe",
        "id": "e4d90b38-8d51-425d-8207-a74e26069c89",
        "nsu": "000000315",
        "customerId": "272e080c-661e-8485-826a-06f649421569",
        "chargeStatus": "Authorized",
        "transactions": [
            {
                "card": {
                    "id": "2ae6b393-134e-4c21-963e-3e8f18799c96",
                    "customerId": "272e080c-661e-8485-826a-06f649421569",
                    "cardNumber": "549167******0005",
                    "brand": "Mastercard",
                    "cardholderName": "VICTOR A BARBOSA",
                    "cardholderDocument": "57730954834",
                    "isPrivateLabel": false,
                    "expirationMonth": 9,
                    "expirationYear": 2029,
                    "brandName": "Mastercard",
                    "cof": true
                },
                "isApproved": true,
                "paymentType": "Voucher",
                "installmentType": "None",
                "installmentNumber": 1,
                "softDescriptor": "EXSTORE123",
                "amount": 1500,
                "originalAmount": 1500,
                "isCapture": true,
                "isRecurrency": false,
                "isCanceled": false,
                "transactionId": "1624024252357",
                "transactionStatus": "Captured",
                "merchantTransactionId": "c8d4a9f2-5b1e-4c3a-8f2d-a7b9e1c6d5f8",
                "acquirer": "Simulator",
                "creationDateTime": "2026-04-23T10:50:52.37",
                "captureDateTime": "2026-04-23T10:50:52.37",
                "authorizationResponseCode": "00",
                "authorizationCode": "927648"
            }
        ]
    },
    "success": true,
    "errors": [],
    "traceKey": "84272215-cfdd-42df-bfcd-4669ed40b269"
}
```

O Endpoint responsável por criar uma nova cobrança do tipo Voucher, contendo uma transação autorizada. A cobrança é processada no trilho de voucher, com as regras específicas do produto de benefícios.

<a id="requisição-4"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| charge | Object | Sim | Dados da transação. |
| charge.merchantChargeId | string | Sim | Identificador da cobrança no estabelecimento. **Sem espaços** no valor. Campos obrigatórios não podem ser `""`. |
| charge.customer | object | Sim | Dados do comprador. |
| charge.customer.name | string | Sim | Nome completo do comprador. |
| charge.customer.email | string | Sim | E-mail do comprador. |
| charge.customer.documentType | int | Sim | Tipo do documento do comprador. |
| charge.customer.document | string | Sim | Documento do comprador. |
| charge.customer.phone | object | Sim | Telefone do comprador. |
| charge.customer.phone.countryCode | string | Sim | Código do país. |
| charge.customer.phone.areaCode | string | Sim | Código de área. |
| charge.customer.phone.number | string | Sim | Número do telefone. |
| charge.customer.phone.type | int | Sim | Tipo do telefone. |
| charge.transactions | array(object) | Sim | Lista de transações enviadas na cobrança. |
| charge.transactions.card | object | Sim | Dados do cartão utilizado na transação. |
| charge.transactions.card.cardNumber | string | Sim | Número do cartão. |
| charge.transactions.card.cvv | string | Sim | Código de segurança do cartão. |
| charge.transactions.card.brand | int | Sim | Bandeira do cartão. |
| charge.transactions.card.cardholderName | string | Sim | Nome do portador do cartão. |
| charge.transactions.card.cardholderDocument | string | Sim | Documento do portador do cartão. |
| charge.transactions.card.expirationMonth | int | Sim | Mês de expiração do cartão. |
| charge.transactions.card.expirationYear | int | Sim | Ano de expiração do cartão. |
| charge.transactions.card.billingAddress | object | Condicional | Endereço de cobrança do cartão. **Obrigatório caso utilize antifraude.** |
| charge.transactions.card.billingAddress.street | string | Não | Rua. |
| charge.transactions.card.billingAddress.number | string | Não | Número. |
| charge.transactions.card.billingAddress.neighborhood | string | Não | Bairro. |
| charge.transactions.card.billingAddress.city | string | Não | Cidade. |
| charge.transactions.card.billingAddress.state | string | Não | Estado. |
| charge.transactions.card.billingAddress.country | string | Não | País. |
| charge.transactions.card.billingAddress.zipCode | string | Não | CEP. |
| charge.transactions.paymentType | int | Sim | Tipo de pagamento. Para transações Voucher, informar o valor **3**. |
| charge.transactions.amount | int | Sim | Valor da transação em centavos. |
| charge.transactions.installmentNumber | int | Sim | Quantidade de parcelas. Para Voucher PAT deve ser sempre **1** (à vista). |
| charge.transactions.installmentType | string | Não | Tipo de parcelamento. Para Voucher PAT deve ser enviado como `"None"`. |
| charge.transactions.softDescriptor | string | Não | Breve descrição apresentada ao portador, quando aplicável. |
| charge.transactions.merchantTransactionId | string | Sim | Identificador da transação no estabelecimento. |
| charge.source | int | Sim | Define a fonte de cobrança. |

<a id="resposta-4"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| merchantChargeId | string | Identificador da cobrança no estabelecimento. |
| id | string | Identificador da cobrança na plataforma. |
| nsu | string | NSU da transação. |
| customerId | string | Identificador do cliente. |
| chargeStatus | string | Status geral da cobrança. |
| transactions | array(object) | Lista de transações processadas. |
| transactions.card | object | Dados mascarados do cartão. |
| transactions.card.cardNumber | string | Número do cartão mascarado. |
| transactions.card.brand | string | Bandeira do cartão. |
| transactions.card.cardholderName | string | Nome do portador. |
| transactions.card.cardholderDocument | string | Documento do portador. |
| transactions.card.expirationMonth | int | Mês de expiração do cartão. |
| transactions.card.expirationYear | int | Ano de expiração do cartão. |
| transactions.isApproved | bool | Indica se a transação foi aprovada. |
| transactions.paymentType | string | Tipo de pagamento. Para Voucher retorna `"Voucher"`. |
| transactions.installmentType | string | Tipo de parcelamento. |
| transactions.installmentNumber | int | Número de parcelas. |
| transactions.softDescriptor | string | Descrição da transação. |
| transactions.amount | int | Valor da transação em centavos. |
| transactions.originalAmount | int | Valor original da transação em centavos. |
| transactions.transactionId | string | Identificador da transação. |
| transactions.transactionStatus | string | Status da transação. |
| transactions.acquirer | string | Nome da adquirente. |
| transactions.authorizationResponseCode | string | Código de resposta da autorização. |
| transactions.authorizationCode | string | Código de autorização. |
| success | bool | Indica se a requisição foi processada com sucesso. |
| errors | array(object) | Lista de erros caso `success: false`. |
| traceKey | string | Identificador da operação. |

<a id="status-possíveis"></a>

#### Status possíveis

| Status | Descrição |
| --- | --- |
| Authorized | Transação autorizada. |
| Denied | Transação negada. |
| Pending | Transação pendente. |
| Canceled | Transação cancelada. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

<a id="body-raw-3"></a>

#### BODY Raw

```http
{
"charge": {
"customer": {
"name": "Victor Barbosa",
"email": "victor.barbosa@safra.com.br",
"document": "57730954834",
"documentType": 1,
"phone": {
"number": "972255710",
"countryCode": 55,
"areaCode": 11,
"type": 5
}
},
"transactions": [
{
"card": {
"cardNumber": "5491670000000005",
"cvv": "911",
"brand": 1,
"cardholderName": "VICTOR A BARBOSA",
"cardholderDocument": "57730954834",
"expirationMonth": "09",
"expirationYear": "2029"
},
"paymentType": 3,
"amount": 1500,
"installmentNumber": 1
}
],
"source": 1
}
}
```

<a id="critério-de-aprovação"></a>

#### Critério de aprovação

A transação deve ser considerada **aprovada** quando atender simultaneamente aos seguintes critérios:

- `chargeStatus` = `"Authorized"`
- `transactions[].isApproved` = `true`

A transação deve ser considerada **negada** quando:

- `chargeStatus` = `"Denied"` **ou**
- `transactions[].isApproved` = `false`

<a id="códigos-de-erro"></a>

#### Códigos de erro

| Código | Descrição |
| --- | --- |
| 400 | Requisição inválida. |
| 401 | Não autorizado. |
| 404 | Recurso não encontrado. |
| 422 | Dados inválidos para autorização. |
| 500 | Erro interno de processamento. |

> Exemplo de resposta com erro

```json
{
    "success": false,
    "errors": [
        {
            "errorCode": 422,
            "message": "Dados do cartão inválidos para transação voucher"
        }
    ]
}
```

<a id="observações"></a>

#### Observações

- O campo `paymentType` deve ser enviado obrigatoriamente como **3** (Voucher).
- O valor da transação deve ser informado em **centavos**.
- Para o fluxo Voucher PAT, o parcelamento deve ser enviado sempre como:
  - `installmentNumber` = `1`
  - `installmentType` = `"None"`
- Os dados do cartão retornam **mascarados** na resposta.
- A autorização depende das regras do emissor, da bandeira e do produto voucher.
- O estabelecimento deve validar o resultado da transação com base nos campos de status e aprovação retornados pela API.

<a id="pré-autorização"></a>

## Pré-Autorização

> 🛡️ **Antifraude:** Para transações com antifraude ativo, os campos `sessionId` e `remoteIp` são obrigatórios. Consulte a [documentação do Device Fingerprint e SDK SafraPay Antifraud](../guias/antifraude.md#device-fingerprint).

<a id="post-charge-preauthorization"></a>

### `POST` /charge/preauthorization

**Versão** `v2.0`

<a id="requisição-http-6"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/charge/preauthorization
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/charge/preauthorization")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n  \"remoteIp\": \"203.0.113.45\",\r\n  \"charge\": {\r\n    \"sessionId\": \"123456789\",\r\n    \"customer\": {\r\n      \"name\": \"Ester Patrícia Aparício\",\r\n      \"email\": \"eesterpatriciaaparicio@ladder.com.br\",\r\n      \"document\": \"71877920002\",\r\n      \"documentType\": 1,\r\n      \"phone\": {\r\n          \"number\": \"999999999\",\r\n          \"countryCode\": \"55\",\r\n          \"areaCode\": \"21\",\r\n          \"type\": 5\r\n      }\r\n    },\r\n    \"transactions\": [\r\n      {\r\n        \"card\": {\r\n          \"cardNumber\": \"4444585001234562\",\r\n          \"cvv\": \"123\",\r\n          \"brand\": 1,\r\n          \"cardholderName\": \"Ester Patrícia Aparício\",\r\n          \"cardholderDocument\": \"71877920002\",\r\n          \"expirationMonth\": 12,\r\n          \"expirationYear\": 2034\r\n        },\r\n        \"paymentType\": 0,\r\n        \"amount\": 1000,\r\n        \"installmentNumber\": 0\r\n        }\r\n    ],\r\n    \"source\": 1\r\n  },\r\n  \"capture\": true\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/charge/preauthorization"

payload="{\r\n  \"remoteIp\": \"203.0.113.45\",\r\n  \"charge\": {\r\n    \"sessionId\": \"123456789\",\r\n    \"customer\": {\r\n      \"name\": \"Ester Patrícia Aparício\",\r\n      \"email\": \"eesterpatriciaaparicio@ladder.com.br\",\r\n      \"document\": \"71877920002\",\r\n      \"documentType\": 1,\r\n      \"phone\": {\r\n          \"number\": \"999999999\",\r\n          \"countryCode\": \"55\",\r\n          \"areaCode\": \"21\",\r\n          \"type\": 5\r\n      }\r\n    },\r\n    \"transactions\": [\r\n      {\r\n        \"card\": {\r\n          \"cardNumber\": \"4444585001234562\",\r\n          \"cvv\": \"123\",\r\n          \"brand\": 1,\r\n          \"cardholderName\": \"Ester Patrícia Aparício\",\r\n          \"cardholderDocument\": \"71877920002\",\r\n          \"expirationMonth\": 12,\r\n          \"expirationYear\": 2034\r\n        },\r\n        \"paymentType\": 0,\r\n        \"amount\": 1000,\r\n        \"installmentNumber\": 0\r\n        }\r\n    ],\r\n    \"source\": 1\r\n  },\r\n  \"capture\": true\r\n}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/charge/preauthorization' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "remoteIp": "203.0.113.45",
  "charge": {
    "sessionId": "123456789",
    "customer": {
      "name": "Ester Patrícia Aparício",
      "email": "eesterpatriciaaparicio@ladder.com.br",
      "document": "71877920002",
      "documentType": 1,
      "phone": {
          "number": "999999999",
          "countryCode": 55,
          "areaCode": 11,
          "type": 5
      }
    },
    "transactions": [
      {
        "card": {
          "cardNumber": "5491670214095346",
          "cvv": "111",
          "brand": "2",
          "cardholderName": "Ester Patrícia Aparício",
          "cardholderDocument": "71877920002",
          "expirationMonth": 12,
          "expirationYear": 2029
        },
        "paymentType": 2,
        "amount": 10000,
        "installmentNumber": 1
      }
    ],
    "source": 1
  },
  "capture": true
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"remoteIp":"203.0.113.45","charge":{"sessionId":"123456789","customer":{"name":"Ester Patrícia Aparício","email":"eesterpatriciaaparicio@ladder.com.br","document":"71877920002","documentType":1,"phone":{"number":"999999999","countryCode":55,"areaCode":11,"type":5}},"transactions":[{"card":{"cardNumber":"5491670214095346","cvv":"111","brand":"2","cardholderName":"Ester Patrícia Aparício","cardholderDocument":"71877920002","expirationMonth":12,"expirationYear":2029},"paymentType":2,"amount":10000,"installmentNumber":1}],"source":1},"capture":true});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/charge/preauthorization", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "charge": {
        "merchantChargeId": "TASK5333",
        "id": "abcc2428-eb4e-4470-9d55-72edca459daf",
        "nsu": "000005044",
        "customerId": "ffede3ee-37ab-47bb-9981-d3d14697d67z",
        "chargeStatus": "PreAuthorized",
        "transactions": [
            {
                "card": {
                    "id": "7903ef09-83c3-458d-ad39-9ea9e736e59e",
                    "customerId": "ffede3ee-37ab-47bb-9981-d3d14697d67z",
                    "cardNumber": "549167******0005",
                    "brand": "Mastercard",
                    "cardholderName": "Yago Sebastião Lima",
                    "cardholderDocument": "78112482802",
                    "isPrivateLabel": false,
                    "expirationMonth": 12,
                    "expirationYear": 2026,
                    "brandName": "Mastercard"
                },
                "isApproved": true,
                "paymentType": "Credit",
                "installmentType": "None",
                "installmentNumber": 1,
                "softDescriptor": "TASK*5333",
                "amount": 1000,
                "isCapture": false,
                "isRecurrency": false,
                "isCanceled": false,
                "transactionId": "1623967391659",
                "transactionStatus": "PreAuthorized",
                "merchantTransactionId": "TASK5333",
                "acquirer": "Simulator",
                "creationDateTime": "2021-06-17T19:03:11.6832635-03:00",
                "captureDateTime": "0001-01-01T00:00:00",
                "authorizationResponseCode": "00",
                "authorizationCode": "304848",
                "merchantAdviceCode": "01",
                "acquirerTransactionId": "ff478f2d-r569-568s-22ds-52s6742",
                "bankSlipStatus": 0
            }
        ],
        "metadata": {
            "key_Sample": "Value_Sample"
        }
    },
    "success": true,
    "errors": [],
    "traceKey": "8d8d389b-8742-4668-8380-ad7ab94bc90d"
}
```

O Endpoint responsável por criar uma nova cobrança, contendo uma transação pré-autorizada, usando adquirente. A carga pode ser capturada posteriormente.

<a id="requisição-5"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| charge | Object | Sim | Dados da transação. |
| charge.merchantChargeId | string | Não | O ID de cobrança definido pelo sistema do comerciante. **Não utilize espaços** no meio do identificador (ex.: `TASK5333`). Campos obrigatórios da estrutura não podem ser enviados vazios nem como string vazia `""`. |
| charge.subscriptionId | string | Não | GUID único relacionado ao subscription. |
| charge.sessionId | string | Condicional | ID da sessão criada pelo servidor do site do cliente e usada durante a visita de um determinado usuário. **Obrigatório caso utilize antifraude.** |
| charge.smartCheckoutId | string | Não | O ID do smartCheckout. |
| charge.id | string | Não | O ID da cobrança. |
| charge.chargeStatus | int | Não | Status atual da cobrança, indicando em qual estágio do processo de autorização a cobrança está. Ele reflete diretamente todos os status de transação dentro da cobrança. |
| charge.subMerchant | object | Não | Objeto com dados referente ao submerchant (Caso exista submerchant). |
| charge.subMerchant.id | string | Sim | ID do submerchant. |
| charge.subMerchant.document | string | Sim | Documento do submerchant. |
| charge.subMerchant.socialName | string | Sim | Razão social do submerchant. |
| charge.subMerchant.address | objeto | Sim | Endereço do submerchant. |
| charge.subMerchant.address.street | string | Sim | Rua. |
| charge.subMerchant.address.number | string | Sim | Número. |
| charge.subMerchant.address.neighborhood | string | Sim | Bairro. |
| charge.subMerchant.address.city | string | Sim | Cidade. |
| charge.subMerchant.address.state | string | Sim | Estado. |
| charge.subMerchant.address.country | string | Sim | País. |
| charge.subMerchant.address.zipCode | string | Sim | CEP. |
| charge.subMerchant.address.complement | string | Não | Complemento. |
| charge.customer | object | Sim | Dados do comprador. |
| charge.customer.id | string | Não | O ID do comprador. |
| charge.customer.name | string | Sim | Nome completo do comprador. |
| charge.customer.email | string | Sim | E-mail do comprador. |
| charge.customer.entityType | entityType | Não | Se é pessoa física ou jurídica. |
| charge.customer.documentType | documentType | Sim | Tipo do documento do comprador. |
| charge.customer.document | string | Sim | Documento do comprador. |
| charge.customer.birthday | date | Não | Data de nascimento do comprador. |
| charge.customer.gender | Gender | Não | Gênero do comprador. |
| charge.customer.phone | object | Sim | Telefone do comprador. |
| charge.customer.phone.countryCode | string | Sim | Código do país. |
| charge.customer.phone.areaCode | string | Sim | Código de área. |
| charge.customer.phone.number | string | Sim | Número do Telefone. |
| charge.customer.phone.type | PhoneType | Sim | Tipo do telefone. |
| charge.customer.address | object | Condicional | Endereço do comprador. **Obrigatório caso utilize antifraude.** |
| charge.customer.address.street | string | Sim | Rua. |
| charge.customer.address.number | string | Sim | Número. |
| charge.customer.address.neighborhood | string | Sim | Bairro. |
| charge.customer.address.city | string | Sim | Cidade. |
| charge.customer.address.state | string | Sim | Estado. |
| charge.customer.address.country | string | Sim | País. |
| charge.customer.address.zipCode | string | Sim | CEP. |
| charge.customer.address.complement | string | Sim | Complemento. |
| charge.customer.bankAccounts | object | Não | Contas do comprador. |
| charge.customer.bankAccounts.bankCode | string | Sim | Código do banco. |
| charge.customer.bankAccounts.bankName | string | Sim | Nome do banco. |
| charge.customer.bankAccounts.branch | string | Sim | Filial. |
| charge.customer.bankAccounts.branchCheckDigit | string | Sim | Dígito de verificação da filial. |
| charge.customer.bankAccounts.account | string | Sim | Conta bancária. |
| charge.customer.bankAccounts.accountCheckDigit | string | Sim | Dígito de verificação da conta bancária. |
| charge.customer.bankAccounts.type | int | Sim | Tipo de conta. |
| charge.customer.bankAccounts.isActive | bool | Sim | Se a conta está ativa ou não. |
| charge.customer.isActive | bool | Não | Se o comprador está ativo ou não. |
| charge.transactions | array(object) | Sim | Uma transação a ser realizada dentro da cobrança. |
| charge.transactions.card | object | Não | O Cartão a ser utilizado na transação. |
| charge.transactions.card.id | string | Não | O ID do cartão. |
| charge.transactions.card.customerId | string | Não | O ID do comprador. |
| charge.transactions.card.cardNumber | string | Sim | O número impresso na frente do cartão. |
| charge.transactions.card.cvv | string | Sim | Card Verification Value (CVV) é um recurso de segurança para transações de cartão de pagamento "cartão ausente" instituído para reduzir a incidência de fraude de cartão de crédito. Consiste em um número de 3-4 dígitos impresso no cartão. |
| charge.transactions.card.cvvMissingReason | int | Não | Razão pela qual o CVV não consta na cobrança, se necessário. Mandatório apenas para PagSeguro. |
| charge.transactions.card.brand | int | Sim | A bandeira do cartão à qual o imposto se aplica. |
| charge.transactions.card.cardholderName | string | Sim | O nome do títular do cartão. |
| charge.transactions.card.cardholderDocument | string | Sim | O documento do títular do cartão. |
| charge.transactions.card.expirationMonth | int | Sim | O Mês de expiração do cartão com 2 dígitos. |
| charge.transactions.card.expirationYear | int | Sim | O Ano de expiração do cartão com 4 dígitos. |
| charge.transactions.card.billingAddress | object | Condicional | É o endereço conectado ao cartão de crédito ou débito. As empresas usam o endereço de cobrança para verificar o uso autorizado de tal cartão. É também para onde as empresas enviam contas em papel e extratos bancários. **Obrigatório caso utilize antifraude** |
| charge.transactions.card.billingAddress.street | string | Não | Rua. |
| charge.transactions.card.billingAddress.number | string | Não | Número. |
| charge.transactions.card.billingAddress.neighborhood | string | Não | Bairro. |
| charge.transactions.card.billingAddress.city | string | Não | Cidade. |
| charge.transactions.card.billingAddress.state | string | Não | Estado. |
| charge.transactions.card.billingAddress.country | string | Não | País. |
| charge.transactions.card.billingAddress.zipCode | string | Não | CEP. |
| charge.transactions.card.billingAddress.complement | string | Não | Complemento. |
| charge.transactions.card.isPrivateLabel | bool | Condicional | Indica se o cartão é um produto de whitelabel ou não. Whitelabel é um produto ou serviço que uma empresa produz e comercializa com outras empresas que tem interesse em utilizar o mesmo com sua marca estampada. **Obrigatório caso utilize antifraude** |
| charge.transactions.card.brandName | string | Não | O nome da bandeira do cartão. |
| charge.transactions.card.cardToken | string | Não | Token do cartão. |
| charge.transactions.card.eci | string | Não | Código de autenticação ECI (Retornado apenas quando a transação passa pelo fluxo do 3DS). |
| charge.transactions.card.cavv | string | Não | Criptorgrama de autenticação (Retornado apenas quando a transação passa pelo fluxo do 3DS). |
| charge.transactions.card.xid | string | Não | Identificador MPI da transação autenticada. |
| charge.transactions.card.cardholderAuthenticationVersion | string | Não | Versão da autentificação retornada pelo provedor. |
| charge.transactions.card.metadata | objeto | Não | Armazena todas as credenciais relacionadas a bandeira. |
| charge.transactions.card.metadata.additionalProp1 | string | Não | Propriedade adicional. |
| charge.transactions.card.metadata.additionalProp2 | string | Não | Propriedade adicional. |
| charge.transactions.card.metadata.additionalProp3 | string | Não | Propriedade adicional. |
| charge.transactions.card.cardTransactionId | string | Não | ID para a requisição da transação do cartão. |
| charge.transactions.card.cof | bool | Não | indica se a transação é COF (Credentials On File). |
| charge.transactions.temporaryCardToken | string | Não | Token do cartão que foi gerado em um endpoint temporário de cartão. |
| charge.transactions.externalWallet | object | Não | Informações de carteira externa. |
| charge.transactions.externalWallet.type | int | Não | Indica qual carteira foi usada. |
| charge.transactions.externalWallet.payload | string | Não | Payload enviado pela carteira para processamento. |
| charge.transactions.externalWallet.billingAddress | object | Não | Endereço relacionado à conta da carteira externa. |
| charge.transactions.externalWallet.street | string | Não | Rua. |
| charge.transactions.externalWallet.number | string | Não | Número. |
| charge.transactions.externalWallet.neighborhood | string | Não | Bairro. |
| charge.transactions.externalWallet.city | string | Não | Cidade. |
| charge.transactions.externalWallet.state | string | Não | Estado. |
| charge.transactions.externalWallet.country | string | Não | País. |
| charge.transactions.externalWallet.zipCode | string | Não | CEP. |
| charge.transactions.externalWallet.complement | string | Não | Complemento. |
| charge.transactions.paymentType | int | Sim | Tipo de transação. |
| charge.transactions.amount | int | Sim | O valor do pagamento em centavos. |
| charge.transactions.installmentNumber | int | Sim | Quantidade de parcelas. Só pode ser maior que **1** se o tipo de transação for crédito. |
| charge.transactions.installmentType | int | Sim | Tipo de parcelamento da transação. |
| charge.transactions.softDescriptor | string | Não | Breve descrição a ser apresentada na fatura bancária do cliente. Este campo aceita apenas strings compostas por letras (maiúsculas ou minúsculas), números e o caractere asterisco (*), **sem espaços** nem outros símbolos. Formato equivalente à expressão regular `/^[a-zA-Z0-9*]+$/`. Se nulo, ele será preenchido com um rótulo padrão definido pela Safrapay. |
| charge.transactions.merchantTransactionId | string | Não | Identificador de pedido definido pelo sistema do estabelecimento comercial. Esta propriedade é obrigatória e servirá para capturar, cancelar e consultar posteriormente a transação. **Não utilize espaços** no meio do valor. |
| charge.transactions.acquirer | int | Não | O ID da adquirente. |
| charge.transactions.firstSubscriptionCharge | bool | Não | Indica se a transação é a primeira cobrança de assinatura. |
| charge.transactions.productIds | array(string) | Não | O ID de cada produto sendo comprado pela transação. |
| charge.transactions.source | object | Não | É a origem da transação. |
| charge.transactions.source.id | string | Sim | O ID do SmartCheckout |
| charge.transactions.source.type | int | Sim | Tipo de smartCheckout. |
| charge.transactions.boardingTaxAmount | object | Não | Representa as informações sobre taxas de embarque para companhias aéreas. |
| charge.transactions.boardingTaxAmount.amount | int | Não | Valor da taxa de embarque cobrada pela companhia aérea. |
| charge.transactions.boardingTaxAmount.entryAmount | int | Não | Valor da taxa de embarque cobrada pela companhia aérea. |
| charge.transactions.acquirerKey | string | Não | Número da chave do contrato do adquirente. |
| charge.transactions.sdwo | object | Não | Dados do integrador. |
| charge.transactions.sdwo.merchantCode | string | Sim | Código do estabelecimento. |
| charge.transactions.sdwo.walletId | string | Sim | ID da carteira que será integrada. |
| charge.transactions.sdwo.mcc | string | Sim | Número MCC que será enviado na integração. |
| charge.transactions.sdwo.name | string | Não | Nome do submerchant. |
| charge.transactions.sdwo.document | string | Não | Número do documento. |
| charge.transactions.sdwo.documentType | int | Não | Tipo de documento de acordo com o número do documento. |
| charge.transactions.sdwo.addressLine | string | Sim | Linha de endereço. |
| charge.transactions.sdwo.phone | object | Sim | Informações de telefone. |
| charge.transactions.sdwo.phone.countryCode | string | Sim | Código do país. |
| charge.transactions.sdwo.phone.areaCode | string | Sim | Código de área. |
| charge.transactions.sdwo.phone.number | string | Sim | Número do Telefone. |
| charge.transactions.sdwo.phone.type | PhoneType | Não | Tipo do telefone. |
| charge.transactions.sdwo.address | object | Não | Informações de endereço. |
| charge.transactions.sdwo.address.city | string | Sim | Cidade. |
| charge.transactions.sdwo.address.state | string | Sim | Estado. |
| charge.transactions.sdwo.address.country | string | Sim | País. |
| charge.transactions.sdwo.address.zipCode | string | Sim | CEP. |
| charge.transactions.sdwo.address.complement | string | Sim | Complemento. |
| charge.transactions.sdwo.operationType | string | Não | Opcional quando vazio, por padrão o valor é "BackToBack". |
| charge.transactions.authentication | object | Não | Dados informativos para autenticação 3DS. |
| charge.transactions.authentication.xid | string | Não | MPI identificador da transação autenticada, no formato base64 (usado apenas para bandeira VISA). |
| charge.transactions.authentication.cavv | string | Não | Identificador de autenticação criptografado pela bandeira (VISA e Mastercard) no formato base64. |
| charge.transactions.authentication.eci | string | Não | Indicador que mostra se a transação foi processada com Bearer authentication. |
| charge.transactions.authentication.directoryServer | string | Não | Campo usado apenas para bandeira Elo. |
| charge.transactions.authentication.version | string | Não | Versão utilizada no 3DS. |
| charge.products | array(object) | Não | Lista com cada produto dentro da cobrança. |
| charge.products.id | string | Não | UUID do produto. |
| charge.products.amount | int | Não | Valor do produto. |
| charge.products.name | int | Não | Nome do produto. |
| charge.products.description | string | Não | Descrição do produto. |
| charge.products.membershipFee | int | Não | Taxa que o cliente paga para ter o produto. |
| charge.products.sku | string | Não | ID único definido pelo comércio para identificar o produto na nossa base de dados (Stock Keeping Unit). |
| charge.products.quantity | int | Não | Quantidade do produto no carrinho. |
| charge.products.imagesRef | array(string) | Não | Lista com URL das imagens do produto. |
| charge.products.isActive | bool | Não | Define se o produto está ativo ou não. |
| charge.source | int | Sim | Define a fonte de cobrança, por exemplo, um POS, pinpad, site de comércio eletrônico. |
| charge.origin | string | Não | Uma propriedade que o cliente pode usar para identificar a origem da cobrança, como nome do fornecedor ou identificador. |
| charge.receivers | array(object) | Não | Recebedores envolvidos na cobrança. Irá definir quem receberá a transação pela divisão do valor total da cobrança em diferentes pagamentos. |
| charge.receivers.id | string | Sim | Documento identificador. |
| charge.receivers.mdrDiscount | bool | Não | Define se terá desconto MDR. |
| charge.receivers.fixedAmountComission | float | Não | Valor fixo que o destinatário deve receber. |
| charge.receivers.chargeRemainder | bool | Não | Após processar os valores divididos para cada parte, se houver centavos que sobraram da divisão, este campo indica qual destinatário deverá receber os centavos restantes. Também pode ser definido para divisão de centavos (exemplo 100/3) ou para quando o destinatário não tiver regra especifica. |
| charge.receivers.percentageComission | float | Não | Esta comissão é calculada no topo do valor da transação. |
| charge.receivers.mdrComission | float | Não | Porcentagem relativa ao MDR calculado na liquidação. |
| charge.receivers.membershipComission | float | Não | Comissão percentual para transações de associação. |
| charge.receivers.amount | float | Não | Valor. |
| charge.metadata | object | Não | Entradas coletadas para iniciação do evento. |
| charge.metadata.key | string | Não | O nome da chave (campo) |
| charge.metadata.value | string | Não | O valor da chave. |
| charge.gatewayId | string | Não | Gateway ID criado para o cliente para uso de autorização do Safra. |
| charge.shippingAddress | object | Não | Representa as informações do endereço de envio. |
| charge.shippingAddress.country | string | Não | Código do país. |
| charge.shippingAddress.street | string | Não | Rua. |
| charge.shippingAddress.number | string | Não | Número. |
| charge.shippingAddress.complement | string | Não | Complemento. |
| charge.shippingAddress.neighborhood | string | Não | Bairro. |
| charge.shippingAddress.postalCode | string | Não | Código postal. |
| charge.shippingAddress.city | string | Não | Cidade. |
| charge.shippingAddress.state | string | Não | Estado. |
| charge.shippingSettings | array(object) | Não | Configurações adicionais de envio. |
| charge.shippingSettings.merchantId | string | Não | ID único do estabelecimento relacionado à configuração de envio. |
| charge.shippingSettings.amount | int | Não | Valor do envio. |
| charge.macAddress | string | Não | Endereço MAC (Media Access Control) do dispositivo de origem usado para identificar exclusivamente um controlador de interface de rede. |
| lateCapture | bool | Não | Informar valor "true" para uma autorização com captura tardia. Valor padrão: false. |
| capture | bool | Não | Se a cobrança deve ou não ser capturada. |
| templateId | string | Não | TemplateId que será usado para enviar o recibo ao cliente. |
| primaryColor | string | Não | A cor primária da configuração do comerciante. |
| secondaryColor | string | Não | A cor secundária da configuração do comerciante. |
| hostname | string | Não | O hostname da configuração do comerciante. |
| merchantCode | string | Não | Código do estabelecimento definido pelo integrador. |
| remoteIp | string | Sim | **\[OBRIGATÓRIO quando antifraude ativo\]** O endereço IP do comprador. Este dado é utilizado em diversas verificações de risco (número de tentativas de pagamento, verificações baseadas em localização, detecção de uso de VPN/proxy). **Suporta IPv4.** **Exemplo:** `192.168.1.100`. Este campo complementa a implementação do Device Fingerprint. Consulte [documentação completa](../guias/antifraude.md#campo-remoteip-complemento-ao-device-fingerprint). |

<a id="resposta-5"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| merchantChargeId | string | O ID de cobrança definido pelo sistema do comerciante. |
| id | string | O ID da cobrança. |
| nsu | string | Identificador do pedido (Safrapay). |
| gatewayId | string | Identificação do gateway ou plataforma. |
| customerId | string | O ID do comprador. |
| chargeStatus | int | Status atual da cobrança, indicando em qual estágio do processo de autorização a cobrança está. Ele reflete diretamente todos os status de transação dentro da cobrança. |
| transactions | object | Uma ou várias transações a serem realizadas dentro da cobrança. |
| transactions.card | object | O Cartão a ser utilizado na transação. |
| transactions.card.id | string | O ID do cartão. |
| transactions.card.customerId | string | O ID do comprador. |
| transactions.card.cardNumber | string | O número impresso na frente do cartão. |
| transactions.card.brand | int | A bandeira do cartão à qual o imposto se aplica. |
| transactions.card.cardholderName | string | O nome do títular do cartão. |
| transactions.card.cardholderDocument | string | O documento do títular do cartão. |
| transactions.card.billingAddress | array | É o endereço conectado ao cartão de crédito ou débito. As empresas usam o endereço de cobrança para verificar o uso autorizado de tal cartão. É também para onde as empresas enviam contas em papel e extratos bancários. |
| transactions.card.billingAddress.street | string | Rua. |
| transactions.card.billingAddress.number | string | Número. |
| transactions.card.billingAddress.neighborhood | string | Bairro. |
| transactions.card.billingAddress.city | string | Cidade. |
| transactions.card.billingAddress.state | string | Estado. |
| transactions.card.billingAddress.country | string | País. |
| transactions.card.billingAddress.zipCode | string | CEP. |
| transactions.card.billingAddress.complement | string | Complemento. |
| transactions.card.isPrivateLabel | bool | Indica se o cartão é um produto de whitelabel ou não. Whitelabel é um produto ou serviço que uma empresa produz e comercializa com outras empresas que tem interesse em utilizar o mesmo com sua marca estampada. |
| transactions.card.expirationMonth | int | O Mês de expiração do cartão com 2 dígitos. |
| transactions.card.expirationYear | int | O Ano de expiração do cartão com 4 dígitos. |
| transactions.card.fallback | bool | Uma bandeira que informa se a cobrança necessária será feita como fita magnética substituta. |
| transactions.card.brandName | string | O nome da bandeira do cartão. |
| isApproved | bool | Indica se a cobrança está aprovada. |
| paymentType | int | Tipo de transação. |
| installmentType | string | Tipo de parcelamento da transação |
| installmentNumber | int | Quantidade de parcelas. Só pode ser maior que **1** se o tipo de transação for crédito. |
| softDescriptor | string | Breve descrição a ser apresentada na fatura bancária do cliente. Apenas letras, números e `*`; **sem espaços**; formato `/^[a-zA-Z0-9*]+$/`. Se nulo, preenchido com rótulo padrão. Apenas letras, números e `*`; **sem espaços**; formato `/^[a-zA-Z0-9*]+$/`. Se nulo, preenchido com rótulo padrão pela Safrapay. |
| amount | int | O valor do pagamento em centavos. |
| isCapture | bool | Indica se a cobrança foi capturada. |
| isRecurrency | bool | Indica se a cobrança é uma recorrência. |
| isCanceled | bool | Indica se a cobrança foi cancelada. |
| transactionId | string | Número Sequencial Único (NSU) da autorização, caso o pagamento seja aprovado pelo Emissor. |
| transactionStatus | string | Indica qual o status da transação. |
| merchantTransactionId | string | O ID da transação do Lojista |
| acquirer | string | O nome da adquirente. |
| creationDateTime | string | A data de criação da transação. |
| captureDateTime | string | A data de captura da transação. |
| bankSlipStatus | int | Status do boleto bancário. |
| receivers | array | Dados dos recebedores. |
| receivers.id | string | O ID do recebedor. |
| receivers.name | string | O nome do recebedor. |
| receivers.email | string | O e-mail do recebedor. |
| receivers.entityType | string | Se é pessoa física ou jurídica. |
| receivers.documentType | string | Se o documento usado é CPF ou CNPJ. |
| receivers.document | string | O documento do recebedor. |
| receivers.birthday | string | A data de nascimento do recebedor. |
| receivers.transferDay | int | O dia de transferência. |
| receivers.transferEnabled | bool | Indica se a transferencia está habilitada. |
| receivers.transferInterval | string | Indica o intervalo da transferencia, Ex: Dia, Semana, Mês e Ano. |
| receivers.anticipatablePercentage | number | Porcentagem da antecipação do recebdor. |
| receivers.automaticAnticipation | bool | Indica se a antecipação automática está habilitada ou não. |
| receivers.address | object | Endereço do comprador. |
| receivers.address.street | string | Rua. |
| receivers.address.number | string | Número. |
| receivers.address.neighborhood | string | Bairro. |
| receivers.address.city | string | Cidade. |
| receivers.address.state | string | Estado. |
| receivers.address.country | string | País. |
| receivers.address.zipCode | string | CEP. |
| receivers.address.complement | string | Complemento. |
| receivers.bankAccounts | object | Contas do comprador. |
| receivers.bankAccounts.bankCode | string | Código do banco. |
| receivers.bankAccounts.bankName | string | Nome do banco. |
| receivers.bankAccounts.branch | string | Filial. |
| receivers.bankAccounts.branchCheckDigit | string | Dígito de verificação da filial. |
| receivers.bankAccounts.account | string | Conta bancária. |
| receivers.bankAccounts.accountCheckDigit | string | Dígito de verificação da conta bancária. |
| receivers.bankAccounts.type | int | Tipo de conta. |
| receivers.bankAccounts.isActive | bool | Se a conta está ativa ou não. |
| receivers.gender | string | Gênero do recebedor. |
| receivers.type | string | Tipo de recebedor. |
| receivers.userId | string | O ID de usuário do recebedor. |
| receivers.isActive | bool | Indica se o recebedor está ativo ou não. |
| receivers.paymentDueDate | string | A data de vencimento. |
| receivers.maximumAmount | int | Quantia máxima. |
| receivers.rentalComission | number | Comissão de locação. |
| receivers.membershipComission | number | Comissão de sócio. |
| receivers.mdrCommission | number | A comissão em cima de uma taxa cobrada na transação. |
| receivers.fixedAmountComission | number | A quantia fixa que o recebedor deve receber. |
| receivers.mdrDiscount | bool | IDs dos receptores envolvidos na cobrança. Isso definirá quem recebe a transação, dividindo o valor total da cobrança em pagamentos separados. |
| receivers.chargeRemainder | bool | Após o processamento dos valores de cada divisão, se sobrar centavos da divisão, este sinalizador indica o recebedor que deve receber os centavos extras. Isso pode ser usado para penny split (exemplo 100/3) ou para quando o recebedor não tem uma regra específica. |
| receivers.percentageComission | number | O valor da comissão em porcentagem. |
| receivers.minimumAmountAutomaticPayment | number | O valor mínimo para pagamento automático do recebedor. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

<a id="body-raw-4"></a>

#### BODY Raw

```http
{
"charge": {
"merchantChargeId": "TASK5333",
"customer": {
"name": "Yago Sebastião Lima",
"email": "yagosebastiaolima@archosolutions.com.br",
"document": "78112482802",
"documentType": 1,
"phone": {
"number": "999999999",
"countryCode": "55",
"areaCode": "21",
"type": 5
}
},
"transactions": [
{
"card": {
"cardNumber": "4444585001234562",
"cvv": "111",
"brand": 1,
"cardholderName": "Yago Sebastião Lima",
"cardholderDocument": "78112482802",
"billingAddress": {
"street": "Rua 51",
"number": "99",
"neighborhood": "Parque Residencial Nova Fronteira",
"city": "Gurupi",
"state": "BA",
"country": "BR",
"zipCode": "77415340"
},
"expirationMonth": 12,
"expirationYear": 2026
},
"paymentType": 2,
"amount": 1000,
"installmentNumber": 0,
"softDescriptor": "TASK*5333",
}
],
"source": 8
}
}
```

<a id="pré-autorização-incremental"></a>

## Pré-Autorização Incremental

A pré-autorização incremental poderá ocorrer quando um estabelecimento necessitar efetuar uma adição à uma transação que ainda não foi capturada.

Para incrementar uma pré-autorização utilize o endpoint POST /charge/preauthorization, sendo necessário passar o `nsu` junto a query. `/v1/charge/preauthorization?nsu=1234123`.

🚧 Obs.: Atenção! Essa funcionalidade está disponível apenas para TEF/POS. Ao utilizar o endpoint, a ausência do `nsu` na query será considerado a criação de uma nova pré-autorização.

Exemplo: Em uma transação de aluguel de um produto/serviço por 2 dias, sendo cobrado valor de R$ 100,00 por dia, totalizando R$ 200,00. Caso o cliente queira continuar utilizando o produto/serviço por mais 1 dia, é possível fazer um incremento na transação, somando R$ 100,00 no valor original de R$ 200,00, totalizando R$ 300,00.

<a id="captura-tardia"></a>

## Captura Tardia

<a id="post-charge-preauthorization-1"></a>

### `POST` /charge/preauthorization

**Versão** `v2.0`

<a id="requisição-http-7"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/charge/preauthorization
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/charge/preauthorization")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n \"lateCapture\": true, \r\n  \"charge\": {\r\n    \"merchantChargeId\": \"TASK5333\",\r\n  \"customer\": {\r\n      \"name\": \"Yago Sebastião Lima\",\r\n      \"email\": \"yagosebastiaolima@archosolutions.com.br\",\r\n      \"document\": \"78112482802\",\r\n      \"documentType\": 1,\r\n      \"phone\": {\r\n          \"number\": \"999999999\",\r\n          \"countryCode\": \"55\",\r\n          \"areaCode\": \"21\",\r\n          \"type\": 5\r\n      }\r\n    },\r\n    \"transactions\": [\r\n      {\r\n        \"card\": {\r\n          \"cardNumber\": \"4444585001234562\",\r\n          \"cvv\": \"111\",\r\n          \"brand\": 1,\r\n          \"cardholderName\": \"Yago Sebastião Lima\",\r\n          \"cardholderDocument\": \"78112482802\",\r\n          \"billingAddress\": {\r\n            \"street\": \"Rua 51\",\r\n            \"number\": \"99\",\r\n            \"neighborhood\": \"Parque Residencial Nova Fronteira\",\r\n            \"city\": \"Gurupi\",\r\n            \"state\": \"BA\",\r\n            \"country\": \"BR\",\r\n            \"zipCode\": \"77415340\"\r\n          },\r\n          \"expirationMonth\": 12,\r\n          \"expirationYear\": 2026\r\n        },\r\n        \"paymentType\": 2,\r\n        \"amount\": 1000,\r\n        \"installmentNumber\": 0,\r\n        \"softDescriptor\": \"TASK*5333\"\r\n      }\r\n    ],\r\n    \"source\": 8\r\n  }\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/charge/preauthorization"

payload="{\r\n \"lateCapture\": true, \r\n  \"charge\": {\r\n    \"merchantChargeId\": \"TASK5333\",\r\n   \"customer\": {\r\n      \"name\": \"Yago Sebastião Lima\",\r\n      \"email\": \"yagosebastiaolima@archosolutions.com.br\",\r\n      \"document\": \"78112482802\",\r\n      \"documentType\": 1,\r\n      \"phone\": {\r\n          \"number\": \"999999999\",\r\n          \"countryCode\": \"55\",\r\n          \"areaCode\": \"21\",\r\n          \"type\": 5\r\n      }\r\n    },\r\n    \"transactions\": [\r\n      {\r\n        \"card\": {\r\n          \"cardNumber\": \"4444585001234562\",\r\n          \"cvv\": \"111\",\r\n          \"brand\": 1,\r\n          \"cardholderName\": \"Yago Sebastião Lima\",\r\n          \"cardholderDocument\": \"78112482802\",\r\n          \"billingAddress\": {\r\n            \"street\": \"Rua 51\",\r\n            \"number\": \"99\",\r\n            \"neighborhood\": \"Parque Residencial Nova Fronteira\",\r\n            \"city\": \"Gurupi\",\r\n            \"state\": \"BA\",\r\n            \"country\": \"BR\",\r\n            \"zipCode\": \"77415340\"\r\n          },\r\n          \"expirationMonth\": 12,\r\n          \"expirationYear\": 2026\r\n        },\r\n        \"paymentType\": 2,\r\n        \"amount\": 1000,\r\n        \"installmentNumber\": 0,\r\n        \"softDescriptor\": \"TASK*5333\"\r\n      }\r\n    ],\r\n    \"source\": 8\r\n  }\r\n}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/charge/preauthorization' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "lateCapture": true,
  "charge": {
    "merchantChargeId": "TASK5333",
    "customer": {
      "name": "Yago Sebastião Lima",
      "email": "yagosebastiaolima@archosolutions.com.br",
      "document": "78112482802",
      "documentType": 1,
      "phone": {
          "number": "999999999",
          "countryCode": "55",
          "areaCode": "21",
          "type": 5
      }
    },
    "transactions": [
      {
        "card": {
          "cardNumber": "4444585001234562",
          "cvv": "111",
          "brand": 1,
          "cardholderName": "Yago Sebastião Lima",
          "cardholderDocument": "78112482802",
          "billingAddress": {
            "street": "Rua 51",
            "number": "99",
            "neighborhood": "Parque Residencial Nova Fronteira",
            "city": "Gurupi",
            "state": "BA",
            "country": "BR",
            "zipCode": "77415340"
          },
          "expirationMonth": 12,
          "expirationYear": 2026
        },
        "paymentType": 2,
        "amount": 1000,
        "installmentNumber": 0,
        "softDescriptor": "TASK*5333"
      }
    ],
    "source": 8
  }
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"lateCapture":true, "charge":{"merchantChargeId":"TASK5333","customer":{"name":"Yago Sebastião Lima","email":"yagosebastiaolima@archosolutions.com.br","document":"78112482802","documentType":1,"phone":{"number":"999999999","countryCode":"55","areaCode":"21","type":5}},"transactions":[{"card":{"cardNumber":"4444585001234562","cvv":"111","brand":1,"cardholderName":"Yago Sebastião Lima","cardholderDocument":"78112482802","billingAddress":{"street":"Rua 51","number":"99","neighborhood":"Parque Residencial Nova Fronteira","city":"Gurupi","state":"BA","country":"BR","zipCode":"77415340"},"expirationMonth":12,"expirationYear":2026},"paymentType":2,"amount":1000,"installmentNumber":0,"softDescriptor":"TASK*5333"}],"source":8}});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/charge/preauthorization", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "charge": {
        "merchantChargeId": "TASK5333",
        "id": "abcc2428-eb4e-4470-9d55-72edca459daf",
        "nsu": "000005044",
        "customerId": "ffede3ee-37ab-47bb-9981-d3d14697d67z",
        "chargeStatus": "PreAuthorized",
        "transactions": [
            {
                "card": {
                    "id": "7903ef09-83c3-458d-ad39-9ea9e736e59e",
                    "customerId": "ffede3ee-37ab-47bb-9981-d3d14697d67z",
                    "cardNumber": "549167******0005",
                    "brand": "Mastercard",
                    "cardholderName": "Yago Sebastião Lima",
                    "cardholderDocument": "78112482802",
                    "isPrivateLabel": false,
                    "expirationMonth": 12,
                    "expirationYear": 2026,
                    "brandName": "Mastercard"
                },
                "isApproved": true,
                "paymentType": "Credit",
                "installmentType": "None",
                "installmentNumber": 1,
                "softDescriptor": "TASK*5333",
                "amount": 1000,
                "isCapture": false,
                "isRecurrency": false,
                "isCanceled": false,
                "transactionId": "1623967391659",
                "transactionStatus": "PreAuthorized",
                "merchantTransactionId": "TASK5333",
                "acquirer": "Simulator",
                "creationDateTime": "2021-06-17T19:03:11.6832635-03:00",
                "captureDateTime": "0001-01-01T00:00:00",
                "authorizationResponseCode": "00",
                "authorizationCode": "304848",
                "merchantAdviceCode": "01",
                "acquirerTransactionId": "ff478f2d-r569-568s-22ds-52s6742",
                "bankSlipStatus": 0
            }
        ],
        "metadata": {
            "key_Sample": "Value_Sample"
        }
    },
    "success": true,
    "errors": [],
    "traceKey": "8d8d389b-8742-4668-8380-ad7ab94bc90d"
}
```

O Endpoint responsável por criar uma nova cobrança, contendo uma ou várias transações pré-autorizadas, usando um ou vários adquirentes. A carga pode ser capturada posteriormente.

<a id="alteração-em-atributos-2"></a>

#### Alteração em Atributos

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| lateCapture | bool | Sim | Para a realização de uma captura tardia, este atributo precisa ter o valor **true**. |

<a id="requisição-6"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| charge | Object | Sim | Dados da transação. |
| charge.merchantChargeId | string | Não | O ID de cobrança definido pelo sistema do comerciante. **Não utilize espaços** no meio do identificador (ex.: `TASK5333`). Campos obrigatórios da estrutura não podem ser enviados vazios nem como string vazia `""`. |
| charge.subscriptionId | string | Não | GUID único relacionado ao subscription. |
| charge.sessionId | string | Não | ID da sessão criada pelo servidor do site do cliente e usada durante a visita de um determinado usuário. |
| charge.smartCheckoutId | string | Não | O ID do smartCheckout. |
| charge.id | string | Não | O ID da cobrança. |
| charge.chargeStatus | int | Não | Status atual da cobrança, indicando em qual estágio do processo de autorização a cobrança está. Ele reflete diretamente todos os status de transação dentro da cobrança. |
| charge.subMerchant | object | Não | Objeto com dados referente ao submerchant (Caso exista submerchant). |
| charge.subMerchant.id | string | Sim | ID do submerchant. |
| charge.subMerchant.document | string | Sim | Documento do submerchant. |
| charge.subMerchant.socialName | string | Sim | Razão social do submerchant. |
| charge.subMerchant.address | objeto | Sim | Endereço do submerchant. |
| charge.subMerchant.address.street | string | Sim | Rua. |
| charge.subMerchant.address.number | string | Sim | Número. |
| charge.subMerchant.address.neighborhood | string | Sim | Bairro. |
| charge.subMerchant.address.city | string | Sim | Cidade. |
| charge.subMerchant.address.state | string | Sim | Estado. |
| charge.subMerchant.address.country | string | Sim | País. |
| charge.subMerchant.address.zipCode | string | Sim | CEP. |
| charge.subMerchant.address.complement | string | Não | Complemento. |
| charge.customer | object | Sim | Dados do comprador. |
| charge.customer.id | string | Não | O ID do comprador. |
| charge.customer.name | string | Sim | Nome completo do comprador. |
| charge.customer.email | string | Sim | E-mail do comprador. |
| charge.customer.entityType | entityType | Não | Se é pessoa física ou jurídica. |
| charge.customer.documentType | documentType | Sim | Tipo do documento do comprador. |
| charge.customer.document | string | Sim | Documento do comprador. |
| charge.customer.birthday | date | Não | Data de nascimento do comprador. |
| charge.customer.gender | Gender | Não | Gênero do comprador. |
| charge.customer.phone | object | Sim | Telefone do comprador. |
| charge.customer.phone.countryCode | string | Sim | Código do país. |
| charge.customer.phone.areaCode | string | Sim | Código de área. |
| charge.customer.phone.number | string | Sim | Número do Telefone. |
| charge.customer.phone.type | PhoneType | Sim | Tipo do telefone. |
| charge.customer.address | object | Não | Endereço do comprador. |
| charge.customer.address.street | string | Sim | Rua. |
| charge.customer.address.number | string | Sim | Número. |
| charge.customer.address.neighborhood | string | Sim | Bairro. |
| charge.customer.address.city | string | Sim | Cidade. |
| charge.customer.address.state | string | Sim | Estado. |
| charge.customer.address.country | string | Sim | País. |
| charge.customer.address.zipCode | string | Sim | CEP. |
| charge.customer.address.complement | string | Sim | Complemento. |
| charge.customer.bankAccounts | object | Não | Contas do comprador. |
| charge.customer.bankAccounts.bankCode | string | Sim | Código do banco. |
| charge.customer.bankAccounts.bankName | string | Sim | Nome do banco. |
| charge.customer.bankAccounts.branch | string | Sim | Filial. |
| charge.customer.bankAccounts.branchCheckDigit | string | Sim | Dígito de verificação da filial. |
| charge.customer.bankAccounts.account | string | Sim | Conta bancária. |
| charge.customer.bankAccounts.accountCheckDigit | string | Sim | Dígito de verificação da conta bancária. |
| charge.customer.bankAccounts.type | int | Sim | Tipo de conta. |
| charge.customer.bankAccounts.isActive | bool | Sim | Se a conta está ativa ou não. |
| charge.customer.isActive | bool | Não | Se o comprador está ativo ou não. |
| charge.transactions | array(object) | Sim | Uma transação a ser realizada dentro da cobrança. |
| charge.transactions.card | object | Não | O Cartão a ser utilizado na transação. |
| charge.transactions.card.id | string | Não | O ID do cartão. |
| charge.transactions.card.customerId | string | Não | O ID do comprador. |
| charge.transactions.card.cardNumber | string | Sim | O número impresso na frente do cartão. |
| charge.transactions.card.cvv | string | Sim | Card Verification Value (CVV) é um recurso de segurança para transações de cartão de pagamento "cartão ausente" instituído para reduzir a incidência de fraude de cartão de crédito. Consiste em um número de 3-4 dígitos impresso no cartão. |
| charge.transactions.card.cvvMissingReason | int | Não | Razão pela qual o CVV não consta na cobrança, se necessário. Mandatório apenas para PagSeguro. |
| charge.transactions.card.brand | int | Sim | A bandeira do cartão à qual o imposto se aplica. |
| charge.transactions.card.cardholderName | string | Sim | O nome do títular do cartão. |
| charge.transactions.card.cardholderDocument | string | Sim | O documento do títular do cartão. |
| charge.transactions.card.billingAddress | object | Não | É o endereço conectado ao cartão de crédito ou débito. As empresas usam o endereço de cobrança para verificar o uso autorizado de tal cartão. É também para onde as empresas enviam contas em papel e extratos bancários. |
| charge.transactions.card.billingAddress.street | string | Não | Rua. |
| charge.transactions.card.billingAddress.number | string | Não | Número. |
| charge.transactions.card.billingAddress.neighborhood | string | Não | Bairro. |
| charge.transactions.card.billingAddress.city | string | Não | Cidade. |
| charge.transactions.card.billingAddress.state | string | Não | Estado. |
| charge.transactions.card.billingAddress.country | string | Não | País. |
| charge.transactions.card.billingAddress.zipCode | string | Não | CEP. |
| charge.transactions.card.billingAddress.complement | string | Não | Complemento. |
| charge.transactions.card.isPrivateLabel | bool | Não | Indica se o cartão é um produto de whitelabel ou não. Whitelabel é um produto ou serviço que uma empresa produz e comercializa com outras empresas que tem interesse em utilizar o mesmo com sua marca estampada. |
| charge.transactions.card.expirationMonth | int | Sim | O Mês de expiração do cartão com 2 dígitos. |
| charge.transactions.card.expirationYear | int | Sim | O Ano de expiração do cartão com 4 dígitos. |
| charge.transactions.card.brandName | string | Não | O nome da bandeira do cartão. |
| charge.transactions.card.cardToken | string | Não | Token do cartão. |
| charge.transactions.card.eci | string | Não | Código de autenticação ECI (Retornado apenas quando a transação passa pelo fluxo do 3DS). |
| charge.transactions.card.cavv | string | Não | Criptorgrama de autenticação (Retornado apenas quando a transação passa pelo fluxo do 3DS). |
| charge.transactions.card.xid | string | Não | Identificador MPI da transação autenticada. |
| charge.transactions.card.cardholderAuthenticationVersion | string | Não | Versão da autentificação retornada pelo provedor. |
| charge.transactions.card.metadata | objeto | Não | Armazena todas as credenciais relacionadas a bandeira. |
| charge.transactions.card.metadata.additionalProp1 | string | Não | Propriedade adicional. |
| charge.transactions.card.metadata.additionalProp2 | string | Não | Propriedade adicional. |
| charge.transactions.card.metadata.additionalProp3 | string | Não | Propriedade adicional. |
| charge.transactions.card.cardTransactionId | string | Não | ID para a requisição da transação do cartão. |
| charge.transactions.card.cof | bool | Não | indica se a transação é COF (Credentials On File). |
| charge.transactions.temporaryCardToken | string | Não | Token do cartão que foi gerado em um endpoint temporário de cartão. |
| charge.transactions.externalWallet | object | Não | Informações de carteira externa. |
| charge.transactions.externalWallet.type | int | Não | Indica qual carteira foi usada. |
| charge.transactions.externalWallet.payload | string | Não | Payload enviado pela carteira para processamento. |
| charge.transactions.externalWallet.billingAddress | object | Não | Endereço relacionado à conta da carteira externa. |
| charge.transactions.externalWallet.street | string | Não | Rua. |
| charge.transactions.externalWallet.number | string | Não | Número. |
| charge.transactions.externalWallet.neighborhood | string | Não | Bairro. |
| charge.transactions.externalWallet.city | string | Não | Cidade. |
| charge.transactions.externalWallet.state | string | Não | Estado. |
| charge.transactions.externalWallet.country | string | Não | País. |
| charge.transactions.externalWallet.zipCode | string | Não | CEP. |
| charge.transactions.externalWallet.complement | string | Não | Complemento. |
| charge.transactions.paymentType | int | Sim | Tipo de transação. |
| charge.transactions.amount | int | Sim | O valor do pagamento em centavos. |
| charge.transactions.installmentNumber | int | Sim | Quantidade de parcelas. Só pode ser maior que **1** se o tipo de transação for crédito. |
| charge.transactions.softDescriptor | string | Não | Breve descrição a ser apresentada na fatura bancária do cliente. Este campo aceita apenas strings compostas por letras (maiúsculas ou minúsculas), números e o caractere asterisco (*), **sem espaços** nem outros símbolos. Formato equivalente à expressão regular `/^[a-zA-Z0-9*]+$/`. Se nulo, ele será preenchido com um rótulo padrão definido pela Safrapay. |
| charge.transactions.merchantTransactionId | string | Não | Identificador de pedido definido pelo sistema do estabelecimento comercial. Esta propriedade é obrigatória e servirá para capturar, cancelar e consultar posteriormente a transação. **Não utilize espaços** no meio do valor. |
| charge.transactions.installmentType | int | Sim | Tipo de parcelamento da transação |
| charge.transactions.acquirer | int | Não | O ID da adquirente. |
| charge.transactions.firstSubscriptionCharge | bool | Não | Indica se a transação é a primeira cobrança de assinatura. |
| charge.transactions.productIds | array(string) | Não | O ID de cada produto sendo comprado pela transação. |
| charge.transactions.source | object | Não | É a origem da transação. |
| charge.transactions.source.id | string | Sim | O ID do SmartCheckout |
| charge.transactions.source.type | int | Sim | Tipo de smartCheckout. |
| charge.transactions.boardingTaxAmount | object | Não | Representa as informações sobre taxas de embarque para companhias aéreas. |
| charge.transactions.boardingTaxAmount.amount | int | Não | Valor da taxa de embarque cobrada pela companhia aérea. |
| charge.transactions.boardingTaxAmount.entryAmount | int | Não | Valor da taxa de embarque cobrada pela companhia aérea. |
| charge.transactions.acquirerKey | string | Não | Número da chave do contrato do adquirente. |
| charge.transactions.sdwo | object | Não | Dados do integrador. |
| charge.transactions.sdwo.merchantCode | string | Sim | Código do estabelecimento. |
| charge.transactions.sdwo.walletId | string | Sim | ID da carteira que será integrada. |
| charge.transactions.sdwo.mcc | string | Sim | Número MCC que será enviado na integração. |
| charge.transactions.sdwo.name | string | Não | Nome do submerchant. |
| charge.transactions.sdwo.document | string | Não | Número do documento. |
| charge.transactions.sdwo.documentType | int | Não | Tipo de documento de acordo com o número do documento. |
| charge.transactions.sdwo.addressLine | string | Sim | Linha de endereço. |
| charge.transactions.sdwo.phone | object | Sim | Informações de telefone. |
| charge.transactions.sdwo.phone.countryCode | string | Sim | Código do país. |
| charge.transactions.sdwo.phone.areaCode | string | Sim | Código de área. |
| charge.transactions.sdwo.phone.number | string | Sim | Número do Telefone. |
| charge.transactions.sdwo.phone.type | PhoneType | Não | Tipo do telefone. |
| charge.transactions.sdwo.address | object | Não | Informações de endereço. |
| charge.transactions.sdwo.address.city | string | Sim | Cidade. |
| charge.transactions.sdwo.address.state | string | Sim | Estado. |
| charge.transactions.sdwo.address.country | string | Sim | País. |
| charge.transactions.sdwo.address.zipCode | string | Sim | CEP. |
| charge.transactions.sdwo.address.complement | string | Sim | Complemento. |
| charge.transactions.sdwo.operationType | string | Não | Opcional quando vazio, por padrão o valor é "BackToBack". |
| charge.transactions.authentication | object | Não | Dados informativos para autenticação 3DS. |
| charge.transactions.authentication.xid | string | Não | MPI identificador da transação autenticada, no formato base64 (usado apenas para bandeira VISA). |
| charge.transactions.authentication.cavv | string | Não | Identificador de autenticação criptografado pela bandeira (VISA e Mastercard) no formato base64. |
| charge.transactions.authentication.eci | string | Não | Indicador que mostra se a transação foi processada com Bearer authentication. |
| charge.transactions.authentication.directoryServer | string | Não | Campo usado apenas para bandeira Elo. |
| charge.transactions.authentication.version | string | Não | Versão utilizada no 3DS. |
| charge.products | array(object) | Não | Lista com cada produto dentro da cobrança. |
| charge.products.id | string | Não | UUID do produto. |
| charge.products.amount | int | Não | Valor do produto. |
| charge.products.name | int | Não | Nome do produto. |
| charge.products.description | string | Não | Descrição do produto. |
| charge.products.membershipFee | int | Não | Taxa que o cliente paga para ter o produto. |
| charge.products.sku | string | Não | ID único definido pelo comércio para identificar o produto na nossa base de dados (Stock Keeping Unit). |
| charge.products.quantity | int | Não | Quantidade do produto no carrinho. |
| charge.products.imagesRef | array(string) | Não | Lista com URL das imagens do produto. |
| charge.products.isActive | bool | Não | Define se o produto está ativo ou não. |
| charge.source | int | Sim | Define a fonte de cobrança, por exemplo, um POS, pinpad, site de comércio eletrônico. |
| charge.origin | string | Não | Uma propriedade que o cliente pode usar para identificar a origem da cobrança, como nome do fornecedor ou identificador. |
| charge.receivers | array(object) | Não | Recebedores envolvidos na cobrança. Irá definir quem receberá a transação pela divisão do valor total da cobrança em diferentes pagamentos. |
| charge.receivers.id | string | Sim | Documento identificador. |
| charge.receivers.mdrDiscount | bool | Não | Define se terá desconto MDR. |
| charge.receivers.fixedAmountComission | float | Não | Valor fixo que o destinatário deve receber. |
| charge.receivers.chargeRemainder | bool | Não | Após processar os valores divididos para cada parte, se houver centavos que sobraram da divisão, este campo indica qual destinatário deverá receber os centavos restantes. Também pode ser definido para divisão de centavos (exemplo 100/3) ou para quando o destinatário não tiver regra especifica. |
| charge.receivers.percentageComission | float | Não | Esta comissão é calculada no topo do valor da transação. |
| charge.receivers.mdrComission | float | Não | Porcentagem relativa ao MDR calculado na liquidação. |
| charge.receivers.membershipComission | float | Não | Comissão percentual para transações de associação. |
| charge.receivers.amount | float | Não | Valor. |
| charge.metadata | object | Não | Entradas coletadas para iniciação do evento. |
| charge.metadata.key | string | Não | O nome da chave (campo) |
| charge.metadata.value | string | Não | O valor da chave. |
| charge.gatewayId | string | Não | Gateway ID criado para o cliente para uso de autorização do Safra. |
| charge.shippingAddress | object | Não | Representa as informações do endereço de envio. |
| charge.shippingAddress.country | string | Não | Código do país. |
| charge.shippingAddress.street | string | Não | Rua. |
| charge.shippingAddress.number | string | Não | Número. |
| charge.shippingAddress.complement | string | Não | Complemento. |
| charge.shippingAddress.neighborhood | string | Não | Bairro. |
| charge.shippingAddress.postalCode | string | Não | Código postal. |
| charge.shippingAddress.city | string | Não | Cidade. |
| charge.shippingAddress.state | string | Não | Estado. |
| charge.shippingSettings | array(object) | Não | Configurações adicionais de envio. |
| charge.shippingSettings.merchantId | string | Não | ID único do estabelecimento relacionado à configuração de envio. |
| charge.shippingSettings.amount | int | Não | Valor do envio. |
| charge.macAddress | string | Não | Endereço MAC (Media Access Control) do dispositivo de origem usado para identificar exclusivamente um controlador de interface de rede. |
| lateCapture | bool | Não | Informar valor "true" para uma autorização com captura tardia. Valor padrão: false. |
| capture | bool | Sim | Se a cobrança deve ou não ser capturada. |
| templateId | string | Não | TemplateId que será usado para enviar o recibo ao cliente. |
| primaryColor | string | Não | A cor primária da configuração do comerciante. |
| secondaryColor | string | Não | A cor secundária da configuração do comerciante. |
| hostname | string | Não | O hostname da configuração do comerciante. |
| merchantCode | string | Não | Código do estabelecimento definido pelo integrador. |
| remoteIp | string | Sim | **\[OBRIGATÓRIO quando antifraude ativo\]** O endereço IP do comprador. Este dado é utilizado em diversas verificações de risco (número de tentativas de pagamento, verificações baseadas em localização, detecção de uso de VPN/proxy). **Suporta IPv4.** **Exemplo:** `192.168.1.100`. Este campo complementa a implementação do Device Fingerprint. Consulte [documentação completa](../guias/antifraude.md#campo-remoteip-complemento-ao-device-fingerprint). |

<a id="resposta-6"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| merchantChargeId | string | O ID de cobrança definido pelo sistema do comerciante. |
| id | string | O ID da cobrança. |
| gatewayId | string | Não |
| nsu | string | Identificador do pedido (Safrapay). |
| customerId | string | O ID do comprador. |
| chargeStatus | int | Status atual da cobrança, indicando em qual estágio do processo de autorização a cobrança está. Ele reflete diretamente todos os status de transação dentro da cobrança. |
| transactions | object | Uma ou várias transações a serem realizadas dentro da cobrança. |
| transactions.card | object | O Cartão a ser utilizado na transação. |
| transactions.card.id | string | O ID do cartão. |
| transactions.card.customerId | string | O ID do comprador. |
| transactions.card.cardNumber | string | O número impresso na frente do cartão. |
| transactions.card.brand | int | A bandeira do cartão à qual o imposto se aplica. |
| transactions.card.cardholderName | string | O nome do títular do cartão. |
| transactions.card.cardholderDocument | string | O documento do títular do cartão. |
| transactions.card.billingAddress | array | É o endereço conectado ao cartão de crédito ou débito. As empresas usam o endereço de cobrança para verificar o uso autorizado de tal cartão. É também para onde as empresas enviam contas em papel e extratos bancários. |
| transactions.card.billingAddress.street | string | Rua. |
| transactions.card.billingAddress.number | string | Número. |
| transactions.card.billingAddress.neighborhood | string | Bairro. |
| transactions.card.billingAddress.city | string | Cidade. |
| transactions.card.billingAddress.state | string | Estado. |
| transactions.card.billingAddress.country | string | País. |
| transactions.card.billingAddress.zipCode | string | CEP. |
| transactions.card.billingAddress.complement | string | Complemento. |
| transactions.card.isPrivateLabel | bool | Indica se o cartão é um produto de whitelabel ou não. Whitelabel é um produto ou serviço que uma empresa produz e comercializa com outras empresas que tem interesse em utilizar o mesmo com sua marca estampada. |
| transactions.card.expirationMonth | int | O Mês de expiração do cartão com 2 dígitos. |
| transactions.card.expirationYear | int | O Ano de expiração do cartão com 4 dígitos. |
| transactions.card.fallback | bool | Uma bandeira que informa se a cobrança necessária será feita como fita magnética substituta. |
| transactions.card.brandName | string | O nome da bandeira do cartão. |
| isApproved | bool | Indica se a cobrança está aprovada. |
| paymentType | int | Tipo de transação. |
| installmentType | string | Tipo de parcelamento da transação |
| installmentNumber | int | Quantidade de parcelas. Só pode ser maior que **1** se o tipo de transação for crédito. |
| softDescriptor | string | Breve descrição a ser apresentada na fatura bancária do cliente. Este campo aceita apenas strings compostas por letras (maiúsculas ou minúsculas), números e o caractere asterisco (*), **sem espaços** nem outros símbolos. Formato equivalente à expressão regular `/^[a-zA-Z0-9*]+$/`. Se nulo, ele será preenchido com um rótulo padrão definido pela Safrapay. |
| amount | int | O valor do pagamento em centavos. |
| isCapture | bool | Indica se a cobrança foi capturada. |
| isRecurrency | bool | Indica se a cobrança é uma recorrência. |
| isCanceled | bool | Indica se a cobrança foi cancelada. |
| transactionId | string | Número Sequencial Único (NSU) da autorização, caso o pagamento seja aprovado pelo Emissor. |
| transactionStatus | string | Indica qual o status da transação. |
| merchantTransactionId | string | O ID da transação do Lojista |
| acquirer | string | O nome da adquirente. |
| creationDateTime | string | A data de criação da transação. |
| captureDateTime | string | A data de captura da transação. |
| bankSlipStatus | int | Status do boleto bancário. |
| metadata | object | Lista de informações personalizados. |
| metadata.key | string | O nome da chave (campo) |
| metadata.value | string | O valor da chave passada no campo `metadata.key`. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

<a id="body-raw-5"></a>

#### BODY Raw

```http
{
"lateCapture": true
"charge": {
"merchantChargeId": "TASK5333",
"customer": {
"name": "Yago Sebastião Lima",
"email": "yagosebastiaolima@archosolutions.com.br",
"document": "78112482802",
"documentType": 1,
"phone": {
"number": "999999999",
"countryCode": "55",
"areaCode": "21",
"type": 5
}
},
"transactions": [
{
"card": {
"cardNumber": "4444585001234562",
"cvv": "111",
"brand": 1,
"cardholderName": "Yago Sebastião Lima",
"cardholderDocument": "78112482802",
"billingAddress": {
"street": "Rua 51",
"number": "99",
"neighborhood": "Parque Residencial Nova Fronteira",
"city": "Gurupi",
"state": "BA",
"country": "BR",
"zipCode": "77415340"
},
"expirationMonth": 12,
"expirationYear": 2026
},
"paymentType": 2,
"amount": 1000,
"installmentNumber": 0,
"softDescriptor": "TASK*5333"
}
],
"source": 8
}
}
```

<a id="captura-automática"></a>

## Captura automática

<a id="post-charge-authorization-3"></a>

### `POST` /charge/authorization

**Versão** `v2.0`

<a id="requisição-http-8"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/charge/authorization
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/charge/authorization")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n  \"charge\": {\r\n    \"merchantChargeId\": \"TASK5333\",\r\n    \"customer\": {\r\n      \"name\": \"Ester Patrícia Aparício\",\r\n      \"email\": \"eesterpatriciaaparicio@ladder.com.br\",\r\n      \"document\": \"71877920002\",\r\n      \"documentType\": 1,\r\n      \"phone\": {\r\n          \"number\": \"999999999\",\r\n          \"countryCode\": \"55\",\r\n          \"areaCode\": \"21\",\r\n          \"type\": 5\r\n      }\r\n    },\r\n    \"transactions\": [\r\n      {\r\n        \"card\": {\r\n          \"cardNumber\": \"4444585001234562\",\r\n          \"cvv\": \"123\",\r\n          \"brand\": 1,\r\n          \"cardholderName\": \"Ester Patrícia Aparício\",\r\n          \"cardholderDocument\": \"71877920002\",\r\n          \"billingAddress\": {\r\n            \"street\": \"Rua Juvêncio Erudilho\",\r\n            \"number\": \"39\",\r\n            \"neighborhood\": \"Centro\",\r\n            \"city\": \"Gurupi\",\r\n            \"state\": \"BA\",\r\n            \"country\": \"BR\",\r\n            \"zipCode\": \"44002-528\"\r\n          },\r\n          \"expirationMonth\": 12,\r\n          \"expirationYear\": 2034\r\n        },\r\n        \"paymentType\": 0,\r\n        \"amount\": 1000,\r\n        \"installmentNumber\": 0,\r\n        \"softDescriptor\": \"TASK*5333\"\r\n      }\r\n    ],\r\n    \"source\": 8\r\n  }\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/charge/authorization"

payload="{\r\n  \"charge\": {\r\n    \"merchantChargeId\": \"TASK5333\",\r\n    \"customer\": {\r\n      \"name\": \"Ester Patrícia Aparício\",\r\n      \"email\": \"eesterpatriciaaparicio@ladder.com.br\",\r\n      \"document\": \"71877920002\",\r\n      \"documentType\": 1,\r\n      \"phone\": {\r\n          \"number\": \"999999999\",\r\n          \"countryCode\": \"55\",\r\n          \"areaCode\": \"21\",\r\n          \"type\": 5\r\n      }\r\n    },\r\n    \"transactions\": [\r\n      {\r\n        \"card\": {\r\n          \"cardNumber\": \"4444585001234562\",\r\n          \"cvv\": \"123\",\r\n          \"brand\": 1,\r\n          \"cardholderName\": \"Ester Patrícia Aparício\",\r\n          \"cardholderDocument\": \"71877920002\",\r\n          \"billingAddress\": {\r\n            \"street\": \"Rua Juvêncio Erudilho\",\r\n            \"number\": \"39\",\r\n            \"neighborhood\": \"Centro\",\r\n            \"city\": \"Gurupi\",\r\n            \"state\": \"BA\",\r\n            \"country\": \"BR\",\r\n            \"zipCode\": \"44002-528\"\r\n          },\r\n          \"expirationMonth\": 12,\r\n          \"expirationYear\": 2034\r\n        },\r\n        \"paymentType\": 0,\r\n        \"amount\": 1000,\r\n        \"installmentNumber\": 0,\r\n        \"softDescriptor\": \"TASK*5333\"\r\n      }\r\n    ],\r\n    \"source\": 8\r\n  }\r\n}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/charge/authorization' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "charge": {
    "merchantChargeId": "TASK5333",
    "customer": {
      "name": "Ester Patrícia Aparício",
      "email": "eesterpatriciaaparicio@ladder.com.br",
      "document": "71877920002",
      "documentType": 1,
      "phone": {
          "number": "999999999",
          "countryCode": "55",
          "areaCode": "21",
          "type": 5
      }
    },
    "transactions": [
      {
        "card": {
          "cardNumber": "4444585001234562",
          "cvv": "123",
          "brand": 1,
          "cardholderName": "Ester Patrícia Aparício",
          "cardholderDocument": "71877920002",
          "billingAddress": {
            "street": "Rua Juvêncio Erudilho",
            "number": "39",
            "neighborhood": "Centro",
            "city": "Gurupi",
            "state": "BA",
            "country": "BR",
            "zipCode": "44002-528"
          },
          "expirationMonth": 12,
          "expirationYear": 2034
        },
        "paymentType": 0,
        "amount": 1000,
        "installmentNumber": 0,
        "softDescriptor": "TASK*5333"
      }
    ],
    "source": 8
  }
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"charge":{"merchantChargeId":"TASK5333","customer":{"name":"Ester Patrícia Aparício","email":"eesterpatriciaaparicio@ladder.com.br","document":"71877920002","documentType":1,"phone":{"number":"999999999","countryCode":"55","areaCode":"21","type":5}},"transactions":[{"card":{"cardNumber":"4444585001234562","cvv":"123","brand":1,"cardholderName":"Ester Patrícia Aparício","cardholderDocument":"71877920002","billingAddress":{"street":"Rua Juvêncio Erudilho","number":"39","neighborhood":"Centro","city":"Gurupi","state":"BA","country":"BR","zipCode":"44002-528"},"expirationMonth":12,"expirationYear":2034},"paymentType":0,"amount":1000,"installmentNumber":0,"softDescriptor":"TASK*5333"}],"source":8}});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/charge/authorization", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "charge": {
        "merchantChargeId": "TASK5333",
        "id": "3e60759b-e818-4a83-a98c-883fcd609d4f",
        "nsu": "000000019",
        "customerId": "a1a5a477-f8b5-471d-ab42-765c2e4b1ad1",
        "chargeStatus": "Authorized",
        "transactions": [
            {
              "card": {
                  "id": "65327e40-37ee-4c23-9369-4845519d19b7",
                  "customerId": "a1a5a477-f8b5-471d-ab42-765c2e4b1ad1",
                  "cardNumber": "549167******0005",
                  "brand": "Mastercard",
                  "cardholderName": "Ester Patrícia Aparício",
                  "cardholderDocument": "71877920002",
                  "billingAddress": {
                      "street": "Rua Juvêncio Erudilho",
                      "number": "39",
                      "neighborhood": "Centro",
                      "city": "Gurupi",
                      "state": "BA",
                      "country": "BR",
                      "zipCode": "44002-528"
                  },
                  "isPrivateLabel": false,
                  "expirationMonth": 12,
                  "expirationYear": 2034,
                  "brandName": "Mastercard"
              },
              "isApproved": true,
              "paymentType": "Credit",
              "installmentType": "None",
              "installmentNumber": 1,
              "softDescriptor": "TASK*5333",
              "amount": 1000,
              "isCapture": true,
              "isRecurrency": false,
              "isCanceled": false,
              "transactionId": "1623709631269",
              "transactionStatus": "Captured",
              "merchantTransactionId": "TASK5333",
              "acquirer": "Simulator",
              "creationDateTime": "2021-06-14T19:27:11.3167988-03:00",
              "captureDateTime": "2021-06-14T19:27:11.3156408-03:00",
              "authorizationResponseCode": "00",
              "authorizationCode": "689020",
              "merchantAdviceCode": "01",
              "acquirerTransactionId": "ff478f2d-r569-568s-22ds-52s6742",
              "bankSlipStatus": 0
            }
        ]
    },
    "success": true,
    "errors": [],
    "traceKey": "ac0ea0e1-ad9f-412e-a0bb-4b97e9893a3f"
}
```

Para a criação de uma nova cobrança utilizando a captura automática, basta realizar uma requisição ao endpoint [POST**/authorization**](#crédito-à-vista) para que isso aconteça. Este endpoint será o responsável por criar a cobrança e capturá-la automaticamente junto a adquirente.

<a id="tokenização-por-bandeira"></a>

## Tokenização por Bandeira

É uma solução que tem o intuito de melhorar a segurança e qualidade das informações de cartão trafegadas nas transações online, realizando o armazenamento de cartões em cofres na própria bandeira, de forma criptografada. 

 Maior segurança: além da criação de um código (token) para substituir a informação do cartão, as bandeiras também emitem os criptogramas, que funcionam como uma senha ou assinatura da bandeira, única para aquele cartão naquele estabelecimento. 

 Atualização automática de cartões: quando um novo cartão é emitido no lugar do cartão anterior, ou quando a data de expiração de um cartão muda, os bancos enviam essas informações para a base da bandeira, e a bandeira automaticamente atualiza os tokens com as novas informações. Ou seja, não tem necessidade de nenhuma ação por parte do estabelecimento. 

 Maior conversão de aprovação: com as transações tokenizadas, os bancos emissores se sentem mais seguros em aprovar as transações. Além disso, com os dados de cartão atualizados automaticamente, mais vendas que poderiam ser negadas por dados de cartão desatualizados, podem ser aprovadas.

<a id="atualmente-as-bandeiras-aceitas-na-tokenização-são-mastercard-visa-e-elo"></a>

### Atualmente as bandeiras aceitas na tokenização são: **MasterCard, Visa e ELO.**

Para utilização de um Cartão Tokenização é necessário o Provisionamento do Token na Bandeira que será utilizada para Tokenização, podendo ser: Visa, Mastercard e ELO.
 Para o Provisionamento do Token do Cartão, utilize o endpoint: [POST V2/CARD](cartao-protegido.md#post-card)

<a id="post-charge-authorization-4"></a>

### `POST` /charge/authorization

**Versão** `v2.0`

<a id="requisição-http-9"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/charge/authorization
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/charge/authorization")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n  \"charge\": {\r\n   \"subMerchant\":{\r\n   \"id\":\"string\",\r\n  \"document\":\"string\",\r\n  \"address\":{\r\n   \"street\:\"string\",\r\n   \"number\":\"string\",\r\n    \"neighborhood\":\"string\",\r\n    \"city\":\"string\",\r\n    \"state\":\"string\",\r\n   \"country\":\"string\",\r\n   \"zipCode\":\"string\",\r\n   \"complement\":\"string\"}},\r\n    \"merchantChargeId\": \"TASK5333\",\r\n    \"customer\": {\r\n      \"name\": \"Ester Patrícia Aparício\",\r\n      \"email\": \"eesterpatriciaaparicio@ladder.com.br\",\r\n      \"document\": \"71877920002\",\r\n      \"documentType\": 1,\r\n      \"phone\": {\r\n          \"number\": \"999999999\",\r\n          \"countryCode\": \"55\",\r\n          \"areaCode\": \"21\",\r\n          \"type\": 5\r\n      }\r\n    },\r\n    \"transactions\": [\r\n      {\r\n        \"card\": {\r\n          \"cardNumber\": \"4444585001234562\",\r\n          \"cvv\": \"123\",\r\n          \"brand\": 1,\r\n          \"cardholderName\": \"Ester Patrícia Aparício\",\r\n          \"cardholderDocument\": \"71877920002\",\r\n          \"billingAddress\": {\r\n            \"street\": \"Rua Juvêncio Erudilho\",\r\n            \"number\": \"39\",\r\n            \"neighborhood\": \"Centro\",\r\n            \"city\": \"Gurupi\",\r\n            \"state\": \"BA\",\r\n            \"country\": \"BR\",\r\n            \"zipCode\": \"44002-528\"\r\n          },\r\n          \"expirationMonth\": 12,\r\n          \"expirationYear\": 2034,\r\n          \"cavv\": \"hsur4t68726eyhduaoewpsdaldi89383hg3\",          \"eci\": \"05\"        },\r\n        \"paymentType\": 0,\r\n        \"amount\": 1000,\r\n        \"installmentNumber\": 0,\r\n        \"softDescriptor\": \"TASK*5333\",\r\n      }\r\n    ],\r\n    \"source\": 8\r\n  }\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/charge/authorization"

payload="{\r\n  \"charge\": {\r\n \"subMerchant\":{\r\n   \"id\":\"string\",\r\n  \"document\":\"string\",\r\n  \"address\":{\r\n   \"street\:\"string\",\r\n   \"number\":\"string\",\r\n    \"neighborhood\":\"string\",\r\n    \"city\":\"string\",\r\n    \"state\":\"string\",\r\n   \"country\":\"string\",\r\n   \"zipCode\":\"string\",\r\n   \"complement\":\"string\"}},\r\n    \"merchantChargeId\": \"TASK5333\",\r\n    \"customer\": {\r\n      \"name\": \"Ester Patrícia Aparício\",\r\n      \"email\": \"eesterpatriciaaparicio@ladder.com.br\",\r\n      \"document\": \"71877920002\",\r\n      \"documentType\": 1,\r\n      \"phone\": {\r\n          \"number\": \"999999999\",\r\n          \"countryCode\": \"55\",\r\n          \"areaCode\": \"21\",\r\n          \"type\": 5\r\n      }\r\n    },\r\n    \"transactions\": [\r\n      {\r\n        \"card\": {\r\n          \"cardNumber\": \"4444585001234562\",\r\n          \"cvv\": \"123\",\r\n          \"brand\": 1,\r\n          \"cardholderName\": \"Ester Patrícia Aparício\",\r\n          \"cardholderDocument\": \"71877920002\",\r\n          \"billingAddress\": {\r\n            \"street\": \"Rua Juvêncio Erudilho\",\r\n            \"number\": \"39\",\r\n            \"neighborhood\": \"Centro\",\r\n            \"city\": \"Gurupi\",\r\n            \"state\": \"BA\",\r\n            \"country\": \"BR\",\r\n            \"zipCode\": \"44002-528\"\r\n          },\r\n          \"expirationMonth\": 12,\r\n          \"expirationYear\": 2034\r\n          \"cavv\": \"hsur4t68726eyhduaoewpsdaldi89383hg3\",          \"eci\": \"05\"        },\r\n        \"paymentType\": 0,\r\n        \"amount\": 1000,\r\n        \"installmentNumber\": 0,\r\n        \"softDescriptor\": \"TASK*5333\",\r\n     }\r\n    ],\r\n    \"source\": 8\r\n  }\r\n}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/charge/authorization' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "charge": {
    "merchantChargeId": "TASK5333",
    "subMerchant": {
      "id": "string",
      "document": "string",
      "address": {
        "street": "string",
        "number": "string",
        "neighborhood": "string",
        "city": "string",
        "state": "string",
        "country": "string",
        "zipCode": "string",
        "complement": "string"
      }
    },
    "customer": {
      "name": "Ester Patrícia Aparício",
      "email": "eesterpatriciaaparicio@ladder.com.br",
      "document": "71877920002",
      "documentType": 1,
      "phone": {
          "number": "999999999",
          "countryCode": "55",
          "areaCode": "21",
          "type": 5
      }
    },
    "transactions": [
      {
        "card": {
          "cardNumber": "4444585001234562",
          "cvv": "123",
          "brand": 1,
          "cardholderName": "Ester Patrícia Aparício",
          "cardholderDocument": "71877920002",
          "billingAddress": {
            "street": "Rua Juvêncio Erudilho",
            "number": "39",
            "neighborhood": "Centro",
            "city": "Gurupi",
            "state": "BA",
            "country": "BR",
            "zipCode": "44002-528"
          },
          "expirationMonth": 12,
          "expirationYear": 2034,
          "cavv":"hsur4t68726eyhduaoewpsdaldi89383hg3",
          "eci":"05"
        },
        "paymentType": 0,
        "amount": 1000,
        "installmentNumber": 0,
        "softDescriptor": "TASK*5333",
      }
    ],
    "source": 8
  }
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"charge":{"merchantChargeId":"TASK5333","subMerchant":{"id":"string","document":"string","address":{"street":"string","number":"string","neighborhood":"string","city":"string","state":"string","country":"string","zipCode":"string","complement":"string"}},"customer":{"name":"Ester Patrícia Aparício","email":"eesterpatriciaaparicio@ladder.com.br","document":"71877920002","documentType":1,"phone":{"number":"999999999","countryCode":"55","areaCode":"21","type":5}},"transactions":[{"card":{"cardNumber":"4444585001234562","cvv":"123","brand":1,"cardholderName":"Ester Patrícia Aparício","cardholderDocument":"71877920002","billingAddress":{"street":"Rua Juvêncio Erudilho","number":"39","neighborhood":"Centro","city":"Gurupi","state":"BA","country":"BR","zipCode":"44002-528"},"expirationMonth":12,"expirationYear":2034,"cavv":"hsur4t68726eyhduaoewpsdaldi89383hg3","eci":"05"},"paymentType":0,"amount":1000,"installmentNumber":0,"softDescriptor":"TASK*5333"}],"source":8}});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/charge/authorization", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "charge": {
        "merchantChargeId": "TASK5333",
        "id": "3e60759b-e818-4a83-a98c-883fcd609d4f",
        "nsu": "000000019",
        "customerId": "a1a5a477-f8b5-471d-ab42-765c2e4b1ad1",
        "chargeStatus": "Authorized",
        "transactions": [
            {
              "card": {
                  "id": "65327e40-37ee-4c23-9369-4845519d19b7",
                  "customerId": "a1a5a477-f8b5-471d-ab42-765c2e4b1ad1",
                  "cardNumber": "549167******0005",
                  "brand": "Mastercard",
                  "cardholderName": "Ester Patrícia Aparício",
                  "cardholderDocument": "71877920002",
                  "billingAddress": {
                      "street": "Rua Juvêncio Erudilho",
                      "number": "39",
                      "neighborhood": "Centro",
                      "city": "Gurupi",
                      "state": "BA",
                      "country": "BR",
                      "zipCode": "44002-528"
                  },
                  "isPrivateLabel": false,
                  "expirationMonth": 12,
                  "expirationYear": 2034,
                  "brandName": "Mastercard"
              },
              "isApproved": true,
              "paymentType": "Credit",
              "installmentType": "None",
              "installmentNumber": 1,
              "softDescriptor": "TASK*5333",
              "amount": 1000,
              "isCapture": true,
              "isRecurrency": false,
              "isCanceled": false,
              "transactionId": "1623709631269",
              "transactionStatus": "Captured",
              "merchantTransactionId": "TASK5333",
              "acquirer": "Simulator",
              "creationDateTime": "2021-06-14T19:27:11.3167988-03:00",
              "captureDateTime": "2021-06-14T19:27:11.3156408-03:00",
              "authorizationResponseCode": "00",
              "authorizationCode": "689020",
              "merchantAdviceCode": "01",
              "acquirerTransactionId": "ff478f2d-r569-568s-22ds-52s6742",
              "bankSlipStatus": 0
            }
        ]
    },
    "success": true,
    "errors": [],
    "traceKey": "ac0ea0e1-ad9f-412e-a0bb-4b97e9893a3f"
}
```

<a id="requisição-7"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| charge | Object | Sim | Dados da transação. |
| charge.merchantChargeId | string | Não | O ID de cobrança definido pelo sistema do comerciante. **Não utilize espaços** no meio do identificador (ex.: `TASK5333`). Campos obrigatórios da estrutura não podem ser enviados vazios nem como string vazia `""`. |
| charge.subscriptionId | string | Não | GUID único relacionado ao subscription. |
| charge.sessionId | string | Não | ID da sessão criada pelo servidor do site do cliente e usada durante a visita de um determinado usuário. |
| charge.smartCheckoutId | string | Não | O ID do smartCheckout. |
| charge.id | string | Não | O ID da cobrança. |
| charge.chargeStatus | int | Não | Status atual da cobrança, indicando em qual estágio do processo de autorização a cobrança está. Ele reflete diretamente todos os status de transação dentro da cobrança. |
| charge.subMerchant | object | Não | Objeto com dados referente ao submerchant (Caso exista submerchant). |
| charge.subMerchant.id | string | Sim | ID do submerchant. |
| charge.subMerchant.document | string | Sim | Documento do submerchant. |
| charge.subMerchant.socialName | string | Sim | Razão social do submerchant. |
| charge.subMerchant.address | objeto | Sim | Endereço do submerchant. |
| charge.subMerchant.address.street | string | Sim | Rua. |
| charge.subMerchant.address.number | string | Sim | Número. |
| charge.subMerchant.address.neighborhood | string | Sim | Bairro. |
| charge.subMerchant.address.city | string | Sim | Cidade. |
| charge.subMerchant.address.state | string | Sim | Estado. |
| charge.subMerchant.address.country | string | Sim | País. |
| charge.subMerchant.address.zipCode | string | Sim | CEP. |
| charge.subMerchant.address.complement | string | Não | Complemento. |
| charge.customer | object | Sim | Dados do comprador. |
| charge.customer.id | string | Não | O ID do comprador. |
| charge.customer.name | string | Sim | Nome completo do comprador. |
| charge.customer.email | string | Sim | E-mail do comprador. |
| charge.customer.entityType | entityType | Não | Se é pessoa física ou jurídica. |
| charge.customer.documentType | documentType | Sim | Tipo do documento do comprador. |
| charge.customer.document | string | Sim | Documento do comprador. |
| charge.customer.birthday | date | Não | Data de nascimento do comprador. |
| charge.customer.gender | Gender | Não | Gênero do comprador. |
| charge.customer.phone | object | Sim | Telefone do comprador. |
| charge.customer.phone.countryCode | string | Sim | Código do país. |
| charge.customer.phone.areaCode | string | Sim | Código de área. |
| charge.customer.phone.number | string | Sim | Número do Telefone. |
| charge.customer.phone.type | PhoneType | Sim | Tipo do telefone. |
| charge.customer.address | object | Não | Endereço do comprador. |
| charge.customer.address.street | string | Sim | Rua. |
| charge.customer.address.number | string | Sim | Número. |
| charge.customer.address.neighborhood | string | Sim | Bairro. |
| charge.customer.address.city | string | Sim | Cidade. |
| charge.customer.address.state | string | Sim | Estado. |
| charge.customer.address.country | string | Sim | País. |
| charge.customer.address.zipCode | string | Sim | CEP. |
| charge.customer.address.complement | string | Sim | Complemento. |
| charge.customer.bankAccounts | object | Não | Contas do comprador. |
| charge.customer.bankAccounts.bankCode | string | Sim | Código do banco. |
| charge.customer.bankAccounts.bankName | string | Sim | Nome do banco. |
| charge.customer.bankAccounts.branch | string | Sim | Filial. |
| charge.customer.bankAccounts.branchCheckDigit | string | Sim | Dígito de verificação da filial. |
| charge.customer.bankAccounts.account | string | Sim | Conta bancária. |
| charge.customer.bankAccounts.accountCheckDigit | string | Sim | Dígito de verificação da conta bancária. |
| charge.customer.bankAccounts.type | int | Sim | Tipo de conta. |
| charge.customer.bankAccounts.isActive | bool | Sim | Se a conta está ativa ou não. |
| charge.customer.isActive | bool | Não | Se o comprador está ativo ou não. |
| charge.transactions | array(object) | Sim | Uma transação a ser realizada dentro da cobrança. |
| charge.transactions.card | object | Não | O Cartão a ser utilizado na transação. |
| charge.transactions.card.id | string | Não | O ID do cartão. |
| charge.transactions.card.customerId | string | Não | O ID do comprador. |
| charge.transactions.card.cardNumber | string | Sim | O número impresso na frente do cartão. |
| charge.transactions.card.cvv | string | Sim | Card Verification Value (CVV) é um recurso de segurança para transações de cartão de pagamento "cartão ausente" instituído para reduzir a incidência de fraude de cartão de crédito. Consiste em um número de 3-4 dígitos impresso no cartão. |
| charge.transactions.card.cvvMissingReason | int | Não | Razão pela qual o CVV não consta na cobrança, se necessário. Mandatório apenas para PagSeguro. |
| charge.transactions.card.brand | int | Sim | A bandeira do cartão à qual o imposto se aplica. |
| charge.transactions.card.cardholderName | string | Sim | O nome do títular do cartão. |
| charge.transactions.card.cardholderDocument | string | Sim | O documento do títular do cartão. |
| charge.transactions.card.billingAddress | object | Não | É o endereço conectado ao cartão de crédito ou débito. As empresas usam o endereço de cobrança para verificar o uso autorizado de tal cartão. É também para onde as empresas enviam contas em papel e extratos bancários. |
| charge.transactions.card.billingAddress.street | string | Não | Rua. |
| charge.transactions.card.billingAddress.number | string | Não | Número. |
| charge.transactions.card.billingAddress.neighborhood | string | Não | Bairro. |
| charge.transactions.card.billingAddress.city | string | Não | Cidade. |
| charge.transactions.card.billingAddress.state | string | Não | Estado. |
| charge.transactions.card.billingAddress.country | string | Não | País. |
| charge.transactions.card.billingAddress.zipCode | string | Não | CEP. |
| charge.transactions.card.billingAddress.complement | string | Não | Complemento. |
| charge.transactions.card.isPrivateLabel | bool | Não | Indica se o cartão é um produto de whitelabel ou não. Whitelabel é um produto ou serviço que uma empresa produz e comercializa com outras empresas que tem interesse em utilizar o mesmo com sua marca estampada. |
| charge.transactions.card.expirationMonth | int | Sim | O Mês de expiração do cartão com 2 dígitos. |
| charge.transactions.card.expirationYear | int | Sim | O Ano de expiração do cartão com 4 dígitos. |
| charge.transactions.card.brandName | string | Não | O nome da bandeira do cartão. |
| charge.transactions.card.cardToken | string | Não | Token do cartão. |
| charge.transactions.card.eci | string | Não | Código de autenticação ECI (Retornado apenas quando a transação passa pelo fluxo do 3DS). |
| charge.transactions.card.cavv | string | Não | Criptorgrama de autenticação (Retornado apenas quando a transação passa pelo fluxo do 3DS). |
| charge.transactions.card.xid | string | Não | Identificador MPI da transação autenticada. |
| charge.transactions.card.cardholderAuthenticationVersion | string | Não | Versão da autentificação retornada pelo provedor. |
| charge.transactions.card.metadata | objeto | Não | Armazena todas as credenciais relacionadas a bandeira. |
| charge.transactions.card.metadata.additionalProp1 | string | Não | Propriedade adicional. |
| charge.transactions.card.metadata.additionalProp2 | string | Não | Propriedade adicional. |
| charge.transactions.card.metadata.additionalProp3 | string | Não | Propriedade adicional. |
| charge.transactions.card.cardTransactionId | string | Não | ID para a requisição da transação do cartão. |
| charge.transactions.card.cof | bool | Não | indica se a transação é COF (Credentials On File). |
| charge.transactions.temporaryCardToken | string | Não | Token do cartão que foi gerado em um endpoint temporário de cartão. |
| charge.transactions.externalWallet | object | Não | Informações de carteira externa. |
| charge.transactions.externalWallet.type | int | Não | Indica qual carteira foi usada. |
| charge.transactions.externalWallet.payload | string | Não | Payload enviado pela carteira para processamento. |
| charge.transactions.externalWallet.billingAddress | object | Não | Endereço relacionado à conta da carteira externa. |
| charge.transactions.externalWallet.street | string | Não | Rua. |
| charge.transactions.externalWallet.number | string | Não | Número. |
| charge.transactions.externalWallet.neighborhood | string | Não | Bairro. |
| charge.transactions.externalWallet.city | string | Não | Cidade. |
| charge.transactions.externalWallet.state | string | Não | Estado. |
| charge.transactions.externalWallet.country | string | Não | País. |
| charge.transactions.externalWallet.zipCode | string | Não | CEP. |
| charge.transactions.externalWallet.complement | string | Não | Complemento. |
| charge.transactions.paymentType | int | Sim | Tipo de transação. |
| charge.transactions.amount | int | Sim | O valor do pagamento em centavos. |
| charge.transactions.installmentNumber | int | Sim | Quantidade de parcelas. Só pode ser maior que **1** se o tipo de transação for crédito. |
| charge.transactions.softDescriptor | string | Não | Breve descrição a ser apresentada na fatura bancária do cliente. Este campo aceita apenas strings compostas por letras (maiúsculas ou minúsculas), números e o caractere asterisco (*), **sem espaços** nem outros símbolos. Formato equivalente à expressão regular `/^[a-zA-Z0-9*]+$/`. Se nulo, ele será preenchido com um rótulo padrão definido pela Safrapay. |
| charge.transactions.merchantTransactionId | string | Não | Identificador de pedido definido pelo sistema do estabelecimento comercial. Esta propriedade é obrigatória e servirá para capturar, cancelar e consultar posteriormente a transação. **Não utilize espaços** no meio do valor. |
| charge.transactions.installmentType | int | Sim | Tipo de parcelamento da transação |
| charge.transactions.acquirer | int | Não | O ID da adquirente. |
| charge.transactions.firstSubscriptionCharge | bool | Não | Indica se a transação é a primeira cobrança de assinatura. |
| charge.transactions.productIds | array(string) | Não | O ID de cada produto sendo comprado pela transação. |
| charge.transactions.source | object | Não | É a origem da transação. |
| charge.transactions.source.id | string | Sim | O ID do SmartCheckout |
| charge.transactions.source.type | int | Sim | Tipo de smartCheckout. |
| charge.transactions.boardingTaxAmount | object | Não | Representa as informações sobre taxas de embarque para companhias aéreas. |
| charge.transactions.boardingTaxAmount.amount | int | Não | Valor da taxa de embarque cobrada pela companhia aérea. |
| charge.transactions.boardingTaxAmount.entryAmount | int | Não | Valor da taxa de embarque cobrada pela companhia aérea. |
| charge.transactions.acquirerKey | string | Não | Número da chave do contrato do adquirente. |
| charge.transactions.sdwo | object | Não | Dados do integrador. |
| charge.transactions.sdwo.merchantCode | string | Sim | Código do estabelecimento. |
| charge.transactions.sdwo.walletId | string | Sim | ID da carteira que será integrada. |
| charge.transactions.sdwo.mcc | string | Sim | Número MCC que será enviado na integração. |
| charge.transactions.sdwo.name | string | Não | Nome do submerchant. |
| charge.transactions.sdwo.document | string | Não | Número do documento. |
| charge.transactions.sdwo.documentType | int | Não | Tipo de documento de acordo com o número do documento. |
| charge.transactions.sdwo.addressLine | string | Sim | Linha de endereço. |
| charge.transactions.sdwo.phone | object | Sim | Informações de telefone. |
| charge.transactions.sdwo.phone.countryCode | string | Sim | Código do país. |
| charge.transactions.sdwo.phone.areaCode | string | Sim | Código de área. |
| charge.transactions.sdwo.phone.number | string | Sim | Número do Telefone. |
| charge.transactions.sdwo.phone.type | PhoneType | Não | Tipo do telefone. |
| charge.transactions.sdwo.address | object | Não | Informações de endereço. |
| charge.transactions.sdwo.address.city | string | Sim | Cidade. |
| charge.transactions.sdwo.address.state | string | Sim | Estado. |
| charge.transactions.sdwo.address.country | string | Sim | País. |
| charge.transactions.sdwo.address.zipCode | string | Sim | CEP. |
| charge.transactions.sdwo.address.complement | string | Sim | Complemento. |
| charge.transactions.sdwo.operationType | string | Não | Opcional quando vazio, por padrão o valor é "BackToBack". |
| charge.transactions.authentication | object | Não | Dados informativos para autenticação 3DS. |
| charge.transactions.authentication.xid | string | Não | MPI identificador da transação autenticada, no formato base64 (usado apenas para bandeira VISA). |
| charge.transactions.authentication.cavv | string | Não | Identificador de autenticação criptografado pela bandeira (VISA e Mastercard) no formato base64. |
| charge.transactions.authentication.eci | string | Não | Indicador que mostra se a transação foi processada com Bearer authentication. |
| charge.transactions.authentication.directoryServer | string | Não | Campo usado apenas para bandeira Elo. |
| charge.transactions.authentication.version | string | Não | Versão utilizada no 3DS. |
| charge.products | array(object) | Não | Lista com cada produto dentro da cobrança. |
| charge.products.id | string | Não | UUID do produto. |
| charge.products.amount | int | Não | Valor do produto. |
| charge.products.name | int | Não | Nome do produto. |
| charge.products.description | string | Não | Descrição do produto. |
| charge.products.membershipFee | int | Não | Taxa que o cliente paga para ter o produto. |
| charge.products.sku | string | Não | ID único definido pelo comércio para identificar o produto na nossa base de dados (Stock Keeping Unit). |
| charge.products.quantity | int | Não | Quantidade do produto no carrinho. |
| charge.products.imagesRef | array(string) | Não | Lista com URL das imagens do produto. |
| charge.products.isActive | bool | Não | Define se o produto está ativo ou não. |
| charge.source | int | Sim | Define a fonte de cobrança, por exemplo, um POS, pinpad, site de comércio eletrônico. |
| charge.origin | string | Não | Uma propriedade que o cliente pode usar para identificar a origem da cobrança, como nome do fornecedor ou identificador. |
| charge.receivers | array(object) | Não | Recebedores envolvidos na cobrança. Irá definir quem receberá a transação pela divisão do valor total da cobrança em diferentes pagamentos. |
| charge.receivers.id | string | Sim | Documento identificador. |
| charge.receivers.mdrDiscount | bool | Não | Define se terá desconto MDR. |
| charge.receivers.fixedAmountComission | float | Não | Valor fixo que o destinatário deve receber. |
| charge.receivers.chargeRemainder | bool | Não | Após processar os valores divididos para cada parte, se houver centavos que sobraram da divisão, este campo indica qual destinatário deverá receber os centavos restantes. Também pode ser definido para divisão de centavos (exemplo 100/3) ou para quando o destinatário não tiver regra especifica. |
| charge.receivers.percentageComission | float | Não | Esta comissão é calculada no topo do valor da transação. |
| charge.receivers.mdrComission | float | Não | Porcentagem relativa ao MDR calculado na liquidação. |
| charge.receivers.membershipComission | float | Não | Comissão percentual para transações de associação. |
| charge.receivers.amount | float | Não | Valor. |
| charge.metadata | object | Não | Entradas coletadas para iniciação do evento. |
| charge.metadata.key | string | Não | O nome da chave (campo) |
| charge.metadata.value | string | Não | O valor da chave. |
| charge.gatewayId | string | Não | Gateway ID criado para o cliente para uso de autorização do Safra. |
| charge.shippingAddress | object | Não | Representa as informações do endereço de envio. |
| charge.shippingAddress.country | string | Não | Código do país. |
| charge.shippingAddress.street | string | Não | Rua. |
| charge.shippingAddress.number | string | Não | Número. |
| charge.shippingAddress.complement | string | Não | Complemento. |
| charge.shippingAddress.neighborhood | string | Não | Bairro. |
| charge.shippingAddress.postalCode | string | Não | Código postal. |
| charge.shippingAddress.city | string | Não | Cidade. |
| charge.shippingAddress.state | string | Não | Estado. |
| charge.shippingSettings | array(object) | Não | Configurações adicionais de envio. |
| charge.shippingSettings.merchantId | string | Não | ID único do estabelecimento relacionado à configuração de envio. |
| charge.shippingSettings.amount | int | Não | Valor do envio. |
| charge.macAddress | string | Não | Endereço MAC (Media Access Control) do dispositivo de origem usado para identificar exclusivamente um controlador de interface de rede. |
| lateCapture | bool | Não | Informar valor "true" para uma autorização com captura tardia. Valor padrão: false. |
| capture | bool | Não | Se a cobrança deve ou não ser capturada. |
| templateId | string | Não | TemplateId que será usado para enviar o recibo ao cliente. |
| primaryColor | string | Não | A cor primária da configuração do comerciante. |
| secondaryColor | string | Não | A cor secundária da configuração do comerciante. |
| hostname | string | Não | O hostname da configuração do comerciante. |
| merchantCode | string | Não | Código do estabelecimento definido pelo integrador. |
| remoteIp | string | Sim | **\[OBRIGATÓRIO quando antifraude ativo\]** O endereço IP do comprador. Este dado é utilizado em diversas verificações de risco (número de tentativas de pagamento, verificações baseadas em localização, detecção de uso de VPN/proxy). **Suporta IPv4.** **Exemplo:** `192.168.1.100`. Este campo complementa a implementação do Device Fingerprint. Consulte [documentação completa](../guias/antifraude.md#campo-remoteip-complemento-ao-device-fingerprint). |

<a id="resposta-7"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| merchantChargeId | string | O ID de cobrança definido pelo sistema do comerciante. |
| id | string | O ID da cobrança. |
| nsu | string | Identificador do pedido (Safrapay). |
| gatewayId | string | Não |
| customerId | string | O ID do comprador. |
| chargeStatus | int | Status atual da cobrança, indicando em qual estágio do processo de autorização a cobrança está. Ele reflete diretamente todos os status de transação dentro da cobrança. |
| transactions | object | Uma ou várias transações a serem realizadas dentro da cobrança. |
| transactions.card | object | O Cartão a ser utilizado na transação. |
| transactions.card.id | string | O ID do cartão. |
| transactions.card.customerId | string | O ID do comprador. |
| transactions.card.cardNumber | string | O número impresso na frente do cartão. |
| transactions.card.brand | int | A bandeira do cartão à qual o imposto se aplica. |
| transactions.card.cardholderName | string | O nome do títular do cartão. |
| transactions.card.cardholderDocument | string | O documento do títular do cartão. |
| transactions.card.billingAddress | array | É o endereço conectado ao cartão de crédito ou débito. As empresas usam o endereço de cobrança para verificar o uso autorizado de tal cartão. É também para onde as empresas enviam contas em papel e extratos bancários. |
| transactions.card.billingAddress.street | string | Rua. |
| transactions.card.billingAddress.number | string | Número. |
| transactions.card.billingAddress.neighborhood | string | Bairro. |
| transactions.card.billingAddress.city | string | Cidade. |
| transactions.card.billingAddress.state | string | Estado. |
| transactions.card.billingAddress.country | string | País. |
| transactions.card.billingAddress.zipCode | string | CEP. |
| transactions.card.billingAddress.complement | string | Complemento. |
| transactions.card.isPrivateLabel | bool | Indica se o cartão é um produto de whitelabel ou não. Whitelabel é um produto ou serviço que uma empresa produz e comercializa com outras empresas que tem interesse em utilizar o mesmo com sua marca estampada. |
| transactions.card.expirationMonth | int | O Mês de expiração do cartão com 2 dígitos. |
| transactions.card.expirationYear | int | O Ano de expiração do cartão com 4 dígitos. |
| transactions.card.fallback | bool | Uma bandeira que informa se a cobrança necessária será feita como fita magnética substituta. |
| transactions.card.brandName | string | O nome da bandeira do cartão. |
| isApproved | bool | Indica se a cobrança está aprovada. |
| paymentType | int | Tipo de transação. |
| installmentType | string | Tipo de parcelamento da transação |
| installmentNumber | int | Quantidade de parcelas. Só pode ser maior que **1** se o tipo de transação for crédito. |
| softDescriptor | string | Breve descrição a ser apresentada na fatura bancária do cliente. Apenas letras, números e `*`; **sem espaços**; formato `/^[a-zA-Z0-9*]+$/`. Se nulo, preenchido com rótulo padrão. |
| amount | int | O valor do pagamento em centavos. |
| isCapture | bool | Indica se a cobrança foi capturada. |
| isRecurrency | bool | Indica se a cobrança é uma recorrência. |
| isCanceled | bool | Indica se a cobrança foi cancelada. |
| transactionId | string | Número Sequencial Único (NSU) da autorização, caso o pagamento seja aprovado pelo Emissor. |
| transactionStatus | string | Indica qual o status da transação. |
| merchantTransactionId | string | O ID da transação do Lojista |
| acquirer | string | O nome da adquirente. |
| creationDateTime | string | A data de criação da transação. |
| captureDateTime | string | A data de captura da transação. |
| bankSlipStatus | int | Status do boleto bancário. |
| metadata | object | Lista de informações personalizados. |
| metadata.key | string | O nome da chave (campo) |
| metadata.value | string | O valor da chave passada no campo `metadata.key`. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

<a id="body-raw-6"></a>

#### BODY Raw

```http
{
"charge": {
"merchantChargeId": "TASK5333",
"customer": {
"name": "Ester Patrícia Aparício",
"email": "eesterpatriciaaparicio@ladder.com.br",
"document": "71877920002",
"documentType": 1,
"phone": {
"number": "999999999",
"countryCode": "55",
"areaCode": "21",
"type": 5
}
},
"transactions": [
{
"card": {
"cardNumber": "4444585001234562",
"cvv": "123",
"brand": 1,
"cardholderName": "Ester Patrícia Aparício",
"cardholderDocument": "71877920002",
"billingAddress": {
"street": "Rua Juvêncio Erudilho",
"number": "39",
"neighborhood": "Centro",
"city": "Gurupi",
"state": "BA",
"country": "BR",
"zipCode": "44002-528"
},
"expirationMonth": 12,
"expirationYear": 2034,
"cavv": "hsur4t68726eyhduaoewpsdaldi89383hg3"
"eci": "05"
},
"paymentType": 2,
"amount": 1000,
"installmentNumber": 0,
"softDescriptor": "TASK*5333"
}
],
"source": 8
}
}
```

<a id="3ds"></a>

## 3DS

O 3D Secure (3DS) é um protocolo de autenticação que adiciona uma camada extra de segurança a pagamentos online. O 3DS na versão 2.0 proporciona um volume maior de dados para análise durante a comunicação entre o titular do cartão, o emissor do cartão e o estabelecimento comercial. Nesse processo de pagamento com autenticação 3DS (3 Domain Secure), estão envolvidas três partes: o Comerciante, o Safrapay (Merchant Plug-in) e o ACS (Access Control Server).

Durante esse processo, os dados de pagamento são trocados de forma segura entre essas partes. Para realizar um pagamento com cartão utilizando o 3DS, são necessárias três etapas para a troca de dados de pagamento com o Gateway Safrapay e para realizar a verificação de segurança para o 3-D Secure (3DS). Disponibilizamos um exemplo de implementação no seu [checkout de pagamento](https://gitlab.com/safrapay/3ds-checkout-example).

![3ds-passo1](../assets/img/3ds-passo1.png)

<a id="cartões-de-teste"></a>

#### Cartões de teste:

| Bandeira | Com Desafio (Challenged) | Sem Desafio (Approved) | Rejeitado |
| --- | --- | --- | --- |
| VISA | 4000000000001091 | 4000000000001000 | 4000000000001018 |
| MasterCard | 5200000000001096 | 5200000000001005 | 5200000000001013 |
| AMEX | 340000000001098 | 340000000001007 | 340000000001015 |
| ELO | 6505290000001234 | 6505290000001002 | 6505290000001010 |

<a id="etapa-1-inicialização-setup"></a>

### Etapa 1. Inicialização (Setup)

Antes de efetuar o pagamento, é necessário iniciar uma sessão 3DS, conhecida como Setup ou fluxo de 'Payer Authentication Setup'. Nesta etapa, é necessário iniciar a sessão para obter o accessToken (JWT), deviceDataCollectionUrl e o cardholderAuthenticationReferenceId. O cardholderAuthenticationReferenceId e chargeId retornados pela API são dados cruciais e serão utilizados nas etapas seguintes (Enrollment e Pagamento). Após isso, os dados do accessToken (JWT) e do deviceDataCollectionUrl devem ser inseridos em um iframe "invisível" na página de checkout (front-end) para que uma solicitação HTTP seja feita ao provedor 3DS (ACS).

<a id="exemplo"></a>

#### Exemplo

```http
<iframe name="ddc-iframe" height="10" width="10" style="display: none;"></iframe>
<form id="ddc-form" target="ddc-iframe"  method="POST" action="https://centinelapistag.cardinalcommerce.com/V1/Cruise/Collect">
<input type="hidden" name="JWT" value="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI0M2M0ODE4NS0xMmRhLTQ4NzAtYmQ3YS04ODcxMmI3NmEzZDUiLCJpYXQiOjE3MTEwMzE4ODUsImlzcyI6IjVkZDgzYmYwMGU0MjNkMTQ5OGRjYmFjYSIsImV4cCI6MTcxMTAzNTQ4NSwiT3JnVW5pdElkIjoiNjE2MDRlNjg2ZDYwYTA3YTZmNDcyNTI5IiwiUmVmZXJlbmNlSWQiOiIwMTRlYTk0Ny00NzI5LTRmMzEtYTEyMS04MDlhMzYxMjMyNWIifQ.VklbW-sIosMxqKmB8PsX-9314VRuI_WYrP7V10d06nA" />
</form>
```

Esse processo é conhecido como "Device Data Collection", que no EMV 3DS (3DS versão 2) permite que o banco emissor obtenha informações adicionais do navegador e do dispositivo antes da solicitação de autenticação. Este passo é crucial, pois permite ao emissor avaliar o risco da transação antes que ela ocorra, resultando em uma taxa mais elevada de transações sem atrito.

Como complemento, também adicione o JavaScript abaixo para invocar o formulário iframe POST. Coloque o JavaScript após o fechamento Elemento `</body>` do seu checkout. O JavaScript irá invocar o formulário iframe POST automaticamente quando a janela é carregada. Esse fluxo preciso ser feito antes de solicitar a etapa de 'Enrollment'.

```http
<script>
window.onload = function() {
var ddcForm = document.querySelector('#ddc-form');
if(ddcForm) // form exists
ddcForm.submit();
}
</script>
```

Para garantir que o envio dos dados do dispositivo (Device Data Collection) seja concluído com sucesso, o processo pode levar até 10 segundos. Portanto, é necessário utilizar o JavaScript abaixo para verificar a resposta ao indicar a URL de coleta de dados do dispositivo e garantir que o processamento tenha sido concluído. Coloque o JavaScript após o fechamento Elemento `</body>`.

```http
<script>
window.addEventListener("message", (event) => {
if (event.origin === "https://centinelapistag.cardinalcommerce.com") {
let data = JSON.parse(event.data);
// Ex. do retorno com sucesso: {"MessageType":"profile.completed","SessionId":"014ea947-4729-4f31-a121-809a3612325b","Status":true}
console.log(data);
if (data !== undefined && data.Status) {
console.log("Device Data Collection - Concluído")
}
}
}, false);
</script>
```

**Observe que o URL event.origin é variável dependendo do seu ambiente:**

| Link | Ambiente |
| --- | --- |
| Teste | [https://centinelapistag.cardinalcommerce.com](https://centinelapistag.cardinalcommerce.com) |
| Produção | [https://centinelapi.cardinalcommerce.com](https://centinelapi.cardinalcommerce.com) |

<a id="post-v2-charge-ecommerce-3ds-setup"></a>

### `POST` /v2/charge/ecommerce/3ds/setup

**Versão** `v2.0`

<a id="requisição-http-10"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/charge/ecommerce/3ds/setup
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"
url = URI("{{ENDPOINT_GATEWAY}}/v2/charge/ecommerce/3ds/setup")
https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n  \"customerId\": \"ffede3ee-37ab-47bb-9981-d3d14697d69g\", \r\n \"transactions\": [\r\n { \r\n \"card\": {\r\n \"expirationMonth\": 3,\r\n  \"expirationYear\": 2030, \r\n \"brand\": 1, \r\n \"cardNumber\": \"5200000000001005\",\r\n \"cardholderName\": \"FERNANDO SILVA\"  \r\n  \"cardholderDocument\": \"95353507495\",  \r\n \"cvv\": \"111\", \"billingAddress\": { \r\n \"street\": \"Rua Ibiapava\", \r\n \"number\": \"144\", \r\n \"neighborhood\": \"Vila Apiai\", \r\n \"city\": \"Santo André\", \r\n \"state\": \"SP\", \r\n \"country\": \"Brasil\", \r\n \"zipCode\": \"09185360\", \r\n \"complement\": \"ap 1702\" \r\n }\r\n}, \r\n \"paymentType\": 2 \r\n} \r\n ], \r\n \"source\": 1 \r\n }"
response = https.request(request)
puts response.read_body
```

```python
import requests
url = "{{ENDPOINT_GATEWAY}}/v2/charge/ecommerce/3ds/setup"
payload="{\r\n  \"customerId\": \"ffede3ee-37ab-47bb-9981-d3d14697d69g\", \r\n \"transactions\": [\r\n { \r\n \"card\": {\r\n \"expirationMonth\": 3,\r\n  \"expirationYear\": 2030, \r\n \"brand\": 1, \r\n \"cardNumber\": \"5200000000001005\",\r\n \"cardholderName\": \"FERNANDO SILVA\"  \r\n  \"cardholderDocument\": \"95353507495\",  \r\n \"cvv\": \"111\", \"billingAddress\": { \r\n \"street\": \"Rua Ibiapava\", \r\n \"number\": \"144\", \r\n \"neighborhood\": \"Vila Apiai\", \r\n \"city\": \"Santo André\", \r\n \"state\": \"SP\", \r\n \"country\": \"Brasil\", \r\n \"zipCode\": \"09185360\", \r\n \"complement\": \"ap 1702\" \r\n }\r\n}, \r\n \"paymentType\": 2 \r\n} \r\n ], \r\n \"source\": 1 \r\n }"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/charge/ecommerce/3ds/setup' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "CustomerId": "d4273875-e7b0-428d-ba5a-45ebf1844693",
  "transactions": [
      {
          "card": {
              "expirationMonth": 3,
              "expirationYear": 2030,
              "brand": 2,
              "number": "5200000000001005",
              "cardholderName": "FERNANDO SILVA",
              "cardholderDocument": "95353507495",
              "cvv": "321",
              "billingAddress": {
                  "street": "Rua Ibiapava",
                  "number": "144",
                  "neighborhood": "Vila Apiai",
                  "city": "Santo André",
                  "state": "SP",
                  "country": "Brasil",
                  "zipCode": "09185360",
                  "complement": "ap 1702"
              }
          },
          "paymentType": 2
      }
  ],
  "source": 1
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");
var raw = JSON.stringify({
  "CustomerId": "d4273875-e7b0-428d-ba5a-45ebf1844693",
  "transactions": [
      {
          "card": {
              "expirationMonth": 3,
              "expirationYear": 2030,
              "brand": 2,
              "number": "5200000000001005",
              "cardholderName": "FERNANDO SILVA",
              "cardholderDocument": "95353507495",
              "cvv": "321",
              "billingAddress": {
                  "street": "Rua Ibiapava",
                  "number": "144",
                  "neighborhood": "Vila Apiai",
                  "city": "Santo André",
                  "state": "SP",
                  "country": "Brasil",
                  "zipCode": "09185360",
                  "complement": "ap 1702"
              }
          },
          "paymentType": 2
      }
  ],
  "source": 1
});
var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};
fetch("{{ENDPOINT_GATEWAY}}/v2/charge/ecommerce/3ds/setup", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
"{
    "chargeId": "b5929032-6f3c-44a7-b865-004d1e240ba2",
    "transactions": [
        {
          "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI0M2M0ODE4NS0xMmRhLTQ4NzAtYmQ3YS04ODcxMmI3NmEzZDUiLCJpYXQiOjE3MTEwMzE4ODUsImlzcyI6IjVkZDgzYmYwMGU0MjNkMTQ5OGRjYmFjYSIsImV4cCI6MTcxMTAzNTQ4NSwiT3JnVW5pdElkIjoiNjE2MDRlNjg2ZDYwYTA3YTZmNDcyNTI5IiwiUmVmZXJlbmNlSWQiOiIwMTRlYTk0Ny00NzI5LTRmMzEtYTEyMS04MDlhMzYxMjMyNWIifQ.VklbW-sIosMxqKmB8PsX-9314VRuI_WYrP7V10d06nA",
          "deviceDataCollectionUrl": "https://centinelapistag.cardinalcommerce.com/V1/Cruise/Collect",
          "cardholderAuthenticationReferenceId": "014ea947-4729-4f31-a121-809a3612325b",
          "cardholderAuthenticationId": "7110318850746425004953",
          "pan": "520000******1005"
        }
    ],
    "success": true,
    "errors": [],
    "traceKey": "4d1f4526-6721-4af7-8238-55bc21dc96a0"
}
"
```

<a id="requisição-8"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| customerId | string | Sim | ID exclusivo de cliente. |
| transactions | array(object) | Sim | Dados da transação. |
| transactions.card | object | Sim | Cartão a ser criado no sistema. |
| transactions.card.expirationMonth | int | Sim | O Mês de expiração do cartão com 2 dígitos. |
| transactions.card.expirationYear | int | Sim | O Ano de expiração do cartão com 4 dígitos. |
| transactions.card.brand | int | Sim | [A bandeira do cartão à qual o imposto se aplica.](../guias/primeiros-passos.md#cardbrand). |
| transactions.card.number | string | Sim | Primary Account Number (PAN), o número impresso na frente do cartão. |
| transactions.card.cardHolderName | string | Sim | Nome do títular do cartão. |
| transactions.card.cardHolderDocument | string | Sim | Número do documento do títular, CNPJ ou CPF. |
| transactions.card.cvv | string | Sim | Card Verification Value (CVV), recurso de segurança para transações de cartão de pagamento com "ausência de cartão" instituídas para reduzir a incidência de fraude. |
| transactions.card.billingAddress | object | Sim | Informações do endereço conectado ao cartão de crédito ou débito. As empresas usam o endereço de cobrança para verificar o uso autorizado de tal cartão. É também para onde as empresas enviam contas em papel e extratos bancários. |
| transactions.card.billingAddress.street | string | Não | Rua. |
| transactions.card.billingAddress.number | string | Não | Número. |
| transactions.card.billingAddress.neighborhood | string | Não | Bairro. |
| transactions.card.billingAddress.city | string | Não | Cidade. |
| transactions.card.billingAddress.state | string | Não | Estado. |
| transactions.card.billingAddress.country | string | Não | País. |
| transactions.card.billingAddress.zipCode | string | Não | CEP. |
| transactions.card.billingAddress.complement | string | Não | Complemento. |
| transactions.paymentType | int | sim | Tipo de pagamento. |
| source | int | sim | Origem da requisição. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | JWT gerado no endpoint de autenticação (gateway) pelo MerchantToken. |

<a id="resposta-8"></a>

#### Resposta

| Proprieadade | Tipo | Descrição |
| --- | --- | --- |
| chargeId | string | ID da cobrança gerada. |
| transactions | array(object) | Informações da transação. |
| transactions.accessToken | string | Token de acesso gerado. |
| transactions.deviceDataCollectionUrl | string | URL com os dados coletados do dispositivo de origem. |
| transactions.cardholderAuthenticationReferenceId | string | ID de referência da autenticação do portador do cartão. |
| transactions.cardholderAuthenticationId | string | ID da autenticação do portador do cartão. |
| transactions.pan | string | Primary Account Number (PAN), o número impresso na frente do cartão. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

<a id="body-raw-7"></a>

#### BODY Raw

```http
{
"CustomerId": "d4273875-e7b0-428d-ba5a-45ebf1844693",
"transactions": [
{
"card": {
"expirationMonth": 3,
"expirationYear": 2030,
"brand": 2,
"number": "5200000000001005",
"cardholderName": "FERNANDO SILVA",
"cardholderDocument": "95353507495",
"cvv": "321",
"billingAddress": {
"street": "Rua Ibiapava",
"number": "144",
"neighborhood": "Vila Apiai",
"city": "Santo André",
"state": "SP",
"country": "Brasil",
"zipCode": "09185360",
"complement": "ap 1702"
}
},
"paymentType": 2
}
],
"source": 1,
}
```

<a id="etapa-2-inscrição-enrollment"></a>

## Etapa 2. Inscrição (Enrollment)

Após a conclusão da **coleta de dados do dispositivo** (Etapa 1), o emissor analisará as informações recebidas e poderá solicitar **autenticação adicional** do titular do cartão. Para isso, é necessário realizar uma chamada ao endpoint de enrollment. Com base nessa análise, a transação poderá ser classificada como:

- **Approved**: Autenticação aprovada sem necessidade de desafio.
- **Challenged**: Autenticação requer desafio adicional (*Step-Up*).
- **Rejected**: Autenticação rejeitada.

⚠️ **Importante:** Esta etapa **somente deve ser iniciada após a coleta completa dos dados do dispositivo**.

<a id="alternativa-em-caso-de-falha-na-coleta-de-dados"></a>

### Alternativa em caso de falha na coleta de dados

Se a coleta de dados do dispositivo não for concluída com sucesso, ainda é possível qualificar a transação para o protocolo **EMV 3-D Secure 2.x**. Para isso, é necessário incluir **todos os 10 campos obrigatórios do objeto `browser`** na requisição de *Enrollment*.

<a id="resposta-sem-desafio-approved"></a>

### Resposta sem desafio (`Approved`)

Caso a autenticação seja aprovada sem necessidade de desafio, a resposta da API conterá:

- `cardholderAuthenticationStatus`: `"Approved"`
- `eci` (Electronic Commerce Indicator)

O valor do **ECI** indica o resultado da autenticação e pode representar:

- Autenticação bem-sucedida
- Tentativa de autenticação sem sucesso
- Impossibilidade de autenticação

Abaixo está a tabela de valores de ECI e a responsabilidade por **chargeback** associada a cada um.

<a id="3ds-eci"></a>

| Mastercard | Visa | Elo | Amex | Resultado da autenticação | A transação foi autenticada? |
| --- | --- | --- | --- | --- | --- |
| 02 | 05 | 05 | 05 | Autenticada pelo emissor – risco de chargeback passa a ser do emissor. | Sim |
| 01 | 06 | 06 | 06 | Autenticada pela bandeira – risco de chargeback passa a ser do emissor. | Sim |
| Diferente de 01, 02 | Diferente de 05 e 06 | Diferente de 05 e 06 | Diferente de 05 e 06 | Não autenticada – risco de chargeback permanece com o estabelecimento. | Não |

<a id="resposta-com-desafio-challenged"></a>

### Resposta com desafio (`Challenged`)

Se a API de *Enrollment* retornar uma resposta com desafio, os seguintes atributos estarão presentes:

- `stepUpUrl`
- `accessToken`
- `heightChallenge`
- `widthChallenge`

Esses valores devem ser utilizados para renderizar a tela de desafio do emissor em um **iframe**.

<a id="exemplo-1"></a>

#### Exemplo

```http
<iframe name="step-up-iframe" height="400" width="390""></iframe>
<form id="step-up-form" target="step-up-iframe" method="post" action="https://centinelapistag.cardinalcommerce.com/V2/Cruise/StepUp">
<input type="hidden" name="JWT" value="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIzM2QwZmI1OC0xNzUyLTRjMjItODdhZC1lNWRkOTk1ZGE1N2YiLCJpYXQiOjE3MTEzNjgwNjEsImlzcyI6IjVkZDgzYmYwMGU0MjNkMTQ5OGRjYmFjYSIsImV4cCI6MTcxMTM3MTY2MSwiT3JnVW5pdElkIjoiNjE2MDRlNjg2ZDYwYTA3YTZmNDcyNTI5IiwiUGF5bG9hZCI6eyJBQ1NVcmwiOiJodHRwczovLzBtZXJjaGFudGFjc3N0YWcuY2FyZGluYWxjb21tZXJjZS5jb20vTWVyY2hhbnRBQ1NXZWIvY3JlcS5qc3AiLCJQYXlsb2FkIjoiZXlKdFpYTnpZV2RsVkhsd1pTSTZJa05TWlhFaUxDSnRaWE56WVdkbFZtVnljMmx2YmlJNklqSXVNUzR3SWl3aWRHaHlaV1ZFVTFObGNuWmxjbFJ5WVc1elNVUWlPaUk1T1RVNFlqVXhZUzFoTW1Nd0xUUm1ZbVV0WVdWalpDMDVNMlJqT1RNeVpHUmlZVEFpTENKaFkzTlVjbUZ1YzBsRUlqb2lNVGRqTmpnek1UVXRNemxsT0MwME56RTNMV0ZrT1dFdFpXUXdNRFF4TmpBeU9XWTRJaXdpWTJoaGJHeGxibWRsVjJsdVpHOTNVMmw2WlNJNklqQXlJbjAiLCJUcmFuc2FjdGlvbklkIjoiNFJZdm9JQW44Sks1ZEVoVVR3UDAifSwiT2JqZWN0aWZ5UGF5bG9hZCI6dHJ1ZSwiUmV0dXJuVXJsIjoiaHR0cHM6Ly9wYXltZW50LWhtbC5zYWZyYXBheS5jb20uYnIvd2ViaG9vay92MS9jaGFyZ2UvZWNvbW1lcmNlLzNkcy9jeWJlcnNvdXJjZS9jYWxsYmFjayJ9.7Lx1KcvojUrvxiNOqDI6940HcPztcAgLXoSZ8VH1Io8" />
<input type="hidden" name="MD" value="null" />
</form>
```

<a id="complemento-invocação-automática-do-formulário-iframe-via-javascript"></a>

### Complemento: Invocação Automática do Formulário iframe via JavaScript.

Para que o formulário iframe com método POST seja invocado automaticamente ao carregar a janela, adicione o JavaScript abaixo logo após o fechamento da tag <body>.

Esse script realiza duas ações principais:

- Submete automaticamente o formulário de Step-Up (caso exista no DOM).
- Escuta mensagens enviadas pelo iframe (via postMessage) e trata a resposta recebida.

```http
<script>
window.onload = function() {
var stepUpForm = document.querySelector('#step-up-form');
if(stepUpForm) // Step-Up form exists {
stepUpForm.submit();
}
}
window.addEventListener("message", function(event) {
try {
const data = JSON.parse(event.data);
console.log("Mensagem recebida do iframe:", data);
// Aqui você pode tratar a resposta como quiser
if (data.NewStatus === "Approved") {
// lógica para status aprovado
}
} catch (e) {
console.warn("Mensagem recebida não é um JSON válido:", event.data);
}
});
</script>
```

<a id="exemplo-2"></a>

#### Exemplo:

![3ds-passo2](../assets/img/3ds-passo2.png)

Quando ocorrer o desafio e a autenticação pelo portador do cartão **não for bem-sucedida**, a resposta no callback será "Rejected".

Exemplo do evento (messsage) de callback:

<a id="exemplo-do-evento-message-de-callback"></a>

#### Exemplo do evento (message) de callback:

```http
{
"newStatus": "Rejected",
"success": true,
"errors": [],
"traceKey": "e19752b8-51e8-41e6-9c08-b2910af9be10"
}
```

Essa resposta com status "Rejected" está sempre associada ao ECI "00" ou "07". Isso impede a continuidade para o pagamento com 3DS (Etapa 3).
 
 ⚠️ Importante: Nesses casos, o lojista ou estabelecimento pode optar por enviar a transação *sem 3DS*, assumindo o risco da operação. 
 
 Por outro lado, quando a autenticação for bem-sucedida, a resposta no callback será "Approved".

<a id="exemplo-do-evento-message-de-callback-1"></a>

#### Exemplo do evento (message) de callback:

```http
{
"newStatus": "Approved",
"success": true,
"errors": [],
"traceKey": "e19752b8-51e8-41e6-9c08-b2910af9be10"
}
```

Nesse cenário, o risco da transação passa a ser do emissor. Isso ocorre porque a autenticação bem-sucedida com desafio está associada ao ECI "02" ou "05". 
 
 ✅ Atenção: Com a autenticação aprovada, é possível seguir para o endpoint de pagamento com 3DS (Etapa 3).

<a id="put-v2-charge-ecommerce-3ds-enrollment"></a>

### `PUT` /v2/charge/ecommerce/3ds/enrollment

**Versão** `v2.0`

<a id="requisição-http-11"></a>

#### Requisição HTTP

```http
PUT {{ENDPOINT_GATEWAY}}/v2/charge/ecommerce/3ds/enrollment
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"
url = URI("{{ENDPOINT_GATEWAY}}/v2/charge/ecommerce/3ds/enrollment")
https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true
request = Net::HTTP::Put.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n  \"chargeId\": \"ffede3ee-37ab-47bb-9981-d3d14697d69g\", \r\n \"customer\": { \r\n \"customerId\": \"ffede3ee-37ab-47bb-9981-d3d14697d69g\" \r\n}, \"browser\": { \r\n \"HttpAcceptBrowserValue\": \"*/*\", \r\n \"HttpAcceptContent\": \"*/*\", \r\n \"HttpBrowserLanguage\": \"pt-BR\", \r\n \"HttpBrowserJavaEnabled\": true, \r\n \"HttpBrowserJavaScriptEnabled\": true, \r\n \"HttpBrowserColorDepth\": \"24\", \r\n \"HttpBrowserScreenHeight\": \"721\", \r\n \"HttpBrowserScreenWidth\": \"1536\" \r\n \"HttpBrowserTimeDifference\": \"180\", \r\n \"UserAgentBrowserValue\": \"Mozilla/5.0\" \r\n },\r\n \"transactions\": [\r\n \"amount\": 1000, \r\n { \r\n \"card\": {\r\n \"expirationMonth\": 3,\r\n  \"expirationYear\": 2030, \r\n \"brand\": 1, \r\n \"cardNumber\": \"5200000000001005\",\r\n \"cardholderName\": \"Renan Soarez\"  \r\n  \"cardholderDocument\": \"95353507495\",  \r\n \"cvv\": \"111\", \"billingAddress\": { \r\n \"street\": \"Rua Ibiapava\", \r\n \"number\": \"144\", \r\n \"neighborhood\": \"Vila Apiai\", \r\n \"city\": \"Santo André\", \r\n \"state\": \"SP\", \r\n \"country\": \"Brasil\", \r\n \"zipCode\": \"09185360\", \r\n \"complement\": \"ap 1702\" \r\n }\r\n}, \r\n} \r\n ]\r\n }"
response = https.request(request)
puts response.read_body
```

```python
import requests
url = "{{ENDPOINT_GATEWAY}}/v2/charge/ecommerce/3ds/enrollment"
payload="{\r\n  \"chargeId\": \"ffede3ee-37ab-47bb-9981-d3d14697d69g\", \r\n \"customer\": { \r\n \"customerId\": \"ffede3ee-37ab-47bb-9981-d3d14697d69g\" \r\n}, \"browser\": { \r\n \"HttpAcceptBrowserValue\": \"*/*\", \r\n \"HttpAcceptContent\": \"*/*\", \r\n \"HttpBrowserLanguage\": \"pt-BR\", \r\n \"HttpBrowserJavaEnabled\": true, \r\n \"HttpBrowserJavaScriptEnabled\": true, \r\n \"HttpBrowserColorDepth\": \"24\", \r\n \"HttpBrowserScreenHeight\": \"721\", \r\n \"HttpBrowserScreenWidth\": \"1536\" \r\n \"HttpBrowserTimeDifference\": \"180\", \r\n \"UserAgentBrowserValue\": \"Mozilla/5.0\" \r\n },\r\n \"transactions\": [\r\n \"amount\": 1000, \r\n { \r\n \"card\": {\r\n \"expirationMonth\": 3,\r\n  \"expirationYear\": 2030, \r\n \"brand\": 1, \r\n \"cardNumber\": \"5200000000001005\",\r\n \"cardholderName\": \"Renan Soarez\"  \r\n  \"cardholderDocument\": \"95353507495\",  \r\n \"cvv\": \"111\", \"billingAddress\": { \r\n \"street\": \"Rua Ibiapava\", \r\n \"number\": \"144\", \r\n \"neighborhood\": \"Vila Apiai\", \r\n \"city\": \"Santo André\", \r\n \"state\": \"SP\", \r\n \"country\": \"Brasil\", \r\n \"zipCode\": \"09185360\", \r\n \"complement\": \"ap 1702\" \r\n }\r\n}, \r\n} \r\n ]\r\n }"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}
response = requests.request("PUT", url, headers=headers, data=payload)
print(response.text)
```

```bash
curl --location --request PUT '{{ENDPOINT_GATEWAY}}/v2/charge/ecommerce/3ds/enrollment' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "chargeId": "41649b0b-3534-4190-a8b1-6194cb56ec54",
  "customer": {
      "customerId": "b2344864-ae28-4399-a3c9-f3d28d682f85"
  },
  "browser": {
      "HttpAcceptBrowserValue": "*/*",
      "HttpAcceptContent": "*/*",
      "HttpBrowserLanguage": "pt-BR",
      "HttpBrowserJavaEnabled": true,
      "HttpBrowserJavaScriptEnabled": true,
      "HttpBrowserColorDepth": "24",
      "HttpBrowserScreenHeight": "721",
      "HttpBrowserScreenWidth": "1536",
      "HttpBrowserTimeDifference": "180",
      "UserAgentBrowserValue": "Mozilla/5.0"
  },
  "transactions": [
      {
          "amount": 1000,
          "card": {
              "expirationMonth": 3,
              "expirationYear": 2030,
              "brand": 2,
              "number": "5200000000001005",
              "cardholderName": "FERNANDO SILVA",
              "cardholderDocument": "95353507495",
              "cvv": "321",
              "billingAddress": {
                  "street": "Rua Ibiapava",
                  "number": "144",
                  "neighborhood": "Vila Apiai",
                  "city": "Santo André",
                  "state": "SP",
                  "country": "Brasil",
                  "zipCode": "09185360",
                  "complement": "ap 1702"
              }
          }
      }
  ]
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");
var raw = JSON.stringify({
  "chargeId": "41649b0b-3534-4190-a8b1-6194cb56ec54",
  "customer": {
      "customerId": "b2344864-ae28-4399-a3c9-f3d28d682f85"
  },
  "browser": {
      "HttpAcceptBrowserValue": "*/*",
      "HttpAcceptContent": "*/*",
      "HttpBrowserLanguage": "pt-BR",
      "HttpBrowserJavaEnabled": true,
      "HttpBrowserJavaScriptEnabled": true,
      "HttpBrowserColorDepth": "24",
      "HttpBrowserScreenHeight": "721",
      "HttpBrowserScreenWidth": "1536",
      "HttpBrowserTimeDifference": "180",
      "UserAgentBrowserValue": "Mozilla/5.0"
  },
  "transactions": [
      {
          "amount": 1000,
          "card": {
              "expirationMonth": 3,
              "expirationYear": 2030,
              "brand": 2,
              "number": "5200000000001005",
              "cardholderName": "FERNANDO SILVA",
              "cardholderDocument": "95353507495",
              "cvv": "321",
              "billingAddress": {
                  "street": "Rua Ibiapava",
                  "number": "144",
                  "neighborhood": "Vila Apiai",
                  "city": "Santo André",
                  "state": "SP",
                  "country": "Brasil",
                  "zipCode": "09185360",
                  "complement": "ap 1702"
              }
          }
      }
  ]

});
var requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};
fetch("{{ENDPOINT_GATEWAY}}/v2/charge/ecommerce/3ds/enrollment", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
"
{
    "chargeId": "b5929032-6f3c-44a7-b865-004d1e240ba2",
    "chargeStatus": "PreAuthorized",
    "transactions": [
        {
            "cardholderAuthenticationVersion": "2.1.0",
            "cardholderAuthenticationStatus": "Challenged",
            "stepUpUrl": "https://centinelapistag.cardinalcommerce.com/V2/Cruise/StepUp",
            "needRunAntifraud": false,
            "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI3ZjUwMzVlZS02M2IzLTRiNzMtYTFhYS1iYmFmOThhZGIyOGUiLCJpYXQiOjE3MTEzNzA3OTYsImlzcyI6IjVkZDgzYmYwMGU0MjNkMTQ5OGRjYmFjYSIsImV4cCI6MTcxMTM3NDM5NiwiT3JnVW5pdElkIjoiNjE2MDRlNjg2ZDYwYTA3YTZmNDcyNTI5IiwiUGF5bG9hZCI6eyJBQ1NVcmwiOiJodHRwczovLzBtZXJjaGFudGFjc3N0YWcuY2FyZGluYWxjb21tZXJjZS5jb20vTWVyY2hhbnRBQ1NXZWIvY3JlcS5qc3AiLCJQYXlsb2FkIjoiZXlKdFpYTnpZV2RsVkhsd1pTSTZJa05TWlhFaUxDSnRaWE56WVdkbFZtVnljMmx2YmlJNklqSXVNUzR3SWl3aWRHaHlaV1ZFVTFObGNuWmxjbFJ5WVc1elNVUWlPaUl5TURReU5EUXlZaTFpWVRWakxUUmtOVE10T1Rsak5TMDNOalF5TXpNMlpHSmlaVFVpTENKaFkzTlVjbUZ1YzBsRUlqb2lOVEJpTlRnMVkyWXROREF3TWkwMFpqWTJMVGcxT0RrdE5HUmxOamxoWXpneU5XRXdJaXdpWTJoaGJHeGxibWRsVjJsdVpHOTNVMmw2WlNJNklqQXlJbjAiLCJUcmFuc2FjdGlvbklkIjoiYUV1OVRwMm5kaWJRQzJEMnQ3azAifSwiT2JqZWN0aWZ5UGF5bG9hZCI6dHJ1ZSwiUmV0dXJuVXJsIjoiaHR0cHM6Ly9wYXltZW50LWhtbC5zYWZyYXBheS5jb20uYnIvd2ViaG9vay92MS9jaGFyZ2UvZWNvbW1lcmNlLzNkcy9jeWJlcnNvdXJjZS9jYWxsYmFjayJ9.vsAsMSt91WGD-_7t3tllCzZ2UBJegSho2sYoIvONiuc",
            "heightChallenge": "400",
            "widthChallenge": "390",
            "pan": "520000******1096"
        }
    ],
    "success": true,
    "errors": [],
    "traceKey": "2bb82ca0-51ed-48e2-8b1d-db4cd6e35591"
}
"
```

<a id="requisição-9"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| chargeId | string | Sim | ID da cobrança. |
| customer | object | Sim | Dados do cliente. |
| customer.customerId | string | Sim | ID exclusivo de cliente. |
| browser | object | Sim | Dados do navegador/dispositivo de origem da requisição. |
| browser.HttpAcceptBrowserValue | string | Sim | Valor de cabeçalho aceito do navegador/dispositivo de origem. |
| browser.HttpAcceptContent | string | Sim | Valor exato do cabeçalho de aceitação HTTP. |
| browser.HttpBrowserLanguage | string | Sim | Linguagem do navegador/dispositivo de origem. |
| browser.HttpBrowserJavaEnabled | bool | Sim | Se JAVA esta habilitado. |
| browser.HttpBrowserJavaScriptEnabled | bool | Sim | Se JAVASCRIPT esta habilitado. |
| browser.HttpBrowserColorDepth | string | Sim | Número de bits usado para exibir imagens. |
| browser.HttpBrowserScreenHeight | string | Sim | Altura da tela do navegador/dispositivo de origem. |
| browser.HttpBrowserScreenWidth | string | Sim | Largura da tela do navegador/dispositivo de origem. |
| browser.HttpBrowserTimeDifference | string | Sim | Diferença em minutos entre tempo GMT e o navegador/dispositivo de origem. |
| browser.UserAgentBrowserValue | string | Sim | O valor exato do User Agent do cabeçalho. |
| transactions | array(object) | Sim | Dados da transação. |
| transactions.amount | double | Sim | Valor total da transação. |
| transactions.card | object | Sim | Cartão a ser criado no sistema. |
| transactions.card.expirationMonth | int | Sim | O Mês de expiração do cartão com 2 dígitos. |
| transactions.card.expirationYear | int | Sim | O Ano de expiração do cartão com 4 dígitos. |
| transactions.card.brand | int | Sim | [A bandeira do cartão à qual o imposto se aplica.](../guias/primeiros-passos.md#cardbrand). |
| transactions.card.number | string | Sim | Primary Account Number (PAN), o número impresso na frente do cartão. |
| transactions.card.cardHolderName | string | Sim | Nome do títular do cartão. |
| transactions.card.cardHolderDocument | string | Sim | Número do documento do títular, CNPJ ou CPF. |
| transactions.card.cvv | string | Sim | Card Verification Value (CVV), recurso de segurança para transações de cartão de pagamento com "ausência de cartão" instituídas para reduzir a incidência de fraude. |
| transactions.card.billingAddress | object | Sim | Informações do endereço conectado ao cartão de crédito ou débito. As empresas usam o endereço de cobrança para verificar o uso autorizado de tal cartão. É também para onde as empresas enviam contas em papel e extratos bancários. |
| transactions.card.billingAddress.street | string | Não | Rua. |
| transactions.card.billingAddress.number | string | Não | Número. |
| transactions.card.billingAddress.neighborhood | string | Não | Bairro. |
| transactions.card.billingAddress.city | string | Não | Cidade. |
| transactions.card.billingAddress.state | string | Não | Estado. |
| transactions.card.billingAddress.country | string | Não | País. |
| transactions.card.billingAddress.zipCode | string | Não | CEP. |
| transactions.card.billingAddress.complement | string | Não | Complemento. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | JWT gerado no endpoint de autenticação (gateway) pelo MerchantToken. |

<a id="resposta-9"></a>

#### Resposta

| Proprieadade | Tipo | Descrição |
| --- | --- | --- |
| chargeId | string | ID da cobrança. |
| chargeStatus | string | Estado da cobrança. |
| transactions | array(object) | Informações da transação. |
| transactions.cardholderAuthenticationVersion | string | Versão da autenticação do cartão. |
| transactions.cardholderAuthenticationStatus | string | Estado da autenticação do cartão. |
| transactions.stepUpUrl | string | Endpoint retornado pelo ACS para utilização no iframe. |
| transactions.needRunAntifraud | bool | Informa se há ou não a necessidade de enviar a transação para um antifraude. |
| transactions.accessToken | string | Token de acesso para efetuar o POST no iframe para a URL de step-up. |
| transactions.heightChallenge | string | Altura do iframe para demonstração da tela de desafio. |
| transactions.widthChallenge | string | Largura do iframe para demonstração da tela de desafio. |
| transactions.pan | string | Primary Account Number (PAN), o número impresso na frente do cartão. |
| transactions.eci | string | [Eletronic Commerce Indicator](gateway.md#3ds-eci) |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

<a id="body-raw-8"></a>

#### BODY Raw

```http
{
"chargeId":"string",
"customer":{
"customerId":"string",
},
"browser":{
"httpAcceptBrowserValue":"string",
"httpAcceptContent":"string",
"httpBrowserLanguage":"string",
"httpBrowserJavaEnabled":true,
"httpBrowserJavaScriptEnabled":true,
"httpBrowserColorDepth":"string",
"httpBrowserScreenHeight":"string",
"httpBrowserScreenWidth":"string",
"httpBrowserTimeDifference":"string",
"userAgentBrowserValue":"string"
},
"transactions":[
{
"amount":0,
"card": {
"expirationMonth": 3,
"expirationYear": 2030,
"brand": 2,
"number": "5200000000001005",
"cardholderName": "FERNANDO SILVA",
"cardholderDocument": "95353507495",
"cvv": "321",
"billingAddress": {
"street": "Rua Ibiapava",
"number": "144",
"neighborhood": "Vila Apiai",
"city": "Santo André",
"state": "SP",
"country": "Brasil",
"zipCode": "09185360",
"complement": "ap 1702"
}
},
}
]
}
```

<a id="etapa-3-pagamento"></a>

### Etapa 3. Pagamento

Nesta etapa final, o pagamento é efetuado, e é fundamental informar na requisição o **chargeId** e o **cardholderAuthenticationId** com o valor retornado na Etapa 1.

<a id="put-v2-charge-ecommerce"></a>

### `PUT` /v2/charge/ecommerce

**Versão** `v2.0`

<a id="requisição-http-12"></a>

#### Requisição HTTP

```http
PUT {{ENDPOINT_GATEWAY}}/v2/charge/ecommerce
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"
url = URI("{{ENDPOINT_GATEWAY}}/v2/charge/ecommerce")
https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true
request = Net::HTTP::Put.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n \"chargeId\": \"b5929032-6f3c-44a7-b865-004d1e240ba2\", \r\n \"capture\": true, \r\n \"transactions\": [\r\n { \r\n \"installmentNumber\": 1, \r\n \"installmentType\": 1, \r\n \"card\": {\r\n \"expirationMonth\": 3,\r\n  \"expirationYear\": 2030, \r\n \"brand\": 1, \r\n \"cardNumber\": \"5200000000001005\",\r\n \"cardholderName\": \"FERNANDO SILVA\"  \r\n  \"cardholderDocument\": \"95353507495\",  \r\n \"cvv\": \"111\", \"billingAddress\": { \r\n \"street\": \"Rua Ibiapava\", \r\n \"number\": \"144\", \r\n \"neighborhood\": \"Vila Apiai\", \r\n \"city\": \"Santo André\", \r\n \"state\": \"SP\", \r\n \"country\": \"Brasil\", \r\n \"zipCode\": \"09185360\", \r\n \"complement\": \"ap 1702\" \r\n } \r\n \"cardholderAuthenticationId\": \"7110318850746425004953\"  \r\n} \r\n} \r\n ] \r\n }"
response = https.request(request)
puts response.read_body
```

```python
import requests
url = "{{ENDPOINT_GATEWAY}}/v2/charge/ecommerce"
payload="{\r\n \"chargeId\": \"b5929032-6f3c-44a7-b865-004d1e240ba2\", \r\n \"capture\": true, \r\n \"transactions\": [\r\n { \r\n \"installmentNumber\": 1, \r\n \"installmentType\": 1, \r\n \"card\": {\r\n \"expirationMonth\": 3,\r\n  \"expirationYear\": 2030, \r\n \"brand\": 1, \r\n \"cardNumber\": \"5200000000001005\",\r\n \"cardholderName\": \"FERNANDO SILVA\"  \r\n  \"cardholderDocument\": \"95353507495\",  \r\n \"cvv\": \"111\", \"billingAddress\": { \r\n \"street\": \"Rua Ibiapava\", \r\n \"number\": \"144\", \r\n \"neighborhood\": \"Vila Apiai\", \r\n \"city\": \"Santo André\", \r\n \"state\": \"SP\", \r\n \"country\": \"Brasil\", \r\n \"zipCode\": \"09185360\", \r\n \"complement\": \"ap 1702\" \r\n } \r\n \"cardholderAuthenticationId\": \"7110318850746425004953\"  \r\n} \r\n} \r\n ] \r\n }"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}
response = requests.request("PUT", url, headers=headers, data=payload)
print(response.text)
```

```bash
curl --location --request PUT '{{ENDPOINT_GATEWAY}}/v2/charge/ecommerce' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "chargeId": "b5929032-6f3c-44a7-b865-004d1e240ba2",
  "capture": true,
  "transactions": [
      {
          "installmentNumber": 1,
          "installmentType": 1,
          "card": {
              "expirationMonth": 3,
              "expirationYear": 2030,
              "brand": 2,
              "number": "5200000000001005",
              "cardholderName": "FERNANDO SILVA",
              "cardholderDocument": "95353507495",
              "cvv": "321",
              "billingAddress": {
                  "street": "Rua Ibiapava",
                  "number": "144",
                  "neighborhood": "Vila Apiai",
                  "city": "Santo André",
                  "state": "SP",
                  "country": "Brasil",
                  "zipCode": "09185360",
                  "complement": "ap 1702"
              },
              "cardholderAuthenticationId": "7110318850746425004953"
          }
      }
  ]
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");
var raw = JSON.stringify({
  "chargeId": "b5929032-6f3c-44a7-b865-004d1e240ba2",
    "capture": true,
    "transactions": [
        {
            "installmentNumber": 1,
            "installmentType": 1,
            "card": {
                "expirationMonth": 3,
                "expirationYear": 2030,
                "brand": 2,
                "number": "5200000000001005",
                "cardholderName": "FERNANDO SILVA",
                "cardholderDocument": "95353507495",
                "cvv": "321",
                "billingAddress": {
                    "street": "Rua Ibiapava",
                    "number": "144",
                    "neighborhood": "Vila Apiai",
                    "city": "Santo André",
                    "state": "SP",
                    "country": "Brasil",
                    "zipCode": "09185360",
                    "complement": "ap 1702"
                },
                "cardholderAuthenticationId": "7110318850746425004953"
            }
        }
    ]
});
var requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};
fetch("{{ENDPOINT_GATEWAY}}/v2/charge/ecommerce", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
"
{
    "charge": {
        "id": "b5929032-6f3c-44a7-b865-004d1e240ba2",
        "nsu": "000002053",
        "customerId": "b2344864-ae28-4399-a3c9-f3d28d682f85",
        "chargeStatus": "Authorized",
        "transactions": [
            {
                "isApproved": true,
                "card": {
                    "number": "520000******1096",
                    "brand": "MasterCard"
                },
                "paymentType": "Credit",
                "installmentType": "None",
                "installmentNumber": 1,
                "softDescriptor": "TASK*5333",
                "amount": 1000,
                "isCapture": true,
                "isRecurrency": false,
                "isCanceled": false,
                "transactionId": "020015695836",
                "authorizationResponseCode": "00",
                "authorizationCode": "214530",
                "transactionStatus": "Captured",
                "acquirer": "Safrapay",
                "errorMessage": "Aprovada",
                "acquirerErrorMessage": "Aprovada",
                "creationDateTime": "2024-03-25T12:04:37.7548143-03:00",
                "captureDateTime": "2024-03-25T12:04:37.7552867-03:00"
                "eci": "05"
            }
        ]
    },
    "success": true,
    "errors": [],
    "traceKey": "cebce70e-5e08-4e23-afbe-57866ede86cf"
}
"
```

<a id="requisição-10"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| chargeId | string | Sim | ID da cobrança. |
| capture | bool | Sim | Indica se a cobrança foi capturada. |
| transactions | array(object) | Sim | Dados da transação. |
| transactions.installmentNumber | int | Sim | Total de parcelas. |
| transactions.installmentType | int | Sim | [Tipo de parcelamento da transação](../guias/primeiros-passos.md#installmenttype). |
| transactions.card | object | Sim | Cartão a ser criado no sistema. |
| transactions.card.expirationMonth | int | Sim | O Mês de expiração do cartão com 2 dígitos. |
| transactions.card.expirationYear | int | Sim | O Ano de expiração do cartão com 4 dígitos. |
| transactions.card.brand | int | Sim | [A bandeira do cartão à qual o imposto se aplica.](../guias/primeiros-passos.md#cardbrand). |
| transactions.card.number | string | Sim | Primary Account Number (PAN), o número impresso na frente do cartão. |
| transactions.card.cardHolderName | string | Sim | Nome do títular do cartão. |
| transactions.card.cardHolderDocument | string | Sim | Número do documento do títular, CNPJ ou CPF. |
| transactions.card.cvv | string | Sim | Card Verification Value (CVV), recurso de segurança para transações de cartão de pagamento com "ausência de cartão" instituídas para reduzir a incidência de fraude. |
| transactions.card.billingAddress | object | Sim | Informações do endereço conectado ao cartão de crédito ou débito. As empresas usam o endereço de cobrança para verificar o uso autorizado de tal cartão. É também para onde as empresas enviam contas em papel e extratos bancários. |
| transactions.card.billingAddress.street | string | Sim | Rua. |
| transactions.card.billingAddress.number | string | Sim | Número. |
| transactions.card.billingAddress.neighborhood | string | Sim | Bairro. |
| transactions.card.billingAddress.city | string | Sim | Cidade. |
| transactions.card.billingAddress.state | string | Sim | Estado. |
| transactions.card.billingAddress.country | string | Sim | País. |
| transactions.card.billingAddress.zipCode | string | Sim | CEP. |
| transactions.card.billingAddress.complement | string | Sim | Complemento. |
| transactions.card.cardholderAuthenticationId | string | Sim | ID de autenticação do cartão. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | JWT gerado no endpoint de autenticação (gateway) pelo MerchantToken. |

<a id="resposta-10"></a>

#### Resposta

| Proprieadade | Tipo | Descrição |
| --- | --- | --- |
| nsu | string | Identificador do pedido (Safrapay). |
| customerId | string | ID do cliente. |
| chargeStatus | string | Estado da cobrança. |
| transactions | array(object) | Informações da transação. |
| transactions.isApproved | bool | Se a transação foi ou não aprovada. |
| transactions.card | object | Informações do cartão. |
| transactions.card.number | string | Primary Account Number (PAN), o número impresso na frente do cartão. |
| transactions.card.brand | string | Bandeira do cartão. |
| transactions.paymentType | string | Tipo de pagamento. |
| transactions.installmentType | string | Tipo de parcelamento. |
| transactions.softDescriptor | string | Breve descrição a ser apresentada na fatura bancária do cliente. Este campo aceita apenas letras, números e `*`; **sem espaços**; formato `/^[a-zA-Z0-9*]+$/`. Se nulo, preenchido com rótulo padrão. |
| transactions.amount | double | Valor total da transação. |
| transactions.isCapture | bool | Se a transação foi ou não capturada. |
| transactions.isRecurrency | bool | Se a transação é ou não recorrente. |
| transactions.isCanceled | bool | Se a transação foi ou não cancelada. |
| transactions.transactionId | string | Número Sequencial Único (NSU) da autorização, caso o pagamento seja aprovado pelo Emissor. |
| transactions.authorizationResponseCode | string | Código de resposta do autorizador. |
| transactions.authorizationCode | string | Código do autorizador. |
| transactions.transactionStatus | string | Estado da transação. |
| transactions.acquirer | string | Adquirente. |
| transactions.errorMessage | string | Mensagem de erro. |
| transactions.acquirerErrorMessage | string | Mensagem de erro do adquirente. |
| transactions.creationDateTime | string | Data de criação da transação no formato UTC. |
| transactions.captureDateTime | string | Data de captura da transação no formato UTC. |
| transactions.eci | string | [Eletronic Commerce Indicator](gateway.md#3ds-eci). |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

<a id="body-raw-9"></a>

#### BODY Raw

```http
{
"chargeId":"string",
"capture":"boolean",
"transactions":[
{
"installmentNumber":1,
"installmentType":1,
"card": {
"expirationMonth": 3,
"expirationYear": 2030,
"brand": 2,
"number": "5200000000001005",
"cardholderName": "FERNANDO SILVA",
"cardholderDocument": "95353507495",
"cvv": "321",
"billingAddress": {
"street": "Rua Ibiapava",
"number": "144",
"neighborhood": "Vila Apiai",
"city": "Santo André",
"state": "SP",
"country": "Brasil",
"zipCode": "09185360",
"complement": "ap 1702"
}
"cardholderAuthenticationId": "7110318850746425004953",
},
}
]
}
```

<a id="produtos"></a>

## Produtos

Os produtos que serão cadastrados na loja, que poderam ser incluidas nas transações futuras.

<a id="post-product"></a>

### `POST` /product

**Versão** `v1.0`

<a id="requisição-http-13"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_PORTAL}}/v1/product
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_PORTAL}}/v1/product")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["merchantId"] = "{{merchantId}}"
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n  \"amount\": 800,\r\n  \"name\": \"Suco de Uva 100%\",\r\n  \"membershipFee\": 350,\r\n  \"isActive\": true,\r\n  \"sku\": \"SKU_Suco_D_Uva\",\r\n  \"merchantId\": \"{{merchantId}}\"\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_PORTAL}}/v1/product"

payload="{\r\n  \"amount\": 800,\r\n  \"name\": \"Suco de Uva 100%\",\r\n  \"membershipFee\": 350,\r\n  \"isActive\": true,\r\n  \"sku\": \"SKU_Suco_D_Uva\",\r\n  \"merchantId\": \"{{merchantId}}\"\r\n}"
headers = {
  'merchantId': '{{merchantId}}',
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_PORTAL}}/v1/product' \
--header 'merchantId: {{merchantId}}' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "amount": 800,
  "name": "Suco de Uva 100%",
  "membershipFee": 350,
  "isActive": true,
  "sku": "SKU_Suco_D_Uva",
  "merchantId": "{{merchantId}}"
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("merchantId", "{{merchantId}}");
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"amount":800,"name":"Suco de Uva 100%","membershipFee":350,"isActive":true,"sku":"SKU_Suco_D_Uva","merchantId":"{{merchantId}}"});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_PORTAL}}/v1/product", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "product": {
        "id": "230fded2-9d2b-4e9f-8bc8-2100c5759e8a",
        "quantity": 0,
        "amount": 800,
        "name": "Suco de Uva 100%",
        "membershipFee": 350,
        "isActive": true,
        "sku": "SKU_Suco_D_Uva",
        "merchantId": "22eb9083-ec20-4b9e-85d6-22cf9c35a898"
    },
    "success": true,
    "errors": [],
    "traceKey": "39b2c0a4-9027-4fed-925e-d6c79be33567"
}
```

O Endpoint responsável por criar um novo produto.

<a id="requisição-11"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| amount | int | Sim | O preço do produto. |
| name | string | Não | O nome do produto. |
| description | string | Não | A descrição do produto. |
| imagesRef | array(string) | Não | Urls das imagens do produto. |
| membershipFee | int | Sim | O valor de entrega. |
| isActive | bool | Sim | Indica se produto está ativo ou não. |
| sku | string | Não | Código identificador do produto. |
| merchantId | string | Não | O ID do comerciante. |

<a id="resposta-11"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| product.id | string | O ID do produto. |
| product.quantity | int | Quantidade do produto. |
| product.amount | int | O preço do produto. |
| product.name | string | O nome do produto. |
| product.description | string | A descrição do produto. |
| product.imagesRef | array | Urls das imagens do produto. |
| product.membershipFee | int | O valor de entrega. |
| product.isActive | bool | Indica se produto está ativo ou não. |
| product.sku | string | Código identificador do produto. |
| product.merchantId | string | O ID do comerciante. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | Use o Merchant Token para gerar o `accessToken` do ENDPOINT_PORTAL. |
| **merchantId** | {{merchantId}} |
| -- | O número de identificação do comerciante. |

<a id="body-raw-10"></a>

#### BODY Raw

```http
{
"amount": 800,
"name": "Suco de Uva 100%",
"membershipFee": 350,
"isActive": true,
"sku": "SKU_Suco_D_Uva",
"merchantId": "{{merchantId}}"
}
```

<a id="get-product"></a>

### `GET` /product

**Versão** `v1.0`

<a id="requisição-http-14"></a>

#### Requisição HTTP

```http
GET {{ENDPOINT_PORTAL}}/v1/product
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_PORTAL}}/v1/product?merchantId={{merchantId}}&currentPage=1&pageSize=10")

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

url = "{{ENDPOINT_PORTAL}}/v1/product?merchantId={{merchantId}}&currentPage=1&pageSize=10"

payload={}
headers = {
  'merchantId': '{{merchantId}}',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location -g --request GET '{{ENDPOINT_PORTAL}}/v1/product?merchantId={{merchantId}}&currentPage=1&pageSize=10' \
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

fetch("{{ENDPOINT_PORTAL}}/v1/product?merchantId={{merchantId}}&currentPage=1&pageSize=10", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "products": [
        {
            "id": "230fded2-9d2b-5e9f-9bc8-2100c5759e8a",
            "quantity": 0,
            "amount": 800,
            "name": "Suco de Uva 100%",
            "membershipFee": 350,
            "isActive": true,
            "sku": "SKU_Suco_D_Uva",
            "merchantId": "22eb9083-ec20-4b0e-95d6-22cf9c35a898"
        }
    ],
    "total": 1,
    "success": true,
    "errors": [],
    "traceKey": "9b72d660-6baf-4066-bfcb-1e55a8f3a547"
}
```

O Endpoint responsável por obter a lista de produtos de um comerciante.

<a id="parâmetros-de-query-1"></a>

#### Parâmetros de query

| Parâmetro | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| merchantId | string | Sim | O ID do comerciante. |
| name | string | Sim | O nome do produto. |
| currentPage | int | Não | Página atual da busca.. |
| pageSize | int | Não | Quantidade de itens por página. |

<a id="resposta-12"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| product.id | string | O ID do produto. |
| product.quantity | int | Quantidade do produto. |
| product.amount | int | O preço do produto. |
| product.name | string | O nome do produto. |
| product.description | string | A descrição do produto. |
| product.imagesRef | array | Urls das imagens do produto. |
| product.membershipFee | int | O valor de entrega. |
| product.isActive | bool | Indica se produto está ativo ou não. |
| product.sku | string | Código identificador do produto. |
| product.merchantId | string | O ID do comerciante. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | Use o Merchant Token para gerar o `accessToken` do ENDPOINT_PORTAL. |
| **merchantId** | {{merchantId}} |
| -- | O número de identificação do comerciante. |

| PARAMS | - |
| --- | --- |
| **merchantId** | {{merchantId}} |
| -- | O número de identificação do comerciante. |
| **name** | -- |
| -- | O nome do produto. |
| **currentPage** | -- |
| -- | Página atual da busca. |
| **pageSize** | -- |
| -- | Quantidade de itens por página. |

<a id="put-product-productid"></a>

### `PUT` /product/{productId}

**Versão** `v1.0`

<a id="requisição-http-15"></a>

#### Requisição HTTP

```http
PUT {{ENDPOINT_PORTAL}}/v1/product/{productId}
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_PORTAL}}/v1/product/{{productId}}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Put.new(url)
request["merchantId"] = "{{merchantId}}"
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n  \"amount\": 850,\r\n  \"name\": \"Suco de Uva 100%\",\r\n  \"membershipFee\": 300,\r\n  \"isActive\": true,\r\n  \"sku\": \"SKU_Suco_D_Uva\",\r\n  \"merchantId\": \"{{merchantId}}\"\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_PORTAL}}/v1/product/{{productId}}"

payload="{\r\n  \"amount\": 850,\r\n  \"name\": \"Suco de Uva 100%\",\r\n  \"membershipFee\": 300,\r\n  \"isActive\": true,\r\n  \"sku\": \"SKU_Suco_D_Uva\",\r\n  \"merchantId\": \"{{merchantId}}\"\r\n}"
headers = {
  'merchantId': '{{merchantId}}',
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location -g --request PUT '{{ENDPOINT_PORTAL}}/v1/product/{{productId}}' \
--header 'merchantId: {{merchantId}}' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "amount": 850,
  "name": "Suco de Uva 100%",
  "membershipFee": 300,
  "isActive": true,
  "sku": "SKU_Suco_D_Uva",
  "merchantId": "{{merchantId}}"
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("merchantId", "{{merchantId}}");
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"amount":850,"name":"Suco de Uva 100%","membershipFee":300,"isActive":true,"sku":"SKU_Suco_D_Uva","merchantId":"{{merchantId}}"});

var requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_PORTAL}}/v1/product/{{productId}}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "product": {
        "id": "230fded2-9d2b-5e9f-9bc8-2100c5759e8a",
        "quantity": 0,
        "amount": 800,
        "name": "Suco de Uva 100%",
        "membershipFee": 350,
        "isActive": true,
        "sku": "SKU_Suco_D_Uva",
        "merchantId": "22eb9083-ec20-4b0e-95d6-22cf9c35a898"
    },
    "success": true,
    "errors": [],
    "traceKey": "8630cfc4-8f0e-4e22-9f1b-868182d018ab"
}
```

O Endpoint responsável por atualizar os dados de um produto.

<a id="parâmetros-de-query-2"></a>

#### Parâmetros de query

| Parâmetro | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| productId | string | Sim | O ID do produto. |

<a id="requisição-12"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| amount | int | Sim | O preço do produto. |
| name | string | Não | O nome do produto. |
| description | string | Não | A descrição do produto. |
| imagesRef | array(string) | Não | Urls das imagens do produto. |
| membershipFee | int | Sim | O valor de entrega. |
| isActive | bool | Sim | Indica se produto está ativo ou não. |
| sku | string | Não | Código identificador do produto. |
| merchantId | string | Não | O ID do comerciante. |

<a id="resposta-13"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| product.id | string | O ID do produto. |
| product.quantity | int | Quantidade do produto. |
| product.amount | int | O preço do produto. |
| product.name | string | O nome do produto. |
| product.description | string | A descrição do produto. |
| product.imagesRef | array | Urls das imagens do produto. |
| product.membershipFee | int | O valor de entrega. |
| product.isActive | bool | Indica se produto está ativo ou não. |
| product.sku | string | Código identificador do produto. |
| product.merchantId | string | O ID do comerciante. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | Use o Merchant Token para gerar o `accessToken` do ENDPOINT_PORTAL. |
| **merchantId** | {{merchantId}} |
| -- | O número de identificação do comerciante. |

<a id="body-raw-11"></a>

#### BODY Raw

```http
{
"amount": 850,
"name": "Suco de Uva 100%",
"membershipFee": 300,
"isActive": true,
"sku": "SKU_Suco_D_Uva",
"merchantId": "{{merchantId}}"
}
```

<a id="get-product-productid"></a>

### `GET` /product/{productId}

**Versão** `v1.0`

<a id="requisição-http-16"></a>

#### Requisição HTTP

```http
GET {{ENDPOINT_PORTAL}}/v1/product/{productId}
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_PORTAL}}/v1/product/{{productId}}")

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

url = "{{ENDPOINT_PORTAL}}/v1/product/{{productId}}"

payload={}
headers = {
  'merchantId': '{{merchantId}}',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location -g --request GET '{{ENDPOINT_PORTAL}}/v1/product/{{productId}}' \
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

fetch("{{ENDPOINT_PORTAL}}/v1/product/{{productId}}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "product": {
        "id": "230fded2-9d2b-5e9f-9bc8-2100c5759e8a",
        "quantity": 0,
        "amount": 850,
        "name": "Suco de Uva 100%",
        "membershipFee": 300,
        "isActive": true,
        "sku": "SKU_Suco_D_Uva",
        "merchantId": "22eb9083-ec20-4b0e-95d6-22cf9c35a898"
    },
    "success": true,
    "errors": [],
    "traceKey": "b076286a-93cf-48fe-806c-68852b3c880f"
}
```

O Endpoint responsável por obter produto pelo ID.

<a id="parâmetros-de-rota"></a>

#### Parâmetros de rota

| Parâmetro | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| productId | string | Sim | O ID do produto. |

<a id="resposta-14"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| product.id | string | O ID do produto. |
| product.quantity | int | Quantidade do produto. |
| product.amount | int | O preço do produto. |
| product.name | string | O nome do produto. |
| product.description | string | A descrição do produto. |
| product.imagesRef | array | Urls das imagens do produto. |
| product.membershipFee | int | O valor de entrega. |
| product.isActive | bool | Indica se produto está ativo ou não. |
| product.sku | string | Código identificador do produto. |
| product.merchantId | string | O ID do comerciante. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | Use o Merchant Token para gerar o `accessToken` do ENDPOINT_PORTAL. |
| **merchantId** | {{merchantId}} |
| -- | O número de identificação do comerciante. |

# PIX

Pix é um meio de pagamento criado pelo Banco Central, o Pix é um meio gratuito e seguro de fazer transaferências e pagamentos.

<a id="post-charge-pix"></a>

### `POST` /charge/pix

**Versão** `v2.0`

<a id="requisição-http-17"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/charge/pix
```

> Exemplo de requisição

```ruby
require "uri"
require "json"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/charge/pix")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accesToken}}"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "charge": {
    "merchantChargeId": "TESTE",
    "customer": {
      "name": "Nicolas Anthony da Cunha",
      "email": "nicolasanthonydacunha@teste.com.br",
      "document": "49349151251",
      "documentType": 1,
      "phone": {
        "number": "999999999",
        "countryCode": "55",
        "areaCode": "21",
        "type": 5
      }
    },
    "transactions": [
      {
        "amount": 1000
      }
    ],
    "metadata": [
      {
        "key": "Key_Sample",
        "value": "Value_Sample"
      }
    ],
    "source": 1
  }
})

response = https.request(request)
puts response.read_body
```

```python
import requests
import json

url = "{{ENDPOINT_GATEWAY}}/v2/charge/pix"

payload = json.dumps({
  "charge": {
    "merchantChargeId": "TESTE",
    "customer": {
      "name": "Nicolas Anthony da Cunha",
      "email": "nicolasanthonydacunha@teste.com.br",
      "document": "49349151251",
      "documentType": 1,
      "phone": {
        "number": "999999999",
        "countryCode": "55",
        "areaCode": "21",
        "type": 5
      }
    },
    "transactions": [
      {
        "amount": 1000
      }
    ],
    "metadata": [
      {
        "key": "Key_Sample",
        "value": "Value_Sample"
      }
    ],
    "source": 1
  }
})
headers = {
  'Authorization': 'Bearer {{accesToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/charge/pix' \
--header 'Authorization: Bearer {{accesToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "charge": {
        "merchantChargeId": "TESTE",
        "customer": {
            "name": "Nicolas Anthony da Cunha",
            "email": "nicolasanthonydacunha@teste.com.br",
            "document": "49349151251",
            "documentType": 1,
            "phone": {
                "number": "999999999",
                "countryCode": "55",
                "areaCode": "21",
                "type": 5
            }
        },
        "transactions": [
            {
                "amount": 1000
            }
        ],
        "metadata": [
            {
                "key": "Key_Sample",
                "value": "Value_Sample"
            }
        ],
        "source": 1
    }
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accesToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  charge: {
    merchantChargeId: "TESTE",
    customer: {
      name: "Nicolas Anthony da Cunha",
      email: "nicolasanthonydacunha@teste.com.br",
      document: "49349151251",
      documentType: 1,
      phone: {
        number: "999999999",
        countryCode: "55",
        areaCode: "21",
        type: 5,
      },
    },
    transactions: [
      {
        amount: 1000,
      },
    ],
    metadata: [
      {
        key: "Key_Sample",
        value: "Value_Sample",
      },
    ],
    source: 1,
  },
});

var requestOptions = {
  method: "POST",
  headers: myHeaders,
  body: raw,
  redirect: "follow",
};

fetch("{{ENDPOINT_GATEWAY}}/v2/charge/pix", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
  .catch((error) => console.log("error", error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
  "charge": {
    "merchantChargeId": "TESTE",
    "id": "402d125e-efcb-7890-9282-58191748178d",
    "customerId": "c4d3398d-47fe-43ec-b819-fe341cc5196f",
    "chargeStatus": "PreAuthorized",
    "transactions": [
      {
        "aditumNumber": "397d6cd312314674a9bbdcaf92606594",
        "qrCode": "00020101021226770014BR.GOV.BCB.PIX0136a826e12e-2156-4f61-84d5-efdab324bc160215QRCODE Safrapay520454625303986540510.005802BR5915MORADA DOS PAES6012SP.SAO PAULO62180514SP1086899020216304A11C",
        "qrCodeBase64": "Qk1GTQEAAAAAADYAAAAoAAAAkgAAAJIAAAABACAAAAAAAAAAAADEDgAAxA4AAAAAAAAAAAAA///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////...",
        "transactionId": "4d9debb0-5t6y-11ec-bf19-235a10ca5ed5",
        "paymentType": "Pix",
        "amount": 1000,
        "transactionStatus": "PendingPayment",
        "acquirer": "Safrapay",
        "creationDateTime": "2021-11-24T18:05:51.4486267-03:00",
        "bankIssuerId": "Safra"
      }
    ],
    "nsu": "000000386"
  },
  "success": true,
  "errors": [],
  "traceKey": "176ba227-8u6t-415d-83c8-06ffce194ecb"
}
```

O endpoint responsável por criar um QRCode para transação pix.

🚧 Obs.: Caso o estabelecimento queira receber uma notificação com relação a transação PIX é necessário integrar com o webhook É possível consultar também utilizando o endpoint [GET /charge/{{chargeId}}](cobranca.md#get-charge-chargeid)

<a id="requisição-13"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| charge | object | Sim | Dados da cobrança. |
| charge.merchantChargeId | string | Não | ID de cobrança definido pelo sistema do comerciante. |
| charge.customer | object | Condicional | Dados do comprador. Obrigatório se o `customerId` não estiver presente. |
| charge.customer.id | string | Sim | ID do comprador. |
| charge.customer.name | string | Sim | Nome completo do comprador. |
| charge.customer.email | string | Sim | E-mail do comprador. |
| charge.customer.document | string | Sim | Documento do comprador. |
| charge.customer.documentType | int | Sim | Tipo do documento do comprador. |
| charge.customer.phone | object | Sim | Telefone do comprador. |
| charge.customer.phone.countryCode | string | Sim | Código do país. |
| charge.customer.phone.areaCode | string | Sim | Código de área. |
| charge.customer.phone.number | string | Sim | Número do Telefone. |
| charge.customer.phone.type | int | Sim | Tipo do telefone |
| charge.customer.bankAccount.bankCode | int | Não | Código definido pela FEBRABAN para identificar de forma única uma empresa bancária. |
| charge.customer.bankAccount.bankName | string | Não | O nome do banco. |
| charge.customer.bankAccount.branch | string | Não | Uma agência, centro bancário ou centro financeiro é um local de varejo onde um banco, cooperativa de crédito ou outra instituição financeira (incluindo uma corretora) oferece uma ampla gama de serviços presenciais e automatizados aos seus clientes. |
| charge.customer.bankAccount.branchCheckDigit | string | Não | Dígito de verificação usado para confirmar. |
| charge.customer.bankAccount.account | string | Não | Uma conta bancária é uma conta financeira mantida por um banco para um cliente. Uma conta bancária pode ser uma conta de depósito, uma conta de cartão de crédito, uma conta corrente ou qualquer outro tipo de conta oferecida por uma instituição financeira e representa os fundos que um cliente confiou à instituição financeira e dos quais o cliente pode fazer retiradas. |
| charge.customer.bankAccount.accountCheckDigit | string | Não | Dígito de verificação usado para confirmar. |
| charge.customer.bankAccount.type | string | Não | (Definido pelo banco no tipo de emissor do cartão, define a forma como o cartão e o banco interagem com os fundos de contas bancárias) bankaccounts. |
| charge.customer.bankAccount.isActive | bool | Não | Define se a conta bancária está ativa ou não. |
| charge.customer.isActive | bool | Não | Define se o comprador a está ativo ou não. |
| charge.transactions | array(object) | Sim | Lista com os valores das transações PIX. |
| charge.transactions.amount | int | Sim | O valor da transação do PIX. |
| charge.receivers | array(object) | Não | Lista com informações dos recebedores envolvidos na transação. |
| charge.receivers.id | string | Não | O ID do recebedor. |
| charge.receivers.mdrDiscount | bool | Não | IDs dos receptores envolvidos na cobrança. Isso definirá quem recebe a transação, dividindo o valor total da cobrança em pagamentos separados. |
| charge.receivers.fixedAmountComission | int | Não | Quantia fixa que o recebedor deve receber. |
| charge.receivers.chargeRemainder | bool | Não | Após o processamento dos valores de cada divisão, se sobrar centavos da divisão, este sinalizador indica o destinatário que deve receber os centavos extras. Isso pode ser usado para penny split (exemplo 100/3) ou para quando o destinatário não tem uma regra específica. |
| charge.receivers.percentageComission | float | Não | Essa comissão é calculada sobre o valor da transação, em porcentagem. |
| charge.receivers.mdrComission | float | Não | Percentual relativo ao mdr calculado na liquidação. |
| charge.receivers.membershipComission | float | Não | Comissão percentual para associados da transação. |
| charge.receivers.amount | float | Não | Valor que será enviado ao recebedor. |
| charge.metadata | object | Não | Lista de informações personalizados. |
| charge.metadata.key | string | Não | O nome da chave (campo) |
| charge.metadata.value | string | Não | O valor da chave passada no campo `metadata.key`. |
| charge.source | int | Sim | Define a o tipo da cobrança, POS, PinPad, E-Commerce, Pix etc... |

<a id="resposta-15"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| merchantChargeId | string | O ID de cobrança definido pelo sistema do comerciante. |
| smartCheckoutId | string | O ID do smartCheckout. |
| id | string | O ID da cobrança. |
| nsu | string | O número da transação. |
| customerId | string | O ID do comprador. |
| chargeStatus | int | Status atual da cobrança, indicando em qual estágio do processo de autorização a cobrança está. Ele reflete diretamente todos os status de transação dentro da cobrança. |
| transactions | object | Uma ou várias transações a serem realizadas dentro da cobrança. |
| transactions.amount | int | O valor da transação PIX. |
| transactions.Id | string | O ID da transação PIX. |
| transactions.paymentType | int | Tipo de transação. |
| transactions.acquirer | string | O nome da adquirente. |
| transactions.creationDateTime | string | A data de criação da transação. |
| transactions.bankIssuerId | string | O nome do banco emissor. |
| transactions.aditumNumber | string | O código de identificação gerado pela Safrapay. |
| transactions.qrCode | string | Código do QRCode. |
| transactions.qrCodeBase64 | string | Código do QRCode em Base64. |
| metadata | object | Lista de informações personalizados. |
| metadata.key | string | O nome da chave (campo) |
| metadata.value | string | O valor da chave passada no campo `metadata.key`. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

<a id="body-raw-12"></a>

#### BODY Raw

```http
{
"charge": {
"merchantChargeId": "TASK5333",
"customer": {
"name": "Nicolas Anthony da Cunha",
"email": "nicolasanthonydacunha@teste.com.br",
"document": "49349151251",
"documentType": 1,
"phone": {
"number": "999999999",
"countryCode": "55",
"areaCode": "21",
"type": 5
}
},
"transactions": [
{
"amount": 1000,
}
],
"metadata": [
{
"key": "Key_Sample",
"value": "Value_Sample"
}
],
"source": 1
}
}
```

<a id="como-funciona-o-pix"></a>

### Como funciona o Pix?

O Pix é composto por uma imagem gráfica (QRCode) que armazena os dados de uma conta e sua chave. Também é gerado um código para copiar e colar na hora do pagamento. O recebedor pode definir o valor da transação para o pagador executar o pagamento.

<a id="como-pagar-com-pix"></a>

### Como pagar com Pix?

**1º** Após ser gerado o link de pagamento na plataforma, o cliente irá receber por e-mail, telefone ou whatsapp esse link. Ao acessar o link ele verá a tela inicial do checkout onde será necessário preencher os dados pessoais.

![Inicio Checkout](../assets/img/pix1.png)

**2º** Na tela seguinte, é o momento de selecionar a forma de pagamento sendo, Cartão de Crédito ou Pix.

![Selecionar Pix](../assets/img/pix2.png)

**3º** Selecionando o meio Pix, será gerado o QRCode e o código de Copiar e Colar.

![QRCode e Code Copy&Paste](../assets/img/pix3.png)

**4º** O QRCode tem uma vida útil de 30(trinta) minutos, mas caso o cliente não consiga pagar dentro desse tempo, o mesmo poderá clicar no botão de atualizar que estará em cima do QRCode expirado, ai será gerado um novo QRCode.

![Refresh QRCode](../assets/img/pix4.png)

**5º** Após o pagamento da transação o sistema vai identificar que o link foi pago e irá atualizar demonstrando que foi pago.

![Pagamento Concluido](../assets/img/pix5.png)

<a id="bin"></a>

## Bin

<a id="get-card-bin-brand-bin"></a>

### `GET` /Card/Bin/Brand/{bin}

**Versão** `v1.0`

<a id="requisição-http-18"></a>

#### Requisição HTTP

```http
GET {{ENDPOINT_PORTAL}}/v1/Card/Bin/Brand/{bin}
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_PORTAL}}/v1/Card/Bin/Brand/{{bin}}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_PORTAL}}/v1/Card/Bin/Brand/{{bin}}"

payload={}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location -g --request GET '{{ENDPOINT_PORTAL}}/v1/Card/Bin/Brand/{{bin}}' \
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

fetch("{{ENDPOINT_PORTAL}}/v1/Card/Bin/Brand/{{bin}}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "cardBrand": "Visa",
    "success": true,
    "errors": [],
    "traceKey": "371dc5c9-227f-4937-a02f-03c2b5d0e86b"
}
```

O endpoint responsável por obter a bandeira de um cartão pelo seu BIN.

<a id="requisição-14"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| bin | int | Sim | Os 6 primeiros digítos do cartão. |

<a id="resposta-16"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| cardBrand | string | A bandeira do cartão. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | Use o Merchant Token para gerar o `accessToken` do ENDPOINT_PORTAL. |

| PARAMS | - |
| --- | --- |
| **bin** | {{bin}} |
