---
title: "Monitor de Webhooks"
parent: "Guias"
nav_order: 70
layout: "doc"
permalink: "/guias/monitor-de-webhooks/"
description: "O Monitor de Webhooks é uma ferramenta para desenvolvedores em fase de integração que ainda não possuem um endpoint próprio para receber webhooks. Com ele, você"
source: "webhook-view-doc.html"
---

# Monitor de Webhooks

O **Monitor de Webhooks** é uma ferramenta para **desenvolvedores em fase de integração** que ainda não possuem um endpoint próprio para receber webhooks. Com ele, você pode visualizar e validar as notificações enviadas pela API SafraPay durante o desenvolvimento, sem precisar implementar um servidor imediatamente.

<a id="visão-geral"></a>

## 📊 Visão Geral

O Monitor de Webhooks oferece:

- **Visualização em tempo real** - Veja todos os webhooks enviados pela SafraPay
- **Sem necessidade de endpoint próprio** - Use durante o desenvolvimento inicial
- **Ambiente de testes** - Perfeito para validação de integração em homologação
- **Histórico de notificações** - Consulte webhooks anteriores
- **Estrutura completa** - Analise payloads JSON detalhados

<a id="para-quem-é-esta-ferramenta"></a>

## 🎯 Para Quem é Esta Ferramenta?

O Monitor de Webhooks é ideal para:

- **Desenvolvedores iniciando a integração** - Ainda não tem servidor para receber webhooks
- **Testes em homologação** - Validar estrutura e conteúdo dos webhooks
- **Debug rápido** - Verificar se webhooks estão sendo enviados corretamente
- **Aprendizado** - Entender como funcionam as notificações da SafraPay

<a id="alternativas-para-recepção-de-webhooks"></a>

## 💡 Alternativas para Recepção de Webhooks

<a id="durante-o-desenvolvimento"></a>

### Durante o Desenvolvimento

Existem algumas opções para receber webhooks durante o desenvolvimento:

**1. Monitor de Webhooks SafraPay (Esta Ferramenta)**

- Endpoint interno fornecido pela SafraPay
- Armazena webhooks automaticamente
- Visualização via interface web
- Ideal para início da integração

**2. URLs Temporárias**

