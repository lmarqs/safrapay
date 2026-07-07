---
title: "Link de Pagamentos"
parent: "Referência da API"
nav_order: 30
layout: "doc"
permalink: "/api/link-de-pagamento/"
description: "Link de pagamento é uma alternativa para efetuar uma venda sem que o cliente precise acessar seu site ou ir à sua loja. Basta enviar o link por mensagem ou e-ma"
source: "payment-link.html"
---

# LINK DE PAGAMENTOS

Link de pagamento é uma alternativa para efetuar uma venda sem que o cliente precise acessar seu site ou ir à sua loja. Basta enviar o link por mensagem ou e-mail para concluir o procedimento.

🚧 Quando for criado através do Portal Safrapay, sempre será criado um link de pagamentos (ao invés de checkout).

A diferença entre o checkout e o link de pagamentos é que no checkout, o comprador está autenticado em uma loja virtual. O link de pagamentos, por sua vez, é público e não necessita de autenticação. Por isso, no checkout é possível visualizar a wallet de cartões do comprador, enquanto no link de pagamentos isso não é possível.

> **💡 Campo Opcional - RemoteIp:**
>
> Para complementar a análise de risco, você pode fornecer opcionalmente o IP do comprador através do campo `remoteIp`. Este dado é especialmente útil quando o antifraude está ativo, pois auxilia em verificações baseadas em localização e detecção de padrões suspeitos.
>
> 📖 Consulte a [documentação completa do RemoteIp](../guias/antifraude.md#campo-remoteip-complemento-ao-device-fingerprint) e [Serviço de Antifraude](../guias/antifraude.md) para mais informações.

<a id="post-paymentlink"></a>

### `POST` /paymentlink

**Versão** `v2.0`

<a id="requisição-http"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/paymentlink
```

> Exemplo de requisição (`Plano`)

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/paymentlink")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n   \"planId\": \"932168be-46b8-45d3-80f1-45cdd0cd7d6a\",\r\n   \"customer\": {\r\n        \"name\": \"Jorge Filipe\",\r\n        \"email\": \"jorginho.felps@email.com.br\",\r\n        \"document\": \"01234567891\",\r\n        \"phone\": {\r\n            \"countryCode\": \"+55\",\r\n            \"areaCode\": \"21\",\r\n            \"number\": \"999999999\",\r\n            \"type\": 5\r\n        }\r\n    }\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/paymentlink"

payload="{\r\n   \"planId\": \"932168be-46b8-45d3-80f1-45cdd0cd7d6a\",\r\n   \"customer\": {\r\n        \"name\": \"Jorge Filipe\",\r\n        \"email\": \"jorginho.felps@email.com.br\",\r\n        \"document\": \"01234567891\",\r\n        \"phone\": {\r\n            \"countryCode\": \"+55\",\r\n            \"areaCode\": \"21\",\r\n            \"number\": \"999999999\",\r\n            \"type\": 5\r\n        }\r\n    }\r\n}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/paymentlink' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
   "planId": "932168be-46b8-45d3-80f1-45cdd0cd7d6a",
   "customer": {
        "name": "Jorge Filipe",
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

var raw = JSON.stringify({"planId":"932168be-46b8-45d3-80f1-45cdd0cd7d6a","customer":{"name":"Jorge Filipe","email":"jorginho.felps@email.com.br","document":"01234567891","phone":{"countryCode":"+55","areaCode":"21","number":"999999999","type":5}}});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/paymentlink", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> Exemplo de requisição (`Valor Avulso`)

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/paymentlink")

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

url = "{{ENDPOINT_GATEWAY}}/v2/paymentlink"

payload="{\r\n  \"amount\": 1000,\r\n  \"description\": \"Descrição do Link\",\r\n  \"emailNotification\": \"jorginho.felps@email.com.br\",\r\n  \"phoneNotification\": \"21999999999\"\r\n}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/paymentlink' \
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

fetch("{{ENDPOINT_GATEWAY}}/v2/paymentlink", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> Exemplo de requisição (`Produtos`)

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/paymentlink")

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

url = "{{ENDPOINT_GATEWAY}}/v2/paymentlink"

payload="{\r\n    \"emailNotification\": \"jorginho.felps@email.com.br\",\r\n    \"phoneNotification\": \"21999999999\",\r\n    \"newProducts\": {\r\n        \"merchantId\": \"e4a78487-ac6d-4d18-8312-934399d70616\",\r\n        \"products\": [\r\n            {\r\n                \"name\": \"Maçã\",\r\n                \"amount\": 500,\r\n                \"sku\": \"SKU_MACA\",\r\n                \"isActive\": true\r\n            }\r\n        ]\r\n    }\r\n}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/paymentlink' \
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

fetch("{{ENDPOINT_GATEWAY}}/v2/paymentlink", requestOptions)
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

O endpoint responsável por criar um link de pagamentos.

<a id="cabeçalho"></a>

#### Cabeçalho

| Chave | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| Authorization | string | Sim | JWT gerado no endpoint de autenticação pelo MerchantToken. |

<a id="requisição"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| amount | int | Condicional | Valor a ser cobrado. Obrigatório se o checkout / link de pagamento não possui produto(s). |
| orderCode | string | Não | Código ou descrição enviado pelo lojista pra identificar o link de pagamento/checkout. |
| description | string | Não | Descrição do checkout / link de pagamento. |
| planId | string | Sim | Se o link de pagamento é para fins de assinatura. |
| remoteIp | string | Sim | **\[OBRIGATÓRIO quando antifraude ativo\]** O endereço IP do comprador. Utilizado em verificações de risco e prevenção de fraudes. **Exemplo:** `192.168.1.100` (IPv4). Consulte [documentação completa](../guias/antifraude.md#campo-remoteip-complemento-ao-device-fingerprint). |
| customer | object | Condicional | Dados do comprador. Obrigatório se o `customerId` não estiver presente. |
| customer.id | string | Sim | ID do comprador. |
| customer.name | string | Sim | Nome completo do comprador. |
| customer.email | string | Sim | E-mail do comprador. |
| customer.entityType | entityType | Sim | [Se é pessoa física ou jurídica](../guias/primeiros-passos.md#entitytype). |
| customer.documentType | documentType | Sim | [Tipo do documento do comprador.](../guias/primeiros-passos.md#documenttype). |
| customer.document | string | Sim | Documento do comprador. |
| customer.birthday | date | Não | Data de nascimento do comprador. |
| customer.gender | Gender | Não | [Gênero do comprador](../guias/primeiros-passos.md#gender). |
| customer.phone | object | Sim | Telefone do comprador. |
| customer.phone.countryCode | string | Sim | Código do país. |
| customer.phone.areaCode | string | Sim | Código de área. |
| customer.phone.number | string | Sim | Número do Telefone. |
| customer.phone.type | PhoneType | Sim | [Tipo do telefone](../guias/primeiros-passos.md#phone). |
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
| paymentSupportedTypes | array(int) | Não | Meios de pagamento permitidos no checkout / link. Cada item do array é um valor inteiro do enum **`PaymentType`** (ver [tabela e descrição no guia de acesso](../guias/primeiros-passos.md#paymenttype)). O comprador só poderá pagar por um dos tipos informados. |
| discount | int | Não | Desconto no pagamento em centavos. |
| shippingAmount | int | Não | Valor do frete em centavos. |
| hostUrl | string | Sim | URL de origem. Utilizado para customizar a logo no e-mail com link para pagamento. |
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
| limitApprovedCharges | int | Não | Número limite de transações aprovadas para o checkout / link de pagamentos. Valor default de apenas 1 pagamento. |
| primaryColor | string | Não | RGB da cor primária da loja. Utilizado para customizar o tema do e-mail com o link para pagamento. |
| secondaryColor | string | Não | RGB da cor secundária da loja. Utilizado para customizar o tema do e-mail com o link para pagamento. |
| installmentNumber | int | Não | Número **exato** de parcelas suportado pelo checkout / link de pagamentos. Se esse valor for recebido, `maxInstallmentNumber` é ignorado. Se não for enviado, será considerado apenas o `maxInstallmentNumber`. |
| limitDeniedCharges | int | Não | Número limite de transações negadas para o checkout / link de pagamentos. Valor default ilimitado. |
| customTemplate | string | Não | Identificador do layout a ser exibido na URL do checkout / link de pagamentos. Se não for enviado, será usado o template default. |
| documentSupportedTypes | array(int) | Não | Os tipos de documentos que o link de pagamento suporta. |
| supportMultipleTransactions | bool | Não | Indica se o link de pagamento suporta múltiplos cartões para um pagamento. Valor padrão sempre será "false". |
| securityLayer | int | Não | Personalização da camada de segurança para estabelecimentos com fluxo híbrido¹. Insira 2, caso deseje que a transação passe pelo 3DS. Insira 3, caso deseje que a transação passe pelo Antifraude. |

¹ Estabelecimentos com fluxo híbrido são aqueles que possuem 3DS e Antifraude cadastrados. Quando a camada de segurança não é personalizada, a transação é enviada primeiro ao 3DS; se a autenticação não for concluída, a transação segue automaticamente para análise do Antifraude.

<a id="resposta"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| id | string | ID do checkout / link de pagamento criado. |
| smartCheckoutUrl | string | URI que deverá ser utilizada em conjunto com uma URL base para acessar a tela de pagamentos. |
| products | array(object) | Lista de produtos criados, se houve algum novo produto na criação do checkout / link de pagamento. |
| products.name | string | Nome do produto, campo livre. |
| products.description | string | Descrição do produto, campo livre. |
| products.imagesRef | array(string) | URLs de Imagens relacionados ao produto, string deve ser URL válida. |
| products.amount | string | Valor do produto em centavos. |
| products.sku | string | Identificador único do produto na loja. Não é permitido valor duplicado. |
| products.isActive | bool | Se o produto está disponível na loja. Default `false`. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

<a id="body-raw"></a>

#### BODY Raw

***Plano***

```http
{
"planId": "932168be-46b8-45d3-80f1-45cdd0cd7d6a",
"customer": {
"name": "Jorge Filipe",
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

<a id="get-smartcheckout-smartcheckoutid-detail"></a>

### `GET` /smartcheckout/{smartcheckoutId}/detail

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

Endpoint responsável por obter os detalhes de um link de pagamento, incluindo informações de cada cobrança efetuada, se houver.

<a id="cabeçalho-1"></a>

#### Cabeçalho

| Chave | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| Authorization | string | Sim | JWT gerado no endpoint de autenticação pelo MerchantToken. |
| merchantId | string | Sim | O ID do estabelecimento. |

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
| shippingAddress | object | Endereço de entrega dos produtos. |
| shippingAddress.street | string | Rua. |
| shippingAddress.number | string | Número. |
| shippingAddress.neighborhood | string | Bairro. |
| shippingAddress.city | string | Cidade. |
| shippingAddress.state | string | Estado. |
| shippingAddress.country | string | País. |
| shippingAddress.zipCode | string | CEP. |
| shippingAddress.complement | string | Complemento. |
| limitApprovedCharges | int | O limite de cobranças aprovadas. |
| productsDetail | object | Detalhes dos produtos. |
| productsDetail.amount | int | O valor do produto. |
| productsDetail.name | string | Nome do produto. |
| productsDetail.quantity | int | A quantidade de produtos. |
| productsDetail.id | int | ID do produto. |
| productsDetail.sku | string | É um código identificador do produto que pode ser usado pela loja pra identificar em seu próprio sistema. |
| type | int | [Tipo de smartCheckout.](../guias/primeiros-passos.md#smartcheckouttype). |
| status | int | Status do smartCheckout. |
| limitDeniedCharges | int | O limite de cobranças negadas. |
| charges | array | Cobranças do smartCheckout. |
| charges.id | string | O ID da cobrança. |
| charges.addedAtUtc | string | A data de adição da cobrança. |
| charges.nsu | string | Identificador do pedido (Safrapay). |
| charges.chargeStatus | int | Indica o status da cobrança. |
| charges.transactions | array(object) | Transações da cobrança. |
| charges.transactions.card | array(object) | O cartão utilizado na transação. |
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
| customer | object | O cliente do smartCheckout. |
| customer.id | string | ID do cliente. |
| customer.name | string | O nome do cliente. |
| customer.email | string | O e-mail do cliente. |
| customer.document | string | O documento do cliente. |
| customer.documentType | string | [O tipo do documento.](../guias/primeiros-passos.md#documenttype). |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

<a id="delete-smartcheckout-smartcheckoutid"></a>

### `DELETE` /smartcheckout/{smartcheckoutId}

**Versão** `v1.0`

<a id="requisição-http-2"></a>

#### Requisição HTTP

```http
DELETE {{ENDPOINT_GATEWAY}}/v2/smartcheckout/{{smartcheckoutId}}
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("https://portal-dev.safrapay.com.br/v1/smartcheckout/{{smartcheckoutId}}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["merchantId"] = "{{merchantId}}"
request["Authorization"] = "Bearer {{accessToken}}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "https://portal-api-hml.safrapay.com.br/v1/smartcheckout/{{smartcheckoutId}}"

payload={}
headers = {
  'merchantId': '{{merchantId}}',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location -g --request DELETE 'https://portal-api-hml.safrapay.com.br/v1/smartcheckout/{{smartcheckoutId}}' \
--header 'merchantId: {{merchantId}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("merchantId", "{{merchantId}}");
myHeaders.append("Authorization", "Bearer {{accessToken}}");

var requestOptions = {
  method: 'DELETE',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://portal-api-hml.safrapay.com.br/v1/smartcheckout/{{smartcheckoutId}}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
   "success": true,
   "errors": [],
   "traceKey": "587c72cf-a761-599f-989b-7e46b21204fa"
}
```

Endpoint responsável por deletar um link de pagamento.

<a id="cabeçalho-2"></a>

#### Cabeçalho

| Chave | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| Authorization | string | Sim | JWT gerado no endpoint de autenticação pelo MerchantToken. |
| merchantId | string | Sim | O ID do estabelecimento. |

<a id="requisição-2"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| smartcheckoutId | string | Sim | Número de identificação da cobrança. |

<a id="resposta-2"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

<a id="get-smartcheckout"></a>

### `GET` /smartcheckout

**Versão** `v1.0`

<a id="requisição-http-3"></a>

#### Requisição HTTP

```http
GET {{ENDPOINT_GATEWAY}}/v2/smartcheckout
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/smartcheckout?startDate=2020-09-27&endDate=2021-09-29&type=1&status=1&pageSize=10&currentPage=1")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Get.new(url)
request["MerchantId"] = "{{merchantId}}"
request["Authorization"] = "Bearer {{accessToken}}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/smartcheckout?startDate=2020-09-27&endDate=2021-09-29&type=1&status=1&pageSize=10&currentPage=1"

payload={}
headers = {
  'MerchantId': '{{merchantId}}',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request GET '{{ENDPOINT_GATEWAY}}/v2/smartcheckout?startDate=2020-09-27&endDate=2021-09-29&type=1&status=1&pageSize=10&currentPage=1' \
--header 'MerchantId: {{merchantId}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("MerchantId", "{{merchantId}}");
myHeaders.append("Authorization", "Bearer {{accessToken}}");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/smartcheckout?startDate=2020-09-27&endDate=2021-09-29&type=1&status=1&pageSize=10&currentPage=1", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
   "smartcheckouts": [
       {
           "id": "5c700232-c987-4a3a-bb99-c8286c20324b",
           "amount": 999,
           "creationDate": "2021-06-01 15:00:44Z",
           "expiration": "2021-06-02 15:00:44Z",
           "status": 101,
           "statusDescription": "Expirado pelo limite de tempo"
       }
   ],
   "total": 1,
   "success": true,
   "errors": [],
   "traceKey": "300f7c93-2cc5-7893-ad52-1b9151b345e2"
}
```

Endpoint responsável por obter a lista de checkouts, por data, status e/ou tipo

🚧OBS: Se não for passado data e status a consulta irá trazer os links de pagamento com data de expiração maior que o dia atual.

<a id="cabeçalho-3"></a>

#### Cabeçalho

| Chave | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| Authorization | string | Sim | JWT gerado no endpoint de autenticação pelo MerchantToken. |
| merchantId | string | Sim | O ID do estabelecimento. |

<a id="parâmetros-de-query"></a>

#### Parâmetros de query

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| startDate | string | Não | A data inicial da consulta |
| endDate | string | Não | A data final da consulta |
| type | int | Sim | [O tipo de smartCheckout](../guias/primeiros-passos.md#smartcheckouttype) |
| status | int | Não | [O status de smartCheckout](../guias/primeiros-passos.md#smartcheckoutstatus) |
| pageSize | int | Sim | Quantidade de items por pagina de consulta |
| currentPage | int | Sim | O número da página atual da consulta |

<a id="resposta-3"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| id | string | O número de identificação do smartCheckout |
| amount | int | A valor do smartCheckout |
| creationDate | string | Data de criação do smartCheckout |
| expiration | string | Data de expiração do smartCheckout |
| status | int | [O status de smartCheckout](../guias/primeiros-passos.md#smartcheckoutstatus) |
| statusDescription | string | Descrição do status. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |
