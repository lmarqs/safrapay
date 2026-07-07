---
title: "Cartão Protegido"
parent: "Referência da API"
nav_order: 80
layout: "doc"
permalink: "/api/cartao-protegido/"
description: "É uma carteira digital que guarda as informações bancárias, dinheiro depositado, transações financeiras e senhas do usuário."
source: "protectedCard.html"
---

# Cartão Protegido

É uma carteira digital que guarda as informações bancárias, dinheiro depositado, transações financeiras e senhas do usuário.

<a id="cartão"></a>

## Cartão

Cartões que podem vir a ser guardados no sistema com criptografia mostrando apenas os 6 primeiros digitos e os 4 ultimos, possibilitando a utilização do mesmo a qualquer momento.

<a id="post-card"></a>

### `POST` /card

**Versão** `v2.0`

<a id="requisição-http"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/card
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("https://payment-dev.safrapay.com.br/v2/card")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n  \"customerId\": \"ffede3ee-37ab-47bb-9981-d3d14697d69g\",\r\n  \"card\": {\r\n    \"cardNumber\": \"4444585001234562\",\r\n    \"cvv\": \"111\",\r\n    \"brand\": 1,\r\n    \"cardholderName\": \"Renan Soarez\",\r\n    \"cardholderDocument\": \"01234567891\",\r\n    \"expirationMonth\": 12,\r\n    \"expirationYear\": 2026\r\n  }\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "https://payment-dev.safrapay.com.br/v2/card"