- Ferramentas como [https://typedwebhook.tools/](https://typedwebhook.tools/)
- Útil para testes rápidos
- Temporárias e não recomendadas para uso contínuo

**3. Endpoint Próprio (Produção)**

- Solução definitiva para produção
- Consulte a [Documentação de Webhooks](../api/webhooks.md) para implementação completa
- Inclui validação de assinatura, segurança e melhores práticas

⚠️ **Importante**: Para **produção**, você deve implementar seu próprio endpoint seguindo as práticas da [Documentação de Webhooks](../api/webhooks.md).

<a id="como-acessar"></a>

## 🚀 Como Acessar

1. Faça login no Portal de Desenvolvedores SafraPay
2. No menu lateral, acesse **Ferramentas > Monitor de Webhooks**
3. Você verá imediatamente os webhooks mais recentes do **ambiente de homologação**

⚠️ **Nota**: Esta ferramenta monitora apenas webhooks do ambiente de **sandbox/homologação**.

<a id="funcionalidades-principais"></a>

## 🔍 Funcionalidades Principais

<a id="1-listagem-de-webhooks"></a>

### 1. Listagem de Webhooks

A tela principal exibe uma lista paginada com os webhooks recebidos, mostrando:

- **Charge ID** - Identificador da cobrança (GUID)
- **Status** - Estado atual da cobrança (badges coloridos)
- **Amount** - Valor da cobrança
- **Customer Name** - Nome do cliente
- **Timestamp** - Data e hora do webhook

<a id="2-status-badges"></a>

### 2. Status Badges

Cada webhook exibe um badge colorido indicando o status da cobrança:

- 🟢 **Paid** (Pago) - Verde
- 🟡 **Pending** (Pendente) - Amarelo
- 🔴 **Cancelled** (Cancelado) - Vermelho
- 🟠 **Refunded** (Estornado) - Laranja
- ⚫ **Expired** (Expirado) - Cinza

<a id="3-filtros"></a>

### 3. Filtros

Use os filtros para encontrar webhooks específicos:

<a id="por-charge-id"></a>

#### **Por Charge ID**

Digite o identificador da cobrança (GUID):

**Exemplo:** `870e8c97-0f47-4b20-b161-5b78c33f18c7`

<a id="por-status"></a>

#### **Por Status**

Filtre por estado da cobrança:

- Paid (Pago)
- Pending (Pendente)
- Cancelled (Cancelado)
- Refunded (Estornado)
- Expired (Expirado)
- Failed (Falha)

<a id="por-período"></a>

#### **Por Período**

Selecione um intervalo de datas:

- **Data Inicial** - Início do período
- **Data Final** - Fim do período

<a id="4-detalhes-do-webhook"></a>

### 4. Detalhes do Webhook

Clique no botão **"Detalhes"** para ver o payload completo do webhook:

<a id="estrutura-do-webhook-pagamento-com-cartão"></a>

#### **Estrutura do Webhook - Pagamento com Cartão**

```http
{
"ChargeId": "870e8c97-0f47-4b20-b161-5b78c33f18c7",
"MerchantId": "91cd6a1b-340d-4a5e-8820-cb814c093cf1",
"Nsu": "000008301",
"CustomerId": "ed4e0403-958c-4920-aa9e-f617fe2ebc6a",
"Customer": {
"Email": "cliente@exemplo.com",
"Name": "Cliente Exemplo",
"Document": "411*****809",
"DocumentType": 1
},
"Transactions": [
{
"Card": {
"Id": "322239db-86d7-4ceb-999a-1eb9cb23ab52",
"Number": "549167******5346",
"Brand": "MasterCard",
"CardHolderName": "NOME DO TITULAR"
},
"Amount": 1000,
"InstallmentNumber": 3,
"TransactionStatus": 2,
"IsApproved": true,
"PaymentType": 2,
"ErrorMessage": "Aprovada"
}
],
"ChargeStatus": 1,
"MerchantChargeId": "d5db34e7-b06a-45b8-8d9c-cc2d9f6ba107",
"DateTime": "2025-05-11T12:00:42.3684333-03:00"
}
```

<a id="estrutura-do-webhook-pagamento-com-pix"></a>

#### **Estrutura do Webhook - Pagamento com PIX**

```http
{
"ChargeId": "9c2f6f40-5ca6-442b-9cec-d5c1b6554801",
"MerchantId": "91cd6a1b-340d-4a5e-8820-cb814c093cf1",
"Nsu": "000008330",
"CustomerId": "ed4e0403-958c-4920-aa9e-f617fe2ebc6a",
"Customer": {
"Email": "cliente@exemplo.com",
"Name": "Cliente Exemplo",
"Document": "411*****809",
"DocumentType": 1
},
"Transactions": [
{
"IsApproved": true,
"PaymentType": 8,
"Amount": 2000,
"TransactionStatus": 8,
"TransactionId": "87910e25-a07d-4f8c-9722-01713f24bd9d",
"EndToEnd": "E58160789202506111638qqyFmZ02pzq",
"PixNsu": "454965989199",
"Payer": {
"Document": "606*****103",
"Name": "PAGADOR EXEMPLO",
"IspbCode": "58160789"
}
}
],
"ChargeStatus": 1,
"MerchantChargeId": "dbdd59bf-4e13-4b98-b8fb-04e1c81a3149",
"DateTime": "2025-05-11T12:00:42.3684333-03:00"
}
```

⚠️ **Nota**: Estes são exemplos do **ambiente de homologação** com dados mascarados.

<a id="5-paginação"></a>

### 5. Paginação

Navegue facilmente pelo histórico de webhooks:

- **Página Atual** - Número da página
- **Itens por Página** - Escolha entre 10, 25, 50 ou 100 itens
- **Total de Itens** - Quantidade total de webhooks
- **Navegação** - Botões Anterior/Próximo

<a id="como-usar"></a>

## 💡 Como Usar

<a id="passo-1-iniciar-integração"></a>

### Passo 1: Iniciar Integração

1. Acesse o Portal de Desenvolvedores SafraPay
2. Abra o **Monitor de Webhooks**
3. Comece a criar cobranças no ambiente de homologação

<a id="passo-2-visualizar-webhooks"></a>

### Passo 2: Visualizar Webhooks

1. Crie uma cobrança via API no **ambiente de homologação**
2. Realize o pagamento no **ambiente de sandbox**
3. Os webhooks aparecerão automaticamente no Monitor
4. Clique em **"Detalhes"** para ver o payload completo

<a id="passo-3-validar-estrutura"></a>

### Passo 3: Validar Estrutura

1. **Analise** a estrutura do JSON recebido
2. **Identifique** os campos importantes para sua aplicação
3. **Documente** os dados que você precisa processar
4. **Prepare** sua implementação futura

<a id="passo-4-testar-cenários"></a>

### Passo 4: Testar Cenários

1. Teste diferentes status (paid, cancelled, refunded)
2. Teste diferentes métodos de pagamento (cartão, PIX, boleto)
3. Verifique os dados em cada cenário
4. Use os filtros para organizar os testes

<a id="entendendo-os-status"></a>

## 📊 Entendendo os Status

<a id="fluxo-típico-de-uma-cobrança"></a>

### Fluxo Típico de uma Cobrança

**1. Pending (Pendente)**
↓
**2. Processing (Processando)**
↓
**3. Paid (Pago) ✅**
ou **Cancelled (Cancelado) ❌**
ou **Failed (Falha) ❌**

<a id="status-detalhados"></a>

### Status Detalhados

| Status | Descrição | O Que Fazer |
| --- | --- | --- |
| **pending** | Aguardando pagamento | Aguardar |
| **processing** | Processando pagamento | Aguardar |
| **paid** | Pagamento confirmado | Liberar produto/serviço |
| **cancelled** | Cobrança cancelada | Não processar pedido |
| **failed** | Pagamento falhou | Notificar cliente |
| **refunded** | Pagamento estornado | Processar devolução |
| **expired** | Cobrança expirou | Criar nova cobrança |

<a id="segurança-e-privacidade"></a>

## 🔐 Segurança e Privacidade

<a id="ambiente-de-homologação"></a>

### Ambiente de Homologação

⚠️ **Importante**: O Monitor de Webhooks exibe **apenas dados do ambiente de homologação (sandbox)**. Esta funcionalidade não está disponível para produção.

<a id="dados-mascarados"></a>

### Dados Mascarados

Por questões de segurança, dados sensíveis são automaticamente mascarados:

- **Números de cartão** - Formato: `549167******5346`
- **CPF/CNPJ** - Parcialmente ocultados: `411*****809`
- **Tokens e senhas** - Nunca são exibidos
- **Dados pessoais** - Protegidos conforme LGPD

<a id="perguntas-frequentes"></a>

## ❓ Perguntas Frequentes

<a id="este-monitor-funciona-em-produção"></a>

### Este monitor funciona em produção?

Não. O Monitor de Webhooks é exclusivo para o **ambiente de homologação/sandbox**. Para produção, você deve implementar seu próprio endpoint conforme a [Documentação de Webhooks](../api/webhooks.md).

<a id="preciso-configurar-algo-para-usar"></a>

### Preciso configurar algo para usar?

Não. O Monitor já está configurado automaticamente para receber webhooks do seu merchant em homologação.

<a id="por-quanto-tempo-os-webhooks-ficam-armazenados"></a>

### Por quanto tempo os webhooks ficam armazenados?

Os webhooks são mantidos por um período limitado. Consulte a política de retenção da SafraPay.

<a id="posso-usar-em-produção"></a>

### Posso usar em produção?

Não. Esta é uma ferramenta exclusiva para **desenvolvimento e testes em homologação**. Para produção, implemente seu próprio endpoint seguindo a [Documentação de Webhooks](../api/webhooks.md).

<a id="como-implementar-meu-próprio-endpoint"></a>

### Como implementar meu próprio endpoint?

Consulte a [Documentação de Webhooks](../api/webhooks.md) para:

- Implementação de endpoint
- Validação de assinatura
- Boas práticas de segurança
- Exemplos de código em múltiplas linguagens
- Tratamento de retentativas

<a id="posso-usar-urls-temporárias-como-typedwebhooktools"></a>

### Posso usar URLs temporárias como typedwebhook.tools?

Sim, durante o desenvolvimento você pode usar URLs temporárias para testes rápidos. Porém, o Monitor de Webhooks oferece uma solução mais integrada e persistente para homologação.

<a id="qual-a-diferença-entre-monitor-de-webhooks-e-documentação-de-webhook"></a>

### Qual a diferença entre Monitor de Webhooks e documentação de Webhook?

- **Monitor de Webhooks** (esta ferramenta): Visualização e debug durante desenvolvimento
- **[Documentação de Webhooks](../api/webhooks.md)**: Guia completo para implementação em produção

<a id="suporte"></a>

## 🆘 Suporte

Precisa de ajuda?

- **Email**: [integracao.ecommerce@safra.com.br](mailto:integracao.ecommerce@safra.com.br)
- **Documentação Completa**: [Webhooks](../api/webhooks.md)

<a id="próximos-passos"></a>

## 📚 Próximos Passos

Depois de validar a estrutura dos webhooks no Monitor:

1. **Consulte** a [Documentação de Webhooks](../api/webhooks.md) completa
2. **Implemente** seu endpoint seguindo as melhores práticas
3. **Configure** a URL do seu endpoint no portal
4. **Valide** a assinatura dos webhooks
5. **Teste** em homologação com seu endpoint próprio
6. **Deploy** para produção quando estiver pronto

<a id="recursos-relacionados"></a>

## 📖 Recursos Relacionados

- [Documentação de Webhooks](../api/webhooks.md) - Implementação completa
- [Monitor de API](monitor-de-api.md) - Debug de requisições HTTP
- [API de Cobranças](../api/cobranca.md) - Criação de cobranças
- [Gateway de Pagamentos](../api/gateway.md) - Processamento de pagamentos
- [Autenticação](../api/autenticacao.md) - Credenciais de API

---

**Última atualização**: Outubro 2025

**Versão da documentação**: 2.0
