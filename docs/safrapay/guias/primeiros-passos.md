---
title: "Primeiros Passos"
parent: "Guias"
nav_order: 10
layout: "doc"
permalink: "/guias/primeiros-passos/"
description: "Essa seção tem como objetivo prover o ferramental necessário para entendimento da documentação a seguir, como por exemplo os endpoints das APIs, variáveis, cart"
source: "first-steps.html"
---

# PRIMEIROS PASSOS

Essa seção tem como objetivo prover o ferramental necessário para entendimento da documentação a seguir, como por exemplo os endpoints das APIs, variáveis, **cartões oficiais de teste** para homologação, **pontos de atenção** de sandbox, códigos de erro e enumeradores.

<a id="introdução"></a>

## Introdução

> Resposta padrão das APIs

```json
{
    "traceKey": "guid",
    "errors": [
        {
            "errorCode": int,
            "message": "string",
            "field": "string"
        }
    ],
    "success": bool
}
```

A forma principal de integração com a Safrapay é com a utilização de APIs, através das quais é possível usufruir de funcionalidades como pagamentos e-commerce e cartão presente, e-wallet, conciliação, extrato digital, entre outras. Essa documentação tem como objetivo facilitar a integração com nossos parceiros e dar autonomia aos desenvolvedores responsáveis pela integração. As APIs da Safrapay foram implementadas com base na arquitetura RESTful, e são divididas por produto, portanto ao longo da documentação serão utilizados endpoints diferentes para pagamento (gateway), gestão (portal) e conciliação. A utilização de cada API pode diferir minimamente, porém todas usam JSON como media-type padrão, JWT como Bearer token na autenticação e sempre com o encoding UTF-8. Além disso, todas as APIs possuem uma resposta padrão.

<a id="segurança"></a>

## Segurança

Para que a Safrapay esteja apta a processar pagamentos, é necessário estarmos adequados às regras do PCI DSS, exigidas e atualizadas trimestralmente. Ao integrar com a Safrapay, nossos parceiros utilizam uma infraestrutura com foco em performance e segurança, que, seguindo normas do PCI, é testada trimestralmente afim de garantir a segurança dos membros do arranjo de pagamentos, estabelecimentos comerciais e prestadores de serviço que armazenam ou transmitam dados de cartões de crédito. Os testes feitos são auditados por empresas terceiras e submetidos ao PCI Council anualmente. Através da certificação PCI DSS, a Safrapay oferece:

- Acesso a 5 anos de armazenamento dos dados
- Rastreabilidade das operações realizadas na plataforma
- Utilização de certificado SSL 1.2 em todas as APIs
- Acesso à gestão de mudanças e changelog

<a id="endpoints"></a>

## Endpoints

As URLs que serão utiizadas para fazer as requisições.

<a id="desenvolvimento"></a>

#### Desenvolvimento

