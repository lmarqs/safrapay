---
title: "Recorrência e Planos"
parent: "Referência da API"
nav_order: 90
layout: "doc"
permalink: "/api/recorrencia/"
description: "O pagamento recorrente é aquele feito no caso de um serviço contínuo, em que existe uma assinatura ou pagamento de mensalidades. Também pode ser utilizado como "
source: "recurrency.html"
---

# RECORRÊNCIA E PLANOS

O pagamento recorrente é aquele feito no caso de um serviço contínuo, em que existe uma assinatura ou pagamento de mensalidades. Também pode ser utilizado como pagamento parcelado, sem a sensibilização do saldo total na fatura do cliente.

Em caso de falha no processamento de um pagamento, o mesmo é retentado por 5 dias até que a assinatura seja cancelada automaticamente.

Nessa modalidade de pagamento, existem dois conceitos fundamentais:

- Plano: o plano é um "template" do pagamento recorrente.
- Assinatura: é a execução do pagamento recorrente e tem como base um plano pré-existente.

Exemplo:

Plano: Academia XPTO - Promoção Semestral - R$79,90 Assinatura: Comprador João fez a assinatura do plano "Academia XPTO - Promoção Semestral"

<a id="plano"></a>

## Plano

São os planos que o estabelecimento possui ou possa vir a criar.

<a id="post-plan"></a>

### `POST` /plan

**Versão** `v2.0`

<a id="requisição-http"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/plan
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/plan")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{  \"plan\": {    \"amount\": 10000,    \"frequency\": 3,    \"label\": \"Academia\",    \"cycles\": 12,    \"merchantId\": \"22eb9083-ec20-4b5e-85d6-22cf9c35a898\",    \"isActive\": true,    \"paymentType\": 2  }}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/plan"

payload="{  \"plan\": {    \"amount\": 10000,    \"frequency\": 3,    \"label\": \"Academia\",    \"cycles\": 12,    \"merchantId\": \"22eb9083-ec20-4b5e-85d6-22cf9c35a898\",    \"isActive\": true,    \"paymentType\": 2  }}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/plan' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "plan": {
    "amount": 10000,
    "frequency": 3,
    "label": "Academia",
    "cycles": 12,
    "merchantId": "22eb9083-ec20-4b5e-85d6-22cf9c35a898",
    "isActive": true,
    "paymentType": 2
  }
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"plan":{"amount":10000,"frequency":3,"label":"Academia","cycles":12,"merchantId":"22eb9083-ec20-4b5e-85d6-22cf9c35a898","isActive":true,"paymentType":2}});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/plan", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "plan": {
        "id": "780f19be-03b2-4b8e-b153-86715225aa5c",
        "amount": 10000,
        "frequency": "Monthly",
        "label": "Academia",
        "cycles": 12,
        "isActive": true,
        "paymentType": "Credit"
    },
    "success": true,
    "errors": [],
    "traceKey": "4112eb66-c429-448f-9d84-662e66f4feb3"
}
```

Endpoint responsável por criar um novo plano.

<a id="requisição"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| plan | object | Sim | Informações do plano. |
| plan.id | string | Sim | ID retornado na criação do plano. |
| plan.amount | int | Sim | Valor do plano em centavos. |
| plan.frequency | int | Sim | [A frequência com que uma assinatura deve ser cobrada.](../guias/primeiros-passos.md#frequency). |
| plan.label | string | Não | Tag do plano definida pelo cliente. |
| plan.cycles | int | Não | O número de vezes que suas assinaturas serão cobradas. |
| plan.freeCycles | int | Não | O número de vezes que suas assinaturas serão cobradas. |
| plan.chargeEvents | array(object) | Não | Eventos de cobrança usados para adicionar descontos e taxas extras às assinaturas do plano. |
| plan.chargeEvents.description | string | Não | Descrição do evento de cobrança. |
| plan.chargeEvents.amount | int | Não | Quantia do evento de cobrança. |
| plan.chargeEvents.mode | int | Não | [Evento de cobrança aplicado a uma recorrência](../guias/primeiros-passos.md#chargeeventmode) |
| plan.chargeEvents.strategy | object | Não | Estratégia do evento de cobrança. |
| plan.chargeEvents.strategy.firstCharges | int | Não | Primeiras cobranças. |
| plan.merchantId | string | Não | Identificação do comerciante que criou este plano. |
| plan.isActive | bool | Não | Define se o plano está ativo ou não. |
| plan.planItems | array(object) | Não | Os itens que irão compor o plano. |
| plan.planItems.itemCode | string | Não | Código do item. |
| plan.planItems.description | string | Não | A descrição do item. |
| plan.planItems.value | int | Não | O valor do item. |
| plan.planItems.quantity | int | Não | A quantidade do item. |
| plan.planItems.categoryId | string | Não | A categoria que o item pertence. |
| plan.planFine | array(object) | Não | A multa que será aplicada ao plano caso não seja paga na data de vencimento. |
| plan.planFine.value | int | Não | O valor da multa. |
| plan.planFine.daysAfterDueDate | int | Não | Dias após a data de vencimento. |
| plan.planFine.interest | number | Não | Os juros financeiros representam um valor em porcentagem que será calculado todos os dias após a data de vencimento. |
| plan.planDiscount | array(object) | Não | O desconto a ser aplicado ao plano. |
| plan.planDiscount.percentual | number | Não | O valor do desconto em porcentagem. |
| plan.planDiscount.fixValue | number | Não | O valor do desconto, valor fixo. |
| plan.planDiscount.dailyValue | number | Não | Valor diário. |
| plan.planDiscount.dayBeforeTheDueDate | int | Não | Dia antes da data de vencimento. |
| plan.closeInvoiceDay | int | Não | O dia em que a fatura será fechada. |
| plan.bankSlipDueDateDay | int | Não | O dia da data de vencimento do boleto bancário. |
| plan.paymentType | int | Não | [Tipo de transação.](../guias/primeiros-passos.md#paymenttype) |

<a id="resposta"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| plan | - | O plano criado. |
| plan.id | string | ID retornado na criação do plano. |
| plan.amount | int | Valor do plano em centavos. |
| plan.frequency | int | [A frequência com que uma assinatura deve ser cobrada.](../guias/primeiros-passos.md#frequency). |
| plan.label | string | Tag do plano definida pelo cliente. |
| plan.cycles | string | O número de vezes que suas assinaturas serão cobradas. |
| plan.chargeEvents | - | Eventos de cobrança usados para adicionar descontos e taxas extras às assinaturas do plano. |
| plan.chargeEvents.description | string | Descrição do evento de cobrança. |
| plan.chargeEvents.amount | int | Quantia do evento de cobrança. |
| plan.chargeEvents.mode | int | [Evento de cobrança aplicado a uma recorrência](../guias/primeiros-passos.md#chargeeventmode) |
| plan.chargeEvents.strategy | array | Estratégia do evento de cobrança. |
| plan.merchantId | string | Identificação do comerciante que criou este plano. |
| plan.isActive | bool | Define se o plano está ativo ou não. |
| plan.planItems | - | Os itens que irão compor o plano. |
| plan.planItems.itemCode | string | Código do item. |
| plan.planItems.description | string | A descrição do item. |
| plan.planItems.value | int | O valor do item. |
| plan.planItems.quantity | int | A quantidade do item. |
| plan.planItems.categoryId | string | A categoria que o item pertence. |
| plan.planFine | - | A multa que será aplicada ao plano caso não seja paga na data de vencimento. |
| plan.planFine.value | int | O valor da multa. |
| plan.planFine.daysAfterDueDate | int | Dias após a data de vencimento. |
| plan.planFine.interest | number | Os juros financeiros representam um valor em porcentagem que será calculado todos os dias após a data de vencimento. |
| plan.planDiscount | - | O desconto a ser aplicado ao plano. |
| plan.planDiscount.percentual | number | O valor do desconto em porcentagem. |
| plan.planDiscount.fixValue | number | O valor do desconto, valor fixo. |
| plan.planDiscount.dailyValue | number | Valor diário. |
| plan.planDiscount.dayBeforeTheDueDate | int | Dia antes da data de vencimento. |
| plan.closeInvoiceDay | int | O dia em que a fatura será fechada. |
| plan.bankSlipDueDateDay | int | O dia da data de vencimento do boleto bancário. |
| plan.paymentType | int | [Tipo de transação.](../guias/primeiros-passos.md#paymenttype) |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. Lembre-se de usar o {{accessToken}} |

<a id="body-raw"></a>

#### BODY Raw

```http
{
"plan": {
"amount": 10000,
"frequency": 3,
"label": "Academia",
"cycles": 12,
"merchantId": "22eb9083-ec20-4b5e-85d6-22cf9c35a898",
"isActive": true,
"paymentType": 2
}
}
```

<a id="put-plan"></a>

### `PUT` /plan

**Versão** `v2.0`

<a id="requisição-http-1"></a>

#### Requisição HTTP

```http
PUT {{ENDPOINT_GATEWAY}}/v2/plan
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/plan")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{  \"plan\": {    \"id\": \"990f19be-02b2-4b8e-b153-86715225aa5c\",    \"amount\": 10000,    \"frequency\": 3,    \"label\": \"Academia\",    \"cycles\": 12,    \"merchantId\": \"22eb9083-ec20-4b5e-85d6-22cf9c35a898\",    \"isActive\": true,    \"paymentType\": 2  }}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/plan"