payload="{\r\n  \"customerId\": \"ffede3ee-37ab-47bb-9981-d3d14697d69g\",\r\n  \"card\": {\r\n    \"cardNumber\": \"4444585001234562\",\r\n    \"cvv\": \"111\",\r\n    \"brand\": 1,\r\n    \"cardholderName\": \"Renan Soarez\",\r\n    \"cardholderDocument\": \"01234567891\",\r\n    \"expirationMonth\": 12,\r\n    \"expirationYear\": 2026\r\n  }\r\n}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST 'https://payment-dev.safrapay.com.br/v2/card' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "customerId": "ffede3ee-37ab-47bb-9981-d3d14697d69g",
  "card": {
    "cardNumber": "4444585001234562",
    "cvv": "111",
    "brand": 1,
    "cardholderName": "Renan Soarez",
    "cardholderDocument": "01234567891",
    "expirationMonth": 12,
    "expirationYear": 2026
  }
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"customerId":"ffede3ee-37ab-47bb-9981-d3d14697d69g","card":{"cardNumber":"4444585001234562","cvv":"111","brand":1,"cardholderName":"Renan Soarez","cardholderDocument":"01234567891","expirationMonth":12,"expirationYear":2026}});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://payment-dev.safrapay.com.br/v2/card", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "card": {
        "id": "7903ef10-81c3-458d-ad39-9ea9e736e59z",
        "customerId": "ffede3ee-37ab-47bb-9981-d3d14697d69g",
        "cardNumber": "444458******4562",
        "brand": "Visa",
        "cardholderName": "Renan Soarez",
        "cardholderDocument": "01234567891",
        "isPrivateLabel": false,
        "expirationMonth": 12,
        "expirationYear": 2026,
        "brandName": "Visa"
    },
    "success": true,
    "errors": [],
    "traceKey": "48347500-d312-4d3b-aebe-c52f379e0386"
}
```

Endpoint responsável por adicionar um novo cartão à wallet de um comprador.

<a id="requisição"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| customerId | string | Sim | ID exclusivo de cliente. |
| card | object | Sim | Cartão a ser criado no sistema. |
| card.id | string | Não | ID do cartão. |
| card.customerId | string | Não | ID do cliente relacionado ao cartão. |
| card.cardNumber | string | Sim | Primary Account Number (PAN), o número impresso na frente do cartão. |
| card.cvv | string | Sim | Card Verification Value (CVV), recurso de segurança para transações de cartão de pagamento com "ausência de cartão" instituídas para reduzir a incidência de fraude. |
| card.cvvMissingReason | string | Não | Razão pela qual o CVV possa estar faltando na transação, se necessário. Obrigatório apenas para PagSeguro. |
| card.brand | int | Sim | [A bandeira do cartão à qual o imposto se aplica.](../guias/primeiros-passos.md#cardbrand). |
| card.cardHolderName | string | Sim | Nome do títular do cartão. |
| card.cardHolderDocument | string | Sim | Número do documento do títular, CNPJ ou CPF. |
| card.cardToken | string | Não | Token do cartão |
| card.billingAddress | object | Não | Informações do endereço conectado ao cartão de crédito ou débito. As empresas usam o endereço de cobrança para verificar o uso autorizado de tal cartão. É também para onde as empresas enviam contas em papel e extratos bancários. |
| card.billingAddress.street | string | Não | Rua. |
| card.billingAddress.number | string | Não | Número. |
| card.billingAddress.neighborhood | string | Não | Bairro. |
| card.billingAddress.city | string | Não | Cidade. |
| card.billingAddress.state | string | Não | Estado. |
| card.billingAddress.country | string | Não | País. |
| card.billingAddress.zipCode | string | Não | CEP. |
| card.billingAddress.complement | string | Não | Complemento. |
| card.isPrivateLabel | bool | Não | Indica se o cartão é um produto de whitelabel ou não. Whitelabel é um produto ou serviço que uma empresa produz e comercializa com outras empresas que tem interesse em utilizar o mesmo com sua marca estampada. |
| card.expirationMonth | int | Sim | O Mês de expiração do cartão com 2 dígitos. |
| card.expirationYear | int | Sim | O Ano de expiração do cartão com 4 dígitos. |
| card.brandName | string | Não | Nome da bandeira do cartão. |
| card.eci | string | Não | Código de autenticação ECI (Retornado apenas quando a transação passa pelo fluxo do 3DS). |
| card.cavv | string | Não | Criptorgrama de autenticação (Retornado apenas quando a transação passa pelo fluxo do 3DS). |
| card.xid | string | Não | Identificador MPI da transação autenticada. |
| card.cardholderAuthenticationVersion | string | Não | Versão da autentificação retornada pelo provedor. |
| card.metadata | objeto | Não | Armazena todas as credenciais relacionadas a bandeira. |
| card.metadata.additionalProp1 | string | Não | Propriedade adicional. |
| card.metadata.additionalProp2 | string | Não | Propriedade adicional. |
| card.metadata.additionalProp3 | string | Não | Propriedade adicional. |
| card.cardTransactionId | string | Não | ID para a requisição da transação do cartão. |
| card.cof | bool | Não | indica se a transação é COF (Credentials On File). |

<a id="resposta"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| card.id | string | Número de identificação(ID) do cartão. |
| card.customerId | string | ID do cliente. |
| card.cardNumber | string | Número do cartão com criptografia, mostrando apenas os 6 primeiros e os 4 últimos dígitos. |
| card.brand | string | Bandeira do cartão. |
| card.cardHolderName | string | Nome do títular do cartão. |
| card.cardHolderDocument | string | Número do documento do títular, CNPJ ou CPF. |
| card.cardToken | string | Não |
| card.billingAddress | array | É o endereço conectado ao cartão de crédito ou débito. As empresas usam o endereço de cobrança para verificar o uso autorizado de tal cartão. É também para onde as empresas enviam contas em papel e extratos bancários. |
| billingAddress.street | string | Rua. |
| billingAddress.number | string | Número. |
| billingAddress.neighborhood | string | Bairro. |
| billingAddress.city | string | Cidade. |
| billingAddress.state | string | Estado. |
| billingAddress.country | string | País. |
| billingAddress.zipCode | string | CEP. |
| billingAddress.complement | string | Complemento. |
| card.isPrivateLabel | bool | Indica se o cartão é um produto de whitelabel ou não. Whitelabel é um produto ou serviço que uma empresa produz e comercializa com outras empresas que tem interesse em utilizar o mesmo com sua marca estampada. |
| card.expirationMonth | int | O Mês de expiração do cartão com 2 dígitos. |
| card.expirationYear | int | O Ano de expiração do cartão com 4 dígitos. |
| card.fallback | bool | Uma bandeira que informa se a cobrança necessária será feita como fita magnética substituta. |
| card.brandName | string | O nome da bandeira do cartão. |
| success | string | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

<a id="body-raw"></a>

#### BODY Raw

```json
{
  "customerId": "ffede3ee-37ab-47bb-9981-d3d14697d69g",
  "card": {
    "cardNumber": "4444585001234562",
    "cvv": "111",
    "brand": 1,
    "cardholderName": "Renan Soarez",
    "cardholderDocument": "01234567891",
    "expirationMonth": 12,
    "expirationYear": 2026
  }
}
```

<a id="put-card"></a>

### `PUT` /card

**Versão** `v2.0`

<a id="requisição-http-1"></a>

#### Requisição HTTP

```http
PUT {{ENDPOINT_GATEWAY}}/v2/card
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/card")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n  \"card\": {\r\n    \"id\": \"7903ef09-83c3-458d-ad39-9ea9e736e59z\",\r\n    \"customerId\": \"ffede3ee-37ab-47bb-9981-d3d14697d69g\",\r\n    \"cardNumber\": \"4444585001234562\",\r\n    \"cvv\": \"111\",\r\n    \"brand\": \"Visa\",\r\n    \"cardholderName\": \"Renan Soarez\",\r\n    \"cardholderDocument\": \"01234567891\",\r\n    \"isPrivateLabel\": false,\r\n    \"expirationMonth\": 12,\r\n    \"expirationYear\": 2026,\r\n    \"brandName\": \"Visa\"\r\n  }\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/card"