| Endpoint | Link | Descrição |
| --- | --- | --- |
| {{ENDPOINT_GATEWAY}} | [https://payment-hml.safrapay.com.br](https://payment-hml.safrapay.com.br) | Url do gateway de desenvolvimento. |
| {{ENDPOINT_RECONCILIATION}} | [https://reconciliation-api-hml.safrapay.com.br](https://reconciliation-api-hml.safrapay.com.br) | Url do reconciliation de desenvolvimento. |
| {{ENDPOINT_WEBHOOK}} | [https://webhook-hml.safrapay.com.br](https://webhook-hml.safrapay.com.br) | Url do Webhook de desenvolvimento. |
| {{OAUTH_URL}} | [https://portal-hml.safrapay.com.br](https://portal-hml.safrapay.com.br) | Url utilizada para acessar o portal de desenvolvimento. |

<a id="produção"></a>

#### Produção

| Endpoint | Link | Descrição |
| --- | --- | --- |
| {{ENDPOINT_GATEWAY}} | [https://payment.safrapay.com.br](https://payment.safrapay.com.br) | Url do gateway. |
| {{ENDPOINT_RECONCILIATION}} | [https://reconciliation-api.safrapay.com.br](https://reconciliation-api.safrapay.com.br) | Url do reconciliation. |
| {{ENDPOINT_WEBHOOK}} | [https://webhook.safrapay.com.br](https://webhook.safrapay.com.br) | Url do Webhook. |
| {{OAUTH_URL}} | [https://portal.safrapay.com.br](https://portal.safrapay.com.br) | Url utilizada para acessar o portal. |

<a id="variáveis"></a>

## Variáveis

Uma variável é um valor nomeado dinamicamente que pode interagir com as funções introduzindo valores predeterminados.

| Variáveis | Descrição |
| --- | --- |
| {{accessToken}} | Token de autorização, que pode ser criado na API do portal e na do gateway. |
| {{merchantId}} | O id do comerciante. |
| {{cardId}} | O id de um cartão. |
| {{smartCheckoutId}} | O id de um smartCheckout. |
| {{customerId}} | O id de um cliente. |
| {{receiverId}} | O id de um recebedor. |
| {{chargeId}} | O id de uma cobrança. |
| {{taxPlanId}} | O id de uma taxa. |
| {{acquirerCode}} | O id da adquirente. |
| {{cardBrand}} | O id da bandeira do cartão. |
| {{taxId}} | O id da taxa. |
| {{transactionsStatus}} | O status da transação de conciliação. |
| {{transactionsType}} | O tipo da transação de conciliação. |
| {{startDate}} | A data inicial a ser filtrada. |
| {{endDate}} | A data final a ser filtrada. |
| {{planId}} | O id do plano. |
| {{bankSlipTaxPlanId}} | O id do plano de taxas de boletos. |
| {{invoiceId}} | O id da fatura. |
| {{productId}} | O id do produto. |
| {{subscriptionId}} | O id da assinatura. |
| {{transferOrderId}} | O id do pedido de transferência. |
| {{virtualAcquirerId}} | O id da adquirente virtual. |
| {{clientId}} | ID de EDI definido pelo adquirente. |
| {{document}} | Número do documento do comprador. |
| {{userId}} | O ID do usuário. |
| {{roleId}} | O número que define a função do perfil do usuário. |
| {{partner_token}} | Código de identificação do integrador, utilizado na integração com TEF. |

<a id="cartões-de-teste"></a>

## Cartões de teste

Utilize **somente** os cartões do quadro abaixo no ambiente de **homologação (sandbox)**. **Desconsidere** números de cartão antigos publicados apenas para o simulador interativo (removido do portal) ou exemplos genéricos de outras fontes.

| Bandeira | @Cartão | @CVV | Validade | Nota | Teste Transação Negada |
| --- | --- | --- | --- | --- | --- |
| MC | 5502093769921690 | 123 | Qualquer futura | Ambiente disponível diariamente das 09.30hs até as 17:30hs para teste. **Janela atualizada a partir de 02/01/23** |   |
| MC | 5502091221618516 | 123 | Qualquer futura | Ambiente disponível diariamente das 09.30hs até as 17:30hs para teste. **Janela atualizada a partir de 02/01/23** |   |
| ELO | 6277800000002390 | 123 | Qualquer futura | Ambiente disponível diariamente das 09.30hs até as 17:30hs para teste. **Janela atualizada a partir de 02/01/23** | R$ 3,33 |
| VISA | 4444585001234562 | 123 | Qualquer futura | Ambiente disponível diariamente das 09.30hs até as 17:30hs para teste. **Janela atualizada a partir de 02/01/23** |   |
| VISA | 4444585006543215 | 123 | Qualquer futura | Ambiente disponível diariamente das 09.30hs até as 17:30hs para teste. **Janela atualizada a partir de 02/01/23** |   |
| AMEX | 375177012458884 | 123 | Qualquer futura | Ambiente disponível diariamente das 09.30hs até as 17:30hs para teste. **Janela atualizada a partir de 02/01/23** | R$ 3,33 |

> **Simulador de adquirente (sandbox):** quando ativo na loja de homologação, o resultado também segue os **centavos do valor** da transação. Consulte o time de integrações para detalhes do cenário configurado na sua credencial.

> **Simulador de antifraude:** por padrão **não** vem ativado; a ativação é feita pelo time de integrações. **Desconsidere** PANs antigos usados apenas na documentação do simulador interativo (removido do portal). Quando o antifraude simulado estiver ativo, siga as orientações enviadas pelo time em conjunto com os cartões oficiais desta tabela.

<a id="pontos-de-atenção-homologação"></a>

## Pontos de atenção (homologação)

<a id="chave-de-acesso-mk-token"></a>

### Chave de acesso (`mk_` + token)

O Merchant Token segue o padrão `mk_` seguido do **token** (`mk_{{token}}`). O trecho `{{token}}` possui **25 caracteres** e pode conter:

- Letras **A–Z** e **a–z**
- Dígitos **0–9**
- Underscore **`_`**

<a id="merchantchargeid-e-merchanttransactionid"></a>

### `merchantChargeId` e `merchantTransactionId`

- **Não** envie esses identificadores **com espaços** no meio do texto. Exemplos corretos: `TASK5333`, `PEDIDO123`, `LOJA_ABC_001`.
- Campos obrigatórios da estrutura da cobrança **não** podem ser enviados vazios nem como string vazia `""`.

<a id="softdescriptor"></a>

### `softDescriptor`

- Aceita **somente** letras, números e asterisco (`*`).
- **Não** aceita espaço nem outros caracteres; formato equivalente: **`/^[a-zA-Z0-9*]+$/`**.
- Nos exemplos de requisição da documentação, use valores **sem espaço** (ex.: `TASK*5333` ou `LOJA*PEDIDO123`).

<a id="cancelamento-no-cartão-de-crédito-conceito"></a>

### Cancelamento no cartão de crédito (conceito)

- **Cancelamento em D+0** (mesmo dia da captura) corresponde a **estorno**: atualização de status ainda **no dia** da solicitação; **somente cancelamento total** (não há estorno parcial).
- **Cancelamento em D+N** (dias após a captura): admite **cancelamento parcial ou total**; o processamento e a atualização de status seguem o fluxo em **D+N** (dia seguinte ou conforme regra do adquirente).

<a id="mensagem-lojista-contate-o-adquirente-safrapay-em-testes"></a>

### Mensagem “Lojista, contate o adquirente (Safrapay)” em testes

Se essa mensagem (ou código associado na resposta de homologação) aparecer, costuma indicar **condição de pagamento não habilitada** na credencial de HML — por exemplo, parcelamento **18x** quando o cadastro de homologação só permite testar até **12x**. Ajuste o cenário (parcelas, produto, MCC etc.) ou solicite liberação ao time de integrações.

<a id="pix-em-homologação"></a>

### PIX em homologação

O valor máximo por transação PIX em ambiente de **homologação** é **R$ 10.000,00**.

<a id="códigos-de-erros"></a>

## Códigos de Erros

Lista com os possíveis códigos de erros que uma requisição não sucedida pode apresentar.

| Valor inteiro | Descrição |
| --- | --- |
| 1 | Uma propriedade obrigatória ou condicional está vazia, apenas com espaços em branco, apenas com zeros ou nula. |
| 2 | Merchant Token inválido. |
| 3 | Cartão não suportado. |
| 4 | Cartão não encontrado na wallet. |
| 5 | Mês de expiração do cartão inválido. |
| 6 | Ano de expiração do cartão inválido. |
| 7 | Cartão expirado. |
| 8 | Comprador não encontrado na Safrapay. |
| 9 | Número de parcelas inválido. |
| 10 | Erro de comunicação com a adquirente. Tentar mais tarde ou entrar em contato com a Safrapay. |
| 11 | Adquirente inválida. |
| 12 | Tipo de pagamento inválido. |
| 13 | Prioridade do tipo de pagamento inválida. |
| 14 | Taxa percentual inválida. |
| 15 | Valor inválido. |
| 16 | Cobrança cancelada. |
| 17 | Cobrança não encontrada na Safrapay. |
| 18 | Data inválida. |
| 19 | Frequência de recorrência inválida. |
| 20 | Plano não encontrado na Safrapay. |
| 21 | Intervalo de datas inválido. |
| 22 | ID do cartão inválido. |
| 23 | Recebedor não encontrado. |
| 24 | Opção de enumerador inválida ou não suportada. |
| 25 | Banco não suportado. |
| 26 | Comprador não pode fazer ou requisitar a operação. |
| 27 | Erro na cobrança recorrente. |
| 28 | Erro ao executar os comandos. |
| 29 | Usuário não encontrado na Safrapay. |
| 31 | Data de início é mais recente que a data final. |
| 32 | CNPJ inválido. |
| 33 | E-mail inválido. |
| 34 | ID da adquirente inválido. |
| 35 | Token da loja pai inválido. |
| 36 | Operação não permitida para a loja. |
| 37 | Operação não permitida. |
| 38 | ID da loja inválido. |
| 39 | Permissão não encontrada. |
| 40 | PAN encriptado está ausente. |
| 41 | PAN sequence number (5F34) inválido. |
| 42 | Terminal não encontrado na Safrapay. |
| 43 | Loja não encontrada na Safrapay. |
| 44 | Erro na senha. |
| 45 | Propriedade inválida (genérico). |
| 46 | Tamanho da página ausente. |
| 47 | Numero da página atual ausente. |
| 48 | Data e hora inválidos. |
| 49 | Transação não suportada. |
| 50 | Erro interno de atualização. |
| 51 | Não foi possível se conectar ao gateway de pagamentos. |
| 52 | A assinatura foi desativada. |
| 53 | A assinatura foi desativada devido a quantidade excessiva de não autorização. |
| 54 | Valor excede o limite. |
| 55 | Assinatura não encontrada. |
| 56 | Cartão inválido. |
| 57 | Histórico de comunicação da loja não encontrado. |
| 58 | Operação não suportada pela adquirente. |
| 59 | ID de conciliação já existe. |
| 60 | ID de conciliação não existe. |
| 61 | Data requisitava é mais recente que a data atual. |
| 62 | Erro de requisição no Safrapay. |
| 63 | O cartão é diferente da transação original. |
| 64 | Transação não pode ser cancelada. |
| 65 | Falha no upload do arquivo .OFX. |
| 66 | Valor requisitado é maior que o saldo atual do recebedor. |
| 67 | Data requisitada é mais antiga que a data atual. |
| 68 | Valor de transferência inválido. |
| 69 | Data requisitava é mais recente que a data atual. |
| 70 | Data requisitada é mais antiga que a data atual. |
| 71 | Formato do GUID inválido. |
| 72 | Status inválido para cancelamento de pedido de transferência. Tente novamente mais tarde. |
| 73 | ID do pedido de transferência não encontrado. |
| 74 | Número de transferências por dia excedido. |
| 75 | ID da linha de extrato no arquivo .OFX é inválida. |
| 76 | Cliente já foi credenciado. |
| 77 | ID do cliente é inválido. |
| 78 | ID do cliente não existe. |
| 79 | Valor não aceito. O valor deve estar no intervalo especificado na mensagem de erro. |
| 80 | Recebedor já possui conta vinculada. |
| 81 | Checkout / link de pagamento expirado. |
| 82 | Erro ao salvar dados. |
| 83 | Cobrança não cancelada. |
| 84 | Checkout / link de pagamento não encontrado. |
| 85 | ID da taxa não encontrado. |
| 86 | Ordem de transferência está em processamento. |
| 87 | Nenhum plano de taxas cadastrado. |
| 88 | Conciliação não cadastrada. |
| 89 | O documento do comprador é inválido para o e-mail requisitado. Isso pode ocorrer se o e-mail já foi cadastrado para um comprador, com outro CPF / CNPJ. |
| 90 | Status da transação conciliada é inválido. |
| 91 | Código da bandeira do cartão é inválido. |
| 92 | Conta bancária não encontrada para o pedido de transferência. |
| 93 | Conta bancária inválida para o pedido de transferência. |
| 94 | O valor solicitado é inferior ao saldo total disponível, descontando o valor total das ordens de transferência em progresso no momento. |
| 95 | Nenhum recebedor encontrado. |
| 96 | Cobrança não elegível para divisão. |
| 97 | Tipo de ajuste inválido. |
| 98 | Razão do ajuste inválida. |
| 99 | Tamanho da lista é inválido. Verifique o tamanho suportado na mensagem de erro. |
| 100 | CNPJ já cadastrado. |
| 101 | Cobrança já autorizada. |
| 102 | Valor inválido (genérico). |
| 103 | Movimentação de ajuste já processada. |
| 104 | Configuração de desconto do boleto está inválida. |
| 105 | Configuração de desconto do boleto está inválida. |
| 106 | Item do plano com valor inválido. |
| 107 | Erro na configuração da fatura. |
| 108 | Erro ao requisitar parâmetros da adquirente. |
| 109 | Erro de ativação na adquirente. |
| 110 | Erro na mensageria ISO-8583. |
| 111 | Erro ao fazer login no portal Safrapay. |
| 112 | Terminal não está ativado na adquirente. |
| 113 | Transação por boleto não suportada. |
| 114 | Fatura não encontrada pelo ID. |
| 115 | Saldo atual insuficiente, descontando a taxa de transferência eletrônica. |
| 116 | Código do banco inválido. |
| 117 | Agência inválida. |
| 118 | Tamanho da agência inválido. |
| 119 | Código de verificação da agência inválido. |
| 120 | Conta bancária inválida. |
| 121 | Tamanho da conta bancária inválido. |
| 122 | Código de verificação da conta bancária inválido. |
| 123 | Dados bancários em branco. |
| 124 | Tipo de conta bancária inválido. |
| 125 | Não foi possível se comunicar com o banco. |
| 126 | Erro no desfazimento. |
| 127 | E-mail já existe. |
| 128 | Comprador não encontrado pelo documento (CPF / CNPJ). |
| 129 | CPF inválido. |
| 130 | Código de área do telefone é inválido. |
| 131 | Código do país do telefone é inválido. |
| 132 | Telefone é inválido. |
| 133 | Documento é inválido. |
| 134 | A origem da requisição é inválida para a operação. |
| 135 | Informação de parcelamento é inválida. |
| 136 | Bandeira do cartão não suportada pela adquirente. |
| 137 | Lançamento futuro não encontrada. |
| 138 | Lançamento futuro já existe. |
| 139 | Tipos de pagamento suportados não encontrados. |
| 140 | Webhook já cadastrado. |
| 141 | URL inválida. |
| 142 | Origem da requisição não suportada. |
| 143 | Modo de entrada do cartão não suportado. |
| 144 | Código de transação não suportado, verifique os códigos de transação suportados. |
| 145 | A loja não pode configurar antecipação. |
| 146 | Acesso negado ao checkout de pagamentos. |
| 147 | Não foi possível processar a transação. Tente novamente em alguns minutos ou entre em contato com a loja. |
| 148 | Código de processamento não suportado, verifique os códigos de processamento suportados. |
| 149 | O valor mínimo da parcela não pode ser maior que o valor do Link de Pagamento ou Checkout. |
| 150 | O webhook informado não foi encontrado. |
| 151 | Número de série do terminal é inválido. |
| 152 | NSU inválido. |
| 153 | Loja requer motor de antifraude cadastrado. |
| 154 | Não foi possível alterar a data de vencimento do boleto. |
| 155 | Recibo disponível apenas se a transferência tiver o status de realizado. |
| 156 | Erro no emissor que foi registrado no boleto, contate um administrador. |
| 157 | Não foi possível emitir o boleto por falta de informações referente ao endereço do comprador. Entre em contato com a loja para atualizar seu cadastro. |
| 158 | Não há recebedor registrado ao CPNJ. |
| 159 | Não foi possível criar a fatura. |
| 160 | Extensão do arquivo não suportada pelo descompactador. |
| 161 | Link de pagamento expirou porque excedeu o número de transações negadas. |
| 162 | Não é possível reemitir boleto pois a fatura ainda não está expirada. |
| 163 | Normalização de arquivos da Carga de Parâmetros não suportou os arquivos recebidos. |
| 164 | Informações da transação original não encontradas. |
| 165 | Necessário de envio de mensagem com a perna de MTI anteriormente. |
| 166 | Parâmetros do terminal não encontrados, efetue a primeira Carga de Parâmetros ou contacte um administrador. |
| 167 | Sub-adquirente não encontrada. |
| 168 | Produto da Sub-adquirente não encontrado. |
| 169 | Sub-adquirente deve ter ao menos 'x' produto |
| 170 | Produto 'x' duplicado. |
| 171 | Já foi criado uma Sub-adquirente com esse lojista e adquirente. |
| 172 | Já existe um termo de uso cadastrado com esse mesmo nome. |
| 173 | O termo de uso informado não foi encontrado. |
| 174 | O plano de taxas de boleto não foi encontrado. |
| 175 | Nenhum lojista foi encontrado com as credenciais informadas. |
| 176 | Não há segmento para o seu MCC 'x'. |
| 177 | Lojista não está habilitado a aceitar transações. |
| 178 | O valor mínimo para criação de link de pagamento de boleto é de 'x'. |
| 179 | O plano de taxas não foi encontrado. |
| 180 | Cobrança com ID 'x' já foi cancelada. |
| 181 | O lojista deve possuir um plano de taxas ativo. |
| 182 | Sem chaves lógicas disponíveis, comunique-se com a adquirente responsável pela geração das novas chaves e solicite a importação das novas chaves ao suporte da Safrapay. |
| 183 | Essa configuração de boleto já existe. |
| 184 | Essa configuração de adquirente já existe. |
| 185 | O plano de taxas selecionado não é suportado pelo MCC do lojista. |
| 186 | A adquirente 'x' não suporta transações de 'x'. |
| 187 | O link para pagamento foi cancelado. |
| 188 | A adquirente 'x' não suporta transações de valor 0. |
| 189 | A adquirente 'x' não suporta cancelamento parcial. |
| 190 | O estabelecimento 'x' não possui contato telefônico cadastrado, favor entrar em contato com o administrador. |
| 191 | A adquirente não possui o serviço de antecipação spot. |
| 192 | Nenhuma transação de liquidação foi encontrada. |
| 193 | Já existe uma solicitação de antecipação para o TID 'x'. |
| 194 | Nenhuma transação foi encontrada. |
| 195 | Boleto só pode ser cancelado um dia após ser criado. |
| 196 | Nenhuma conta encontrada. |
| 197 | Pagamento de conta já processado. |
| 198 | Profile do Adquirente não encontrado. |
| 199 | Parceiro não identificado. Entre em contato com o suporte. |
| 200 | Parceiro não está atribuído para esta loja. Entre em contato com o suporte. |
| 201 | Código de autenticação inválido. |
| 202 | Checkout com ID 'x' não encontrado. |
| 203 | O token passado não é válido. |
| 204 | Venda com o ID 'x' não encontrada. |
| 205 | Tamanho de arquivo não permitido, o tamanho deve estar entre 'x' e 'y'. |
| 206 | Extensão não permida, apenas arquivos com a extensão 'x' são permitidos. |
| 207 | Quantidade de linhas no arquivo não permitida, apenas arquivos que possuem a quantidade de linhas entre 'x' e 'x' são permitidos. |
| 208 | Formato incorreto em uma ou mais linhas. Posição da linha: 'x'. Contéudo da linha: 'x'. |
| 209 | Arquivo de Venda com o ID 'x' não encontrado. |
| 210 | Já existe uma venda com esse NSU 'x' na adquirente'x'. |
| 211 | Esse arquivo já foi importado. |
| 212 | A Adquirente 'x' não é conhecido. |
| 213 | Não é possível importar um novo arquivo. Você possui arquivos pendentes para conciliar!. |
| 214 | Atualizar tabelas do terminal. |
| 215 | Transação referida inválida ou não existe. |
| 216 | A transação não foi encontrada. |
| 217 | Cancelamento parcial não permitido. |
| 218 | Captura parcial não é permitida. |
| 219 | Erro ao cancelar transação. Adquirente retornou código 'x' com a mensagem de erro 'x'. |
| 220 | Plano de taxas não pode ser associado ao Estabelecimento. |
| 221 | O registro de chargeback não foi encontrado. |
| 222 | O formato do ID é inválido. |
| 223 | O arquivo de comprovante da abertura de disputa não foi encontrado. |
| 224 | O Passaporte 'x' é inválido. |
| 225 | Erro no processo de validação do Captcha. |
| 226 | O visitante já foi cadastrado. |
| 227 | Visitante {0} não foi encontrado. |
| 228 | Visitante já confirmou a inscrição. |
| 229 | Documento ou email já cadastrados como usuário ou loja. |
| 230 | Nenhuma configuração de 3DS cadastrada. |
| 231 | UnreachableThreeDomainSecureProvider. |
| 232 | Autenticação negada pelo provedor 'x'. |
| 233 | O arquivo solicitado não foi encontrado no banco de dados. |
| 234 | O registro solicitado não foi encontrado no banco de dados. |
| 235 | O evento solicitado não foi encontrado no banco de dados. |
| 236 | O Relatório financeiro não foi encontrado. |
| 237 | Falha no upload do arquivo para o bucket. |
| 238 | O arquivo de conciliação solicitado para download não foi encontrado. |
| 239 | O parceiro não foi encontrado. |
| 240 | A propriedade 'TransactionMac' na requisição não é válida. Deve estar de acordo com as informações passadas. |
| 241 | O integrador 'x' não pôde ser encontrado. |
| 242 | Não foi possível estabelecer comunicação com o tokenizador 'x'. |
| 243 | Valor do link de pagamento maior que o saldo disponível. |
| 244 | Integração para sensibilização de saldo desabilitada para o estabelecimento 'x' |
| 245 | Tabela de chaves do adquirente não encontrada. |
| 9999 | Outros. |

<a id="enumeradores"></a>

## Enumeradores

Lista com os enumeradores, eles te ajudarão a escolher a opção correta dentro de um campo da requisição.

<a id="phone"></a>

### `Phone`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Residencial | Telefone Residencial |
| 2 | Commercial | Telefone Comercial |
| 3 | Voicemail | Correio de Voz |
| 4 | Temporary | Telefone Temporário |
| 5 | Mobile | Celular |

<a id="smartcheckouttype"></a>

### `SmartCheckoutType`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | PaymentLink | SmartCheckout do tipo Link de Pagamento, criado via endpoint /paymentlink. |
| 2 | Checkout | SmartCheckout do tipo Checkout, criado via endpoint /smartcheckout. |

<a id="paymenttype"></a>

### `PaymentType`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Debit | Débito. |
| 2 | Credit | Crédito. |
| 3 | Voucher | Voucher. |
| 4 | Boleto | Boleto. |
| 5 | Ted | Transferência Eletrônica de Fundos. |
| 6 | Doc | Documento de Ordem de Crédito. |
| 7 | SafetyPay | SafetyPay. |
| 8 | Pix | Pix |

**Link de Pagamento e Checkout:** o campo `paymentSupportedTypes` (array de inteiros) utiliza os **mesmos valores numéricos deste enum `PaymentType`**. Cada elemento define um meio de pagamento que o comprador poderá escolher no checkout ou no link de pagamento.

<a id="installmenttype"></a>

### `InstallmentType`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 0 | None | Transação a vista. |
| 1 | Merchant | Transação parcelada pelo lojista, ou seja, **sem juros**. |
| 2 | Issuer | Transação parcelada pelo emissor do cartão, ou seja, **com juros**. |

<a id="notificationmethod"></a>

### `NotificationMethod`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Email | As notificações são enviadas por e-mail. |

<a id="transferorderstatus"></a>

### `TransferOrderStatus`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Ordered | Quando a transferência é solicitada. |
| 2 | Transferred | Quando o pedido de transferência é feito, ou seja, pago. |
| 3 | Cancelled | Status de quando o usuário cancela o pedido de transferência. |
| 4 | NotTransferred | Situação de quando o pedido de transferência não é realizada por motivos internos. |
| 5 | Processing | Status de quando a transferência está sendo processada. |
| 6 | InsufficientBalanceAtExecuteTed | Saldo total no inferior ao solicitado no momento da TED. Como as transferências podem ser agendadas e não é necessário prever o saldo no horário agendado, visto que muitas operações podem ocorrer naquele horário, então no momento do TED é feita uma verificação para ver se o saldo da conta é maior que o valor de TED solicitado. |
| 7 | BankAccountInexistent | Acontece quando a conta bancária não é encontrada antes do envio do TED. |
| 8 | BankAccountInvalid | Acontece quando a conta bancária encontrada é inválida antes do envio do TED. |

<a id="cardbrand"></a>

### `CardBrand`

| Valor inteiro | Valor string |
| --- | --- |
| 1 | Visa |
| 2 | MasterCard |
| 3 | Amex |
| 4 | Elo |
| 9 | Hipercard |

<a id="chargestatus"></a>

### `ChargeStatus`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Authorized | Todas as transações da cobrança foram aprovadas. |
| 2 | PreAuthorized | Todas as transações da cobrança foram pré-autorizadas. |
| 4 | Canceled | Todas as transações da cobrança foram canceladas. |
| 5 | Partial | As transações da cobrança diferem em status. Verificar o status de cada transação individualmente. |
| 6 | NotAuthorized | Todas as transações da cobrança foram negadas. |
| 7 | PendingCancel | Todas as transações da cobrança estão com cancelamento pendente. |
| 8 | Expired | Cobrança vencida. |

<a id="merchanttype"></a>

### `MerchantType`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Upsell | O comerciante que terá impostos predefinidos e fará upsell para um estabelecimento, também pode gerenciar o portal. |
| 2 | Establishment | Comerciante que não pode vender, mas terá impostos definidos por um comerciante de upsell. Normalmente, esse tipo de comerciante vende produtos aos clientes e não adiciona novos comerciantes. |
| 3 | ISO | Comerciante que é o parceiro que usa nossa plataforma e gerencia todos os impostos para seus parceiros. |

<a id="transactionstatus"></a>

### `TransactionStatus`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | PreAuthorized | Transação pré-autorizada. |
| 2 | Captured | Transação autorizada ou capturada posteriormente. |
| 3 | Denied | Transação negada. |
| 4 | Pending | Transação pendente, a ser processada pela adquirente ou banco. |
| 5 | Canceled | Transação cancelada. |
| 6 | PendingCancel | Transação com cancelamento pendente pela adquirente ou banco. |
| 7 | PendingPayment | Transação enviada a adquirente ou banco, aguardando retorno. |
| 8 | Paid | Boleto pago. |
| 9 | ErrorCreation | Erro ao criar boleto. |
| 10 | Expired | Boleto expirado. |

<a id="smartcheckoutstatus"></a>

### `SmartCheckoutStatus`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Pending | Pendente de pagamento, nenhuma cobrança foi feita ainda. |
| 2 | Activated | Alguma cobrança foi feita, porém não atingiu ainda o limite ou expiração. |
| 3 | Canceled | Cancelado. |
| 100 | ExpiredByMaximumApprovals | Expirado, porque o numero de cobranças atingiu o máximo. |
| 101 | ExpiredByDate | Expirado, porque atingiu a data de expiração. |
| 102 | ExpiredByTooManyDenials | Expirado / bloqueado, devido a muitas tentativas não aprovadas. |

<a id="receivablemode"></a>

### `ReceivableMode`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Default | Usado para recebíveis comuns. D + 30. |
| 2 | NextDay | Usado para recebíveis do dia seguinte. D + 1. |

<a id="acquirercode"></a>

### `AcquirerCode`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Cielo | Cielo |
| 2 | Rede | Rede |
| 3 | Stone | Stone |
| 4 | VBI | VBI |
| 5 | Granito | Granito |
| 6 | InfinitePay | InfinitePay |
| 7 | Safrapay | SafraPay |
| 8 | Adiq (e-commerce) | Adiq |
| 9 | PagSeguro | PagSeguro |
| 10 | Adiq (TEF) | Adiq |
| 11 | SafrapayTef | SafrapayTef |
| 12 | VrBenefits | VR |
| 999 | Simulador | Simulador |

<a id="eventtype"></a>

### `EventType`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Created | Evento disparado quando uma cobrança é feita. |
| 2 | Updated | Evento disparado quando uma atualização na cobrança é feita, ou seja, captura, cancelamento, etc. |

<a id="webhookstatus"></a>

### `WebhookStatus`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Pending | Webhook pendente, ou seja, eventos não serão enviados para ele nesse momento. |
| 2 | Active | Webhook está ativo, ou seja, os eventos configurados serão entregues. |
| 3 | Failed | Limite máximo de falhas atingidos. |
| 4 | Canceled | Webhook cancelado pelo usuário. |

<a id="entitytype"></a>

### `EntityType`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | IndividualMerchant | Pessoa Física |
| 2 | Company | Pessoa Jurídica |

<a id="documenttype"></a>

### `DocumentType`

Atenção: Não fazer o envio da pontuação do número dos documentos.

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Cpf | CPF |
| 2 | Cnpj | CNPJ |
| 3 | Passport | Passaporte |

<a id="documentfiletype"></a>

### `DocumentFileType`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Cnpj | Principal documento jurídico da empresa. |
| 2 | OwnerLegalDocument | Documento jurídico principal do proprietário da empresa. |
| 3 | ProofOfAddress | Documento que comprova o endereço da empresa. |
| 4 | CompanyActivity | Documento que especifica quais produtos ou serviços uma determinada empresa vende. |
| 5 | ReconciliationAgreement | Documento que especifica que contém permissão para acessar EDI. |

<a id="gender"></a>

### `Gender`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Female | Mulher |
| 2 | Male | Homem |
| 3 | Other | Outro |

<a id="cancelstatus"></a>

### `CancelStatus`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 0 | PendingCancel | Cancelamento pendente. |
| 1 | Canceled | Transação cancelada. |
| 2 | NotCanceled | Transação não cancelada ou cancelamento não aprovado. |

<a id="sortdirection"></a>

### `SortDirection`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Ascending | Usado para classificação crescente. |
| 2 | Descending | Usado para classificação decrescente. |

<a id="establishmentstatusenum"></a>

### `EstablishmentStatusEnum`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Pending | Validação pendente e envio para registro. |
| 2 | Active | Ativo no registro e com adquirentes ativos. |
| 3 | Inactive | O estabelecimento não possui transações a serem pagas e não é capaz de efetuar transações no Gateway. |
| 4 | Canceled | O estabelecimento foi cancelado pela matriz. |
| 5 | Suspended | Estabelecimento foi desativado pela matriz e contém transações a serem pagas. |
| 6 | InactiveByRegister | Estabelecimento foi enviado para registro e, em seguida, retornou erro. |

<a id="rolesenum"></a>

### `RolesEnum`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Master | Usuário com nível absoluto de permissões. |
| 2 | Administrator | Usuário pode gerenciar e criar outros usuários. Deve ser capaz de cancelar e capturar cobranças. |
| 3 | Operator | Usuário com permissões básicas, como visualização de cobranças. Não é possível gerenciar outros usuários nem criar novos usuários. |
| 4 | Affiliator | Usuário com permissão apenas para adicionar comerciante dentro de um comerciante pai e ver comerciantes que adicionaram comerciante. |
| 5 | Manager | Usuário com permissão para gerenciar apenas seu comerciante, sem adquirente ou qualquer capacidade para adicionar novo comerciante. |
| 6 | Attendant | Usuário com permissão para visualizar informações no portal mas não pode executar nenhuma ação, como cancelar, criar ou atualizar. |

<a id="bankaccounts"></a>

### `BankAccounts`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | CheckingAccount | Ele está disponível para o proprietário da conta "sob demanda" e está disponível para acesso imediato pelo proprietário da conta ou a outros conforme o proprietário da conta pode direcionar. O acesso pode ser feito de várias maneiras, como saques em dinheiro, uso de cartões de débito, cheques (cheques) e transferência eletrônica. Em termos econômicos, os fundos detidos em um as contas de transações são consideradas como fundos líquidos. Em termos contábeis, eles são considerado como dinheiro. |
| 2 | SavingsAccount | Uma conta de poupança é uma conta de depósito mantida em um banco de varejo que paga juros, mas não pode ser usado diretamente como dinheiro no sentido estrito de um meio de troca (pois exemplo, preenchendo um cheque). Essas contas permitem que os clientes reservem uma parte de seus ativos líquidos enquanto ganham um retorno monetário. |

<a id="entrymode"></a>

### `EntryMode`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | MagneticStripe | Fita Magnética |
| 2 | Emv | EMV |
| 3 | ContactlessMagneticStripe | Fita Magnética sem contato |
| 4 | ContactlessEmv | EMV sem contato |
| 5 | Typed | Digitado |

<a id="reconciliationadjustment"></a>

### `ReconciliationAdjustment`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Credit | O ajuste de crédito adicionará mais dinheiro para a conta do comerciante. |
| 2 | Debit | O ajuste de débito subtrairá o dinheiro das contas a receber do comerciante. |

<a id="reconciliationtype"></a>

### `ReconciliationType`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Sale | Tipo relacionado a conciliações com base na data de venda / transação. |
| 2 | Receivable | Tipo relacionado a conciliações com base na data de pagamento. |

<a id="reconciliationtransactionsstatus"></a>

### `ReconciliationTransactionsStatus`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | PendingPayment | Pendente de Pagamento. |
| 2 | Paid | Pago |
| 3 | Anticipated | Antecipado. |
| 4 | Canceled | Cancelado. |
| 5 | Chargeback | Chargeback. |
| 6 | PendingAnticipation | Pendente de antecipação. |

<a id="reconciliationadjustmentreason"></a>

### `ReconciliationAdjustmentReason`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Payment | Valor de crédito que se refere a uma transação. |
| 2 | Chargeback | Valor de débito que vem de uma transação estornada. |
| 3 | Cancellation | Valor de débito que se refere a uma transação cancelada. |
| 4 | POSRent | Debit value that refers to a POS rent. |
| 5 | Antecipation | Valor de crédito referente a antecipação de transação. |
| 6 | ChargebackRefund | Valor de crédito que se refere a um estorno que foi refutado. |
| 999 | Others | Outros motivos que não são mapeados. |

<a id="documentfile"></a>

### `DocumentFile`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | CNPJ | Principal documento jurídico da empresa. |
| 2 | OwnerLegalDocument | Documento jurídico principal do proprietário da empresa. |
| 3 | ProofOfAddress | Documento que comprova o endereço da empresa. |
| 4 | CompanyActivity | Documento que especifica quais produtos ou serviços uma determinada empresa vende. |
| 5 | ReconciliationAgreement | Documento que especifica que contém permissão para acessar EDI. |

<a id="reconciliationsettingsstatus"></a>

### `ReconciliationSettingsStatus`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Enabled | Quando EDI está disponível para obter registros. |
| 2 | Disabled | O comerciante desativa as configurações de reconciliação ou o EDI não está habilitado. |
| 3 | PendingTerm | O comerciante não enviou termo assinado para Safrapay. |
| 4 | WaitingActivation | O termo foi enviado para o adquirente, mas o EDI ainda não estava habilitado. |

<a id="discounttype"></a>

### `DiscountType`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Percentual | Aplicará desconto percentual com base em uma data de pagamento. |
| 2 | Fixed | Aplicará um valor fixo em centavos com base na data de pagamento. |
| 3 | Daily | Aplicará um valor diário em centavos com base na data de pagamento. |

<a id="paymentsource"></a>

### `PaymentSource`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Gateway | Gateway |
| 2 | Pos | POS |
| 3 | Pinpad | Pinpad |
| 4 | Recurrency | Recorrência |
| 5 | PaymentLink | Link de Pagamento |
| 6 | MobilePos | POS Móvel |
| 8 | ThirdPartyEcommerce | Comércio eletrônico de terceiros |
| 10 | Checkout | Checkout |
| 11 | RecurrencyCheckout | Recorrência Checkout |
| 12 | VtexPaymentProvider | Provedor de Pagamento VTEX |
| 13 | SmartPos | POS Inteligente |
| 1001 | SafrapayCheckout | Checkout Safrapay |
| 1002 | SafrapayPaymentLink | Link de Pagamento Safrapay |
| 1003 | SafrapayCatalogPaymentLink | Link de pagamento do catálogo Safrapay |

<a id="frequency"></a>

### `Frequency`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Daily | Diário |
| 2 | Weekly | Semanal |
| 3 | Monthly | Mensal |
| 6 | Annual | Anual |

<a id="bankslipissuer"></a>

### `BankSlipIssuer`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Bs2 | Banco Bs2. |
| 2 | Safra | Banco Safra. |
| 3 | Santander | Banco Santander. |

<a id="chargeeventmode"></a>

### `ChargeEventMode`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 0 | Undefined | Define como os eventos de cobrança são aplicados a uma determinada assinatura. |
| 1 | ApplyToFirstCharges | O evento de cobrança será aplicado apenas nas primeiras `N` cobranças recorrentes. `N` também é definido ao criar ou atualizar um plano. |

<a id="receivertype"></a>

### `ReceiverType`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Distributor | Distribuidor |
| 2 | Seller | Vendedor |
| 3 | MerchantReceiver | Comerciante Destinatário |

<a id="transferinterval"></a>

### `TransferInterval`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Day | Dia |
| 2 | Week | Semana |
| 3 | Month | Mês |
| 4 | Year | Ano |

<a id="contacttype"></a>

### `ContactType`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Administration | Administração |
| 2 | Financial | Financeiro |
| 3 | Technical | Técnico |

<a id="safrapayproduct"></a>

### `SafrapayProduct`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Ecommerce | Representa o produto de comércio eletrônico |
| 2 | Pos | Representa o produto PDV |
| 3 | Tef | Representa o produto TEF |
| 4 | BankSlip | Representa o produto Boleto Bancário |
| 5 | Voucher | Representa processo de transações VAN, integrando-se diretamente com as bandeiras e adquirentes de cartões voucher. |

<a id="adjustmentstype"></a>

### `AdjustmentsType`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Credit | O ajuste de crédito adicionará mais dinheiro para a conta do comerciante |
| 2 | Debit | O ajuste de débito subtrairá o dinheiro das contas a receber do comerciante |

<a id="adjustmentsreason"></a>

### `AdjustmentsReason`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | Payment | Valor de crédito que se refere a uma transação |
| 2 | Chargeback | Valor de débito que vem de uma transação estornada |
| 3 | Cancellation | Valor de débito que se refere a uma transação cancelada |
| 4 | POSRent | Valor de débito que se refere a um aluguel de POS |
| 5 | Antecipation | Valor de crédito referente a antecipação de transação |
| 6 | ChargebackRefund | Valor de crédito que se refere a um estorno que foi refutado |
| 999 | Others | Outros motivos que não são mapeados |

<a id="transactionstatus-1"></a>

### `TransactionStatus`

| Valor inteiro | Valor string | Descrição |
| --- | --- | --- |
| 1 | PreAuthorized | Transação aprovada |
| 2 | Captured | Transação aprovada e capturada |
| 3 | Denied | Transação não aprovada ou rejeitada |
| 4 | Pending | Transação ainda não processada pela adquirente |
| 5 | Canceled | Transação cancelada |
| 6 | PendingCancel | Transação com cancelamento pendente |
| 7 | PendingPayment | Transação com pagamento pendente |
| 8 | Paid | Transação paga |
| 9 | ErrorCreation | Houve um erro com a transação |
| 10 | Expired | Transação vencida |
| 11 | PendingNewDeadline | Nova data de vencimento pendente |
| 12 | Timeout | Transação não processada devido ao limite de tempo |

<a id="códigos-de-erro-abecs"></a>

## Códigos de Erro ABECs

<a id="visa"></a>

### Visa

| MENSAGEM GENÉRICA | VISA | MENSAGEM DA BANDEIRA |
| --- | --- | --- |
| GENÉRICA | 5 - REVERSÍVEL | CONTATE A CENTRAL DO SEU CARTÃO |
| SALDO/LIMITE INSUFICIENTE | 51 - REVERSÍVEL | NÃO AUTORIZADA |
| SENHA INVÁLIDA | 55 ou 86 - REVERSÍVEL | SENHA INVÁLIDA |
| TRANSAÇÃO NÃO PERMITIDA PARA O CARTÃO | 57 - IRREVERSÍVEL | TRANSAÇÃO NÃO PERMITIDA PARA O CARTÃO - NÃO TENTE NOVAMENTE |
| Nº CARTÃO NÃO PERTENCE AO EMISSOR/Nº CARTÃO INVÁLIDO | 06 - IRREVERSÍVEL | VERIFIQUE OS DADOS DO CARTÃO |
| VIOLAÇÃO DE SEGURANÇA | 06 - IRREVERSÍVEL | VERIFIQUE OS DADOS DO CARTÃO |
| SUSPEITA DE FRAUDE | 59 - REVERSÍVEL | CONTATE A CENTRAL DO SEU CARTÃO |
| COMERCIANTE INVÁLIDO | 3 - IRREVERSÍVEL | TRANSAÇÃO NÃO PERMITIDA - NÃO TENTE NOVAMENTE |
| REFAZER A TRANSAÇÃO (EMISSOR SOLICITA RETENTATIVA) | SEM CÓDIGO CORRESPONDENTE | REFAZER A TRANSAÇÃO |
| CONSULTAR CREDENCIADOR | SEM CÓDIGO CORRESPONDENTE | LOJISTA, CONTATE O ADQUIRENTE |
| PROBLEMA NO ADQUIRENTE | SEM CÓDIGO CORRESPONDENTE | ERRO NO CARTÃO – NÃO TENTE NOVAMENTE |
| ERRO NO CARTÃO | 06 - IRREVERSÍVEL | ERRO NO CARTÃO - VERIFIQUE OS DADOS DO CARTÃO |
| ERRO DE FORMATO(MENSAGERIA) | 12 - IRREVERSÍVEL | ERRO NO CARTÃO - NÃO TENTE NOVAMENTE |
| VALOR DA TRANSAÇÃO INVÁLIDA | 13 - IRREVERSÍVEL | VALOR DA TRANSAÇÃO NÃO PERMITIDO - NÃO TENTE NOVAMENTE |
| VALOR DA PARCELA INVÁLIDA | SEM CÓDIGO CORRESPONDENTE | PARCELAMENTO INVÁLIDO - NÃO TENTE NOVAMENTE |
| EXCEDIDAS TENTATIVAS DE SENHA / COMPRAS | 75 - REVERSÍVEL | EXCEDIDAS TENTATIVAS DE SENHA.CONTATE A CENTRAL DO SEU CARTÃO |
| CARTÃO PERDIDO | 41 - IRREVERSÍVEL | TRANSAÇÃO NÃO PERMITIDA - NÃO TENTE NOVAMENTE |
| CARTÃO ROUBADO | 43 - IRREVERSÍVEL | TRANSAÇÃO NÃO PERMITIDA - NÃO TENTE NOVAMENTE |
| CARTÃO VENCIDO/DT EXPIRAÇÃO INVÁLIDA | 06 - IRREVERSÍVEL | VERIFIQUE OS DADOS DO CARTÃO |
| TRANSAÇÃO NÃO PERMITIDA/CAPACIDADE DO TERMINAL | 58 - IRREVERSÍVEL | TRANSAÇÃO NÃO PERMITIDA PARA O CARTÃO - NÃO TENTE NOVAMENTE |
| VALOR EXCESSO | SAQUE 61 ou N4 - REVERSÍVEL | VALOR EXCEDIDO.CONTATE A CENTRAL DO SEU CARTÃO |
| CARTÃO DOMÉSTICO - TRANSAÇÃO INTERNACIONAL | 62 - IRREVERSÍVEL | CARTÃO NÃO PERMITE TRANSAÇÃO INTERNACIONAL |
| VALOR MÍNIMO DA TRANSAÇÃO INVÁLIDO | SEM CÓDIGO CORRESPONDENTE | VALOR DA TRANSAÇÃO NÃO PERMITIDO - NÃO TENTE NOVAMENTE |
| QUANT. DE SAQUES EXCEDIDO | 65 - REVERSÍVEL | QTDADE DE SAQUES EXCEDIDA.CONTATE A CENTRAL DO SEU CARTÃO |
| SENHA VENCIDA/ERRO DE CRIPTOGRAFIA DE SENHA | 74 ou 81 - IRREVERSÍVEL | SENHA INVÁLIDA - NÃO TENTE NOVAMENTE |
| EXCEDIDAS TENTATIVAS DE SENHA/SAQUE | 75 - REVERSÍVEL | EXCEDIDAS TENTATIVAS DE SENHA.CONTATE A CENTRAL DO SEU CARTÃO |
| CONTA DESTINO INVÁLIDA OU INEXISTENTE | SEM CÓDIGO CORRESPONDENTE | CONTA DESTINO INVÁLIDA - NÃO TENTE NOVAMENTE |
| CONTA ORIGEM INVÁLIDA OU INEXISTENTE | SEM CÓDIGO CORRESPONDENTE | CONTA ORIGEM INVÁLIDA - NÃO TENTE NOVAMENTE |
| CARTÃO NOVO SEM DESBLOQUEIO | 78 - REVERSÍVEL | DESBLOQUEIE O CARTÃO |
| CARTÃO INVÁLIDO (criptograma) | 82 - IRREVERSÍVEL | ERRO NO CARTÃO - NÃO TENTE NOVAMENTE |
| EMISSOR FORA DO AR | 91 - REVERSÍVEL | FALHA DE COMUNICAÇÃO - TENTE MAIS TARDE |
| FALHA DO SISTEMA | 96 - REVERSÍVEL | FALHA DE COMUNICAÇÃO - TENTE MAIS TARDE |
| DIFERENÇA - PRÉ AUTORIZAÇÃO | N8 - IRREVERSÍVEL | VALOR DIFERENTE DA PRÉ AUTORIZAÇÃO - NÃO TENTE NOVAMENTE |
| FUNÇÃO INCORRETA (DÉBITO) | 52 ou 53 - IRREVERSÍVEL | UTILIZE FUNÇÃO CRÉDITO |
| FUNÇÃO INCORRETA (CRÉDITO) | 39 - IRREVERSÍVEL | UTILIZE FUNÇÃO DÉBITO |
| TROCA DE SENHA / DESBLOQUEIO | SEM CÓDIGO CORRESPONDENTE | SENHA INVÁLIDA - NÃO TENTE NOVAMENTE |
| NOVA SENHA NÃO ACEITA | SEM CÓDIGO CORRESPONDENTE | SENHA INVÁLIDA UTILIZE A NOVA SENHA |
| RECOLHER CARTÃO (NÃO HÁ FRAUDE) | 4 - IRREVERSÍVEL | CONTATE A CENTRAL DO SEU CARTÃO - NÃO TENTE NOVAMENTE |
| ERRO POR MUDANÇA DE CHAVE DINÂMICA | 6 - IRREVERSÍVEL | ERRO NO CARTÃO - NÃO TENTE NOVAMENTE |
| FRAUDE CONFIRMADA | 7 - IRREVERSÍVEL | TRANSAÇÃO NÃO PERMITIDA PARA O CARTÃO - NÃO TENTE NOVAMENTE |
| EMISSOR NÃO LOCALIZADO - BIN INCORRETO (negativa do adquirente) | 15 - IRREVERSÍVEL | DADOS DO CARTÃO INVÁLIDO - NÃO TENTE NOVAMENTE |
| NÃO CUMPRIMENTO PELAS LEIS DE ANTE LAVAGEM DE DINHEIRO | 64 - IRREVERSÍVEL | CONTATE A CENTRAL DO SEU CARTÃO - NÃO TENTE NOVAMENTE |
| REVERSÃO INVÁLIDA | 76 - IRREVERSÍVEL | CONTATE A CENTRAL DO SEU CARTÃO - NÃO TENTE NOVAMENTE |
| NÃO LOCALIZADO PELO ROTEADOR | 92 - IRREVERSÍVEL | CONTATE A CENTRAL DO SEU CARTÃO - NÃO TENTE NOVAMENTE |
| TRANSAÇÃO NEGADA POR INFRAÇÃO DE LEI | 93 - IRREVERSÍVEL | TRANSAÇÃO NÃO PERMITIDA PARA O CARTÃO - NÃO TENTE NOVAMENTE |
| VALOR DO TRACING DATA DUPLICADO | 94 - IRREVERSÍVEL | CONTATE A CENTRAL DO SEU CARTÃO - NÃO TENTE NOVAMENTE |
| SURCHARGE NÃO SUPORTADO | B1 - REVERSÍVEL | CONTATE A CENTRAL DO SEU CARTÃO |
| SURCHARGE NÃO SUPORTADO PELA REDE DE DÉBITO | B2 - REVERSÍVEL | CONTATE A CENTRAL DO SEU CARTÃO |
| FORÇAR STIP | N0 - REVERSÍVEL | CONTATE A CENTRAL DO SEU CARTÃO |
| SAQUE NÃO DISPONÍVEL | N3 - IRREVERSÍVEL | SAQUE NÃO DISPONÍVEL - NÃO TENTE NOVAMENTE |
| SUSPENSÃO DE PAGAMENTO RECORRENTE PARA UM SERVIÇO | R0 - IRREVERSÍVEL | SUSPENSÃO DE PAGAMENTO RECORRENTE PARA SERVIÇO - NÃO TENTE NOVAMENTE |
| SUSPENSÃO DE PAGAMENTO RECORRENTE PARA TODOS SERVIÇO | R1 - IRREVERSÍVEL | SUSPENSÃO DE PAGAMENTO RECORRENTE PARA SERVIÇO - NÃO TENTE NOVAMENTE |
| TRANSAÇÃO NÃO QUALIFICADA PARA VISA PIN | R2 - IRREVERSÍVEL | TRANSAÇÃO NÃO PERMITIDA PARA O CARTÃO - NÃO TENTE NOVAMENTE |
| SUSPENSÃO DE TODAS AS ORDENS DE AUTORIZAÇÃO | R3 - IRREVERSÍVEL | SUSPENSÃO DE PAGAMENTO RECORRENTE PARA SERVIÇO - NÃO TENTE NOVAMENTE |
| NÃO É POSSÍVEL LOCALIZAR O REGISTRO NO ARQUIVO | SEM CÓDIGO CORRESPONDENTE | CONTATE A CENTRAL DO SEU CARTÃO - NÃO TENTE NOVAMENTE |
| ARQUIVO NÃO DISPONÍVEL PARA ATUALIZAÇÃO | SEM CÓDIGO CORRESPONDENTE | CONTATE A CENTRAL DO SEU CARTÃO - NÃO TENTE NOVAMENTE |

<a id="mastercard"></a>

### Mastercard

| MENSAGEM GENÉRICA | MASTERCARD/HIPER | MENSAGEM DA BANDEIRA |
| --- | --- | --- |
| GENÉRICA | 5 - REVERSÍVEL | CONTATE A CENTRAL DO SEU CARTÃO |
| SALDO/LIMITE INSUFICIENTE | 51 - REVERSÍVEL | NÃO AUTORIZADA |
| SENHA INVÁLIDA | 55 ou 86 - REVERSÍVEL | SENHA INVÁLIDA |
| TRANSAÇÃO NÃO PERMITIDA PARA O CARTÃO | 57 - IRREVERSÍVEL | TRANSAÇÃO NÃO PERMITIDA PARA O CARTÃO - NÃO TENTE NOVAMENTE |
| Nº CARTÃO NÃO PERTENCE AO EMISSOR/Nº CARTÃO INVÁLIDO | 14 ou 1 - IRREVERSÍVEL | VERIFIQUE OS DADOS DO CARTÃO |
| VIOLAÇÃO DE SEGURANÇA | 14 - IRREVERSÍVEL | VERIFIQUE OS DADOS DO CARTÃO |
| SUSPEITA DE FRAUDE | 63 - REVERSÍVEL | CONTATE A CENTRAL DO SEU CARTÃO |
| COMERCIANTE INVÁLIDO | 3 - IRREVERSÍVEL | TRANSAÇÃO NÃO PERMITIDA - NÃO TENTE NOVAMENTE |
| REFAZER A TRANSAÇÃO (EMISSOR SOLICITA RETENTATIVA) | SEM CÓDIGO CORRESPONDENTE | REFAZER A TRANSAÇÃO |
| CONSULTAR CREDENCIADOR | SEM CÓDIGO CORRESPONDENTE | LOJISTA, CONTATE O ADQUIRENTE |
| PROBLEMA NO ADQUIRENTE | 30 - IRREVERSÍVEL | ERRO NO CARTÃO – NÃO TENTE NOVAMENTE |
| ERRO NO CARTÃO | SEM CÓDIGO CORRESPONDENTE | ERRO NO CARTÃO - VERIFIQUE OS DADOS DO CARTÃO |
| ERRO DE FORMATO(MENSAGERIA) | 30 - IRREVERSÍVEL | ERRO NO CARTÃO - NÃO TENTE NOVAMENTE |
| VALOR DA TRANSAÇÃO INVÁLIDA | 13 - IRREVERSÍVEL | VALOR DA TRANSAÇÃO NÃO PERMITIDO - NÃO TENTE NOVAMENTE |
| VALOR DA PARCELA INVÁLIDA | 12 - IRREVERSÍVEL | PARCELAMENTO INVÁLIDO - NÃO TENTE NOVAMENTE |
| EXCEDIDAS TENTATIVAS DE SENHA / COMPRAS | 75 - REVERSÍVEL | EXCEDIDAS TENTATIVAS DE SENHA.CONTATE A CENTRAL DO SEU CARTÃO |
| CARTÃO PERDIDO | 41 - IRREVERSÍVEL | TRANSAÇÃO NÃO PERMITIDA - NÃO TENTE NOVAMENTE |
| CARTÃO ROUBADO | 43 - IRREVERSÍVEL | TRANSAÇÃO NÃO PERMITIDA - NÃO TENTE NOVAMENTE |
| CARTÃO VENCIDO/DT EXPIRAÇÃO INVÁLIDA | 54 - IRREVERSÍVEL | VERIFIQUE OS DADOS DO CARTÃO |
| TRANSAÇÃO NÃO PERMITIDA/CAPACIDADE DO TERMINAL | 58 - IRREVERSÍVEL | TRANSAÇÃO NÃO PERMITIDA PARA O CARTÃO - NÃO TENTE NOVAMENTE |
| VALOR EXCESSO | 61 - REVERSÍVEL | VALOR EXCEDIDO.CONTATE A CENTRAL DO SEU CARTÃO |
| CARTÃO DOMÉSTICO - TRANSAÇÃO INTERNACIONAL | 62 - IRREVERSÍVEL | CARTÃO NÃO PERMITE TRANSAÇÃO INTERNACIONAL |
| VALOR MÍNIMO DA TRANSAÇÃO INVÁLIDO | SEM CÓDIGO CORRESPONDENTE | VALOR DA TRANSAÇÃO NÃO PERMITIDO - NÃO TENTE NOVAMENTE |
| QUANT. DE SAQUES EXCEDIDO | 65 - REVERSÍVEL | QTDADE DE SAQUES EXCEDIDA.CONTATE A CENTRAL DO SEU CARTÃO |
| SENHA VENCIDA/ERRO DE CRIPTOGRAFIA DE SENHA | 88 - IRREVERSÍVEL | SENHA INVÁLIDA - NÃO TENTE NOVAMENTE |
| EXCEDIDAS TENTATIVAS DE SENHA/SAQUE | 75 - REVERSÍVEL | EXCEDIDAS TENTATIVAS DE SENHA.CONTATE A CENTRAL DO SEU CARTÃO |
| CONTA DESTINO INVÁLIDA OU INEXISTENTE | SEM CÓDIGO CORRESPONDENTE | CONTA DESTINO INVÁLIDA - NÃO TENTE NOVAMENTE |
| CONTA ORIGEM INVÁLIDA OU INEXISTENTE | SEM CÓDIGO CORRESPONDENTE | CONTA ORIGEM INVÁLIDA - NÃO TENTE NOVAMENTE |
| CARTÃO NOVO SEM DESBLOQUEIO | SEM CÓDIGO CORRESPONDENTE | DESBLOQUEIE O CARTÃO |
| CARTÃO INVÁLIDO (criptograma) | 88 - IRREVERSÍVEL | ERRO NO CARTÃO - NÃO TENTE NOVAMENTE |
| EMISSOR FORA DO AR | 91 - REVERSÍVEL | FALHA DE COMUNICAÇÃO - TENTE MAIS TARDE |
| FALHA DO SISTEMA | 96 - REVERSÍVEL | FALHA DE COMUNICAÇÃO - TENTE MAIS TARDE |
| DIFERENÇA - PRÉ AUTORIZAÇÃO | SEM CÓDIGO CORRESPONDENTE | VALOR DIFERENTE DA PRÉ AUTORIZAÇÃO - NÃO TENTE NOVAMENTE |
| FUNÇÃO INCORRETA (DÉBITO) | SEM CÓDIGO CORRESPONDENTE | UTILIZE FUNÇÃO CRÉDITO |
| FUNÇÃO INCORRETA (CRÉDITO) | SEM CÓDIGO CORRESPONDENTE | UTILIZE FUNÇÃO DÉBITO |
| TROCA DE SENHA / DESBLOQUEIO | SEM CÓDIGO CORRESPONDENTE | SENHA INVÁLIDA - NÃO TENTE NOVAMENTE |
| NOVA SENHA NÃO ACEITA | SEM CÓDIGO CORRESPONDENTE | SENHA INVÁLIDA UTILIZE A NOVA SENHA |
| RECOLHER CARTÃO (NÃO HÁ FRAUDE) | SEM CÓDIGO CORRESPONDENTE | CONTATE A CENTRAL DO SEU CARTÃO - NÃO TENTE NOVAMENTE |
| ERRO POR MUDANÇA DE CHAVE DINÂMICA | SEM CÓDIGO CORRESPONDENTE | ERRO NO CARTÃO - NÃO TENTE NOVAMENTE |
| FRAUDE CONFIRMADA | 4 - IRREVERSÍVEL | TRANSAÇÃO NÃO PERMITIDA PARA O CARTÃO - NÃO TENTE NOVAMENTE |
| EMISSOR NÃO LOCALIZADO - BIN INCORRETO (negativa do adquirente) | 15 - IRREVERSÍVEL | DADOS DO CARTÃO INVÁLIDO - NÃO TENTE NOVAMENTE |
| NÃO CUMPRIMENTO PELAS LEIS DE ANTE LAVAGEM DE DINHEIRO | SEM CÓDIGO CORRESPONDENTE | CONTATE A CENTRAL DO SEU CARTÃO - NÃO TENTE NOVAMENTE |
| REVERSÃO INVÁLIDA | SEM CÓDIGO CORRESPONDENTE | CONTATE A CENTRAL DO SEU CARTÃO - NÃO TENTE NOVAMENTE |
| NÃO LOCALIZADO PELO ROTEADOR | 92 - IRREVERSÍVEL | CONTATE A CENTRAL DO SEU CARTÃO - NÃO TENTE NOVAMENTE |
| TRANSAÇÃO NEGADA POR INFRAÇÃO DE LEI | 57 - IRREVERSÍVEL | TRANSAÇÃO NÃO PERMITIDA PARA O CARTÃO - NÃO TENTE NOVAMENTE |
| VALOR DO TRACING DATA DUPLICADO | 94 - IRREVERSÍVEL | CONTATE A CENTRAL DO SEU CARTÃO - NÃO TENTE NOVAMENTE |
| SURCHARGE NÃO SUPORTADO | SEM CÓDIGO CORRESPONDENTE | CONTATE A CENTRAL DO SEU CARTÃO |
| SURCHARGE NÃO SUPORTADO PELA REDE DE DÉBITO | SEM CÓDIGO CORRESPONDENTE | CONTATE A CENTRAL DO SEU CARTÃO |
| FORÇAR STIP | SEM CÓDIGO CORRESPONDENTE | CONTATE A CENTRAL DO SEU CARTÃO |
| SAQUE NÃO DISPONÍVEL | SEM CÓDIGO CORRESPONDENTE | SAQUE NÃO DISPONÍVEL - NÃO TENTE NOVAMENTE |
| SUSPENSÃO DE PAGAMENTO RECORRENTE PARA UM SERVIÇO | SEM CÓDIGO CORRESPONDENTE | SUSPENSÃO DE PAGAMENTO RECORRENTE PARA SERVIÇO - NÃO TENTE NOVAMENTE |
| SUSPENSÃO DE PAGAMENTO RECORRENTE PARA TODOS SERVIÇO | SEM CÓDIGO CORRESPONDENTE | SUSPENSÃO DE PAGAMENTO RECORRENTE PARA SERVIÇO - NÃO TENTE NOVAMENTE |
| TRANSAÇÃO NÃO QUALIFICADA PARA VISA PIN | SEM CÓDIGO CORRESPONDENTE | TRANSAÇÃO NÃO PERMITIDA PARA O CARTÃO - NÃO TENTE NOVAMENTE |
| SUSPENSÃO DE TODAS AS ORDENS DE AUTORIZAÇÃO | SEM CÓDIGO CORRESPONDENTE | SUSPENSÃO DE PAGAMENTO RECORRENTE PARA SERVIÇO - NÃO TENTE NOVAMENTE |
| NÃO É POSSÍVEL LOCALIZAR O REGISTRO NO ARQUIVO | 25 - IRREVERSÍVEL | CONTATE A CENTRAL DO SEU CARTÃO - NÃO TENTE NOVAMENTE |
| ARQUIVO NÃO DISPONÍVEL PARA ATUALIZAÇÃO | 28 - IRREVERSÍVEL | CONTATE A CENTRAL DO SEU CARTÃO - NÃO TENTE NOVAMENTE |

<a id="retentativas"></a>

## Retentativas

O Merchant Advice Code é um valor retornado no atributo **charge.transactions.merchantAdviceCode** de nossa API de pagamento, permitindo que o estabelecimento comercial resubmeta uma transação com base no código de resposta e/ou valor retornado nesse atributo pela bandeira. Este programa foi desenvolvido pelas bandeiras com o objetivo de orientar ações apropriadas para transações negadas, evitando reenvios excessivos ou retentativas em transações que não suportam tal procedimento. Até o momento, as bandeiras **Mastercard, VISA** e **ELO** estabeleceram regras em um programa de excelência que penalizam o reenvio excessivo de transações nesse cenário, aplicando tarifas adicionais que variam conforme a bandeira. 

 Os códigos Merchant Advice Code **03** ou **21**, retornados no atributo **charge.transactions.merchantAdviceCode**, **não são passíveis de retentativa**. Quando a transação for bandeira VISA, apenas o MAC **01** **não é passível** de retentativa (vide tabela VISA com as categorias 1, 2, 3 e 4 devolvidas no atributo merchantAdviceCode). No caso de transações com os códigos MAC **24, 25, 26, 27, 28, 29** e **30**, devolvidos especificamente pela bandeira Mastercard, e acompanhados pela recusa da transação por **51** (Saldo Insuficiente) no atributo charge.transactions.authorizationResponseCode, devem seguir as seguintes regras para retentativa:

<a id="bandeira-mastercard"></a>

#### Bandeira Mastercard

| merchantAdviceCode | Descrição |
| --- | --- |
| 01 | Novas informações disponíveis sobre a conta. |
| 02 | Tente mais tarde. |
| 03 | Não tente novamente. |
| 04 | Transação não suportada. |
| 05 | Não tente novamente. |
| 21 | Plano cancelado. |
| 24 | Tente novamente após 1 hora. |
| 25 | Tente novamente após 24 hora. |
| 26 | Tente novamente após 2 dias. |
| 27 | Tente novamente após 4 dias. |
| 28 | Tente novamente após 6 dias. |
| 29 | Tente novamente após 8 dias. |
| 30 | Tente novamente após 10 dias. |
| 40 | Não tente novamente. |
| 41 | Não tente novamente. |

<a id="bandeira-visa"></a>

#### Bandeira VISA

| merchantAdviceCode | Descrição |
| --- | --- |
| 01 | Não tente novamente. |
| 02 | Tente mais tarde (Retentar até 15 vezes no periodo de 30 dias). |
| 03 | Revisar os dados (Retentar até 15 vezes no periodo de 30 dias). |
| 04 | Códigos de respostas genéricos (Retentar até 15 vezes no periodo de 30 dias). |
