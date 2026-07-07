---
title: "Cobrança"
parent: "Referência da API"
nav_order: 70
layout: "doc"
permalink: "/api/cobranca/"
description: "A cobrança das transações, são os meios que serão utilizados nas mesmas. Exemplo: Boleto, crédito etc..."
source: "charge.html"
---

# Cobrança

A cobrança das transações, são os meios que serão utilizados nas mesmas. Exemplo: Boleto, crédito etc...

> **💡 Campo Opcional - RemoteIp:**
>
> Todos os endpoints de criação de cobrança suportam o campo opcional `remoteIp` para complementar a análise de risco e prevenção de fraudes.
>
> - **Recomendado:** Fornecer o IP real do comprador quando disponível
> - **Formato:** IPv4 (`192.168.1.100`) ou IPv6 completo
> - **Uso:** Utilizado em verificações de risco, detecção de múltiplas tentativas e validações de localização
>
> 📖 Consulte a [documentação completa do RemoteIp](../guias/antifraude.md#campo-remoteip-complemento-ao-device-fingerprint) e [Serviço de Antifraude](../guias/antifraude.md) para mais informações.

<a id="busca-de-cobrança"></a>

## Busca de cobrança

<a id="get-charge-chargeid"></a>

### `GET` /charge/{{chargeId}}

**Versão** `v2.0`

<a id="requisição-http"></a>

#### Requisição HTTP

```http
GET {{ENDPOINT_GATEWAY}}/v2/charge/{{chargeId}}
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/charge/{{chargeId}}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/charge/{{chargeId}}"

payload={}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location -g --request GET '{{ENDPOINT_GATEWAY}}/v2/charge/{{chargeId}}' \
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

fetch("{{ENDPOINT_GATEWAY}}/v2/charge/{{chargeId}}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "charge": {
        "merchantChargeId": "TASK5333",
        "id": "a7a1a873-ce15-5f83-a5fa-eb6f8637d102",
        "nsu": "000005047",
        "customerId": "ffede3ee-37ab-47bb-9971-d3d14697d67a",
        "chargeStatus": "Authorized",
        "transactions": [
            {
                "card": {
                    "id": "7903ef09-83c3-438d-ad39-9ea9e736e59b",
                    "customerId": "ffede3ee-37ab-47bb-9971-d3d14697d67a",
                    "cardNumber": "444458******4562",
                    "brand": "Visa",
                    "cardholderName": "Yago Sebastião Lima",
                    "cardholderDocument": "78112482802",
                    "isPrivateLabel": false,
                    "expirationMonth": 12,
                    "expirationYear": 2026,
                    "brandName": "Visa"
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
                "transactionId": "1624024252357",
                "transactionStatus": "Captured",
                "merchantTransactionId": "ff9624132c274c0ca878be991d3b6a87",
                "acquirer": "Simulator",
                "creationDateTime": "2021-06-18T10:50:52.37",
                "captureDateTime": "2021-06-18T10:50:52.37",
                "authorizationResponseCode": "00",
                "authorizationCode": "927648",
                "bankSlipStatus": 0,
                "payer": {
                "document": "81101910020",
                "name": "Jose da Silva",
                "ispbCode": "01234567",
                "bankCode": "01234567",
                "branch": "0001",
                "account": "12345678"
                 },
               "receiver": {
                "document": "11914993000123",
                "ispbCode": "58160789",
                "branch": "09700",
                "account": "0332840"
               }
            }
        ]
    },
    "success": true,
    "errors": [],
    "traceKey": "84272215-cfdd-42df-bfcd-4669ed40b269"
}
```

O Endpoint responsável por obter informações de uma cobrança pelo seu GUID ID ou NSU.

<a id="parâmetros-de-rota"></a>

#### Parâmetros de rota

| parâmetro | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| chargeId | string | Sim | O ID da cobrança. |

<a id="resposta"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| id | string | O ID da cobrança. |
| merchantChargeId | string | O ID de cobrança definido pelo sistema do comerciante. |
| customerId | string | O ID do comprador. |
| chargeStatus | string | Indica qual o status da cobrança. Ex: Não autorizado. |
| transactions | - | Uma ou várias transações a serem realizadas dentro da cobrança. |
| transactions.isApproved | bool | Indica se a transação foi aprovada ou não. |
| transactions.installmentType | string | [Tipo de parcelamento da transação](../guias/primeiros-passos.md#installmenttype) |
| transactions.installmentNumber | int | Numero de parcelas da transação, sendo **1** o valor mínimo. |
| transactions.amount | int | Valor a ser cobrado. Obrigatório se o checkout / link de pagamento não possui produto(s). |
| transactions.isCapture | bool | Indica se a cobrança foi capturada. |
| transactions.isRecurrency | bool | Indica se a cobrança é uma recorrência. |
| transactions.isCanceled | bool | Indica se a cobrança foi cancelada. |
| transactions.acquirer | string | O nome da adquirente. |
| transactions.creationDateTime | string | A data de criação da cobrança. |
| transactions.bankSlipStatus | int | Indica o status do boleto bancário. |
| transactions.bankIssuerNumber | string | O número do emissor do banco. |
| transactions.aditumNumber | string | O número transacional. |
| transactions.barcode | string | O código de barras do boleto. |
| transactions.digitalLine | string | Uma linha de transmissão que usa apenas código binário para recepção e emissão. |
| transactions.bankSlipId | string | O ID do boleto bancário. |
| transactions.payer | Payer | Pagador da cobrança. *Apenas Pix |
| transactions.receiver | Receiver | Recebedor da cobrança. *Apenas Pix |
| receivers | array | Informações dos recebedores, caso tenha cadastrado algum na cobrança. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| traceKey | string | Identificador da operação. |

<a id="payer"></a>

#### `Payer`

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| document | string | Documento de identificação do pagador (CPF ou CNPJ). |
| name | string | Nome do pagador |
| ispbCode | string | Código ISPB (Identificador do Sistema de Pagamentos Brasileiros) do banco do pagador. |
| bankCode | string | Código numérico do banco do pagador, conforme o padrão do Banco Central. |
| branch | string | Código da agência bancária onde a conta do pagador está registrada. |
| account | string | Número da conta bancária do pagador. |

<a id="receiver"></a>

#### `Receiver`

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| document | string | Documento de identificação do pagador (CPF ou CNPJ). |
| ispbCode | string | Código ISPB (Identificador do Sistema de Pagamentos Brasileiros) do banco do recebedor. |
| bankCode | string | Código numérico do banco do recebedor, conforme o padrão do Banco Central. |
| branch | string | Código da agência bancária onde a conta do recebedor está registrada. |
| account | string | Número da conta bancária do recebedor. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

| PARAMS | - |
| --- | --- |
| **chargeId** | {{chargeId}} |
| -- | O ID da cobrança. |

<a id="captura-de-cobrança"></a>

## Captura de cobrança

<a id="put-charge-capture-chargeid"></a>

### `PUT` /charge/capture/{{chargeId}}

**Versão** `v2.0`

<a id="requisição-http-1"></a>

#### Requisição HTTP

```http
PUT {{ENDPOINT_GATEWAY}}/v2/charge/capture/{{chargeId}}
```

> Exemplo de requisição

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/charge/capture/{{chargeId}}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/charge/capture/{{chargeId}}"

payload="{}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location -g --request PUT '{{ENDPOINT_GATEWAY}}/v2/charge/capture/{{chargeId}}' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({});

var requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/charge/capture/{{chargeId}}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "captured": true,
    "charge": {
        "merchantChargeId": "TASK5333",
        "id": "abcc2428-eb4e-4470-9d55-72edca459daf",
        "nsu": "000005044",
        "customerId": "ffede3ee-37ab-47bb-9981-d3d14697d67z",
        "chargeStatus": "Authorized",
        "transactions": [
            {
                "card": {
                    "id": "7903ef09-83c3-458d-ad39-9ea9e736e59b",
                    "customerId": "ffede3ee-37ab-47bb-9981-d3d14697d67z",
                    "cardNumber": "444458******4562",
                    "brand": "Visa",
                    "cardholderName": "Yago Sebastião Lima",
                    "cardholderDocument": "78112482802",
                    "isPrivateLabel": false,
                    "expirationMonth": 12,
                    "expirationYear": 2026,
                    "brandName": "Visa"
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
                "transactionId": "1623967391659",
                "transactionStatus": "Captured",
                "merchantTransactionId": "TASK5333",
                "acquirer": "Simulator",
                "creationDateTime": "2021-06-17T19:03:11.683",
                "captureDateTime": "2021-06-17T19:12:18.2281922-03:00",
                "authorizationResponseCode": "00",
                "authorizationCode": "304848",
                "bankSlipStatus": 0
            }
        ],
        "metadata": {
            "key_Sample": "Value_Sample"
        }
    },
    "success": true,
    "errors": [],
    "traceKey": "8e3bbb8b-f38e-4872-bcaa-5b858d143d0d"
}
```

O Endpoint responsável por capturar uma transação pré autorizada.

<a id="parâmetros-de-rota-1"></a>

#### Parâmetros de rota

| Parâmetro | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| chargeId | string | Sim | O ID da cobrança. |

<a id="requisição"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| amount | int | Não | Valor final que será capturado na transação. |
| source | int | Não | Origem da requisição. |
| receivers | array(object) | Não | Lista com informações dos recebedores envolvidos na transação. |
| receivers.id | string | Sim | ID do recebedor. |
| receivers.mdrDiscount | bool | Não | Define se terá desconto MDR. |
| receivers.fixedAmountComission | float | Não | Valor fixo que o destinatário deve receber. |
| receivers.chargeRemainder | bool | Não | Após processar os valores divididos para cada parte, se houver centavos que sobraram da divisão, este campo indica qual destinatário deverá receber os centavos restantes. Também pode ser definido para divisão de centavos (exemplo 100/3) ou para quando o destinatário não tiver regra especifica. |
| receivers.percentageComission | float | Não | Esta comissão é calculada no topo do valor da transação. |
| receivers.mdrComission | float | Não | Porcentagem relativa ao MDR calculado na liquidação. |
| receivers.membershipComission | float | Não | Comissão percentual para transações de associação. |
| receivers.amount | float | Não | Valor. |

<a id="resposta-1"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| captured | bool | Indica se a transação foi capturada. |
| merchantChargeId | string | O ID de cobrança definido pelo sistema do comerciante. |
| id | string | O ID da cobrança. |
| nsu | string | O número da transação. |
| customerId | string | O ID do comprador. |
| chargeStatus | string | Indica o status da cobrança. Ex: Autorizada. |
| transactions | - | Uma ou várias transações a serem realizadas dentro da cobrança. |
| transactions.card | - | O cartão utilizado na transação. |
| transactions.card.id | string | O ID do cartão. |
| transactions.card.customerId | string | O ID do comprador títular do cartão. |
| transactions.card.cardNumber | string | O número impresso na frente do cartão. |
| transactions.card.brand | string | A bandeira do cartão. |
| transactions.card.cardholderName | string | O nome do títular impresso na frente do cartão. |
| transactions.card.cardholderDocument | string | O documento do títular do cartão. |
| transactions.card.billingAddress | array | É o endereço conectado ao cartão de crédito ou débito. As empresas usam o endereço de cobrança para verificar o uso autorizado de tal cartão. É também para onde as empresas enviam contas em papel e extratos bancários. |
| transactions.card.billingAddress.street | string | Rua. |
| transactions.card.billingAddress.number | string | Número. |
| transactions.card.billingAddress.neighborhood | string | Bairro. |
| transactions.card.billingAddress.city | string | Cidade. |
| transactions.card.billingAddress.state | string | Estado. |
| transactions.card.billingAddress.country | string | País. |
| transactions.card.billingAddress.zipCode | string | CEP. |
| transactions.card.isPrivateLabel | bool | Indica se o cartão é um produto de whitelabel ou não. Whitelabel é um produto ou serviço que uma empresa produz e comercializa com outras empresas que tem interesse em utilizar o mesmo com sua marca estampada. |
| transactions.card.expirationMonth | int | O Mês de expiração do cartão com 2 dígitos. |
| transactions.card.expirationYear | int | O Ano de expiração do cartão com 4 dígitos. |
| transactions.card.fallback | bool | Uma bandeira que informa se a cobrança necessária será feita como fita magnética substituta. |
| transactions.card.brandName | string | O nome da bandeira do cartão. |
| transactions.isApproved | bool | Indica se a transação foi aprovada. |
| transactions.paymentType | string | Tipo de pagamento. |
| transactions.installmentType | string | [Tipo de parcelamento da transação](../guias/primeiros-passos.md#installmenttype) |
| transactions.installmentNumber | int | Numero de parcelas da transação, sendo **1** o valor mínimo. |
| transactions.softDescriptor | string | Breve descrição a ser apresentada na fatura bancária do cliente. Este campo aceita apenas strings compostas por letras (maiúsculas ou minúsculas), números e o caractere asterisco (*), sem espaços ou símbolos especiais. Se nulo, ele será preenchido com um rótulo padrão definido pela Safrapay. |
| transactions.amount | int | Valor a ser cobrado. Obrigatório se o checkout / link de pagamento não possui produto(s). |
| transactions.isCapture | bool | Indica se a cobrança foi capturada. |
| transactions.isRecurrency | bool | Indica se a cobrança é uma recorrência. |
| transactions.isCanceled | bool | Indica se a cobrança foi cancelada. |
| transactions.transactionId | string | Número Sequencial Único (NSU) da autorização, caso o pagamento seja aprovado pelo Emissor. |
| transactions.transactionStatus | string | Indica qual o status da transação. |
| transactions.merchantTransactionId | string | O ID da transação do Lojista |
| transactions.acquirer | string | O nome da adquirente. |
| transactions.creationDateTime | string | A data de criação da transação. |
| transactions.captureDateTime | string | A data de captura da transação. |
| transactions.bankSlipStatus | int | Status do boleto bancário. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

<a id="captura-parcial"></a>

## Captura Parcial

A captura parcial permite capturar uma reserva do valor menor do que o valor pré-autorizado.

Para realizar a captura parcial utilize o endpoint [PUT /charge/capture/{chargeId}](#put-charge-capture-chargeid), sendo necessário passar, através da propriedade `amount` no corpo da requisição, o valor desejado.

🚧 Obs.: Atenção! Não é possível realizar multíplas capturas. E caso `amount` não seja enviado, será considerado o valor integral da transação, se o valor de `amount` for enviado como `0` será retornado com um erro.

Exemplo: Em uma transação de aluguel de um produto/serviço por 3 dias, sendo cobrado R$ 50,00 por dia, totalizando R$ 150,00. Caso necessário finalizar a transação 1 dia antes do tempo acordado, é permitido efetuar a captura parcial na transação original com valor de R$ 150,00 passando o valor R$ 100,00(referente aos dias de uso).

<a id="cancelamento-de-cobrança"></a>

## Cancelamento de cobrança

> **Cartão de crédito — D+0 (estorno) e D+N (cancelamento)**
>
> - **Cancelamento no mesmo dia da captura (D+0)** equivale a **estorno**: não há cancelamento parcial, apenas **total**; o status é atualizado ainda **no dia** da solicitação.
> - **Cancelamento em dia posterior (D+N)** permite **cancelamento parcial ou total**; o processamento e a atualização de status seguem o fluxo em **D+N** (por exemplo, dia útil seguinte, conforme adquirente).

<a id="put-charge-cancelation-chargeid"></a>

### `PUT` /charge/cancelation/{chargeId}

**Versão** `v2.0`

<a id="requisição-http-2"></a>

#### Requisição HTTP

```http
PUT {{ENDPOINT_GATEWAY}}/v2/charge/cancelation/{{chargeId}}
```

> Exemplo de requisição (Cancelamento Total)

```ruby
require "uri"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/charge/cancelation/{{chargeId}}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = "{}"

response = https.request(request)
puts response.read_body
```

```python
import requests

url = "{{ENDPOINT_GATEWAY}}/v2/charge/cancelation/{{chargeId}}"

payload="{}"
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location -g --request PUT '{{ENDPOINT_GATEWAY}}/v2/charge/cancelation/{{chargeId}}' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({});

var requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/charge/cancelation/{{chargeId}}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

O Endpoint responsável por cancelar uma transação autorizada.

<a id="parâmetro-de-rota"></a>

#### Parâmetro de rota

| Parâmetro | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| chargeId | string | Sim | O ID da cobrança. |

<a id="requisição-1"></a>

#### Requisição

| Propriedade | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| antifraudCancel | bool | Não | Se a transação precisar ser cancelada, mas marcada como negada. |
| amount | int | Não | Valor parcial para cancelar. |
| source | int | Não | Origem da requisição. |
| receiverId | string | Não | ID do recebedor relacionado. |

<a id="resposta-2"></a>

#### Resposta

| Propriedade | Tipo | Descrição |
| --- | --- | --- |
| canceled | bool | Indica se a transação foi cancelada. |
| merchantChargeId | string | O ID de cobrança definido pelo sistema do comerciante. |
| id | string | O ID da cobrança. |
| nsu | string | O número da transação. |
| customerId | string | O ID do comprador. |
| chargeStatus | string | Indica o status da cobrança. Ex: Não autorizada. |
| transactions | - | Uma ou várias transações a serem realizadas dentro da cobrança. |
| transactions.card | - | O cartão utilizado na transação. |
| transactions.card.id | string | O ID do cartão. |
| transactions.card.customerId | string | O ID do comprador títular do cartão. |
| transactions.card.cardNumber | string | O número impresso na frente do cartão. |
| transactions.card.brand | string | A bandeira do cartão. |
| transactions.card.cardholderName | string | O nome do títular impresso na frente do cartão. |
| transactions.card.cardholderDocument | string | O documento do títular do cartão. |
| transactions.card.billingAddress | array | É o endereço conectado ao cartão de crédito ou débito. As empresas usam o endereço de cobrança para verificar o uso autorizado de tal cartão. É também para onde as empresas enviam contas em papel e extratos bancários. |
| transactions.card.billingAddress.street | string | Rua. |
| transactions.card.billingAddress.number | string | Número. |
| transactions.card.billingAddress.neighborhood | string | Bairro. |
| transactions.card.billingAddress.city | string | Cidade. |
| transactions.card.billingAddress.state | string | Estado. |
| transactions.card.billingAddress.country | string | País. |
| transactions.card.billingAddress.zipCode | string | CEP. |
| transactions.card.isPrivateLabel | bool | Indica se o cartão é um produto de whitelabel ou não. Whitelabel é um produto ou serviço que uma empresa produz e comercializa com outras empresas que tem interesse em utilizar o mesmo com sua marca estampada. |
| transactions.card.expirationMonth | int | O Mês de expiração do cartão com 2 dígitos. |
| transactions.card.expirationYear | int | O Ano de expiração do cartão com 4 dígitos. |
| transactions.card.fallback | bool | Uma bandeira que informa se a cobrança necessária será feita como fita magnética substituta. |
| transactions.card.brandName | string | O nome da bandeira do cartão. |
| transactions.isApproved | bool | Indica se a transação foi aprovada. |
| transactions.paymentType | string | Tipo de pagamento. |
| transactions.installmentType | string | [Tipo de parcelamento da transação](../guias/primeiros-passos.md#installmenttype) |
| transactions.installmentNumber | int | Numero de parcelas da transação, sendo **1** o valor mínimo. |
| transactions.softDescriptor | string | Breve descrição a ser apresentada na fatura bancária do cliente. Este campo aceita apenas strings compostas por letras (maiúsculas ou minúsculas), números e o caractere asterisco (*), sem espaços ou símbolos especiais. Se nulo, ele será preenchido com um rótulo padrão definido pela Safrapay. |
| transactions.amount | int | Valor a ser cobrado. Obrigatório se o checkout / link de pagamento não possui produto(s). |
| transactions.isCapture | bool | Indica se a cobrança foi capturada. |
| transactions.isRecurrency | bool | Indica se a cobrança é uma recorrência. |
| transactions.isCanceled | bool | Indica se a cobrança foi cancelada. |
| transactions.transactionId | string | Número Sequencial Único (NSU) da autorização, caso o pagamento seja aprovado pelo Emissor. |
| transactions.transactionStatus | string | Indica qual o status da transação. |
| transactions.merchantTransactionId | string | O ID da transação do Lojista |
| transactions.acquirer | string | O nome da adquirente. |
| transactions.errorCode | string | Indica o erro que foi apresentado na transação. |
| transactions.errorMessage | string | A mensagem explicativa referente ao `errorCode`. |
| transactions.creationDateTime | string | A data de criação da transação. |
| transactions.captureDateTime | string | A data de captura da transação. |
| transactions.bankSlipStatus | int | Status do boleto bancário. |
| success | bool | Se o endpoint processou a requisição com sucesso. |
| errors | array(object) | Se `success: false`, esse array contem a descrição dos erros retornados. |
| traceKey | string | Identificador da operação. |

| HEADERS | - |
| --- | --- |
| **Bearer Token** | {{accessToken}} |
| -- | BCrypt gerado a partir da concatenação do CNPJ da loja e o Merchant Token. |

<a id="cancelamento-parcial"></a>

## Cancelamento Parcial

> Exemplo de requisição (Cancelamento Parcial)

```ruby
require "uri"
require "json"
require "net/http"

url = URI("{{ENDPOINT_GATEWAY}}/v2/charge/cancelation/{{chargeId}}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = "Bearer {{accessToken}}"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "amount": 1000
})

response = https.request(request)
puts response.read_body
```

```python
import requests
import json

url = "{{ENDPOINT_GATEWAY}}/v2/charge/cancelation/{{chargeId}}"

payload = json.dumps({
  "amount": 1000
})
headers = {
  'Authorization': 'Bearer {{accessToken}}',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
```

```bash
curl --location -g --request PUT '{{ENDPOINT_GATEWAY}}/v2/charge/cancelation/{{chargeId}}' \
--header 'Authorization: Bearer {{accessToken}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "amount": 1000
}'
```

```javascript
var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer {{accessToken}}");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "amount": 1000
});

var requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("{{ENDPOINT_GATEWAY}}/v2/charge/cancelation/{{chargeId}}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

> O comando acima retorna um JSON estruturado assim:

```json
{
    "canceled": true,
    "charge": {
        "merchantChargeId": "TASK5333",
        "id": "7903ef09-83c3-458d-ad39-9ea9e736e59b",
        "nsu": "000005045",
        "customerId": "ffede3ee-37ab-47bb-9981-d3d14697d67z",
        "chargeStatus": "Canceled",
        "transactions": [
            {
                "card": {
                    "id": "7903ef09-83c3-458d-ad39-9ea9e736e59y",
                    "customerId": "ffede3ee-37ab-47bb-9981-d3d14697d67z",
                    "cardNumber": "444458******4562",
                    "brand": "Visa",
                    "cardholderName": "Yago Sebastião Lima",
                    "cardholderDocument": "78112482802",
                    "isPrivateLabel": false,
                    "expirationMonth": 12,
                    "expirationYear": 2026,
                    "brandName": "Visa"
                },
                "isApproved": true,
                "paymentType": "Credit",
                "installmentType": "None",
                "installmentNumber": 1,
                "softDescriptor": "TASK*5333",
                "amount": 1000,
                "isCapture": false,
                "isRecurrency": false,
                "isCanceled": true,
                "transactionId": "1623968171596",
                "transactionStatus": "Canceled",
                "merchantTransactionId": "TASK5333",
                "acquirer": "Simulator",
                "creationDateTime": "2021-06-17T19:16:11.602",
                "captureDateTime": "0001-01-01T00:00:00",
                "canceledDateTime": "2021-06-17T19:16:21.392273-03:00",
                "authorizationResponseCode": "00",
                "authorizationCode": "824057",
                "bankSlipStatus": 0
            }
        ],
        "metadata": {
            "key_Sample": "Value_Sample"
        }
    },
    "success": true,
    "errors": [],
    "traceKey": "3803a0fd-9cc7-4ec1-bb69-ae5b87912c34"
}
```

O cancelamento parcial permite efetuar múltiplos cancelamentos em uma transação, desde que a soma de todas as solicitações não excedam o valor original da transação, caso aconteça, o cancelamento será negado.

Para realizar o cancelamento parcial utilize o endpoint [PUT /charge/cancelation/{chargeId}](#put-charge-cancelation-chargeid), será necessário passar, através da propriedade `amount` no corpo da requisição, o valor desejado.

🚧 Obs.: Caso `amount` não seja enviado, será considerado o valor integral da transação, se o valor de `amount` for enviado como `0` será retornado com um erro.

Exemplo: Em uma transação de R$ 50,00, efetuando um Cancelamento Parcial de R$ 20,00, o status da transação permanecerá como Autorizada, porém com o valor ajustado para R$ 30,00. Nessa mesma transação ainda é permitido efetuar mais cancelamentos parciais, até que o valor de R$ 30,00 sejá atingido. Considerando que a primeira solicitação de cancelamento no valor de R$ 20,00 tenha sido acatada pelo Autorizador.
