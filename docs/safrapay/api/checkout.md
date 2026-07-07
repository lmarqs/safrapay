---
title: "Checkout"
parent: "Referência da API"
nav_order: 40
layout: "doc"
permalink: "/api/checkout/"
description: "Checkout é a última etapa do processo de vendas em uma loja virtual. Nesse momento, o comprador já selecionou os produtos, inseriu informações referentes à fret"
source: "checkout.html"
---

# CHECKOUT

Checkout é a última etapa do processo de vendas em uma loja virtual. Nesse momento, o comprador já selecionou os produtos, inseriu informações referentes à frete (se houver entrega) e agora deseja pagar pelos produtos a serem adquiridos.

A diferença entre o checkout e o link de pagamentos é que no checkout, o comprador está autenticado em uma loja virtual. O link de pagamentos, por sua vez, é público e não necessita de autenticação. Por isso, no checkout é possível visualizar a wallet de cartões do comprador, enquanto no link de pagamentos isso não é possível.

Na Safrapay, existem 3 formas principais de integração com o checkout:

Checkout transparente: para o cliente final, não existirá diferença visual entre a loja virtual e a página de inserção dos dados do cartão. Para isso, o integrador deve usar a nossa SDK de checkout transparente.

Checkout redirect: o cliente final será redirecionado à uma página de checkout white-label da Safrapay, onde a logo e cores do cliente serão usadas.