payload="{\r\n  \"card\": {\r\n    \"id\": \"7903ef09-83c3-458d-ad39-9ea9e736e59z\",\r\n    \"customerId\": \"ffede3ee-37ab-47bb-9981-d3d14697d69g\",\r\n    \"cardNumber\": \"4444585001234562\",\r\n    \"cvv\": \"111\",\r\n    \"brand\": \"Visa\",\r\n    \"cardholderName\": \"Renan Soarez\",\r\n    \"cardholderDocument\": \"01234567891\",\r\n    \"isPrivateLabel\": false,\r\n    \"expirationMonth\": 12,\r\n    \"expirationYear\": 2026,\r\n    \"brandName\": \"Visa\"\r\n  }\r\n}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request PUT '{{ENDPOINT_GATEWAY}}/v2/card' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "card": {
    "id": "7903ef09-83c3-458d-ad39-9ea9e736e59z",
    "customerId": "ffede3ee-37ab-47bb-9981-d3d14697d69g",
    "cardNumber": "4444585001234562",
    "cvv": "111",
    "brand": "Visa",
    "cardholderName": "Renan Soarez",
    "cardholderDocument": "01234567891",
    "isPrivateLabel": false,
    "expirationMonth": 12,
    "expirationYear": 2026,
    "brandName": "Visa"
  }
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"card":{"id":"7903ef09-83c3-458d-ad39-9ea9e736e59z","customerId":"ffede3ee-37ab-47bb-9981-d3d14697d69g","cardNumber":"4444585001234562","cvv":"111","brand":"Visa","cardholderName":"Renan Soarez","cardholderDocument":"01234567891","isPrivateLabel":false,"expirationMonth":12,"expirationYear":2026,"brandName":"Visa"}});

var requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/card", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "updatedCard": {
        "id": "7903ef09-83c3-458d-ad39-9ea9e736e59z",
        "customerId": "ffede3ee-37ab-47bb-9981-d3d14697d69g",
        "cardNumber": "444458******4562",
        "isPrivateLabel": false,
        "expirationMonth": 12,
        "expirationYear": 2026
    },
    "success": true,
    "errors": [],
    "traceKey": "7ab17f07-8bcb-4634-b3f5-fca35bcb81c6"
}
```

O endpoint utilizado para atualizar um cartão existente por seu ID. Informações que podem ser atualizadas: ID do cliente, endereço de cobrança e bandeira de marca própria.

<a id="requisição-1"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| customerId | string | Sim | ID exclusivo de cliente. |
| card | object | Sim | Cartão a ser criado no sistema. |
| card.id | string | Não | Número de identificação(ID) do cartão. |
| card.customerId | string | Sim | ID do cliente. |
| card.cardNumber | string | Sim | Primary Account Number (PAN), o número impresso na frente do cartão. |
| card.cvv | string | Sim | Card Verification Value (CVV), recurso de segurança para transações de cartão de pagamento com "ausência de cartão" instituídas para reduzir a incidência de fraude. |
| card.brand | int | Sim | [A bandeira do cartão à qual o imposto se aplica.](../guias/primeiros-passos.md#cardbrand). |
| card.cardHolderName | string | Sim | Nome do títular do cartão. |
| card.cardHolderDocument | string | Sim | Número do documento do títular, CNPJ ou CPF. |
| card.cardToken | string | Não | Token do cartão |
| card.billingAddress | array | Não | É o endereço conectado ao cartão de crédito ou débito. As empresas usam o endereço de cobrança para verificar o uso autorizado de tal cartão. É também para onde as empresas enviam contas em papel e extratos bancários. |
| card.billingAddress.street | string | Não | Rua. |
| card.billingAddress.number | string | Não | Número. |
| card.billingAddress.neighborhood | string | Não | Bairro. |
| card.billingAddress.city | string | Não | Cidade. |
| card.billingAddress.state | string | Não | Estado. |
| card.billingAddress.country | string | Não | País. |
| card.billingAddress.zipCode | string | Não | CEP. |
| card.billingAddress.complement | string | Não | Complemento. |
| card.isPrivateLabel | bool | Sim | Indica se o cartão é um produto de whitelabel ou não. Whitelabel é um produto ou serviço que uma empresa produz e comercializa com outras. |
| card.expirationMonth | int | Sim | O Mês de expiração do cartão com 2 dígitos. |
| card.expirationYear | int | Sim | O Ano de expiração do cartão com 4 dígitos. |

<a id="resposta-1"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| updatedCard.id | string | Número de identificação(ID) do cartão. |
| updatedCardcustomer.Id | string | ID do cliente. |
| updatedCard.cardNumber | string | Número do cartão com criptografia, mostrando apenas os 6 primeiros e os 4 últimos dígitos. |
| updatedCard.brand | string | Bandeira do cartão. |
| updatedCard.cardHolderName | string | Nome do títular do cartão. |
| updatedCard.cardHolderDocument | string | Número do documento do títular, CNPJ ou CPF. |
| updatedCard.cardToken | string | Não |
| updatedCard.billingAddress | array | É o endereço conectado ao cartão de crédito ou débito. As empresas usam o endereço de cobrança para verificar o uso autorizado de tal cartão. É também para onde as empresas enviam contas em papel e extratos bancários. |
| updatedCard.billingAddress.street | string | Rua. |
| updatedCard.billingAddress.number | string | Número. |
| updatedCard.billingAddress.neighborhood | string | Bairro. |
| updatedCard.billingAddress.city | string | Cidade. |
| updatedCard.billingAddress.state | string | Estado. |
| updatedCard.billingAddress.country | string | País. |
| updatedCard.billingAddress.zipCode | string | CEP. |
| updatedCard.billingAddress.complement | string | Complemento. |
| updatedCard.isPrivateLabel | bool | Indica se o cartão é um produto de whitelabel ou não. Whitelabel é um produto ou serviço que uma empresa produz e comercializa com outras empresas que tem interesse em utilizar o mesmo com sua marca estampada. |
| updatedCard.expirationMonth | int | O Mês de expiração do cartão com 2 dígitos. |
| updatedCard.expirationYear | int | O Ano de expiração do cartão com 4 dígitos. |
| updatedCard.fallback | bool | Uma bandeira que informa se a cobrança necessária será feita como fita magnética substituta. |
| updatedCard.brandName | string | O nome da bandeira do cartão. |
| success | string | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

<a id="body-raw-1"></a>

#### BODY Raw

```json
{
  "card": {
    "id": "7903ef09-83c3-458d-ad39-9ea9e736e59z",
    "customerId": "ffede3ee-37ab-47bb-9981-d3d14697d69g",
    "cardNumber": "4444585001234562",
    "cvv": "111",
    "brand": "Visa",
    "cardholderName": "Renan Soarez",
    "cardholderDocument": "01234567891",
    "isPrivateLabel": false,
    "expirationMonth": 12,
    "expirationYear": 2026,
    "brandName": "Visa"
  }
}
```

<a id="get-card"></a>

### `GET` /card

**Versão** `v2.0`

<a id="requisição-http-2"></a>

#### Requisição HTTP

```http
GET {{ENDPOINT_GATEWAY}}/v2/card?id={{cardId}}
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/card?id={{cardId}}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/card?id={{cardId}}"