payload="{  \"plan\": {    \"id\": \"990f19be-02b2-4b8e-b153-86715225aa5c\",    \"amount\": 10000,    \"frequency\": 3,    \"label\": \"Academia\",    \"cycles\": 12,    \"merchantId\": \"22eb9083-ec20-4b5e-85d6-22cf9c35a898\",    \"isActive\": true,    \"paymentType\": 2  }}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request PUT '{{ENDPOINT_GATEWAY}}/v2/plan' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "plan": {
    "id": "990f19be-02b2-4b8e-b153-86715225aa5c",
    "amount": 10000,
    "frequency": 3,
    "label": "Academia",
    "cycles": 12,
    "merchantId": "22eb9083-ec20-4b5e-85d6-22cf9c35a898",
    "isActive": true,
    "paymentType": 2
  }
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"plan":{"id":"990f19be-02b2-4b8e-b153-86715225aa5c","amount":10000,"frequency":3,"label":"Academia","cycles":12,"merchantId":"22eb9083-ec20-4b5e-85d6-22cf9c35a898","isActive":true,"paymentType":2}});

var requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/plan", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "updatedPlan": {
        "id": "990f19be-02b2-4b8e-b153-86715225aa5c",
        "amount": 10000,
        "frequency": "Monthly",
        "label": "Academia",
        "cycles": 12,
        "isActive": true,
        "paymentType": "Credit"
    },
    "success": true,
    "errors": [],
    "traceKey": "501f7e09-2537-414b-9e97-d72cfea3d496"
}
```

Endpoint responsável por atualizar os dados de um plano através do ID retornado na criação do plano.

<a id="requisição-1"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| plan | - | Sim | Plano atualizado. Deve conter apenas as propriedades com informações atualizadas; ou o objeto do plano completo. Os planos definem informações básicas para assinaturas. |
| plan.id | string | Sim | ID retornado na criação do plano. |
| plan.amount | int | Sim | Valor do plano em centavos. |
| plan.frequency | int | Sim | [A frequência com que uma assinatura deve ser cobrada.](../guias/primeiros-passos.md#frequency). |
| plan.label | string | Não | Tag do plano definida pelo cliente. |
| plan.cycles | string | Não | O número de vezes que suas assinaturas serão cobradas. |
| plan.freeCycles | int | Não | O número de vezes que suas assinaturas serão cobradas. |
| plan.chargeEvents | array(object) | Não | Eventos de cobrança usados para adicionar descontos e taxas extras às assinaturas do plano. |
| plan.chargeEvents.description | string | Não | Descrição do evento de cobrança. |
| plan.chargeEvents.amount | int | Sim | Quantia do evento de cobrança. |
| plan.chargeEvents.mode | int | Sim | [Evento de cobrança aplicado a uma recorrência](../guias/primeiros-passos.md#chargeeventmode) |
| plan.chargeEvents.strategy | object | Sim | Estratégia do evento de cobrança. |
| plan.chargeEvents.strategy.firstCharges | int | Não | Primeiras cobranças. |
| plan.merchantId | string | Não | Identificação do comerciante que criou este plano. |
| plan.isActive | bool | Sim | Define se o plano está ativo ou não. |
| plan.planItems | array(object) | Não | Os itens que irão compor o plano. |
| plan.planItems.itemCode | string | Não | Código do item. |
| plan.planItems.description | string | Não | A descrição do item. |
| plan.planItems.value | int | Sim | O valor do item. |
| plan.planItems.quantity | int | Sim | A quantidade do item. |
| plan.planItems.categoryId | string | Não | A categoria que o item pertence. |
| plan.planFine | array(object) | Sim | A multa que será aplicada ao plano caso não seja paga na data de vencimento. |
| plan.planFine.value | int | Não | O valor da multa. |
| plan.planFine.daysAfterDueDate | int | Não | Dias após a data de vencimento. |
| plan.planFine.interest | number | Não | Os juros financeiros representam um valor em porcentagem que será calculado todos os dias após a data de vencimento. |
| plan.planDiscount | array(object) | Sim | O desconto a ser aplicado ao plano. |
| plan.planDiscount.percentual | number | Não | O valor do desconto em porcentagem. |
| plan.planDiscount.fixValue | number | Não | O valor do desconto, valor fixo. |
| plan.planDiscount.dailyValue | number | Não | Valor diário. |
| plan.planDiscount.dayBeforeTheDueDate | int | Não | Dia antes da data de vencimento. |
| plan.closeInvoiceDay | int | Não | O dia em que a fatura será fechada. |
| plan.bankSlipDueDateDay | int | Não | O dia da data de vencimento do boleto bancário. |
| plan.paymentType | int | Sim | [Tipo de transação.](../guias/primeiros-passos.md#paymenttype) |

<a id="resposta-1"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| updatedPlan | - | Plano atualizado. |
| plan.id | string | ID retornado na criação do plano. |
| plan.amount | int | Valor do plano em centavos. |
| plan.frequency | int | [A frequência com que uma assinatura deve ser cobrada.](../guias/primeiros-passos.md#frequency). |
| plan.label | string | Tag do plano definida pelo cliente. |
| plan.cycles | string | O número de vezes que suas assinaturas serão cobradas. |
| plan.chargeEvents | - | Eventos de cobrança usados para adicionar descontos e taxas extras às assinaturas do plano. |
| plan.chargeEvents.description | string | Descrição do evento de cobrança. |
| plan.chargeEvents.amount | int | Quantia do evento de cobrança. |
| plan.chargeEvents.mode | int | [Evento de cobrança aplicado a uma recorrência](../guias/primeiros-passos.md#chargeeventmode) |
| plan.chargeEvents.strategy | array | Estratégia do evento de cobrança. |
| plan.merchantId | string | Identificação do comerciante que criou este plano. |
| plan.isActive | bool | Define se o plano está ativo ou não. |
| plan.planItems | - | Os itens que irão compor o plano. |
| plan.planItems.itemCode | string | Código do item. |
| plan.planItems.description | string | A descrição do item. |
| plan.planItems.value | int | O valor do item. |
| plan.planItems.quantity | int | A quantidade do item. |
| plan.planItems.categoryId | string | A categoria que o item pertence. |
| plan.planFine | - | A multa que será aplicada ao plano caso não seja paga na data de vencimento. |
| plan.planFine.value | int | O valor da multa. |
| plan.planFine.daysAfterDueDate | int | Dias após a data de vencimento. |
| plan.planFine.interest | number | Os juros financeiros representam um valor em porcentagem que será calculado todos os dias após a data de vencimento. |
| plan.planDiscount | - | O desconto a ser aplicado ao plano. |
| plan.planDiscount.percentual | number | O valor do desconto em porcentagem. |
| plan.planDiscount.fixValue | number | O valor do desconto, valor fixo. |
| plan.planDiscount.dailyValue | number | Valor diário. |
| plan.planDiscount.dayBeforeTheDueDate | int | Dia antes da data de vencimento. |
| plan.closeInvoiceDay | int | O dia em que a fatura será fechada. |
| plan.bankSlipDueDateDay | int | O dia da data de vencimento do boleto bancário. |
| plan.paymentType | int | [Tipo de transação.](../guias/primeiros-passos.md#paymenttype) |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. Lembre-se de usar o {{accessToken}} |

<a id="body-raw-1"></a>

#### BODY Raw

```http
{
"id": "990f19be-02b2-4b8e-b153-86715225aa5c"
"plan": {
"amount": 10000,
"frequency": 3,
"label": "Academia",
"cycles": 12,
"merchantId": "22eb9083-ec20-4b5e-85d6-22cf9c35a898",
"isActive": true,
"paymentType": 2
}
}
```

<a id="get-plan-all"></a>

### `GET` /plan/all

**Versão** `v2.0`

<a id="requisição-http-2"></a>

#### Requisição HTTP

```http
GET {{ENDPOINT_GATEWAY}}/v2/plan/all
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/plan/all")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/plan/all"

payload={}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request GET '{{ENDPOINT_GATEWAY}}/v2/plan/all' \
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

fetch("{{ENDPOINT_GATEWAY}}/v2/plan/all", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "plans": [
        {
            "id": "990f19be-02b2-4b8e-b153-86715225aa5c",
            "amount": 10000,
            "frequency": "Monthly",
            "label": "Academia",
            "cycles": 12,
            "isActive": true,
            "paymentType": "Credit"
        }
    ],
    "success": true,
    "errors": [],
    "traceKey": "de8b01cb-d23e-400f-967f-e37ea43f3a91"
}
```

O Endpoint responsável por obter todos os planos relacionados ao comerciante solicitante.

<a id="requisição-2"></a>

#### Requisição

Utilizar all na requisição HTTP

<a id="resposta-2"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| Plans | array(object) | Todos os planos cadastrados. |
| plan.id | string | ID retornado na criação do plano. |
| plan.amount | int | Valor do plano em centavos. |
| plan.frequency | int | [A frequência com que uma assinatura deve ser cobrada.](../guias/primeiros-passos.md#frequency). |
| plan.label | string | Tag do plano definida pelo cliente. |
| plan.cycles | string | O número de vezes que suas assinaturas serão cobradas. |
| plan.chargeEvents | array(object) | Eventos de cobrança usados para adicionar descontos e taxas extras às assinaturas do plano. |
| plan.chargeEvents.description | string | Descrição do evento de cobrança. |
| plan.chargeEvents.amount | int | Quantia do evento de cobrança. |
| plan.chargeEvents.mode | int | [Evento de cobrança aplicado a uma recorrência](../guias/primeiros-passos.md#chargeeventmode) |
| plan.chargeEvents.strategy | array | Estratégia do evento de cobrança. |
| plan.merchantId | string | Identificação do comerciante que criou este plano. |
| plan.isActive | bool | Define se o plano está ativo ou não. |
| plan.planItems | array(object) | Os itens que irão compor o plano. |
| plan.planItems.itemCode | string | Código do item. |
| plan.planItems.description | string | A descrição do item. |
| plan.planItems.value | int | O valor do item. |
| plan.planItems.quantity | int | A quantidade do item. |
| plan.planItems.categoryId | string | A categoria que o item pertence. |
| plan.planFine | array(object) | A multa que será aplicada ao plano caso não seja paga na data de vencimento. |
| plan.planFine.value | int | O valor da multa. |
| plan.planFine.daysAfterDueDate | int | Dias após a data de vencimento. |
| plan.planFine.interest | number | Os juros financeiros representam um valor em porcentagem que será calculado todos os dias após a data de vencimento. |
| plan.planDiscount | array(object) | O desconto a ser aplicado ao plano. |
| plan.planDiscount.percentual | number | O valor do desconto em porcentagem. |
| plan.planDiscount.fixValue | number | O valor do desconto, valor fixo. |
| plan.planDiscount.dailyValue | number | Valor diário. |
| plan.planDiscount.dayBeforeTheDueDate | int | Dia antes da data de vencimento. |
| plan.closeInvoiceDay | int | O dia em que a fatura será fechada. |
| plan.bankSlipDueDateDay | int | O dia da data de vencimento do boleto bancário. |
| plan.paymentType | int | [Tipo de transação.](../guias/primeiros-passos.md#paymenttype) |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. Lembre-se de usar o {{accessToken}} |

<a id="delete-plan"></a>

### `DELETE` /plan

**Versão** `v2.0`

<a id="requisição-http-3"></a>

#### Requisição HTTP

```http
DELETE {{ENDPOINT_GATEWAY}}/v2/plan
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/plan?planId={{planId}}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/plan?planId={{planId}}"

payload={}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location -g --request DELETE '{{ENDPOINT_GATEWAY}}/v2/plan?planId={{planId}}' \
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

fetch("{{ENDPOINT_GATEWAY}}/v2/plan?planId={{planId}}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "success": true,
    "errors": [],
    "traceKey": "118e455d-20f9-4fce-afca-9c57d3df7f87"
}
```

O Endpoint responsável por excluir um plano existente por seu ID.

<a id="parâmetros-de-query"></a>

#### Parâmetros de query

| Parâmetro | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| planId | string | Sim | O ID do plano. |

<a id="resposta-3"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. Lembre-se de usar o {{accessToken}} |

| PARAMS | - |
| --- | --- |
| **planId** | {{planId}} |
| -- | O número identificador do plano. |

<a id="assinatura"></a>

## Assinatura

As assinaturas relacionam os clientes com os planos do estabelecimento. Sendo assim, formando as cobranças em cima dos planos e direcionando ao cliente que fez a assinatura.

<a id="regras-gerais"></a>

### Regras gerais

A edição de uma assinatura é permitida somente após 30 dias corridos a contar da data do primeiro pagamento. É permitida somente uma edição a cada 30 dias, portanto não será permitida edição de assinaturas com frequências do tipo diária ou semanal. Somente perfis Master e Adm. são permitidos para acessar a edição.

É permitido editar apenas os campos valor da cobrança ('amount'), descrição dos itens ('planItems.description') e dia da cobrança ('nextDayExecution').

Se a solicitação de alteração do dia da cobrança for para um dia inferior ao da solicitação, consequentemente, a cobrança dentro do mês em questão (da solicitação) não terá sido efetuada, portanto deverá ocorrer conforme provisionamento vigente e a alteração deverá ser acatada a partir da cobrança subsequente. Se a solicitação de alteração for para um dia superior ao da solicitação, a mudança poderá ser acatada para a partir da próxima parcela provisionada

<a id="exemplos"></a>

#### Exemplos

**1-** Dia atual da cobrança: 20
Próxima cobrança prevista: 20/02
Dia da solicitação da alteração: 10/02
Novo dia de cobrança solicitado: 05
No caso acima, a cobrança prevista para 20/02 deve permanecer inalterada e novo dia de cobrança solicitado, 05, deverá começar a valer somente no mês de fevereiro e seguir pelos meses subsequentes. 
 **2-** Dia atual da cobrança: 20
Próxima cobrança prevista: 20/02
Dia da solicitação da alteração: 10/02
Novo dia de cobrança solicitado: 25
No caso acima, o novo dia de cobrança solicitado poderá ser acatado a partir da próxima, ou seja, a parcela prevista para 20/02, será cancelada e a próxima cobrança será em 25/02 e da mesma forma nos meses subsequentes.

<a id="post-subscription"></a>

### `POST` /subscription

**Versão** `v2.0`

<a id="requisição-http-4"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/subscription
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/subscription")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{  \"customerId\": \"ffede3ee-37ab-47bb-9981-d3d14697d67a\",  \"sessionId\": \"123456789\",  \"subscription\": {    \"planId\": \"7d4a4d9f-d3f4-4fad-b290-663c38be6200\",    \"cardId\": \"7903ef09-83c3-458d-ad39-9ea9e736e59b\"  }}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/subscription"

payload="{  \"customerId\": \"ffede3ee-37ab-47bb-9981-d3d14697d67a\",  \"sessionId\": \"123456789\",  \"subscription\": {    \"planId\": \"7d4a4d9f-d3f4-4fad-b290-663c38be6200\",    \"cardId\": \"7903ef09-83c3-458d-ad39-9ea9e736e59b\"  }}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/subscription' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "customerId": "ffede3ee-37ab-47bb-9981-d3d14697d67a",
  "sessionId": "123456789",
  "subscription": {
    "planId": "7d4a4d9f-d3f4-4fad-b290-663c38be6200",
    "cardId": "7903ef09-83c3-458d-ad39-9ea9e736e59b"
  }
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"customerId":"ffede3ee-37ab-47bb-9981-d3d14697d67a","sessionId":"123456789","subscription":{"planId":"7d4a4d9f-d3f4-4fad-b290-663c38be6200","cardId":"7903ef09-83c3-458d-ad39-9ea9e736e59b"}});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/subscription", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "subscriptions": [
        {
            "id": "096d7bf9-45ee-4891-83ad-eda57b808ee3",
            "planId": "7d4a4d9f-d3f4-4fad-b290-663c38be6200",
            "cardId": "7903ef09-83c3-458d-ad39-9ea9e736e59b",
            "capture": true,
            "quantity": 1,
            "isActive": true,
            "nextExecution": "2021-07-17T00:00:00-03:00",
            "failedAttempts": 0,
            "charges": [
                "f9199878-79b2-4367-9832-a7392718c14a"
            ],
            "acquirerCode": "Simulator",
            "cycles":12,
            "subscriptionItems":[
            {
                "description":"teste 12 meses",
                "value":2500,
                "quantity":1
            }],
            "frequency":3
        }
    ],
    "success": true,
    "errors": [],
    "traceKey": "491df2aa-ab00-40a5-a836-72f3496564c7"
}
```

O Endpoint responsável por criar uma nova assinatura.

> **⚠️ IMPORTANTE - Device Fingerprint para Antifraude:**
>
> Se o [serviço de Antifraude](../guias/antifraude.md#device-fingerprint) estiver ativo para o seu estabelecimento, é **obrigatório** implementar o Device Fingerprint na página de checkout e enviar o campo `sessionId` na requisição.
>
> - **No Frontend (Device Fingerprint):** Use o formato `safrapay_br{{seuIdentificador}}`
> - **Na API (campo sessionId):** Use apenas `{{seuIdentificador}}` (sem o prefixo)
>
> **Exemplo:**
>
> - Device Fingerprint na página: `safrapay_br123456789`
> - API (sessionId): `123456789`
>
> 📖 Consulte a [documentação completa do Device Fingerprint e SDK SafraPay Antifraud](../guias/antifraude.md#device-fingerprint) para instruções de implementação.

> **💡 Campo Obrigatório - RemoteIp:**
>
> Além do `sessionId`, você **deve** fornecer o campo `remoteIp` quando o antifraude estiver ativo para complementar os dados de análise de risco:
>
> - **Obrigatório:** Fornecer o IP real do comprador quando antifraude estiver ativo
> - **Formato:** IPv4 (exemplo: `192.168.1.100`)
> - **Uso:** Utilizado em verificações de risco e prevenção de fraudes
> - **Prioridade:** Será priorizado sobre outras fontes de captura de IP
>
> 📖 Consulte a [documentação completa do RemoteIp](../guias/antifraude.md#campo-remoteip-complemento-ao-device-fingerprint) para mais informações.

<a id="requisição-3"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| customerId | string | Sim | O ID de cliente por meio do qual a assinatura será anexada. |
| sessionId | string | Condicional | ID da sessão criada pelo servidor do site do cliente e usada durante a visita de um determinado usuário. **Obrigatório se o Antifraude estiver ativo.** Deve corresponder ao mesmo identificador único utilizado no Device Fingerprint da página de checkout, porém sem o prefixo `safrapay_br`. [Ver documentação do Device Fingerprint](../guias/antifraude.md#device-fingerprint). |
| remoteIp | string | Sim | **\[OBRIGATÓRIO quando antifraude ativo\]** O endereço IP do comprador. Este dado é utilizado em verificações de risco (número de tentativas de pagamento ou verificações baseadas em localização). **Exemplo:** `192.168.1.100` |
| subscription | object | Sim | Informações da assinatura. |
| subscription.id | string | Não | O ID da assinatura. |
| subscription.planId | string | Sim | Consulta um plano criado anteriormente, que representa o modelo de assinatura. Este ID é único. |
| subscription.cardID | string | Sim | Consulta um cartão criado anteriormente. Este ID é único. |
| subscription.cardCvv | string | Não | Código de segurança do cartão. |
| subscription.capture | bool | Não | Indica se a transação deve ser capturada ou apenas pré-autorizadora. True para capturar a transação; False para pré-autorizar, deixando a captura pendente da transação. Valor padrão: verdadeiro. |
| subscription.lateCapture | bool | Não | Informe verdadeiro para realizar uma autorização com captura atrasada. Valor padrão: falso. |
| subscription.merchantSubscriptionId | string | Não | ID de assinatura, de preferência único, definido pelo estabelecimento. |
| subscription.quantity | int | Não | Quantidade de planos dentro da assinatura. |
| subscription.customAmount | int | Não | Novo valor da assinatura a ser cobrado, valor de substituição definido pelo plano. |
| subscription.isActive | bool | Não | Define se a assinatura estará ativa ou não. |
| subscription.nextExecution | string | Não | Na próxima vez, a assinatura será cobrada. |
| subscription.failedAttempts | int | Não | Número de cobranças com falha consecutivas. |
| subscription.charges | array(string) | Não | Lista de IDs de cobrança, bem-sucedidos ou não. |
| subscription.acquirerCode | int | Não | [O ID da adquirente.](../guias/primeiros-passos.md#acquirercode). |
| subscription.cycles | int | Não | Número de ciclos que a assinatura cobrará do cliente. |
| subscription.jobs | array(object) | Não | Tarefas recorrentes executadas no ciclo de vida da assinatura. |
| subscription.jobs.createAt | string | Não | Data de criação. |
| subscription.jobs.id | string | Não | O ID da tarefa da assinatura. |
| subscription.jobs.exception | object | Não | - |
| subscription.jobs.exception.typeName | string | Não | - |
| subscription.jobs.exception.message | string | Não | - |
| subscription.jobs.exception.stackTrace | string | Não | - |
| subscription.jobs.exception.source | string | Não | - |
| subscription.jobs.exceptionHandled | bool | Não | - |
| subscription.jobs.result | string | Não | - |
| subscription.jobs.arguments | array(string) | Não | - |
| subscription.jobs.classMethodName | string | Não | - |
| subscription.jobs.classTypeName | string | Não | - |
| subscription.subscriptionItems | object | Não | Itens da assinatura que irão compor a assinatura. |
| subscription.subscriptionItems.numberofExecutions | int | Não | Número de execuções efetuadas. |
| subscription.subscriptionItems.itemCode | string | Não | O código do item. |
| subscription.subscriptionItems.description | string | Não | Descrição do item. |
| subscription.subscriptionItems.value | int | Não | Valor do item. |
| subscription.subscriptionItems.quantity | int | Não | Quantidade do item. |
| subscription.subscriptionItems.categoryId | string | Não | O ID da categoria do item. |
| subscription.smartcheckoutId | string | Não | ID de Link de Pagamento ou Checkout. |
| subscription.frequency | int | Não | A frequência com que uma assinatura deve ser cobrada. |

<a id="resposta-4"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| subscriptions.id | string | O ID da assinatura. |
| subscriptions.planId | string | O ID do plano. |
| subscriptions.cardId | string | O ID do cartão. |
| subscriptions.quantity | int | Quantidade de planos dentro da assinatura |
| subscriptions.customAmount | int | Novo valor da assinatura a ser cobrado, valor de substituição definido pelo plano. |
| subscriptions.isActive | bool | Indica se a assinatura está ativa ou não. |
| subscriptions.nextExecution | string | Na próxima vez, a assinatura será cobrada. |
| subscriptions.failedAttempts | int | Quantidade de tentativas que falharam. |
| subscriptions.charges | array | Lista de IDs de cobrança, bem-sucedidos ou não. |
| subscriptions.acquirerCode | string | Nome da adquirente. |
| subscriptions.cycles | int | Número de ciclos que a assinatura cobrará do cliente. |
| subscriptions.subscriptionItems.description | string | Descrição do item. |
| subscriptions.subscriptionItems.value | int | Valor do item. |
| subscriptions.subscriptionItems.quantity | int | Quantidade do item. |
| subscriptions.frequency | int | A frequência com que uma assinatura deve ser cobrada. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. Lembre-se de usar o {{accessToken}} |

<a id="body-raw-2"></a>

#### BODY Raw

```http
{
"customerId": "ffede3ee-37ab-47bb-9981-d3d14697d67a",
"sessionId": "123456789",
"subscription": {
"planId": "7d4a4d9f-d3f4-4fad-b290-663c38be6200",
"cardId": "7903ef09-83c3-458d-ad39-9ea9e736e59b",
"cardCvv": "111",
"capture": true
}
}
```

<a id="post-subscription-bulk"></a>

### `POST` /subscription/bulk

**Versão** `v2.0`

<a id="requisição-http-5"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/subscription/bulk
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/subscription/bulk")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{  \"customerIds\": [    \"1980bc04-4c3c-4cdd-a7d5-b3b5771644b4\",    \"ffede3ee-37ab-47bb-9981-d3d14697d67a\"  ],  \"subscription\": {        \"planId\": \"11b10c11-56be-49d7-936b-e93a74ed2487\",        \"capture\": true    }}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/subscription/bulk"

payload="{  \"customerIds\": [    \"1980bc04-4c3c-4cdd-a7d5-b3b5771644b4\",    \"ffede3ee-37ab-47bb-9981-d3d14697d67a\"  ],  \"subscription\": {        \"planId\": \"11b10c11-56be-49d7-936b-e93a74ed2487\",        \"capture\": true    }}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/subscription/bulk' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "customerIds": [
    "1980bc04-4c3c-4cdd-a7d5-b3b5771644b4",
    "ffede3ee-37ab-47bb-9981-d3d14697d67a"
  ],
  "subscription": {
        "planId": "11b10c11-56be-49d7-936b-e93a74ed2487",
        "capture": true
    }
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({"customerIds":["1980bc04-4c3c-4cdd-a7d5-b3b5771644b4","ffede3ee-37ab-47bb-9981-d3d14697d67a"],"subscription":{"planId":"11b10c11-56be-49d7-936b-e93a74ed2487","capture":true}});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/subscription/bulk", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "subscriptions": [
        {
            "id": "1f15e647-7447-47b8-8b98-c1fc5a02dfe6",
            "planId": "13b10c28-56be-49d7-936b-e93a74ed2487",
            "cardId": "00000000-0000-0000-0000-000000000000",
            "capture": true,
            "quantity": 1,
            "isActive": true,
            "nextExecution": "2021-06-22T17:37:44.5810808-03:00",
            "failedAttempts": 0,
            "charges": [],
            "acquirerCode": "Undefined",
            "subscriptionItems": [
                {
                    "description": "Matricula",
                    "value": 1000,
                    "quantity": 1
                }
            ]
        },
        {
            "id": "180a64a9-e4bd-4ee2-863d-4677beafbbe7",
            "planId": "13b10c28-56be-49d7-936b-e93a74ed2487",
            "cardId": "00000000-0000-0000-0000-000000000000",
            "capture": true,
            "quantity": 1,
            "isActive": true,
            "nextExecution": "2021-06-22T17:37:44.5811087-03:00",
            "failedAttempts": 0,
            "charges": [],
            "acquirerCode": "Undefined",
            "subscriptionItems": [
                {
                    "description": "Matricula",
                    "value": 1000,
                    "quantity": 1
                }
            ]
        }
    ],
    "success": true,
    "errors": [],
    "traceKey": "bfabd6f7-616a-48c9-bc7f-0105cfe52dc5"
}
```

O Endpoint responsável por criar uma nova lista de assinatura.

> **⚠️ IMPORTANTE - Device Fingerprint para Antifraude:**
>
> Se o [serviço de Antifraude](../guias/antifraude.md#device-fingerprint) estiver ativo para o seu estabelecimento, é **obrigatório** implementar o Device Fingerprint na página de checkout e enviar o campo `sessionId` na requisição.
>
> - **No Frontend (Device Fingerprint):** Use o formato `safrapay_br{{seuIdentificador}}`
> - **Na API (campo sessionId):** Use apenas `{{seuIdentificador}}` (sem o prefixo)
>
> 📖 Consulte a [documentação completa do Device Fingerprint e SDK SafraPay Antifraud](../guias/antifraude.md#device-fingerprint) para instruções de implementação.

> **💡 Campo Opcional - RemoteIp:**
>
> Além do `sessionId`, você pode fornecer opcionalmente o campo `remoteIp` para complementar os dados de análise de risco. Consulte a [documentação completa do RemoteIp](../guias/antifraude.md#campo-remoteip-complemento-ao-device-fingerprint).

<a id="requisição-4"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| customerIds | array(string) | Sim | Os IDs de clientes por meio do qual a assinatura será anexada. |
| sessionId | string | Condicional | ID da sessão criada pelo servidor do site do cliente e usada durante a visita de um determinado usuário. **Obrigatório se o Antifraude estiver ativo.** Deve corresponder ao mesmo identificador único utilizado no Device Fingerprint da página de checkout, porém sem o prefixo `safrapay_br`. |
| remoteIp | string | Sim | **\[OBRIGATÓRIO quando antifraude ativo\]** O endereço IP do comprador. Utilizado em verificações de risco e prevenção de fraudes. **Exemplo:** `192.168.1.100` |
| subscription.id | string | Sim | O ID da assinatura. |
| subscription.planId | string | Sim | Consulta um plano criado anteriormente, que representa o modelo de assinatura. Este ID é único. |
| subscription.cardID | string | Sim | Consulta um cartão criado anteriormente. Este ID é único. |
| subscription.cardCvv | string | Sim | Código de segurança do cartão. |
| subscription.capture | bool | Não | Indica se a transação deve ser capturada ou apenas pré-autorizadora. True para capturar a transação; False para pré-autorizar, deixando a captura pendente da transação. Valor padrão: verdadeiro. |
| subscription.lateCapture | bool | Não | Informe verdadeiro para realizar uma autorização com captura atrasada. Valor padrão: falso. |
| subscription.merchantSubscriptionId | string | Não | ID de assinatura, de preferência único, definido pelo estabelecimento. |
| subscription.quantity | int | Não | Quantidade de planos dentro da assinatura. |
| subscription.customAmount | int | Não | Novo valor da assinatura a ser cobrado, valor de substituição definido pelo plano. |
| subscription.isActive | bool | Sim | Define se a assinatura estará ativa ou não. |
| subscription.nextExecution | string | Não | Na próxima vez, a assinatura será cobrada. |
| subscription.failedAttempts | int | Sim | Número de cobranças com falha consecutivas. |
| subscription.charges | array(string) | Não | Lista de IDs de cobrança, bem-sucedidos ou não. |
| subscription.acquirerCode | int | Sim | [O ID da adquirente.](../guias/primeiros-passos.md#acquirercode). |
| subscription.cycles | int | Não | Número de ciclos que a assinatura cobrará do cliente. |
| subscription.jobs | array(object) | Sim | Tarefas recorrentes executadas no ciclo de vida da assinatura. |
| subscription.jobs.createAt | string | Sim | Data de criação. |
| subscription.jobs.id | string | Não | O ID da tarefa da assinatura. |
| subscription.jobs.exception | object | Não | - |
| subscription.jobs.exception.typeName | string | Não | - |
| subscription.jobs.exception.message | string | Não | - |
| subscription.jobs.exception.stackTrace | string | Não | - |
| subscription.jobs.exception.source | string | Não | - |
| subscription.jobs.exceptionHandled | bool | Sim | - |
| subscription.jobs.result | string | Não | - |
| subscription.jobs.arguments | array(string) | Não | - |
| subscription.jobs.classMethodName | string | Não | - |
| subscription.jobs.classTypeName | string | Não | - |
| subscription.subscriptionItems | object | Não | Itens da assinatura que irão compor a assinatura. |
| subscription.subscriptionItems.numberofExecutions | int | Não | Número de execuções efetuadas. |
| subscription.subscriptionItems.itemCode | string | Não | O código do item. |
| subscription.subscriptionItems.description | string | Não | Descrição do item. |
| subscription.subscriptionItems.value | int | Não | Valor do item. |
| subscription.subscriptionItems.quantity | int | Não | Quantidade do item. |
| subscription.subscriptionItems.categoryId | string | Não | O ID da categoria do item. |
| subscription.smartcheckoutId | string | Não | ID de Link de Pagamento ou Checkout. |
| subscription.frequency | int | Não | A frequência com que uma assinatura deve ser cobrada. |
| lateCapture | bool | Não | Informar valor "true" para uma autorização com captura tardia. Valor padrão: false. |
| capture | bool | Sim | Se a cobrança deve ou não ser capturada. |
| templateId | string | Não | TemplateId que será usado para enviar o recibo ao cliente. |
| primaryColor | string | Não | A cor primária da configuração do comerciante. |
| secondaryColor | string | Não | A cor secundária da configuração do comerciante. |
| hostname | string | Não | O hostname da configuração do comerciante. |
| sessionId | string | Condicional | ID da sessão criada pelo servidor do site do cliente e usada durante a visita de um determinado usuário. **Obrigatório se o Antifraude estiver ativo.** Deve corresponder ao mesmo identificador único utilizado no Device Fingerprint da página de checkout, porém sem o prefixo `safrapay_br`. [Ver documentação do Device Fingerprint](../guias/antifraude.md#device-fingerprint). |
| remoteIp | string | Sim | **\[OBRIGATÓRIO quando antifraude ativo\]** Endereço IP do comprador. |

<a id="resposta-5"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| id | string | O ID da assinatura. |
| planId | string | O ID do plano. |
| cardId | string | O ID do cartão. |
| capture | bool | Indica se a transação deve ser capturada ou apenas pré-autorizadora. True para capturar a transação; False para pré-autorizar, deixando a captura pendente da transação. Valor padrão: verdadeiro. |
| lateCapture | bool | Informe verdadeiro para realizar uma autorização com captura atrasada. Valor padrão: falso. |
| merchantSubscriptionId | string | ID de assinatura, de preferência único, definido pelo estabelecimento. |
| quantity | int | Quantidade de planos dentro da assinatura |
| customAmount | int | Novo valor da assinatura a ser cobrado, valor de substituição definido pelo plano. |
| isActive | bool | Indica se a assinatura está ativa ou não. |
| nextExecution | string | Na próxima vez, a assinatura será cobrada. |
| failedAttempts | int | Quantidade de tentativas que falharam. |
| charge | array | Lista de IDs de cobrança, bem-sucedidos ou não. |
| acquirerCode | string | Nome da adquirente. |
| subscriptionItems.numberofExecutions | int | Número de execuções efetuadas. |
| subscriptionItems.itemCode | string | O código do item. |
| subscriptionItems.description | string | Descrição do item. |
| subscriptionItems.value | int | Valor do item. |
| subscriptionItems.quantity | int | Quantidade do item. |
| subscriptionItems.categoryId | string | O ID da categoria do item. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Não |
| errors.message | string | Não |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. Lembre-se de usar o {{accessToken}} |

<a id="body-raw-3"></a>

#### BODY Raw

```http
{
"customerIds": [
"1980bc04-4c3c-4cdd-a7d5-b3b5771644b4",
"ffede3ee-37ab-47bb-9981-d3d14697d67a"
],
"subscription": {
"planId": "11b10c11-56be-49d7-936b-e93a74ed2487",
"capture": true
}
}
```

<a id="put-subscription-cancelation-subscriptionid"></a>

### `PUT` /subscription/cancelation/{subscriptionId}

**Versão** `v2.0`

<a id="requisição-http-6"></a>

#### Requisição HTTP

```http
PUT {{ENDPOINT_GATEWAY}}/v2/subscription/cancelation/{subscriptionId}
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/subscription/cancelation/{{subscriptionId}}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/subscription/cancelation/{{subscriptionId}}"

payload={}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location -g --request PUT '{{ENDPOINT_GATEWAY}}/v2/subscription/cancelation/{{subscriptionId}}' \
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

fetch("{{ENDPOINT_GATEWAY}}/v2/subscription/cancelation/{{subscriptionId}}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "success": true,
    "errors": [],
    "traceKey": "b33677d9-6ce2-4d59-bb25-e4a2898671b7"
}
```

O Endpoint responsável por desativar uma assinatura.

<a id="parâmetros-de-rota"></a>

#### Parâmetros de rota

| Parâmetro | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| subscriptionId | string | Sim | ID GUID exclusivo da assinatura. |

<a id="resposta-6"></a>

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
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. Lembre-se de usar o {{accessToken}} |

<a id="get-subscription-subscriptionid"></a>

### `GET` /Subscription/{{subscriptionId}}

**Versão** `v2.0`

<a id="requisição-http-7"></a>

#### Requisição HTTP

```http
GET {{ENDPOINT_GATEWAY}}/v2/subscription/{{subscriptionId}}
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/subscription/{{subscriptionId}}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Get.new(url)
request["merchantId"] = "{{subscriptionId}}"
request["Authorization"] = "Bearer {{accessToken}}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/subscription/{{subscriptionId}}"

payload={}
headers = {
  'merchantId': '{{subscriptionId}}',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location -g --request GET '{{ENDPOINT_GATEWAY}}/v2/subscription/{{subscriptionId}}' \
--header 'merchantId: {{subscriptionId}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("merchantId", "{{subscriptionId}}");
myHeaders.append("Authorization", "Bearer {{accessToken}}");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/subscription/{{subscriptionId}}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "name": "Betina Stefany Gabrielly Nunes",
    "email": "betinastefanygabriellynunes@br.pwc.com",
    "startDate": "2021-07-13T19:40:02.000",
    "endDate": "2023-08-12T00:00:00",
    "amount": 1000,
    "cycles": 24,
    "isActive": true,
    "card": {
        "id": "9d3cc5d6-88d4-7954-a784-7e10ctt55f74",
        "cardNumber": "444458******4562",
        "brandName": "Visa",
        "cardholderName": "Betina Stefany Gabrielly Nunes",
        "expirationMonth": 12,
        "expirationYear": 2032,
        "billingAddress": {
            "street": "Avenida Lucio Costa",
            "number": "322",
            "neighborhood": "Barra da Tijuca",
            "city": "Rio de Janeiro",
            "state": "RJ",
            "country": "BR",
            "zipCode": "22795007"
        }
    },
    "frequency": 3,
    "charges": [
        {
            "id": "g9e58745-7895-1235-9632-c782d0999b7c",
            "chargeStatus": "Autorizada",
            "chargeDate": "2021-07-13T19:40:03.322",
            "amount": 1000
        }
    ],
    "planName": "Nome do Plano",
    "plan": {
        "id": "60e5c767-8647-465a-a73c-9fd075d00401",
        "amount": 1000,
        "frequency": 3,
        "cycles": 24,
        "freeCycles": 0,
        "frequencyTranslated": "Mensal",
        "label": "Descrição do plano",
        "isActive": true,
        "merchantId": "y099b10f-cd9c-9784-8cd9-781a99f2154c",
        "planItems": [
            {
                "description": "Item do plano",
                "value": 1000,
                "quantity": 1
            }
        ],
        "paymentType": "Credit"
    },
    "subscriptionItems": [],
    "invoices": [],
    "lastUpdate": "2021-07-13T19:40:02.000",
    "nextExecution": "2021-08-13T19:40:02.000",
    "nextExecutionJob": "2021-08-13T19:00:00.000",
    "success": true,
    "errors": [],
    "traceKey": "d4d39add-c875-4855-95c8-6f5de388aa53"
}
```

O Endpoint responsável por obter informações da assinatura pelo ID.

<a id="parâmetros-de-rota-1"></a>

#### Parâmetros de rota

| Parâmetro | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| subscriptionId | string | Sim | ID GUID exclusivo da assinatura. |

<a id="resposta-7"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| name | string | Nome do cliente. |
| email | string | E-mail do cliente. |
| startDate | string | Data de inicio da assinatura. |
| endDate | string | Data de término da assinatura. |
| amount | int | Valor da assinatura. |
| cycles | int | Número de vezes que a assinatura irá ser cobrada. |
| isActive | bool | Indica se a assinatura está ativa ou não. |
| card | - | Dados do cartão utilizado na assinatura. |
| card.id | string | ID do cartão utilizado. |
| card.cardNumber | string | Número do cartão mostrando apenas os 6 primeiros dígitos e os 4 últimos. |
| card.brandName | string | Bandeira do cartão. |
| card.cardholderName | string | Nome do titular do cartão. |
| card.expirationMonth | int | Mês da validade do cartão. |
| card.expirationYear | int | Ano da validade do cartão. |
| card.billingAddress | - | Dados de endereço do cartão. |
| card.billingAddress.street | string | Rua. |
| card.billingAddress.number | string | Número. |
| card.billingAddress.neighborhood | string | Bairro. |
| card.billingAddress.city | string | Cidade. |
| card.billingAddress.state | string | Estado. |
| card.billingAddress.country | string | País. |
| card.billingAddress.zipCode | string | Cep. |
| frequency | int | A frequencia do plano. |
| charges | array | Conjunto composto com as cobranças da assinatura. |
| charges.id | string | ID da cobrança. |
| charges.chargeStatus | string | Status da cobrança. |
| charges.chargeDate | string | Data em que a cobrança foi realizada. |
| charges.amount | int | Valor da cobrança. |
| planName | string | Nome do plano usado na assinatura. |
| plan | - | Dados do plano que foi usado na assinatura. |
| plan.id | string | ID do plano. |
| plan.amount | int | Valor do plano. |
| plan.frequency | int | Frequencia do plano. |
| plan.cycles | int | Número de vezes que a assinatura irá ser cobrada. |
| plan.freeCycles | int | Tempo de carência. |
| plan.frequencyTranslated | string | Indica a frequência do plano. |
| plan.label | string | Descrição sobre o plano. |
| plan.isActive | bool | Indica se o plano está ativo ou não. |
| plan.merchantId | string | O ID único do estabelecimento. |
| plan.planItems | array | Lista com os itens do plano. |
| plan.planItems.description | string | Descrição do item. |
| plan.planItems.value | int | O valor do item. |
| plan.planItems.quantity | int | A quantidade do item. |
| plan.paymentType | string | Indica o tipo de pagamento. |
| subscriptionItems | array | Lista com os itens da assinatura. |
| invoices | array | Lista com as faturas da assinatura. |
| lastUpdate | string | Data da última atualização da assinatura. |
| nextExecution | string | Data armazena o dia da cobrança. |
| nextExecutionJob | string | Data da próxima cobrança. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | Use o Merchant Token para gerar o `accessToken` do ENDPOINT_GATEWAY. |

<a id="patch-subscription-subscriptionid"></a>

### `PATCH` /subscription/{subscriptionId}

**Versão** `v2.0`

<a id="requisição-http-8"></a>

#### Requisição HTTP

```http
PACTH {{ENDPOINT_GATEWAY}}/v2/subscription/{subscriptionId}
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/subscription/{subscriptionId}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "nextDayExecution": 30,
  "planItems": [
    {
      "description": "string"
    }
  ]
})

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/subscription/{subscriptionId}"

payload = json.dumps({
  "nextDayExecution": 30,
  "planItems": [
    {
      "description": "string"
    }
  ]
})

headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/subscription/{subscriptionId}' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "nextDayExecution": 30,
  "planItems": [
    {
      "description": "string"
    }
  ]
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "nextDayExecution": 30,
  "planItems": [
    {
      "description": "string"
    }
  ]
});

var requestOptions = {
  method: 'PATCH',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/subscription/{subscriptionId}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
  "subscription": {
    "id": "096d7bf9-45ee-4891-83ad-eda57b808ee3",
    "planId": "7d4a4d9f-d3f4-4fad-b290-663c38be6200",
    "cardId": "7903ef09-83c3-458d-ad39-9ea9e736e59b",
    "capture": true,
    "quantity": 1,
    "customAmount": 2500,
    "isActive": true,
    "nextExecution": "2021-08-17T00:00:00",
    "failedAttempts": 0,
    "charges": [
      "f9199878-79b2-4367-9832-a7392718c14a",
      "77de44dd-2916-4c12-969c-c0b7eb00cf1e"
    ],
    "acquirerCode": "Simulator",
    "cycles": 12,
    "subscriptionItems": [
      {
        "description":"teste 12 meses",
        "value": 2500,
        "quantity": 1
      }
    ],
    "frequency": 3,
    "lastUpdate": "2021-07-17T03:00:07.542"
  },
  "success": true,
  "errors": [],
  "traceKey": "491df2aa-ab00-40a5-a836-72f3496564c7"
}
```

O Endpoint responsável por atualizar uma nova assinatura.

<a id="requisição-5"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| amount | int | Não | Novo valor da assinatura a ser cobrado, valor de substituição definido pelo plano. |
| isActive | bool | Não | Define se a assinatura estará ativa ou não. |
| nextDayExecution | int | Sim | Novo dia de cobrança que a assinatura será cobrada. |
| planItems | array(object) | Sim | Os itens que irão compor a assinatura. |
| planItems.numberofExecutions | int | Não | Número de execuções efetuadas. |
| planItems.itemCode | string | Não | O código do item. |
| planItems.description | string | Sim | Descrição do item. |
| planItems.value | int | Não | Valor do item. |
| planItems.quantity | int | Não | Quantidade do item. |
| planItems.categoryId | string | Não | O ID da categoria do item. |

<a id="resposta-8"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| subscriptions.id | string | O ID da assinatura. |
| subscriptions.planId | string | O ID do plano. |
| subscriptions.cardId | string | O ID do cartão. |
| subscriptions.capture | bool | Indica se a transação foi capturada ou apenas pré-autorizadora. |
| subscriptions.quantity | int | Quantidade de planos dentro da assinatura |
| subscriptions.customAmount | int | Novo valor da assinatura a ser cobrado, valor de substituição definido pelo plano. |
| subscriptions.isActive | bool | Indica se a assinatura está ativa ou não. |
| subscriptions.nextExecution | string | Data na próxima vez, a assinatura será cobrada. |
| subscriptions.failedAttempts | int | Quantidade de tentativas que falharam. |
| subscriptions.charges | array | Lista de IDs de cobrança, bem-sucedidos ou não. |
| subscriptions.acquirerCode | string | Nome da adquirente. |
| subscriptions.cycles | int | Número de ciclos que a assinatura cobrará do cliente. |
| subscriptions.subscriptionItems.description | string | Descrição do item. |
| subscriptions.subscriptionItems.value | int | Valor do item. |
| subscriptions.subscriptionItems.quantity | int | Quantidade do item. |
| subscriptions.frequency | int | A frequência com que uma assinatura deve ser cobrada. |
| subscriptions.lastUpdate | string | Data da última atualização da assinatura. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| errors.errorCode | int | Código do erro. |
| errors.message | string | Mensagem para identificar qual foi o erro retornado. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. Lembre-se de usar o {{accessToken}} |

<a id="body-raw-4"></a>

#### BODY Raw

```http
{
"nextDayExecution": 30,
"planItems": [
{
"description": "Plano MENSAL de teste atualiza"
}]
}
```

# 3DS - Pass through

Documentação do fluxo **Pass-Through** para autenticação **3DS** em transações comuns e recorrentes (**3RI / MIT**). Para detalhes adicionais do protocolo 3DS, consulte também [3DS no Gateway](gateway.md#3ds).

<a id="endpoints-envolvidos"></a>

## Endpoints envolvidos

| Endpoint | Método | Descrição |
| --- | --- | --- |
| `/v2/charge/ecommerce/3ds/setup` | POST | Inicializa autenticação 3DS |
| `/v2/charge/ecommerce/3ds/enrollment` | PUT | Processa enrollment 3DS |
| `/v2/charge/ecommerce` | PUT | Autoriza transação autenticada |
| `/v2/charge/preauthorization` | POST | Pré-autorização (MIT recorrente) |
| `/v2/charge/authorization` | POST | Autorização com captura (MIT recorrente) |

---

<a id="1-transação-comum-com-3ds"></a>

## 1. Transação comum com 3DS

<a id="post-v2-charge-ecommerce-3ds-setup"></a>

### `POST` /v2/charge/ecommerce/3ds/setup

**Versão** `v2.0`

Inicializa a sessão 3DS (Device Data Collection). Aceita payload **completo** (dados do cartão) ou **mínimo** (`customerId` + `cardId`).

<a id="requisição-http-9"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/charge/ecommerce/3ds/setup
```

> Exemplo de requisição (payload mínimo)

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/charge/ecommerce/3ds/setup' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "customerId": "fd43eb2d-0034-4274-882e-afd27ff65192",
  "transactions": [
    {
      "card": {
        "cardId": "ed8dc20b-4674-4eaa-89a5-7ba4dbe3d8b5"
      },
      "paymentType": 2
    }
  ],
  "source": 1
}'
```

<a id="requisição-6"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| customerId | string | Condicional | ID do cliente. Obrigatório no payload mínimo. |
| transactions | array | Sim | Lista de transações. |
| transactions\[\].card | object | Sim | Dados do cartão ou referência (`cardId`). |
| transactions\[\].card.cardId | string | Condicional | ID do cartão tokenizado (payload mínimo). |
| transactions\[\].card.number | string | Condicional | Número do cartão (payload completo). |
| transactions\[\].card.expirationMonth | int | Condicional | Mês de validade (payload completo). |
| transactions\[\].card.expirationYear | int | Condicional | Ano de validade (payload completo). |
| transactions\[\].card.cardholderName | string | Condicional | Nome do portador (payload completo). |
| transactions\[\].card.cardholderDocument | string | Condicional | Documento do portador (payload completo). |
| transactions\[\].card.billingAddress | object | Condicional | Endereço de cobrança (payload completo). |
| transactions\[\].paymentType | int | Sim | Tipo de pagamento (ex.: `2` = crédito). |
| source | int | Sim | Origem da transação. |

> O comando acima retorna um JSON estruturado assim:

```json
{
  "chargeId": "8cf35e58-f895-4a7a-8937-66a707f092a8",
  "transactions": [
    {
      "accessToken": "eyJhbGciOiJIUzI1NiIs...",
      "deviceDataCollectionUrl": "https://centinelapistag.cardinalcommerce.com/...",
      "cardholderAuthenticationReferenceId": "d82e58c1-20fc-4b57-894e-73f8fda737ca",
      "cardholderAuthenticationId": "7731709875686966104807",
      "pan": "400000******1000"
    }
  ],
  "success": true,
  "errors": [],
  "traceKey": "3a2f884b-a5ad-42a6-b6c0-ff4daf282971"
}
```

<a id="resposta-9"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| chargeId | string | ID da cobrança gerada para o fluxo 3DS. |
| transactions\[\].accessToken | string | Token para Device Data Collection. |
| transactions\[\].deviceDataCollectionUrl | string | URL para coleta de dados do navegador. |
| transactions\[\].cardholderAuthenticationReferenceId | string | Referência da autenticação. |
| transactions\[\].cardholderAuthenticationId | string | ID da autenticação do portador. |
| transactions\[\].pan | string | PAN mascarado. |
| success | bool | Indica sucesso da operação. |
| errors | array | Lista de erros (vazio em sucesso). |
| traceKey | string | Identificador de rastreamento. |

> Use `accessToken` e `deviceDataCollectionUrl` para coletar dados do navegador (Device Data Collection).

---

<a id="put-v2-charge-ecommerce-3ds-enrollment"></a>

### `PUT` /v2/charge/ecommerce/3ds/enrollment

**Versão** `v2.0`

Processa o enrollment 3DS. Aceita payload **completo** ou **mínimo** (`chargeId`, `browser` e `cardId`).

<a id="requisição-http-10"></a>

#### Requisição HTTP

```http
PUT {{ENDPOINT_GATEWAY}}/v2/charge/ecommerce/3ds/enrollment
```

> Exemplo de requisição (payload mínimo)

```bash
curl --location --request PUT '{{ENDPOINT_GATEWAY}}/v2/charge/ecommerce/3ds/enrollment' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "chargeId": "8cf35e58-f895-4a7a-8937-66a707f092a8",
  "browser": {
    "httpAcceptBrowserValue": "text/html",
    "httpAcceptContent": "text/html",
    "httpBrowserLanguage": "pt-BR",
    "httpBrowserJavaEnabled": false,
    "httpBrowserJavaScriptEnabled": true,
    "httpBrowserColorDepth": "24",
    "httpBrowserScreenHeight": "1080",
    "httpBrowserScreenWidth": "1920",
    "httpBrowserTimeDifference": "180",
    "userAgentBrowserValue": "Mozilla/5.0..."
  },
  "transactions": [
    {
      "amount": 5000,
      "card": {
        "cardId": "ed8dc20b-4674-4eaa-89a5-7ba4dbe3d8b5"
      }
    }
  ]
}'
```

<a id="requisição-7"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| chargeId | string | Sim | ID retornado no setup. |
| customer | object | Condicional | Dados do cliente (payload completo). |
| browser | object | Sim | Dados do navegador para autenticação. |
| transactions | array | Sim | Transações com valor e cartão. |
| transactions\[\].amount | int | Sim | Valor em centavos. |
| transactions\[\].card | object | Sim | Cartão completo ou `cardId`. |
| recurring | object | Não | Objeto de recorrência (apenas fluxo Pass-Through). Ver seção [Objeto recurring](#objeto-recurring-enrollment). |

> O comando acima retorna um JSON estruturado assim (frictionless):

```json
{
  "chargeId": "8cf35e58-f895-4a7a-8937-66a707f092a8",
  "chargeStatus": "PreAuthorized",
  "transactions": [
    {
      "cardholderAuthenticationVersion": "2.1.0",
      "cardholderAuthenticationStatus": "Approved",
      "directoryServer": "a7e103f3-2e0f-4804-860d-e50e6259de4b",
      "needRunAntifraud": false,
      "pan": "400000******1000",
      "eci": "05"
    }
  ],
  "success": true,
  "errors": [],
  "traceKey": "7070c7f3-26e7-4b34-84ce-a89ad7a4e1be"
}
```

<a id="resposta-10"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| chargeId | string | ID da cobrança. |
| chargeStatus | string | Status da cobrança (ex.: `PreAuthorized`). |
| transactions\[\].cardholderAuthenticationStatus | string | Status da autenticação (`Approved`, `challenged`, etc.). |
| transactions\[\].eci | string | ECI da autenticação. |
| transactions\[\].pan | string | PAN mascarado. |
| success | bool | Indica sucesso da operação. |
| traceKey | string | Identificador de rastreamento. |

> Se `stepUpUrl` ou `cardholderAuthenticationStatus` como `challenged` for retornado, exibir challenge ao portador antes de prosseguir.

---

<a id="put-v2-charge-ecommerce"></a>

### `PUT` /v2/charge/ecommerce

**Versão** `v2.0`

Autoriza a transação após autenticação 3DS aprovada. Quando `cardId` é informado, o envio de `cvv` é **opcional**.

<a id="requisição-http-11"></a>

#### Requisição HTTP

```http
PUT {{ENDPOINT_GATEWAY}}/v2/charge/ecommerce
```

> Exemplo de requisição

```bash
curl --location --request PUT '{{ENDPOINT_GATEWAY}}/v2/charge/ecommerce' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "chargeId": "8cf35e58-f895-4a7a-8937-66a707f092a8",
  "capture": true,
  "transactions": [
    {
      "installmentNumber": 1,
      "installmentType": 1,
      "card": {
        "cardId": "ed8dc20b-4674-4eaa-89a5-7ba4dbe3d8b5",
        "cvv": "123"
      }
    }
  ]
}'
```

<a id="requisição-8"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| chargeId | string | Sim | ID da cobrança do fluxo 3DS. |
| capture | bool | Sim | `true` para captura imediata. |
| transactions | array | Sim | Transações a autorizar. |
| transactions\[\].installmentNumber | int | Sim | Número de parcelas. |
| transactions\[\].installmentType | int | Sim | Tipo de parcelamento. |
| transactions\[\].card.cardId | string | Sim | ID do cartão tokenizado. |
| transactions\[\].card.cvv | string | Não | CVV (opcional quando `cardId` informado). |

> O comando acima retorna um JSON estruturado assim:

```json
{
  "charge": {
    "id": "8cf35e58-f895-4a7a-8937-66a707f092a8",
    "nsu": "000026801",
    "customerId": "fd43eb2d-0034-4274-882e-afd27ff65192",
    "chargeStatus": "Authorized",
    "transactions": [
      {
        "isApproved": true,
        "card": {
          "id": "ed8dc20b-4674-4eaa-89a5-7ba4dbe3d8b5",
          "number": "400000******1000",
          "brand": "Visa"
        },
        "paymentType": "Credit",
        "amount": 5000,
        "isCapture": true,
        "isRecurrency": false,
        "transactionStatus": "Captured",
        "eci": "05"
      }
    ]
  },
  "success": true,
  "errors": [],
  "traceKey": "a932b090-c3d1-49cf-bab7-393df8fe6bb0"
}
```

<a id="resposta-11"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| charge.id | string | ID da cobrança. |
| charge.chargeStatus | string | Status final (ex.: `Authorized`). |
| charge.transactions\[\].isApproved | bool | Indica aprovação. |
| charge.transactions\[\].isRecurrency | bool | Indica se é recorrente. |
| charge.transactions\[\].eci | string | ECI da autenticação. |
| success | bool | Indica sucesso da operação. |
| traceKey | string | Identificador de rastreamento. |

---

<a id="2-recorrência-pass-through-com-3ds-3ri-mit"></a>

## 2. Recorrência Pass-Through com 3DS + 3RI (MIT)

<a id="setup"></a>

### Setup

Idêntico ao fluxo comum (POST /v2/charge/ecommerce/3ds/setup).

<a id="enrollment-com-recurring"></a>

### Enrollment com `recurring`

O objeto `recurring` marca o início da série recorrente no **PUT /v2/charge/ecommerce/3ds/enrollment**.

> Exemplo de requisição (recorrência)

```bash
curl --location --request PUT '{{ENDPOINT_GATEWAY}}/v2/charge/ecommerce/3ds/enrollment' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "chargeId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "customer": {
    "name": "Marcelo Lima",
    "email": "marcelo@email.com",
    "documentType": 1,
    "document": "51947958909"
  },
  "browser": {
    "httpAcceptBrowserValue": "text/html",
    "httpAcceptContent": "text/html",
    "httpBrowserLanguage": "pt-BR",
    "httpBrowserJavaEnabled": false,
    "httpBrowserJavaScriptEnabled": true,
    "httpBrowserColorDepth": "24",
    "httpBrowserScreenHeight": "1080",
    "httpBrowserScreenWidth": "1920",
    "httpBrowserTimeDifference": "180",
    "userAgentBrowserValue": "Mozilla/5.0..."
  },
  "transactions": [
    {
      "amount": 10000,
      "card": {
        "cardId": "ed8dc20b-4674-4eaa-89a5-7ba4dbe3d8b5"
      }
    }
  ],
  "recurring": {
    "frequency": "Monthly",
    "totalPayments": 12
  }
}'
```

<a id="requisição-campos-adicionais"></a>

#### Requisição (campos adicionais)

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| recurring | object | Sim | Indica início da série recorrente. |
| recurring.frequency | string | Sim | Periodicidade (`Daily`, `Weekly`, `Monthly`, etc.). |
| recurring.totalPayments | int | Sim | Total de cobranças programadas (1–999). |

<a id="primeira-cobrança-recorrente-cit"></a>

### Primeira cobrança recorrente (CIT)

**PUT /v2/charge/ecommerce** — mesmo endpoint da seção 1.3. O `cvv` é **opcional** com `cardId`.

> Exemplo de requisição

```bash
curl --location --request PUT '{{ENDPOINT_GATEWAY}}/v2/charge/ecommerce' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "chargeId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "capture": true,
  "transactions": [
    {
      "installmentNumber": 1,
      "installmentType": 1,
      "card": {
        "cardId": "ed8dc20b-4674-4eaa-89a5-7ba4dbe3d8b5"
      }
    }
  ]
}'
```

> O comando acima retorna um JSON estruturado assim (guardar o `recurrencyId`):

```json
{
  "charge": {
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "chargeStatus": "Authorized",
    "transactions": [
      {
        "isApproved": true,
        "isRecurrency": true,
        "amount": 10000,
        "card": {
          "id": "ed8dc20b-4674-4eaa-89a5-7ba4dbe3d8b5",
          "number": "400000******1000",
          "brand": "Visa",
          "recurrencyId": "020019048898123"
        },
        "transactionStatus": "Captured"
      }
    ]
  },
  "success": true,
  "errors": []
}
```

<a id="resposta-campos-relevantes"></a>

#### Resposta (campos relevantes)

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| charge.transactions\[\].isRecurrency | bool | `true` na primeira cobrança recorrente. |
| charge.transactions\[\].card.recurrencyId | string | TID da primeira recorrência — **guardar para cobranças subsequentes**. |

---

<a id="post-v2-charge-preauthorization"></a>

### `POST` /v2/charge/preauthorization

**Versão** `v2.0`

Cobranças subsequentes **MIT** com pré-autorização.

> Quando `cardId` é informado e a transação é recorrente (`isRecurrency: true` ou `source: 4`), o Safrapay carrega automaticamente o `recurrencyId`. O envio de `recurrencyId` no payload é **opcional** e serve para sobrescrever o valor armazenado.

<a id="requisição-http-12"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/charge/preauthorization
```

> Exemplo de requisição

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/charge/preauthorization' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "charge": {
    "customer": {
      "id": "fd43eb2d-0034-4274-882e-afd27ff65192"
    },
    "transactions": [
      {
        "card": {
          "id": "ed8dc20b-4674-4eaa-89a5-7ba4dbe3d8b5",
          "recurrencyId": "020019048898123"
        },
        "paymentType": 2,
        "amount": 10000,
        "installmentNumber": 1,
        "isRecurrency": true
      }
    ],
    "source": 1
  }
}'
```

<a id="requisição-9"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| charge.customer.id | string | Sim | ID do cliente. |
| charge.transactions\[\].card.id | string | Sim | ID do cartão tokenizado. |
| charge.transactions\[\].card.recurrencyId | string | Não | TID da 1ª cobrança (sobrescreve valor armazenado). |
| charge.transactions\[\].paymentType | int | Sim | Tipo de pagamento. |
| charge.transactions\[\].amount | int | Sim | Valor em centavos. |
| charge.transactions\[\].isRecurrency | bool | Sim | `true` para MIT recorrente. |
| charge.source | int | Sim | Origem da transação. |

> O comando acima retorna um JSON estruturado assim:

```json
{
  "charge": {
    "chargeStatus": "PreAuthorized",
    "transactions": [
      {
        "isApproved": true,
        "isRecurrency": true,
        "amount": 10000,
        "card": {
          "id": "ed8dc20b-4674-4eaa-89a5-7ba4dbe3d8b5",
          "number": "400000******1000",
          "brand": "Visa",
          "recurrencyId": "020019048898123"
        },
        "transactionStatus": "PreAuthorized"
      }
    ]
  },
  "success": true,
  "errors": []
}
```

---

<a id="post-v2-charge-authorization"></a>

### `POST` /v2/charge/authorization

**Versão** `v2.0`

Cobranças subsequentes **MIT** com captura imediata.

<a id="requisição-http-13"></a>

#### Requisição HTTP

```http
POST {{ENDPOINT_GATEWAY}}/v2/charge/authorization
```

> Exemplo de requisição

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/charge/authorization' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "charge": {
    "customer": {
      "id": "fd43eb2d-0034-4274-882e-afd27ff65192"
    },
    "transactions": [
      {
        "card": {
          "id": "ed8dc20b-4674-4eaa-89a5-7ba4dbe3d8b5"
        },
        "paymentType": 2,
        "amount": 10000,
        "installmentNumber": 1,
        "isRecurrency": true
      }
    ],
    "source": 1
  }
}'
```