> **💡 Integração com Device Fingerprint e RemoteIp:**
>
> Para melhorar a análise de risco e prevenção de fraudes, especialmente quando o antifraude estiver ativo:
>
> 1. **Device Fingerprint (Obrigatório com Antifraude):** Implemente o script de coleta na página de checkout
> 2. **RemoteIp (Opcional mas Recomendado):** Forneça o IP do comprador quando disponível no campo `remoteIp`
>
> 📖 Consulte a [documentação do Device Fingerprint e SDK SafraPay Antifraud](../guias/antifraude.md#device-fingerprint) e [Serviço de Antifraude](../guias/antifraude.md) para mais detalhes.

<a id="post-smartcheckout"></a>

### `POST` /smartcheckout

**Versão** `v2.0`

<a id="requisição-http"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/smartcheckout
```

> Exemplo de requisição (`Plano`)

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/smartcheckout")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n   \"planId\": \"932168be-46b8-45d3-80f1-45cdd0cd7d6a\",\r\n   \"customer\": {\r\n        \"name\": \"Jorge Felipe\",\r\n        \"email\": \"jorginho.felps@email.com.br\",\r\n        \"document\": \"01234567891\",\r\n        \"phone\": {\r\n            \"countryCode\": \"+55\",\r\n            \"areaCode\": \"21\",\r\n            \"number\": \"999999999\",\r\n            \"type\": 5\r\n        }\r\n    }\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/smartcheckout"

payload="{\r\n   \"planId\": \"932168be-46b8-45d3-80f1-45cdd0cd7d6a\",\r\n   \"customer\": {\r\n        \"name\": \"Jorge Felipe\",\r\n        \"email\": \"jorginho.felps@email.com.br\",\r\n        \"document\": \"01234567891\",\r\n        \"phone\": {\r\n            \"countryCode\": \"+55\",\r\n            \"areaCode\": \"21\",\r\n            \"number\": \"999999999\",\r\n            \"type\": 5\r\n        }\r\n    }\r\n}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/smartcheckout' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
   "planId": "932168be-46b8-45d3-80f1-45cdd0cd7d6a",
   "customer": {
        "name": "Jorge Felipe",
        "email": "jorginho.felps@email.com.br",
        "document": "01234567891",
        "phone": {
            "countryCode": "+55",
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

var raw = JSON.stringify({"planId":"932168be-46b8-45d3-80f1-45cdd0cd7d6a","customer":{"name":"Jorge Felipe","email":"jorginho.felps@email.com.br","document":"01234567891","phone":{"countryCode":"+55","areaCode":"21","number":"999999999","type":5}}});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/smartcheckout", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> Exemplo de requisição (`Valor Avulso`)

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/smartcheckout")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n  \"amount\": 1000,\r\n  \"description\": \"Descrição do Link\",\r\n  \"emailNotification\": \"jorginho.felps@email.com.br\",\r\n  \"phoneNotification\": \"21999999999\"\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/smartcheckout"

payload="{\r\n  \"amount\": 1000,\r\n  \"description\": \"Descrição do Link\",\r\n  \"emailNotification\": \"jorginho.felps@email.com.br\",\r\n  \"phoneNotification\": \"21999999999\"\r\n}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/smartcheckout' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "amount": 1000,
  "description": "Descrição do Link",
  "emailNotification": "jorginho.felps@email.com.br",
  "phoneNotification": "21999999999"
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"amount":1000,"description":"Descrição do Link","emailNotification":"jorginho.felps@email.com.br","phoneNotification":"21999999999"});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/smartcheckout", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> Exemplo de requisição (`Produtos`)

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/smartcheckout")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n    \"emailNotification\": \"jorginho.felps@email.com.br\",\r\n    \"phoneNotification\": \"21999999999\",\r\n    \"newProducts\": {\r\n        \"merchantId\": \"e4a78487-ac6d-4d18-8312-934399d70616\",\r\n        \"products\": [\r\n            {\r\n                \"name\": \"Maçã\",\r\n                \"amount\": 500,\r\n                \"sku\": \"SKU_MACA\",\r\n                \"isActive\": true\r\n            }\r\n        ]\r\n    }\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/smartcheckout"

payload="{\r\n    \"emailNotification\": \"jorginho.felps@email.com.br\",\r\n    \"phoneNotification\": \"21999999999\",\r\n    \"newProducts\": {\r\n        \"merchantId\": \"e4a78487-ac6d-4d18-8312-934399d70616\",\r\n        \"products\": [\r\n            {\r\n                \"name\": \"Maçã\",\r\n                \"amount\": 500,\r\n                \"sku\": \"SKU_MACA\",\r\n                \"isActive\": true\r\n            }\r\n        ]\r\n    }\r\n}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/smartcheckout' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "emailNotification": "jorginho.felps@email.com.br",
    "phoneNotification": "21999999999",
    "newProducts": {
        "merchantId": "e4a78487-ac6d-4d18-8312-934399d70616",
        "products": [
            {
                "name": "Maçã",
                "amount": 500,
                "sku": "SKU_MACA",
                "isActive": true
            }
        ]
    }
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"emailNotification":"jorginho.felps@email.com.br","phoneNotification":"21999999999","newProducts":{"merchantId":"e4a78487-ac6d-4d18-8312-934399d70616","products":[{"name":"Maçã","amount":500,"sku":"SKU_MACA","isActive":true}]}});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/smartcheckout", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

> Resposta (`Plano`)

```json
{
    "id": "50025917-afac-4d16-9b5f-982840064591",
    "smartCheckoutUrl": "/v2/checkout/50025917-afac-4d16-9b5f-982840064591?signinToken=eyJhbHciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MjQwMzIwOTQsImlzcyI6IkFkaXR1bSIsImF1ZCI6IndhbGxldCJ9.QzuLYDtGOcjwH6-jc7UFEHo_iTWqYVM9yvQfHirfNmw",
    "success": true,
    "errors": [],
    "traceKey": "17139692-d012-441d-bb34-fa4007383ba2"
}
```

> Resposta (`Valor Avulso`)

```json
{
    "id": "84e6e7c9-d56d-4418-bd82-cdbb92c0302a",
    "smartCheckoutUrl": "/v2/checkout/84e6e7c9-d56d-4418-bd82-cdbb92c0302a?signinToken=eyJhbHciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MjQwMzE5MjQsImlzcyI6IkFkaXR1bSIsImF1ZCI6IndhbGxldCJ9.tlusUUQaRK8Fsnk_-EYJl05mr7IXhEnDTzmiptuKWaY",
    "success": true,
    "errors": [],
    "traceKey": "f6c98b33-a433-4686-b463-5267d6aa73dd"
}
```

> Resposta (`Produtos`)

```json
{
    "id": "2efa5041-3c12-47e7-bc89-d1b34cb806ab",
    "smartCheckoutUrl": "/v2/checkout/2efa5041-3c12-47e7-bc89-d1b34cb806ab?signinToken=eyJhbHciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MjQwMzE3NzYsImlzcyI6IkFkaXR1bSIsImF1ZCI6IndhbGxldCJ9.RLXiLOu2fNVqErAilrfdh4lpY9OqxO38Y7WNBoUWEzY",
    "products": [
        {
            "amount": 500,
            "name": "Maçã",
            "quantity": 1,
            "id": "4a60763a-9912-49df-98c9-8bb813e6a885",
            "sku": "SKU_MACA"
        }
    ],
    "success": true,
    "errors": [],
    "traceKey": "d00525ff-f58c-41ee-8849-4e598404d1c7"
}
```

O endpoint responsável por criar um checkout.

<a id="requisição"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| amount | int | Condicional | Valor a ser cobrado. Obrigatório se o checkout / link de pagamento não possui produto(s). |
| orderCode | string | Não | Código ou descrição enviado pelo lojista pra identificar o link de pagamento/checkout. |
| description | string | Não | Descrição do checkout / link de pagamento. |
| planId | string | Sim | Se o link de pagamento é para fins de assinatura. |
| remoteIp | string | Sim | **\[OBRIGATÓRIO quando antifraude ativo\]** O endereço IP do comprador. Este dado é fundamental para análises de risco mais precisas. Suporta IPv4 (exemplo: `192.168.1.100`). Consulte [documentação completa](../guias/antifraude.md#campo-remoteip-complemento-ao-device-fingerprint). |
| customer | object | Sim | Dados do comprador. |
| customer.id | string | Não | ID do comprador. |
| customer.name | string | Sim | Nome completo do comprador. |
| customer.email | string | Sim | E-mail do comprador. |
| customer.entityType | entityType | Sim | [Se é pessoa física ou jurídica](../guias/primeiros-passos.md#entitytype) |
| customer.documentType | documentType | Sim | [Tipo do documento do comprador](../guias/primeiros-passos.md#documenttype) |
| customer.document | string | Sim | Documento do comprador. |
| customer.birthday | date | Não | Data de nascimento do comprador. |
| customer.gender | Gender | Não | [Gênero do comprador.](../guias/primeiros-passos.md#gender) |
| customer.phone | object | Sim | Telefone do comprador. |
| customer.phone.countryCode | string | Sim | Código do país. |
| customer.phone.areaCode | string | Sim | Código de área. |
| customer.phone.number | string | Sim | Número do Telefone. |
| customer.phone.type | PhoneType | Sim | [Tipo do telefone.](../guias/primeiros-passos.md#phone) |
| customer.address | object | Sim | Endereço do comprador. |
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
| customer.bankAccounts.bankName | string | Sim | Nome do banco. |
| customer.bankAccounts.branch | string | Sim | Filial. |
| customer.bankAccounts.branchCheckDigit | string | Sim | Dígito de verificação da filial. |
| customer.bankAccounts.account | string | Sim | Conta bancária. |
| customer.bankAccounts.accountCheckDigit | string | Sim | Dígito de verificação da conta bancária. |
| customer.bankAccounts.type | int | Sim | Tipo de conta. |
| customer.bankAccounts.isActive | bool | Sim | Se a conta está ativa ou não. |
| customer.isActive | bool | Não | Se o comprador está ativo ou não. |
| products | array(string) | Não | ID dos produtos vendidos no checkout / link de pagamentos. |
| emailNotification | string | Não | E-mail do comprador. Se preenchido, será enviado link para pagamento por e-mail. |
| phoneNotification | string | Não | Telefone do comprador. Se preenchido, será enviado link para pagamento por SMS. |
| paymentSupportedTypes | array(int) | Não | Meios de pagamento permitidos no checkout. Cada item do array é um valor inteiro do enum **`PaymentType`** (ver [guia de acesso](../guias/primeiros-passos.md#paymenttype)). O comprador só poderá pagar por um dos tipos informados. |
| discount | int | Não | Desconto no pagamento em centavos. |
| shippingAmount | int | Não | Valor do frete em centavos. |
| hostUrl | string | Não | URL de origem. Utilizado para customizar a logo no e-mail com link para pagamento. |
| shippingAddress | Address | Não | Endereço de entrega dos produtos. |
| shippingAddress.street | string | Sim | Rua. |
| shippingAddress.number | string | Sim | Número. |
| shippingAddress.neighborhood | string | Sim | Bairro. |
| shippingAddress.city | string | Sim | Cidade. |
| shippingAddress.state | string | Sim | Estado. |
| shippingAddress.country | string | Sim | País. |
| shippingAddress.zipCode | string | Sim | CEP. |
| shippingAddress.complement | string | Sim | Complemento. |
| newProducts | NewProducts | Não | Produtos a serem cadastrados e vendidos no checkout / link de pagamentos. **Importante: Os produtos nesse objeto também podem já ter sido cadastrados, porém seus IDs são desconhecidos. Nesse caso, a estrutura do produto deve ser reenviada utilizando o SKU original**. |
| newProducts.merchantId | string | Sim | ID da loja dona dos produtos cadastrados. |
| newProducts.products | array(object) | Sim | Informação dos produtos cadastrados. |
| newProducts.products.name | string | Sim | Nome do produto, campo livre. |
| newProducts.products.description | string | Não | Descrição do produto, campo livre. |
| newProducts.products.imagesRef | array(string) | Não | URLs de Imagens relacionados ao produto, string deve ser URL válida. |
| newProducts.products.amount | string | Sim | Valor do produto em centavos. |
| newProducts.products.sku | string | Sim | Identificador único do produto na loja. Não é permitido valor duplicado. |
| newProducts.products.isActive | bool | Não | Se o produto está disponível na loja. Default `false`. |
| newProducts.userId | string | Não | O usuário que está inserindo o produto no banco de dados. |
| expiration | date | Não | Data de expiração do checkout / link de pagamento. Valor default próximo dia (+ 24 horas). |
| maxInstallmentNumber | int | Não | Número máximo de parcelas suportadas pelo checkout / link de pagamentos. Valor default 12. |
| minInstallmentAmount | int | Não | Valor mínimo por parcela. Valor default ilimitado. |
| limitApprovedCharges | int | Não | Número limite de transações aprovadas para o checkout / link de pagamentos. Valor default ilimitado. |
| primaryColor | string | Não | RGB da cor primária da loja. Utilizado para customizar o tema do e-mail com o link para pagamento. |
| secondaryColor | string | Não | RGB da cor secundária da loja. Utilizado para customizar o tema do e-mail com o link para pagamento. |
| installmentNumber | int | Não | Número **exato** de parcelas suportado pelo checkout / link de pagamentos. Se esse valor for recebido, `maxInstallmentNumber` é ignorado. Se não for enviado, será considerado apenas o `maxInstallmentNumber`. |
| limitDeniedCharges | int | Não | Número limite de transações negadas para o checkout / link de pagamentos. Valor default ilimitado. |
| customTemplate | string | Não | Identificador do layout a ser exibido na URL do checkout / link de pagamentos. Se não for enviado, será usado o template default. |
| documentSupportedTypes | array(int) | Não | Os tipos de documentos que o link de pagamento suporta. |
| supportMultipleTransactions | bool | Não | Indica se o link de pagamento suporta múltiplos cartões para um pagamento. Valor padrão sempre será "false". |

<a id="resposta"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| id | string | ID do checkout / link de pagamento criado. |
| smartCheckoutUrl | string | URI que deverá ser utilizada em conjunto com uma URL base para acessar a tela de pagamentos. |
| products | Product\[\] | Lista de produtos criados, se houve algum novo produto na criação do checkout / link de pagamento. |
| products.name | string | Sim |
| products.description | string | Não |
| products.imagesRef | string\[\] | Não |
| products.amount | string | Sim |
| products.sku | string | Sim |
| products.isActive | bool | Não |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Não |
| errors.message | string | Não |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

<a id="body-raw"></a>

#### BODY Raw

***Plano***

```http
{
"planId": "932168be-46b8-45d3-80f1-45cdd0cd7d6a",
"customer": {
"name": "Jorge Felipe",
"email": "jorginho.felps@email.com.br",
"document": "01234567891",
"phone": {
"countryCode": "+55",
"areaCode": "21",
"number": "999999999",
"type": 5
}
}
}
```

***Valor Avulso***

```http
{
"amount": 1000,
"description": "Descrição do Link",
"emailNotification": "jorginho.felps@email.com.br",
"phoneNotification": "21999999999"
}
```

***Produtos***

```http
{
"emailNotification": "jorginho.felps@email.com.br",
"phoneNotification": "21999999999",
"newProducts": {
"merchantId": "e4a78487-ac6d-4d18-8312-934399d70616",
"products": [
{
"name": "Maçã",
"amount": 500,
"sku": "SKU_MACA",
"isActive": true
}
]
}
}
```

<a id="get-smartcheckout-smartcheckoutid-detail-checkout"></a>

### `GET` /smartcheckout/{smartcheckoutId}/detail Checkout

**Versão** `v1.0`

<a id="requisição-http-1"></a>

#### Requisição HTTP

```http
GET {{ENDPOINT_GATEWAY}}/v2/smartcheckout/{smartcheckoutId}/detail
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/smartcheckout/{{smartCheckoutId}}/detail")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Get.new(url)
request["MerchantId"] = "{{merchantId}}"
request[""] = ""
request["Authorization"] = "Bearer {{accessToken}}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/smartcheckout/{{smartCheckoutId}}/detail"

payload={}
headers = {
  'MerchantId': '{{merchantId}}',
  '': '',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location -g --request GET '{{ENDPOINT_GATEWAY}}/v2/smartcheckout/{{smartCheckoutId}}/detail' \
--header 'MerchantId: {{merchantId}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("MerchantId", "{{merchantId}}");
myHeaders.append("", "");
myHeaders.append("Authorization", "Bearer {{accessToken}}");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/smartcheckout/{{smartCheckoutId}}/detail", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "smartCheckout": {
        "creationDate": "2021-06-18T16:16:25.956",
        "id": "5c233e94-ea21-438b-95e5-ed38df758534",
        "amount": 1000,
        "description": "Descrição do Link",
        "paymentSupportedTypes": [
            "Credit"
        ],
        "discount": 0,
        "expiration": "2021-06-19T16:16:25.956",
        "limitApprovedCharges": 1,
        "type": 1,
        "status": 1,
        "limitDeniedCharges": 5,
        "charges": []
    },
    "success": true,
    "errors": [],
    "traceKey": "77a5ce37-fb8e-46c8-92e9-761b1964af3b"
}
```

Endpoint responsável por obter as informações sobre um link de pagamentos ou checkout, incluindo as cobranças efetuadas, se houver alguma.

<a id="requisição-1"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| smartcheckoutId | string | Sim | Número de identificação da cobrança. |

<a id="resposta-1"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| creationDate | string | Data de criação do smartCheckout. |
| id | string | ID do smartCheckout. |
| amount | int | O valor do smartCheckout. |
| description | string | A descrição do smartCheckout. |
| paymentSupportedTypes | string | Lista dos tipos de pagamento suportados; os valores correspondem ao enum **`PaymentType`** ([guia de acesso](../guias/primeiros-passos.md#paymenttype)). |
| discount | int | O valor do disconto. |
| shippingAmount | int | O valor do frete. |
| maxInstallmentNumber | int | O número máximo de prestações. |
| expiration | string | Data de expiração do smartCheckout. |
| shippingAddress | Address | Endereço de entrega dos produtos. |
| shippingAddress.street | string | Rua. |
| shippingAddress.number | string | Número. |
| shippingAddress.neighborhood | string | Bairro. |
| shippingAddress.city | string | Cidade. |
| shippingAddress.state | string | Estado. |
| shippingAddress.country | string | País. |
| shippingAddress.zipCode | string | CEP. |
| shippingAddress.complement | string | Complemento. |
| limitApprovedCharges | int | O limite de cobranças aprovadas. |
| productsDetail | ProductDetail | Detalhes dos produtos. |
| productsDetail.amount | int | O valor do produto. |
| productsDetail.name | string | Nome do produto. |
| productsDetail.quantity | int | A quantidade de produtos. |
| productsDetail.id | int | ID do produto. |
| productsDetail.sku | string | É um código identificador do produto que pode ser usado pela loja pra identificar em seu próprio sistema. |
| type | int | [Tipo de smartCheckOut.](../guias/primeiros-passos.md#smartcheckouttype). |
| status | int | Status do smartCheckout. |
| limitDeniedCharges | int | O limite de cobranças negadas. |
| charges | array | Cobranças do smartCheckout. |
| charges.id | string | O ID da cobrança. |
| charges.addedAtUtc | string | A data de adição da cobrança. |
| charges.nsu | string | O número da transação. |
| charges.chargeStatus | int | Indica o status da cobrança. |
| charges.transactions | array | Transações da cobrança. |
| charges.transactions.card | array | O cartão utilizado na transação. |
| charges.transactions.card.firstSixDigits | string | Os 6 primeiros dígitos do cartão. |
| charges.transactions.card.lasFourDigits | string | Os 4 últimos dígitos do cartão. |
| charges.transactions.card.brandName | string | O nome da bandeira do cartão. |
| charges.transactions.card.cardHolderName | string | O nome do títular impresso na frente do cartão. |
| charges.transactions.card.cardHolderDocument | string | O documento do títular do cartão. |
| charges.transactions.amount | int | O valor da transação. |
| charges.transactions.transactionId | string | Número Sequencial Único (NSU) da autorização, caso o pagamento seja aprovado pelo Emissor. |
| charges.transactions.transactionsStatus | int | Indica o status da transação. |
| charges.transactions.paymentType | int | Indica o tipo de pagamento da transação. |
| charges.transactions.installmentNumber | int | Quantidade de parcelas. Só pode ser maior que **1** se o tipo de transação for crédito. |
| charges.transactions.acquirerId | int | O ID da adquirente. |
| charges.transactions.bankIssuerId | int | O ID do banco. |
| charges.transactions.creationDateTime | string | A data de criação da transação. |
| charges.transactions.captureDateTime | string | A data de captura da transação. |
| customer | Customer | O cliente do smartCheckout. |
| customer.id | string | ID do cliente. |
| customer.name | string | O nome do cliente. |
| customer.email | string | O e-mail do cliente. |
| customer.document | string | O documento do cliente. |
| customer.documentType | string | [Tipo de documento.](../guias/primeiros-passos.md#documenttype). |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | Use o Merchant Token para gerar o `accessToken` do ENDPOINT_GATEWAY. |
| **MerchantId** | {{merchantId}} |
| -- | Número de identificação da loja. |

<a id="sdk-checkout-transparente"></a>

## SDK Checkout Transparente

<a id="instalação-checkout-transparente"></a>

### Instalação Checkout Transparente

Atualmente é possível instalar o Checkout Transparente utilizando o CDN.

<a id="cdn"></a>

#### CDN

Para instalar utilizando **CDN** basta inserir o script do checkout transparente apontando para o local onde ele esta salvo.

| Link | Ambiente |
| --- | --- |
| [https://safrastatic-a.akamaihd.net/safrapay/checkout/prod/safrapay-transparent-v2.0.0.js](https://safrastatic-a.akamaihd.net/safrapay/checkout/prod/safrapay-transparent-v2.0.0.js) | Produção |
| [https://safrastatic-a.akamaihd.net/safrapay/checkout/dev/safrapay-transparent-v2.0.0.js](https://safrastatic-a.akamaihd.net/safrapay/checkout/dev/safrapay-transparent-v2.0.0.js) | Desenvolvimento |

```http
< script src="INSERIR-LINK-AQUI">< /script>
```

Logo após a instalação, estará disponível o objeto chamado `SafraPayTransparent` e nele contém os métodos necessários para tokenizar o cartão.

<a id="passo-1"></a>

#### Passo 1

A primeira coisa a se fazer é registrar as credenciais da loja em que vai ser criado o cartão tokenizado, chamando o método `setCredentials` da SDK. Nesse método é necessário passar a MerchantCredential(CNPJ) e o MerchantId dessa forma aqui:

```http
SafraPayTransparent.setCredentials({merchantCredential: "{{cnpj}}", merchantId: "{{merchantId}}"})`
```