payload={}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location -g --request GET '{{ENDPOINT_GATEWAY}}/v2/card?id={{cardId}}' \
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

fetch("{{ENDPOINT_GATEWAY}}/v2/card?id={{cardId}}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "card": {
        "id": "7903ef09-83c3-458d-ad39-9ea9e736e59z",
        "customerId": "ffede3ee-37ab-47bb-9981-d3d14697d69a",
        "cardNumber": "444458******4562",
        "isPrivateLabel": false,
        "expirationMonth": 12,
        "expirationYear": 2026
    },
    "success": true,
    "errors": [],
    "traceKey": "929bc149-4d64-4450-b5d1-800d5a4f5449"
}
```

O endpoint utilizado para pesquisar um cartão com base no ID recebido.

<a id="parâmetros-de-query"></a>

#### Parâmetros de query

| Parâmetro | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| id | string | Sim | ID do cartão. |

<a id="resposta-2"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| card.id | string | Número de identificação(ID) do cartão. |
| card.customerId | string | ID do cliente. |
| card.cardNumber | string | Número do cartão com criptografia, mostrando apenas os 6 primeiros e os 4 últimos dígitos. |
| card.brand | string | Bandeira do cartão. |
| card.cardHolderName | string | Nome do títular do cartão. |
| card.cardHolderDocument | string | Número do documento do títular, CNPJ ou CPF. |
| card.cardToken | string | Token de cartão. |
| card.billingAddress | array | É o endereço conectado ao cartão de crédito ou débito. As empresas usam o endereço de cobrança para verificar o uso autorizado de tal cartão. É também para onde as empresas enviam contas em papel e extratos bancários. |
| billingAddress.street | string | Rua. |
| billingAddress.number | string | Número. |
| billingAddress.neighborhood | string | Bairro. |
| billingAddress.city | string | Cidade. |
| billingAddress.state | string | Estado. |
| billingAddress.country | string | País. |
| billingAddress.zipCode | string | CEP. |
| billingAddress.complement | string | Complemento. |
| card.isPrivateLabel | bool | Indica se o cartão é um produto de whitelabel ou não. Whitelabel é um produto ou serviço que uma empresa produz e comercializa com outras empresas que tem interesse em utilizar o mesmo com sua marca estampada. |
| card.expirationMonth | int | O Mês de expiração do cartão com 2 dígitos. |
| card.expirationYear | int | O Ano de expiração do cartão com 4 dígitos. |
| card.fallback | bool | Uma bandeira que informa se a cobrança necessária será feita como fita magnética substituta. |
| card.brandName | string | O nome da bandeira do cartão. |
| success | string | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

| PARAMS | - |
| --- | --- |
| **Id** | {{cardId}} |
| -- | Número de identificação do cartão. |

<a id="get-card-bycustomer"></a>

### `GET` /card/byCustomer

**Versão** `v2.0`

<a id="requisição-http-3"></a>

#### Requisição HTTP

```http
GET {{ENDPOINT_GATEWAY}}/v2/card/byCustomer?id={{customerId}}
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/card/byCustomer?id={{customerId}}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/card/byCustomer?id={{customerId}}"

payload={}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request GET '{{ENDPOINT_GATEWAY}}/v2/card/byCustomer?id={{customerId}}' \
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

fetch("{{ENDPOINT_GATEWAY}}/v2/card/byCustomer?id={{customerId}}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "cards": [
        {
            "id": "7903ef09-83c3-458d-ad39-9ea9e736e59z",
            "customerId": "ffede3ee-37ab-47bb-9981-d3d14697d69a",
            "cardNumber": "444458******4562",
            "brand": "Visa",
            "cardholderName": "Renan Soarez",
            "cardholderDocument": "01234567891",
            "isPrivateLabel": false,
            "expirationMonth": 12,
            "expirationYear": 2026,
            "brandName": "Visa"
        }
    ],
    "success": true,
    "errors": [],
    "traceKey": "e693cdb5-47d2-4fae-8670-bba1f8568d21"
}
```

O endpoint utilizado para pesquisar todos os cartões relacionados a um cliente com base em seu ID.

<a id="parâmetros-de-query-1"></a>

#### Parâmetros de query

| Parâmetro | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| id | string | Sim | ID do cliente. |

<a id="resposta-3"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| card.id | string | Número de identificação(ID) do cartão. |
| card.customerId | string | ID do cliente. |
| card.cardNumber | string | Número do cartão com criptografia, mostrando apenas os 6 primeiros e os 4 últimos dígitos. |
| card.brand | string | Bandeira do cartão. |
| card.cardHolderName | string | Nome do títular do cartão. |
| card.cardHolderDocument | string | Número do documento do títular, CNPJ ou CPF. |
| card.cardToken | string | Token de cartão. |
| card.billingAddress | array | É o endereço conectado ao cartão de crédito ou débito. As empresas usam o endereço de cobrança para verificar o uso autorizado de tal cartão. É também para onde as empresas enviam contas em papel e extratos bancários. |
| billingAddress.street | string | Rua. |
| billingAddress.number | string | Número. |
| billingAddress.neighborhood | string | Bairro. |
| billingAddress.city | string | Cidade. |
| billingAddress.state | string | Estado. |
| billingAddress.country | string | País. |
| billingAddress.zipCode | string | CEP. |
| card.isPrivateLabel | bool | Indica se o cartão é um produto de whitelabel ou não. Whitelabel é um produto ou serviço que uma empresa produz e comercializa com outras empresas que tem interesse em utilizar o mesmo com sua marca estampada. |
| card.expirationMonth | int | O Mês de expiração do cartão com 2 dígitos. |
| card.expirationYear | int | O Ano de expiração do cartão com 4 dígitos. |
| card.fallback | bool | Uma bandeira que informa se a cobrança necessária será feita como fita magnética substituta. |
| card.brandName | string | O nome da bandeira do cartão. |
| success | string | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

| PARAMS | - |
| --- | --- |
| **Id** | {{customerId}} |
| -- | Número de identificação do cliente. |

<a id="delete-card-cardid"></a>

### `DELETE` /card/{cardId}

**Versão** `v2.0`

<a id="requisição-http-4"></a>

#### Requisição HTTP

```http
DELETE {{ENDPOINT_GATEWAY}}/v2/card/{cardId}
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/card/{{cardId}}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/card/{{cardId}}"

payload={}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request DELETE '{{ENDPOINT_GATEWAY}}/v2/card/{{cardId}}' \
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

fetch("{{ENDPOINT_GATEWAY}}/v2/card/{{cardId}}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "success": true,
    "errors": [],
    "traceKey": "string"
}
```

O endpoint utilizado para deletar um cartão com base em seu ID.

<a id="parâmetro-de-rota"></a>

#### Parâmetro de rota

| Parâmetro | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| id | string | Sim | ID do cartão. |

<a id="resposta-4"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| success | string | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

<a id="cartão-temporário"></a>

## Cartão Temporário

Um cartão que é criado temporáriamente, podendo ser utilizado dentro de um período de 5 minutos.

<a id="post-temporary-card"></a>

### `POST` /temporary/card

**Versão** `v2.0`

<a id="requisição-http-5"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/temporary/card
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/temporary/card")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n  \"brand\": 1,\r\n  \"cardNumber\": \"4444585001234562\",\r\n  \"cardholderName\": \"Renan Soarez\",\r\n  \"cardholderDocument\": \"01234567891\",\r\n  \"expirationMonth\": 12,\r\n  \"expirationYear\": 2026,\r\n  \"cvv\": \"111\"\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/temporary/card"

payload="{\r\n  \"brand\": 1,\r\n  \"cardNumber\": \"4444585001234562\",\r\n  \"cardholderName\": \"Renan Soarez\",\r\n  \"cardholderDocument\": \"01234567891\",\r\n  \"expirationMonth\": 12,\r\n  \"expirationYear\": 2026,\r\n  \"cvv\": \"111\"\r\n}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/temporary/card' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "brand": 1,
  "cardNumber": "4444585001234562",
  "cardholderName": "Renan Soarez",
  "cardholderDocument": "01234567891",
  "expirationMonth": 12,
  "expirationYear": 2026,
  "cvv": "111"
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"brand":1,"cardNumber":"4444585001234562","cardholderName":"Renan Soarez","cardholderDocument":"01234567891","expirationMonth":12,"expirationYear":2026,"cvv":"111"});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/temporary/card", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "cardToken": "card_0CLtvaYy2UgPN2U4Mq8UQqYZnxdxnhVc",
    "success": true,
    "errors": [],
    "traceKey": "ddf2f808-2ce1-4d8a-88e4-1982b5ae7d8a"
}
```

