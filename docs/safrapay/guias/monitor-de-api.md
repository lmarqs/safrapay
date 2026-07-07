---
title: "Monitor de API (Tracer)"
parent: "Guias"
nav_order: 60
layout: "doc"
permalink: "/guias/monitor-de-api/"
description: "O Monitor de API é uma ferramenta avançada de monitoramento e debug que permite visualizar em tempo real todas as requisições HTTP feitas à API SafraPay. Com el"
source: "tracer-doc.html"
---

# Monitor de API (Tracer)

O **Monitor de API** é uma ferramenta avançada de monitoramento e debug que permite visualizar em tempo real todas as requisições HTTP feitas à API SafraPay. Com ele, você pode acompanhar, filtrar e analisar detalhadamente cada chamada à API, facilitando o desenvolvimento, testes e resolução de problemas.

<a id="visão-geral"></a>

## 📊 Visão Geral

O Monitor de API (também conhecido como Tracer) oferece uma interface intuitiva para:

- **Visualizar requisições em tempo real** - Acompanhe todas as chamadas à API conforme elas acontecem
- **Filtrar por múltiplos critérios** - Encontre rapidamente a requisição que procura
- **Analisar detalhes completos** - Veja headers, body, response e timing de cada requisição
- **Monitorar performance** - Identifique gargalos e otimize suas integrações
- **Debug eficiente** - Resolva problemas rapidamente com informações detalhadas

<a id="para-quem-é-esta-ferramenta"></a>

## 🎯 Para Quem é Esta Ferramenta?

O Monitor de API é ideal para:

- **Desenvolvedores** - Debug e análise de integrações
- **Equipes de QA** - Testes e validação de APIs
- **DevOps** - Monitoramento e troubleshooting
- **Suporte Técnico** - Investigação de incidentes

<a id="como-acessar"></a>

## 🚀 Como Acessar

1. Faça login no Portal de Desenvolvedores SafraPay
2. No menu lateral, acesse **Ferramentas > Monitor de API**
3. Você verá imediatamente as requisições mais recentes do **ambiente de homologação**

⚠️ **Nota**: Esta ferramenta monitora apenas requisições do ambiente de **sandbox/homologação**.

<a id="funcionalidades-principais"></a>

## 🔍 Funcionalidades Principais

<a id="1-listagem-de-requisições"></a>

### 1. Listagem de Requisições

A tela principal exibe uma lista paginada com as requisições mais recentes, mostrando:

- **TraceKey** - Identificador único da requisição (UUID)
- **Método HTTP** - GET, POST, PUT, DELETE, etc.
- **Endpoint** - Caminho da API chamada
- **Status Code** - Código de resposta HTTP (200, 400, 500, etc.)
- **Duração** - Tempo de resposta em milissegundos
- **Timestamp** - Data e hora da requisição

<a id="2-filtros-avançados"></a>

### 2. Filtros Avançados

Use os filtros para encontrar requisições específicas:

<a id="por-tracekey"></a>

#### **Por TraceKey**

Digite o identificador único da requisição para localizá-la diretamente.

**Exemplo:** `a7b3c1d5-e2f4-4a5b-9c3d-1e2f3a4b5c6d`

<a id="por-método-http"></a>

#### **Por Método HTTP**

Filtre por tipo de requisição:

- GET
- POST
- PUT
- DELETE
- PATCH

<a id="por-status-code"></a>

#### **Por Status Code**

Encontre requisições por código de resposta:

- `2xx` - Sucesso (200, 201, 204, etc.)
- `4xx` - Erros do cliente (400, 401, 404, etc.)
- `5xx` - Erros do servidor (500, 502, 503, etc.)

<a id="por-período"></a>

#### **Por Período**

Selecione um intervalo de datas para análise histórica:

- **Data Inicial** - Início do período
- **Data Final** - Fim do período

<a id="por-endpoint"></a>

#### **Por Endpoint**

Digite parte da URL para filtrar por rota específica:

**Exemplos:**

- `/v1/Charge`
- `/v1/Subscription`
- `/v1/Transaction`

<a id="3-detalhes-da-requisição"></a>

### 3. Detalhes da Requisição

Clique no botão **"Detalhes"** em qualquer requisição para ver informações completas:

<a id="request-requisição"></a>

#### **Request (Requisição)**

**Headers (Cabeçalhos)**

```json
{
  "Content-Type": "application/json",
  "Authorization": "Bearer YOUR_TOKEN",
  "X-Merchant-Id": "your-merchant-id",
  "User-Agent": "MyApp/1.0"
}
```

**Body (Corpo)**

```json
{
  "amount": 10000,
  "description": "Pedido #12345",
  "customer": {
    "name": "João Silva",
    "email": "joao@example.com"
  }
}
```

<a id="response-resposta"></a>

#### **Response (Resposta)**

**Status Code**

- Código HTTP retornado pela API

**Headers (Cabeçalhos de Resposta)**

```json
{
  "Content-Type": "application/json",
  "X-Request-Id": "abc123",
  "X-Rate-Limit-Remaining": "99"
}
```

**Body (Corpo da Resposta)**

```json
{
  "id": "chr_abc123",
  "status": "pending",
  "amount": 10000,
  "created_at": "2025-10-14T10:30:00Z"
}
```

<a id="timing-análise-de-performance"></a>

#### **Timing (Análise de Performance)**

- **Duração Total** - Tempo total da requisição
- **Timestamp** - Momento exato da chamada

<a id="4-paginação"></a>

### 4. Paginação

Navegue facilmente por milhares de requisições:

