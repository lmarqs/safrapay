---
title: "Visão Geral"
layout: home
nav_order: 0
permalink: /
description: "Documentação não oficial da API SafraPay: pagamentos, cobranças, recorrência, boletos, cartão protegido, TEF e webhooks."
---

# Documentação da API SafraPay

> **⚠️ Não oficial.** Esta documentação foi reconstruída por **engenharia reversa** do
> portal de desenvolvedores da SafraPay (ambiente de homologação). Ela serve como
> referência de integração e **não constitui garantia contratual**.
> Em caso de divergência, o portal oficial da SafraPay prevalece.

A SafraPay expõe APIs RESTful divididas por produto — **pagamento (gateway)**,
**gestão (portal)**, **webhook** e **conciliação**. Todas usam JSON como media-type
padrão, JWT como *Bearer token* na autenticação e encoding UTF-8.

## Por onde começar

1. **[Primeiros Passos](guias/primeiros-passos.md)** — endpoints, variáveis, cartões de teste, pontos de atenção de sandbox, códigos de erro e enumeradores.
2. **[Autenticação](api/autenticacao.md)** — gere o token de acesso antes de chamar qualquer endpoint.
3. **[Pagamentos (Gateway)](api/gateway.md)** — crie compradores e realize cobranças (crédito, PIX, 3DS).

## Ambientes

| Variável | Homologação | Produção |
| --- | --- | --- |
| `{{ENDPOINT_GATEWAY}}` | `https://payment-hml.safrapay.com.br` | `https://payment.safrapay.com.br` |
| `{{ENDPOINT_WEBHOOK}}` | `https://webhook-hml.safrapay.com.br` | `https://webhook.safrapay.com.br` |
| `{{ENDPOINT_RECONCILIATION}}` | `https://reconciliation-api-hml.safrapay.com.br` | `https://reconciliation-api.safrapay.com.br` |
| `{{OAUTH_URL}}` (portal) | `https://portal-hml.safrapay.com.br` | `https://portal.safrapay.com.br` |

> **ℹ️ Teste sempre em homologação primeiro.** Cobranças, capturas e estornos têm
> efeito financeiro real em produção.

## Autenticação em resumo

1. `POST {{ENDPOINT_GATEWAY}}/v2/merchant/auth` com o `MerchantToken` no header `Authorization`.
2. Guarde o `accessToken` (JWT, expira em ~30 minutos) e o `refreshToken`.
3. Envie `Authorization: Bearer {{accessToken}}` nas demais chamadas.
4. Renove com `POST {{ENDPOINT_GATEWAY}}/v2/refreshtoken` usando o `refreshToken`.

Detalhes em **[Autenticação](api/autenticacao.md)**.

## Mapa da documentação

### Guias
- [Primeiros Passos](guias/primeiros-passos.md) — fundamentos da integração.
- [Antifraude](guias/antifraude.md) — device fingerprint e campos obrigatórios.
- [Chargeback](guias/chargeback.md) — API de contestações.
- [Integrações com Plataformas](guias/integracoes.md) — VTEX, Magento, WooCommerce, Wbuy, Opencart e outras.
- [Smart POS](guias/smart-pos.md) — guia para desenvolvedores da maquininha.
- [Monitor de API (Tracer)](guias/monitor-de-api.md) e [Monitor de Webhooks](guias/monitor-de-webhooks.md) — ferramentas de observabilidade do portal.

### Referência da API
- [Autenticação](api/autenticacao.md)
- [Pagamentos (Gateway)](api/gateway.md) — compradores, cobranças, 3DS, PIX, produtos.
- [Link de Pagamentos](api/link-de-pagamento.md) e [Checkout](api/checkout.md)
- [Boletos](api/boletos.md) · [Taxas](api/taxas.md) · [Cobrança](api/cobranca.md)
- [Cartão Protegido](api/cartao-protegido.md) — tokenização de cartões.
- [Recorrência e Planos](api/recorrencia.md) — planos e assinaturas.
- [Webhooks](api/webhooks.md) · [TEF](api/tef.md)

### Referência rápida
- [Índice de Endpoints](referencia/endpoints.md) — todos os endpoints em uma tabela.
- [Enumeradores](referencia/enumeradores.md) — valores de todos os enums.
- [Variáveis](referencia/variaveis.md) — glossário dos marcadores `{{variavel}}`.

---

*Estrutura, convenções e como manter esta documentação: veja [`TEMPLATES.md`](TEMPLATES.md) e [`README.md`](README.md).*