O endpoint utilizado para criar um novo cartão temporário.

<a id="requisição-2"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| brand | int | Sim | [A bandeira do cartão à qual o imposto se aplica.](../guias/primeiros-passos.md#cardbrand). |
| cardNumber | string | Sim | O número impresso na frente do cartão. |
| cardholderName | string | Sim | O nome do títular do cartão. |
| cardholderDocument | string | Sim | O documento do títular do cartão. |
| expirationMonth | int | Sim | O Mês de expiração do cartão com 2 dígitos. |
| expirationYear | int | Sim | O Ano de expiração do cartão com 4 dígitos. |
| cvv | string | Sim | Card Verification Value (CVV), recurso de segurança para transações de cartão de pagamento com "ausência de cartão" instituídas para reduzir a incidência de fraude. |
| billingAddress | object | Não | Informações do endereço conectado ao cartão de crédito ou débito. As empresas usam o endereço de cobrança para verificar o uso autorizado de tal cartão. É também para onde as empresas enviam contas em papel e extratos bancários. |
| billingAddress.street | string | Não | Rua. |
| billingAddress.number | string | Não | Número. |
| billingAddress.neighborhood | string | Não | Bairro. |
| billingAddress.city | string | Não | Cidade. |
| billingAddress.state | string | Não | Estado. |
| billingAddress.country | string | Não | País. |
| billingAddress.zipCode | string | Não | CEP. |
| billingAddress.complement | string | Não | Complemento. |

<a id="resposta-5"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| success | string | Se o endpoint processou a requisição com sucesso. |
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

```json
{
  "brand": 1,
  "cardNumber": "4444585001234562",
  "cardholderName": "Renan Soarez",
  "cardholderDocument": "01234567891",
  "expirationMonth": 12,
  "expirationYear": 2026,
  "cvv": "111"
}
```

<a id="zero-dollar"></a>

## Zero Dollar

As transações de Verificação de Cartão, também conhecidas como Autorizações Zero Dólar, são transações não financeiras, que não têm impacto no limite disponibilizado pelo Emissor ao Portador, e permitem a verificação de que o cartão é válido e apto a realizar transações.

<a id="post-card-validation-zerodollar"></a>

### `POST` /card/validation/zerodollar

**Versão** `v2.0`

<a id="requisição-http-6"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/card/validation/zerodollar
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/card/validation/zerodollar")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n \"brand\": 1,\r\n \"cardId\": \"2d13a4f4-fae6-4c82-a45f-2c7458265312\",\r\n \"customerId\": \"0a273474-1755-4eaa-adb8-70e55cb014c2\",\r\n \"cardNumber\": \"4444585001234562\",\r\n \"cardholderName\": \"Renan Soarez\",\r\n \"cardholderDocument\": \"01234567891\",\r\n \"expirationMonth\": 12,\r\n \"expirationYear\": 2026,\r\n \"cvv\": \"111\"\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/card/validation/zerodollar"

payload="{\r\n \"brand\": 1,\r\n \"cardId\": \"2d13a4f4-fae6-4c82-a45f-2c7458265312\",\r\n \"customerId\": \"0a273474-1755-4eaa-adb8-70e55cb014c2\",\r\n \"cardNumber\": \"4444585001234562\",\r\n \"cardholderName\": \"Renan Soarez\",\r\n \"cardholderDocument\": \"01234567891\",\r\n \"expirationMonth\": 12,\r\n  \"expirationYear\": 2026,\r\n \"cvv\": \"111\"\r\n}"

headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/card/validation/zerodollar' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "brand": 1,
  "cardId": "2d13a4f4-fae6-4c82-a45f-2c7458265312",
  "customerId": "0a273474-1755-4eaa-adb8-70e55cb014c2",
  "cardNumber": "4444585001234562",
  "cardholderName": "Renan Soarez",
  "cardholderDocument": "01234567891",
  "expirationMonth": 12,
  "expirationYear": 2026,
  "cvv": "111"
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"brand":1,"cardId":"2d13a4f4-fae6-4c82-a45f-2c7458265312","cardNumber":"4444585001234562","cardholderName":"Renan Soarez","cardholderDocument":"01234567891","expirationMonth":12,"expirationYear":2026,"cvv":"111"});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/card/validation/zerodollar", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "authorization": "007480",
    "nsu": "020006454677",
    "acquirerErrorCode": "00",
    "acquirerErrorMessage": "00 - Aprovada",
    "isValid": true,
    "acquirer": "Safrapay",
    "cardId": "25743acc-3aa1-470f-803d-0024c8d46bbc",
    "cardToken": "card_0CLtvaYy2UgPN2U4Mq8UQqYZnxdxnhVc",
    "success": true,
    "errors": [],
    "traceKey": "ddf2f808-2ce1-4d8a-88e4-1982b5ae7d8a"
}
```

O endpoint verifica se o cartão é válido e apto à realizar transações.

<a id="requisição-3"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| brand | int | Não | Identificação da marca do cartão. Opcional quando você tem cartão de identificação. |
| cardId | string | Não | ID do cartão obtido ao salvar o cartão na carteira SafraPay. Opcional se o cartão já estiver salvo no SafraPay. |
| customerId | string | Sim | Identifica um cliente no sistema SafraPay. |
| cardNumber | string | Não | Número de conta primária do cartão (PAN), também conhecido como o número impresso na frente do cartão. Opcional quando você tem cartão de identificação. |
| cardholderName | string | Não | Nome do titular do cartão impresso na frente do cartão. Opcional quando você tem cartão de identificação. |
| cardholderDocument | string | Não | Identificação legal do titular do cartão, como CPF, RG ou CNPJ. Opcional quando você tem cartão de identificação. |
| expirationMonth | int | Não | Mês de vencimento do cartão com 2 dígitos. Formato MM. Opcional quando você tem cartão de identificação. |
| expirationYear | int | Não | Ano de expiração do cartão com 4 dígitos. Formato aaaa. Opcional quando você tem cartão de identificação. |
| cvv | string | Não | O Card Verification Value (CVV) é um recurso de segurança para transações com cartão de pagamento "cartão não presente" instituído para reduzir a incidência de fraudes de cartão de crédito. Consiste em um número de 3-4 dígitos impresso no cartão. Opcional quando você tem cartão de identificação. |
| cardType | int | Não | Tipo do cartão como crédito, débito ou voucher. Opcional quando já se tem o ID do cartão. |

<a id="resposta-6"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| authorization | string | Código de autorização. |
| nsu | string | Identificador do pedido (Safrapay). |
| acquirerErrorCode | string | Código de erro da adquirente. |
| acquirerErrorMessage | string | Mensagem proveniente da adquirente. |
| isValid | bool | Um booleano que sinaliza se o cartão tem permissão para processar a transação. |
| acquirer | string | Nome da adquirente. |
| cardId | string | Identificação do cartão. |
| success | string | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

<a id="body-raw-3"></a>

#### BODY Raw

```json
{
  "brand": 1,
  "customerId": "0a273474-1755-4eaa-adb8-70e55cb014c2",
  "cardId": "2d13a4f4-fae6-4c82-a45f-2c7458265312",
  "cardNumber": "5152786439456756",
  "cardholderName": "Renan Soarez",
  "cardholderDocument": "01234567891",
  "expirationMonth": 12,
  "expirationYear": 2026,
  "cvv": "111"
}
```