<a id="requisição-10"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| charge.customer.id | string | Sim | ID do cliente. |
| charge.transactions\[\].card.id | string | Sim | ID do cartão tokenizado. |
| charge.transactions\[\].amount | int | Sim | Valor em centavos. |
| charge.transactions\[\].isRecurrency | bool | Sim | `true` para MIT recorrente. |
| charge.source | int | Sim | Origem da transação. |

<a id="alternativa-source-4-recurrency"></a>

### Alternativa: `source = 4` (Recurrency)

Se `source: 4` for enviado, `isRecurrency: true` é inferido automaticamente:

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| charge.source | int | Sim | Use `4` para recorrência (infere `isRecurrency`). |

> Exemplo de requisição

```bash
curl --location --request POST '{{ENDPOINT_GATEWAY}}/v2/charge/authorization' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "charge": {
    "customer": {
      "id": "fd43eb2d-0034-4274-882e-afd27ff65192"
    },
    "transactions": [
      {
        "card": {
          "id": "ed8dc20b-4674-4eaa-89a5-7ba4dbe3d8b5"
        },
        "paymentType": 2,
        "amount": 10000,
        "installmentNumber": 1
      }
    ],
    "source": 4
  }
}'
```

---

<a id="resumo-dos-campos-por-modalidade"></a>

## Resumo dos campos por modalidade

| Campo | Comum 3DS | Recorrência 3DS + 3RI |
| --- | --- | --- |
| `enrollment.recurring` | -- | `{ frequency, totalPayments }` |
| `transaction.isRecurrency` | false | true (ou `source=4`) |
| `transaction.card.recurrencyId` | -- | TID da 1ª cobrança (subsequentes) |

<a id="regras-de-recurrencyid-nas-subsequentes"></a>

## Regras de `recurrencyId` nas subsequentes

- Quando `cardId` é informado e a transação é recorrente, o `recurrencyId` é **carregado automaticamente**.
- Se `recurrencyId` for enviado no payload: **sobrescreve** o valor armazenado.
- Se `recurrencyId` **não** for enviado: usa o valor salvo no ambiente Safrapay.
- O envio de `recurrencyId` no payload é **opcional** — necessário apenas quando se deseja usar um TID diferente do armazenado.

<a id="objeto-recurring-enrollment"></a>

## Objeto `recurring` (Enrollment)

Enviado no body do **PUT /v2/charge/ecommerce/3ds/enrollment** para indicar o início de uma série recorrente.

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| recurring.frequency | string (enum) | Sim | Periodicidade entre cobranças. |
| recurring.totalPayments | int | Sim | Total de cobranças programadas. Range: 1–999. |

> Exemplo do objeto:

```json
{
  "recurring": {
    "frequency": "Monthly",
    "totalPayments": 12
  }
}
```

<a id="valores-de-frequency"></a>

### Valores de `frequency`

| Valor | Descrição | Dias enviados à CyberSource |
| --- | --- | --- |
| `Daily` | Diário | 1 |
| `Weekly` | Semanal | 7 |
| `Monthly` | Mensal | 28 |
| `Quarterly` | Trimestral | 84 |
| `Biannual` | Semestral | 168 |
| `Annual` | Anual | 336 |

<a id="quando-não-enviar-recurring"></a>

### Quando NÃO enviar `recurring`

- Transações comuns com 3DS (sem recorrência).
- Cobranças subsequentes (MIT) via POST `/v2/charge/preauthorization` ou POST `/v2/charge/authorization` — estas não passam pelo enrollment.
