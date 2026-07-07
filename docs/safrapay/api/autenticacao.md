---
title: "Autenticação"
parent: "Referência da API"
nav_order: 10
layout: "doc"
permalink: "/api/autenticacao/"
description: "A autenticação é a forma que deve ser utilizada para gerar um Token de acesso, para que você consiga utilizar os endpoints."
source: "authentication.html"
---

# AUTENTICAÇÃO

A autenticação é a forma que deve ser utilizada para gerar um Token de acesso, para que você consiga utilizar os endpoints.

<a id="gateway-api"></a>

## Gateway API

A autenticação do Gateway é feita através `MerchantToken`. Liberando assim o acesso para utilizar os endpoints do Gateway.

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
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/merchant/auth")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "{{MerchantToken}}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/merchant/auth"

payload={}
headers = {
  'Authorization': '{{MerchantToken}}',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/merchant/auth' \
--header 'Authorization: {{MerchantToken}}' 
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "{{MerchantToken}}");

var requestOptions = {
  method: "POST",
  headers: myHeaders,
  redirect: "follow",
};

fetch("{{ENDPOINT_GATEWAY}}/v2/merchant/auth", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
  .catch((error) => console.log("error", error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
  "accessToken": "eyJhbHciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Im1rX2c1RHJLQ0RzRGt1RjFpTFBuRFdvbUEiLCJuYW1laWQiOiJta19nNURyS0NEc0RrdUYxaUxQbkRXb21BIiwibmJmIjoxNjI0MDIzNDc3LCJleHAiOjE2MjUyMzMwNzcsImlhdCI6MTYyNDAyMzQ3NywiaXNzIjoiQWRpdHVtIiwiYXVkIjoiQWRpdHVtIn0.g9jVQKHCsmCwj35ST-tIkhpilGivLKMXG_rVJSI9hXUK5kTklEjV-Pzta5j94UwpvAljcbVAG0uuyL06-Vg1qTMq9UoieynGwzyDXDbKMC8bVbcioJaN7XSLqCEUS6dTizhyXESCaZtpQop0_ibAaBa0yJAIfzCyZYQxeLBcvNENOiaKrMRSYLzAmsBcBsg7EgnD_VvAoqvdQG9J_ZkdDxMlc0e8UHrDlSVBUoEpF09UOH7TtHedHFpgeF5CANUU9-MD7epb5AGLR6cOR-HvHIyrGH-mdKcCXQiGj5tZ8JIcH6diLOp1AP5DZQecCvHxGChIIV2MF2f55OeuMwvZnQ",
  "refreshToken": "6546f5a4a9bb43d39b7cde6b8fdce5d9",
  "success": true,
  "errors": [],
  "traceKey": "e899d6bc-954b-46b7-a52d-5d9ddcf9dbb0"
}
```

O Endpoint é utilizado para gerar um par de acessos, token de acesso e token de atualização, que são necessários para consumir a API.

<a id="cabeçalho"></a>

#### Cabeçalho

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| Authorization | string | Sim | Chave de acesso a API. |

<a id="resposta"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| accessToken | string | Token JWT que deve ser utilizado no `Authorization` das próximas requisições. Esse token expira em 30 minutos e pode ser atualizado com o `refreshToken`. |
| refreshToken | string | Token utilizado para gerar outros JWT sem precisar enviar o `merchantToken`. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| traceKey | string | Identificador da operação. |

<a id="post-refreshtoken"></a>

### `POST` /refreshtoken

**Versão** `v2.0`

<a id="requisição-http-1"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/refreshtoken
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("https://payment-dev.safrapay.com.br/v2/refreshtoken")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{\r\n    \"accessToken\": \"eyJhbHciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Im1rX2c1RHJLQ0RzRGt1RjFpTFBuRFdvbUEiLCJuYW1laWQiOiJta19nNURyS0NEc0RrdUYxaUxQbkRXb21BIiwibmJmIjoxNjI0MDIzNDc3LCJleHAiOjE2MjUyMzMwNzcsImlhdCI6MTYyNDAyMzQ3NywiaXNzIjoiQWRpdHVtIiwiYXVkIjoiQWRpdHVtIn0.g9jVQKHCsmCwj35ST-tIkhpilGivLKMXG_rVJSI9hXUK5kTklEjV-Pzta5j94UwpvAljcbVAG0uuyL06-Vg1qTMq9UoieynGwzyDXDbKMC8bVbcioJaN7XSLqCEUS6dTizhyXESCaZtpQop0_ibAaBa0yJAIfzCyZYQxeLBcvNENOiaKrMRSYLzAmsBcBsg7EgnD_VvAoqvdQG9J_ZkdDxMlc0e8UHrDlSVBUoEpF09UOH7TtHedHFpgeF5CANUU9-MD7epb5AGLR6cOR-HvHIyrGH-mdKcCXQiGj5tZ8JIcH6diLOp1AP5DZQecCvHxGChIIV2MF2f55OeuMwvZnQ\",\r\n    \"refreshToken\": \"612179235e914cba90a9743803ba397f\"\r\n}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/refreshtoken"

payload="{\r\n    \"accessToken\": \"eyJhbHciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Im1rX2c1RHJLQ0RzRGt1RjFpTFBuRFdvbUEiLCJuYW1laWQiOiJta19nNURyS0NEc0RrdUYxaUxQbkRXb21BIiwibmJmIjoxNjI0MDIzNDc3LCJleHAiOjE2MjUyMzMwNzcsImlhdCI6MTYyNDAyMzQ3NywiaXNzIjoiQWRpdHVtIiwiYXVkIjoiQWRpdHVtIn0.g9jVQKHCsmCwj35ST-tIkhpilGivLKMXG_rVJSI9hXUK5kTklEjV-Pzta5j94UwpvAljcbVAG0uuyL06-Vg1qTMq9UoieynGwzyDXDbKMC8bVbcioJaN7XSLqCEUS6dTizhyXESCaZtpQop0_ibAaBa0yJAIfzCyZYQxeLBcvNENOiaKrMRSYLzAmsBcBsg7EgnD_VvAoqvdQG9J_ZkdDxMlc0e8UHrDlSVBUoEpF09UOH7TtHedHFpgeF5CANUU9-MD7epb5AGLR6cOR-HvHIyrGH-mdKcCXQiGj5tZ8JIcH6diLOp1AP5DZQecCvHxGChIIV2MF2f55OeuMwvZnQ\",\r\n    \"refreshToken\": \"612179235e914cba90a9743803ba397f\"\r\n}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/refreshtoken' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "accessToken": "eyJhbHciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Im1rX2c1RHJLQ0RzRGt1RjFpTFBuRFdvbUEiLCJuYW1laWQiOiJta19nNURyS0NEc0RrdUYxaUxQbkRXb21BIiwibmJmIjoxNjI0MDIzNDc3LCJleHAiOjE2MjUyMzMwNzcsImlhdCI6MTYyNDAyMzQ3NywiaXNzIjoiQWRpdHVtIiwiYXVkIjoiQWRpdHVtIn0.g9jVQKHCsmCwj35ST-tIkhpilGivLKMXG_rVJSI9hXUK5kTklEjV-Pzta5j94UwpvAljcbVAG0uuyL06-Vg1qTMq9UoieynGwzyDXDbKMC8bVbcioJaN7XSLqCEUS6dTizhyXESCaZtpQop0_ibAaBa0yJAIfzCyZYQxeLBcvNENOiaKrMRSYLzAmsBcBsg7EgnD_VvAoqvdQG9J_ZkdDxMlc0e8UHrDlSVBUoEpF09UOH7TtHedHFpgeF5CANUU9-MD7epb5AGLR6cOR-HvHIyrGH-mdKcCXQiGj5tZ8JIcH6diLOp1AP5DZQecCvHxGChIIV2MF2f55OeuMwvZnQ",
    "refreshToken": "612179235e914cba90a9743803ba397f"
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  accessToken:
    "eyJhbHciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Im1rX2c1RHJLQ0RzRGt1RjFpTFBuRFdvbUEiLCJuYW1laWQiOiJta19nNURyS0NEc0RrdUYxaUxQbkRXb21BIiwibmJmIjoxNjI0MDIzNDc3LCJleHAiOjE2MjUyMzMwNzcsImlhdCI6MTYyNDAyMzQ3NywiaXNzIjoiQWRpdHVtIiwiYXVkIjoiQWRpdHVtIn0.g9jVQKHCsmCwj35ST-tIkhpilGivLKMXG_rVJSI9hXUK5kTklEjV-Pzta5j94UwpvAljcbVAG0uuyL06-Vg1qTMq9UoieynGwzyDXDbKMC8bVbcioJaN7XSLqCEUS6dTizhyXESCaZtpQop0_ibAaBa0yJAIfzCyZYQxeLBcvNENOiaKrMRSYLzAmsBcBsg7EgnD_VvAoqvdQG9J_ZkdDxMlc0e8UHrDlSVBUoEpF09UOH7TtHedHFpgeF5CANUU9-MD7epb5AGLR6cOR-HvHIyrGH-mdKcCXQiGj5tZ8JIcH6diLOp1AP5DZQecCvHxGChIIV2MF2f55OeuMwvZnQ",
  refreshToken: "612179235e914cba90a9743803ba397f",
});

var requestOptions = {
  method: "POST",
  headers: myHeaders,
  body: raw,
  redirect: "follow",
};

fetch("{{ENDPOINT_GATEWAY}}/v2/refreshtoken", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
  .catch((error) => console.log("error", error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
  "accessToken": "eyJhbHciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Im1rX2c1RHJLQ0RzRGt1RjFpTFBuRFdvbUEiLCJuYW1laWQiOiJta19nNURyS0NEc0RrdUYxaUxQbkRXb21BIiwibmJmIjoxNjI0MDI4MTE2LCJleHAiOjE2MjUyMzc3MTYsImlhdCI6MTYyNDAyODExNiwiaXNzIjoiQWRpdHVtIiwiYXVkIjoiQWRpdHVtIn0.Vzt387BFC1amWYPdbm0vf2wPYwwak1Gj7dmyGWJhpgzIfX9QET1sQTE7YJdFmN6JPKcTnArPzx80wY68hte9_AyDYkSa_P-Jeg6x3NxOyvCxcMPfnv1Qv-gtrfWyA7mnPm2nXXfavzeTZZ7ZQjfMvYBR15a2QVvKLyU3MYFLLo3swW5fsKzxmkn7RaqSFLwS4XI8rNXqLN_zKjGCBu7F4gV-3G2YGivaabZ8nqB1ODo5LDqNieFBnuVAMUiU5s-eORVeEhB-j40LDPICG5poeXYPw7L4VXMhNH8ivY5mCtxbfvk9jWIVBQkWAGrSjRWvOIU35h2-Ym2A8O4-hdqUjw",
  "refreshToken": "612179235e914cba90a9743803ba397f",
  "success": true,
  "errors": [],
  "traceKey": "498c960d-8b70-4658-9d13-fac92eaec6b8"
}
```

O endpoint é utilizado para atualizar o token de acesso.

<a id="cabeçalho-1"></a>

#### Cabeçalho

| Chave | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| Authorization | string | Sim | JWT gerado no endpoint de autenticação pelo MerchantToken. |

<a id="requisição"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| accessToken | string | Sim | Token JWT que deve ser utilizado no `Authorization` das próximas requisições. Esse token expira em 30 minutos e pode ser atualizado com o `refreshToken`. |
| refreshToken | string | Sim | Token utilizado para gerar outros JWT sem precisar enviar o `merchantToken`. |

<a id="resposta-1"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| accessToken | string | Token JWT que deve ser utilizado no `Authorization` das próximas requisições. Esse token expira em 30 minutos e pode ser atualizado com o `refreshToken`. |
| refreshToken | string | Token utilizado para gerar outros JWT sem precisar enviar o `merchantToken`. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| traceKey | string | Identificador da operação. |
