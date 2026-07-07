---
title: "Endpoints"
parent: "Referência"
nav_order: 10
layout: "doc"
permalink: "/referencia/endpoints/"
description: "Índice completo de todos os endpoints da API SafraPay documentados aqui."
---


# Índice de Endpoints

Total: **79 endpoints** documentados. Clique no caminho para abrir a documentação completa do endpoint.

| Método | Caminho | Recurso |
| --- | --- | --- |
| `POST` | [`/merchant/auth`](../api/autenticacao.md#post-merchant-auth) | Autenticação |
| `POST` | [`/refreshtoken`](../api/autenticacao.md#post-refreshtoken) | Autenticação |
| `POST` | [`/customer`](../api/gateway.md#post-customer) | Pagamentos (Gateway) |
| `PUT` | [`/customer`](../api/gateway.md#put-customer) | Pagamentos (Gateway) |
| `GET` | [`/customer`](../api/gateway.md#get-customer) | Pagamentos (Gateway) |
| `POST` | [`/charge/authorization`](../api/gateway.md#post-charge-authorization) | Pagamentos (Gateway) |
| `POST` | [`/charge/authorization`](../api/gateway.md#post-charge-authorization-1) | Pagamentos (Gateway) |
| `POST` | [`/charge/authorization`](../api/gateway.md#post-charge-authorization-2) | Pagamentos (Gateway) |
| `POST` | [`/charge/preauthorization`](../api/gateway.md#post-charge-preauthorization) | Pagamentos (Gateway) |
| `POST` | [`/charge/preauthorization`](../api/gateway.md#post-charge-preauthorization-1) | Pagamentos (Gateway) |
| `POST` | [`/charge/authorization`](../api/gateway.md#post-charge-authorization-3) | Pagamentos (Gateway) |
| `POST` | [`/charge/authorization`](../api/gateway.md#post-charge-authorization-4) | Pagamentos (Gateway) |
| `POST` | [`/v2/charge/ecommerce/3ds/setup`](../api/gateway.md#post-v2-charge-ecommerce-3ds-setup) | Pagamentos (Gateway) |
| `PUT` | [`/v2/charge/ecommerce/3ds/enrollment`](../api/gateway.md#put-v2-charge-ecommerce-3ds-enrollment) | Pagamentos (Gateway) |
| `PUT` | [`/v2/charge/ecommerce`](../api/gateway.md#put-v2-charge-ecommerce) | Pagamentos (Gateway) |
| `POST` | [`/product`](../api/gateway.md#post-product) | Pagamentos (Gateway) |
| `GET` | [`/product`](../api/gateway.md#get-product) | Pagamentos (Gateway) |
| `PUT` | [`/product/{productId}`](../api/gateway.md#put-product-productid) | Pagamentos (Gateway) |
| `GET` | [`/product/{productId}`](../api/gateway.md#get-product-productid) | Pagamentos (Gateway) |
| `POST` | [`/charge/pix`](../api/gateway.md#post-charge-pix) | Pagamentos (Gateway) |
| `GET` | [`/Card/Bin/Brand/{bin}`](../api/gateway.md#get-card-bin-brand-bin) | Pagamentos (Gateway) |
| `POST` | [`/paymentlink`](../api/link-de-pagamento.md#post-paymentlink) | Link de Pagamentos |
| `GET` | [`/smartcheckout/{smartcheckoutId}/detail`](../api/link-de-pagamento.md#get-smartcheckout-smartcheckoutid-detail) | Link de Pagamentos |
| `DELETE` | [`/smartcheckout/{smartcheckoutId}`](../api/link-de-pagamento.md#delete-smartcheckout-smartcheckoutid) | Link de Pagamentos |
| `GET` | [`/smartcheckout`](../api/link-de-pagamento.md#get-smartcheckout) | Link de Pagamentos |
| `POST` | [`/smartcheckout`](../api/checkout.md#post-smartcheckout) | Checkout |
| `GET` | [`/smartcheckout/{smartcheckoutId}/detail Checkout`](../api/checkout.md#get-smartcheckout-smartcheckoutid-detail-checkout) | Checkout |
| `POST` | [`/charge/boleto`](../api/boletos.md#post-charge-boleto) | Boletos |
| `GET` | [`/charge/{{chargeId}}/boleto/{{transactionId}}`](../api/boletos.md#get-charge-chargeid-boleto-transactionid) | Boletos |
| `POST` | [`/tax`](../api/taxas.md#post-tax) | Taxas |
| `GET` | [`/tax`](../api/taxas.md#get-tax) | Taxas |
| `PUT` | [`/tax`](../api/taxas.md#put-tax) | Taxas |
| `DELETE` | [`/tax/{taxPlanId}`](../api/taxas.md#delete-tax-taxplanid) | Taxas |
| `PUT` | [`/tax/Activate/{{taxPlanId}}`](../api/taxas.md#put-tax-activate-taxplanid) | Taxas |
| `GET` | [`/charge/{{chargeId}}`](../api/cobranca.md#get-charge-chargeid) | Cobrança |
| `PUT` | [`/charge/capture/{{chargeId}}`](../api/cobranca.md#put-charge-capture-chargeid) | Cobrança |
| `PUT` | [`/charge/cancelation/{chargeId}`](../api/cobranca.md#put-charge-cancelation-chargeid) | Cobrança |
| `POST` | [`/card`](../api/cartao-protegido.md#post-card) | Cartão Protegido |
| `PUT` | [`/card`](../api/cartao-protegido.md#put-card) | Cartão Protegido |
| `GET` | [`/card`](../api/cartao-protegido.md#get-card) | Cartão Protegido |
| `GET` | [`/card/byCustomer`](../api/cartao-protegido.md#get-card-bycustomer) | Cartão Protegido |
| `DELETE` | [`/card/{cardId}`](../api/cartao-protegido.md#delete-card-cardid) | Cartão Protegido |
| `POST` | [`/temporary/card`](../api/cartao-protegido.md#post-temporary-card) | Cartão Protegido |
| `POST` | [`/card/validation/zerodollar`](../api/cartao-protegido.md#post-card-validation-zerodollar) | Cartão Protegido |
| `POST` | [`/plan`](../api/recorrencia.md#post-plan) | Recorrência e Planos |
| `PUT` | [`/plan`](../api/recorrencia.md#put-plan) | Recorrência e Planos |
| `GET` | [`/plan/all`](../api/recorrencia.md#get-plan-all) | Recorrência e Planos |
| `DELETE` | [`/plan`](../api/recorrencia.md#delete-plan) | Recorrência e Planos |
| `POST` | [`/subscription`](../api/recorrencia.md#post-subscription) | Recorrência e Planos |
| `POST` | [`/subscription/bulk`](../api/recorrencia.md#post-subscription-bulk) | Recorrência e Planos |
| `PUT` | [`/subscription/cancelation/{subscriptionId}`](../api/recorrencia.md#put-subscription-cancelation-subscriptionid) | Recorrência e Planos |
| `GET` | [`/Subscription/{{subscriptionId}}`](../api/recorrencia.md#get-subscription-subscriptionid) | Recorrência e Planos |
| `PATCH` | [`/subscription/{subscriptionId}`](../api/recorrencia.md#patch-subscription-subscriptionid) | Recorrência e Planos |
| `POST` | [`/v2/charge/ecommerce/3ds/setup`](../api/recorrencia.md#post-v2-charge-ecommerce-3ds-setup) | Recorrência e Planos |
| `PUT` | [`/v2/charge/ecommerce/3ds/enrollment`](../api/recorrencia.md#put-v2-charge-ecommerce-3ds-enrollment) | Recorrência e Planos |
| `PUT` | [`/v2/charge/ecommerce`](../api/recorrencia.md#put-v2-charge-ecommerce) | Recorrência e Planos |
| `POST` | [`/v2/charge/preauthorization`](../api/recorrencia.md#post-v2-charge-preauthorization) | Recorrência e Planos |
| `POST` | [`/v2/charge/authorization`](../api/recorrencia.md#post-v2-charge-authorization) | Recorrência e Planos |
| `POST` | [`/v1/merchant/auth`](../guias/chargeback.md#gerar-token-de-autenticação) | Chargeback |
| `GET` | [`/v1/disputes/summary`](../guias/chargeback.md#consultar-disputa-sumário) | Chargeback |
| `GET` | [`/v1/disputes/total`](../guias/chargeback.md#totais-de-disputas) | Chargeback |
| `GET` | [`/v1/disputes/{disputeId}`](../guias/chargeback.md#detalhes-da-disputa) | Chargeback |
| `POST` | [`/v1/disputes/{disputeId}/debts/accept`](../guias/chargeback.md#acatar-débito-da-disputa) | Chargeback |
| `POST` | [`/v1/disputes/second-presentment`](../guias/chargeback.md#criar-representação-secundária) | Chargeback |
| `POST` | [`/webhook/bulk`](../api/webhooks.md#post-webhook-bulk) | Webhooks |
| `GET` | [`/webhook`](../api/webhooks.md#get-webhook) | Webhooks |
| `PUT` | [`/Webhook/Cancel/{webhookId}`](../api/webhooks.md#put-webhook-cancel-webhookid) | Webhooks |
| `POST` | [`Init`](../api/tef.md#post-init) | TEF |
| `POST` | [`Payment`](../api/tef.md#post-payment) | TEF |
| `GET` | [`Abort`](../api/tef.md#get-abort) | TEF |
| `GET` | [`Cancelation`](../api/tef.md#get-cancelation) | TEF |
| `GET` | [`Reversal`](../api/tef.md#get-reversal) | TEF |
| `GET` | [`GetPending`](../api/tef.md#get-getpending) | TEF |
| `GET` | [`Confirm`](../api/tef.md#get-confirm) | TEF |
| `GET` | [`Display`](../api/tef.md#get-display) | TEF |
| `POST` | [`DataPicker`](../api/tef.md#post-datapicker) | TEF |
| `GET` | [`WaitEvent`](../api/tef.md#get-waitevent) | TEF |
| `GET` | [`Status`](../api/tef.md#get-status) | TEF |
| `GET` | [`RemoveCard`](../api/tef.md#get-removecard) | TEF |