<a id="passo-2"></a>

#### Passo 2

Após adicionar as credenciais deve chamar o método:

```http
SafraPayTransparent.getCardBrand({bin: "444458", success, error})
```

Onde o bin é os 6 primeiros dígitos do cartão usado para identificar a bandeira, success é o callback que vamos chamar retornando a resposta com a bandeira então deve passar uma função para fazer esse tratamento e o error é o callback quando acontecer algum erro no processamento da requisição. Lembrando que success e error são funções callback então não esqueça de construir-los.

```http
function success(body){}
```

e

```http
function error(body){}
```

Caso deseje ver o retorno no console de seu navegador utilize `console.log(body)` dentro das funções.

- Objeto de sucesso na response

```http
{
"brand":"Visa"
}
```

- Objeto de erro na response

```http
{
"errors": [{
"errorCode": 1,
"message": "Propriedade 'CardBin' está ausente",
"field": "CardBin"v
}]
}
```

<a id="passo-3"></a>

#### Passo 3

Após o retorno da bandeira de cartão, pode chamar o método `SafraPayTransparent.createTemporaryCard({card, success, error})` que é responsável por criar o token do cartão, onde card é o objeto contendo informações do cartão, success é o callback onde será informado o token gerado e o error é o callback que será chamado quando estiver algum erro na requisição. Abaixo um exemplo do objeto card preenchido:

```http
{
"brand":"Visa",
"number":"4444585001234562",
"holderName":"FULANO SILVA",
"holderDocument":"65844359038",
"expirationMonth":"02",
"expirationYear":"2026",
"cvv":"223"
}
```

- Objeto de retorno de sucesso:

```http
{
"temporaryToken":"card_t/AIChh82EgN440hTW8vQqHcPC82EwBW"
}
```

- Objeto de retorno de erro:

```http
{
"errors":[{
"errorCode":1,
"message":"Propriedade 'Cvv' está ausente.",
"field":"Cvv"
}]
}
```

Para múltiplos cartões, basta chamar esse método novamente com os dados do novo cartão e utilizar nos objetos de transação abaixo.

<a id="passo-4"></a>

#### Passo 4

Após gerar o token, esse token pode ser enviado para seu servidor e ser usado pra passar uma requisição no endpoint [POST /charge/authorization](gateway.md#post-charge-authorization) ou [POST /charge/preauthorization](gateway.md#post-charge-preauthorization). Para passar uma cobrança com múltiplos cartões, basta adicionar mais um objeto de transação, com o token gerado para este cartão. Abaixo um exemplo de requisição usando esse token temporário.

🚧 Obs.: Utilizando o endpoint /charge/authorization não é preciso enviar o campo `capture`, pois a captura é automatica. O campo `capture` é utilizado no endpoint /charge/preauthorization, sendo passado como `true` ou `false`.

```http
{
"charge": {
"customer": {
"name": "FULANO SILVA",
"email": "fulano@email.com.br",
"entityType": 1,
"documentType": 1,
"document": "40398236720",
"gender": 2,
"phone": {
"countryCode": "55",
"areaCode": "21",
"number": "997027788",
"type": 5
},
"address": {
"street": "Nome da Rua",
"number": "999",
"neighborhood": "Nome do Bairro",
"city": "Nome da Cidade",
"state": "RJ",
"country": "BR",
"zipCode": "21229-999",
"complement": "Complemento"
}
},
"transactions": [
{
"temporaryCardToken": "d2rtf1yuenjkdsm327g38rhiue",
"paymentType": 2,
"amount": 1000,
"installmentNumber": 1,
"acquirer": 999
}
],
"source": 8,
"capture": true
}
}
```

<a id="checkout-redirect"></a>

## Checkout Redirect

**1º** Crie o link de pagamento através do endpoint [POST /smartcheckout](checkout.md#post-smartcheckout).

**2º** Após a criação do link de pagamento, o mesmo deve ser enviado para o cliente com um novo parametro na URL, que é o `redirect_url`.

**Exemplo:** [https://portal.safrapay.com.br/safrapaylink/cc3ef047-9876-49ca-bebe-92ec312a59a2?redirect_url=https://site-para-direcionar.com.br](https://portal.safrapay.com.br/safrapaylink/cc3ef047-9876-49ca-bebe-92ec312a59a2?redirect_url=https://site-para-direcionar.com.br)

🚧 Obs.: o valor do `redirect_url` tem que ser passado com o `https://`, caso contrário não irá funcionar.

**3º** Assim que o cliente receber o link de pagamento e efetuar o pagamento do mesmo, a página irá informar que o pagamento foi aprovado e redirecionará o cliente de volta ao site de compras.

🚧 Obs.: Após o redirecionamento será possível ver o `chargeId` na URL, como mostrado na imagem abaixo.

```http
google.com?chargeId=3c87da61-5d79-4a2d-9f7d-1e2050f5b6bd
```