- **Página Atual** - Número da página
- **Itens por Página** - Escolha entre 10, 25, 50 ou 100 itens
- **Total de Itens** - Quantidade total de requisições encontradas
- **Navegação** - Botões Anterior/Próximo

<a id="casos-de-uso-práticos"></a>

## 💡 Casos de Uso Práticos

<a id="debug-de-erro-400-bad-request"></a>

### Debug de Erro 400 (Bad Request)

1. **Filtre** por Status Code `400`
2. **Identifique** a requisição problemática
3. **Analise** o body enviado no request
4. **Compare** com a documentação da API
5. **Corrija** os dados e teste novamente

<a id="análise-de-performance"></a>

### Análise de Performance

1. **Ordene** por duração (maior para menor)
2. **Identifique** endpoints lentos
3. **Verifique** o tamanho dos payloads
4. **Otimize** suas requisições

<a id="investigação-de-falha"></a>

### Investigação de Falha

1. **Obtenha** o TraceKey do erro
2. **Cole** no filtro de TraceKey
3. **Veja** exatamente o que foi enviado e recebido
4. **Identifique** a causa raiz

<a id="validação-de-integração"></a>

### Validação de Integração

1. **Execute** sua integração
2. **Verifique** no Monitor de API se as chamadas foram feitas corretamente
3. **Confirme** os status codes esperados
4. **Valide** os dados enviados e recebidos

<a id="segurança-e-privacidade"></a>

## 🔐 Segurança e Privacidade

<a id="ambiente-de-homologação"></a>

### Ambiente de Homologação

⚠️ **Importante**: O Monitor de API exibe **apenas dados do ambiente de homologação (sandbox)**. Esta funcionalidade não está disponível para produção.

<a id="dados-mascarados"></a>

### Dados Mascarados

Por questões de segurança, dados sensíveis são automaticamente mascarados:

- **Números de cartão** - Apenas os 6 primeiros e 4 últimos dígitos são exibidos
- **CVV** - Nunca é armazenado ou exibido
- **Tokens de autenticação** - Parcialmente ocultados
- **Dados pessoais** - Protegidos conforme LGPD

<a id="retenção-de-dados"></a>

### Retenção de Dados

- Os traces são armazenados por um período limitado
- Dados antigos são automaticamente removidos
- Consulte a política de retenção da SafraPay

<a id="controle-de-acesso"></a>

### Controle de Acesso

- Apenas usuários autenticados podem acessar
- Você vê apenas as requisições do seu merchant em homologação
- Credenciais são necessárias para visualização

<a id="glossário"></a>

## 📖 Glossário

<a id="tracekey"></a>

### TraceKey

Identificador único (UUID) de cada requisição. Use-o para rastrear chamadas específicas ou reportar problemas ao suporte.

<a id="endpoint"></a>

### Endpoint

O caminho da API que foi chamado. Exemplo: `/v1/Charge/Create`

<a id="status-code"></a>

### Status Code

Código numérico HTTP que indica o resultado da requisição:

- `2xx` - Sucesso
- `3xx` - Redirecionamento
- `4xx` - Erro do cliente
- `5xx` - Erro do servidor

<a id="headers"></a>

### Headers

Metadados enviados junto com a requisição/resposta, como autenticação, tipo de conteúdo, etc.

<a id="body-payload"></a>

### Body (Payload)

Dados enviados no corpo da requisição ou resposta, geralmente em formato JSON.

<a id="duração"></a>

### Duração

Tempo total que a API levou para processar e responder à requisição, medido em milissegundos.

<a id="perguntas-frequentes"></a>

## ❓ Perguntas Frequentes

<a id="como-encontro-uma-requisição-específica"></a>

### Como encontro uma requisição específica?

Use o **TraceKey** (identificador único) que você pode obter dos logs da sua aplicação ou de respostas de erro.

<a id="por-quanto-tempo-os-traces-ficam-disponíveis"></a>

### Por quanto tempo os traces ficam disponíveis?

Os traces são mantidos por um período específico. Consulte a documentação de retenção de dados da SafraPay.

<a id="posso-exportar-os-dados"></a>

### Posso exportar os dados?

Atualmente, os traces podem ser visualizados na interface. Para exportação de dados, entre em contato com o suporte.

<a id="o-que-significa-cada-cor-do-status"></a>

### O que significa cada cor do status?

- 🟢 **Verde** (2xx) - Sucesso
- 🟡 **Amarelo** (4xx) - Erro do cliente (problema na requisição)
- 🔴 **Vermelho** (5xx) - Erro do servidor (problema na API)

<a id="posso-ver-requisições-de-outros-merchants"></a>

### Posso ver requisições de outros merchants?

Não. Por questões de segurança, você visualiza apenas as requisições do seu próprio merchant.

<a id="como-reportar-um-problema-usando-o-monitor-de-api"></a>

### Como reportar um problema usando o Monitor de API?

1. Encontre a requisição problemática
2. Copie o **TraceKey**
3. Entre em contato com o suporte informando o TraceKey
4. Nossa equipe poderá investigar rapidamente

<a id="suporte"></a>

## 🆘 Suporte

Precisa de ajuda?

- **Email**: [integracao.ecommerce@safra.com.br](mailto:integracao.ecommerce@safra.com.br)

<a id="recursos-relacionados"></a>

## 📚 Recursos Relacionados

- [Documentação da API SafraPay](../api/gateway.md)
- [Autenticação](../api/autenticacao.md)
- [Webhooks](../api/webhooks.md)
- [Monitor de Webhooks](monitor-de-webhooks.md)
- [Primeiros Passos](primeiros-passos.md)

---

**Última atualização**: Outubro 2025

**Versão da documentação**: 1.0
