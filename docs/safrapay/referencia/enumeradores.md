---
title: "Enumeradores"
parent: "Referência"
nav_order: 20
layout: "doc"
permalink: "/referencia/enumeradores/"
description: "Tabela de referência de todos os enumeradores usados pela API SafraPay."
---


# Enumeradores

Lista com os enumeradores, eles te ajudarão a escolher a opção correta dentro de um campo da requisição.

## Índice

[AcquirerCode](#acquirercode) · [AdjustmentsReason](#adjustmentsreason) · [AdjustmentsType](#adjustmentstype) · [BankAccounts](#bankaccounts) · [BankSlipIssuer](#bankslipissuer) · [CancelStatus](#cancelstatus) · [CardBrand](#cardbrand) · [ChargeEventMode](#chargeeventmode) · [ChargeStatus](#chargestatus) · [ContactType](#contacttype) · [DiscountType](#discounttype) · [DocumentFile](#documentfile) · [DocumentFileType](#documentfiletype) · [DocumentType](#documenttype) · [EntityType](#entitytype) · [EntryMode](#entrymode) · [EstablishmentStatusEnum](#establishmentstatusenum) · [EventType](#eventtype) · [Frequency](#frequency) · [Gender](#gender) · [InstallmentType](#installmenttype) · [MerchantType](#merchanttype) · [NotificationMethod](#notificationmethod) · [PaymentSource](#paymentsource) · [PaymentType](#paymenttype) · [Phone](#phone) · [ReceivableMode](#receivablemode) · [ReceiverType](#receivertype) · [ReconciliationAdjustment](#reconciliationadjustment) · [ReconciliationAdjustmentReason](#reconciliationadjustmentreason) · [ReconciliationSettingsStatus](#reconciliationsettingsstatus) · [ReconciliationTransactionsStatus](#reconciliationtransactionsstatus) · [ReconciliationType](#reconciliationtype) · [RolesEnum](#rolesenum) · [SafrapayProduct](#safrapayproduct) · [SmartCheckoutStatus](#smartcheckoutstatus) · [SmartCheckoutType](#smartcheckouttype) · [SortDirection](#sortdirection) · [TransactionStatus](#transactionstatus) · [TransactionStatus (2)](#transactionstatus-1) · [TransferInterval](#transferinterval) · [TransferOrderStatus](#transferorderstatus) · [WebhookStatus](#webhookstatus)

## AcquirerCode

| Valor | Nome | Descrição |
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

## AdjustmentsReason

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Payment | Valor de crédito que se refere a uma transação |
| 2 | Chargeback | Valor de débito que vem de uma transação estornada |
| 3 | Cancellation | Valor de débito que se refere a uma transação cancelada |
| 4 | POSRent | Valor de débito que se refere a um aluguel de POS |
| 5 | Antecipation | Valor de crédito referente a antecipação de transação |
| 6 | ChargebackRefund | Valor de crédito que se refere a um estorno que foi refutado |
| 999 | Others | Outros motivos que não são mapeados |

## AdjustmentsType

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Credit | O ajuste de crédito adicionará mais dinheiro para a conta do comerciante |
| 2 | Debit | O ajuste de débito subtrairá o dinheiro das contas a receber do comerciante |

## BankAccounts

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | CheckingAccount | Ele está disponível para o proprietário da conta "sob demanda" e está disponível para acesso imediato pelo proprietário da conta ou a outros conforme o proprietário da conta pode direcionar. O acesso pode ser feito de várias maneiras, como saques em dinheiro, uso de cartões de débito, cheques (cheques) e transferência eletrônica. Em termos econômicos, os fundos detidos em um as contas de transações são consideradas como fundos líquidos. Em termos contábeis, eles são considerado como dinheiro. |
| 2 | SavingsAccount | Uma conta de poupança é uma conta de depósito mantida em um banco de varejo que paga juros, mas não pode ser usado diretamente como dinheiro no sentido estrito de um meio de troca (pois exemplo, preenchendo um cheque). Essas contas permitem que os clientes reservem uma parte de seus ativos líquidos enquanto ganham um retorno monetário. |

## BankSlipIssuer

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Bs2 | Banco Bs2. |
| 2 | Safra | Banco Safra. |
| 3 | Santander | Banco Santander. |

## CancelStatus

| Valor | Nome | Descrição |
| --- | --- | --- |
| 0 | PendingCancel | Cancelamento pendente. |
| 1 | Canceled | Transação cancelada. |
| 2 | NotCanceled | Transação não cancelada ou cancelamento não aprovado. |

## CardBrand

| Valor | Nome |
| --- | --- |
| 1 | Visa |
| 2 | MasterCard |
| 3 | Amex |
| 4 | Elo |
| 9 | Hipercard |

## ChargeEventMode

| Valor | Nome | Descrição |
| --- | --- | --- |
| 0 | Undefined | Define como os eventos de cobrança são aplicados a uma determinada assinatura. |
| 1 | ApplyToFirstCharges | O evento de cobrança será aplicado apenas nas primeiras N cobranças recorrentes. N também é definido ao criar ou atualizar um plano. |

## ChargeStatus

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Authorized | Todas as transações da cobrança foram aprovadas. |
| 2 | PreAuthorized | Todas as transações da cobrança foram pré-autorizadas. |
| 4 | Canceled | Todas as transações da cobrança foram canceladas. |
| 5 | Partial | As transações da cobrança diferem em status. Verificar o status de cada transação individualmente. |
| 6 | NotAuthorized | Todas as transações da cobrança foram negadas. |
| 7 | PendingCancel | Todas as transações da cobrança estão com cancelamento pendente. |
| 8 | Expired | Cobrança vencida. |

## ContactType

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Administration | Administração |
| 2 | Financial | Financeiro |
| 3 | Technical | Técnico |

## DiscountType

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Percentual | Aplicará desconto percentual com base em uma data de pagamento. |
| 2 | Fixed | Aplicará um valor fixo em centavos com base na data de pagamento. |
| 3 | Daily | Aplicará um valor diário em centavos com base na data de pagamento. |

## DocumentFile

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | CNPJ | Principal documento jurídico da empresa. |
| 2 | OwnerLegalDocument | Documento jurídico principal do proprietário da empresa. |
| 3 | ProofOfAddress | Documento que comprova o endereço da empresa. |
| 4 | CompanyActivity | Documento que especifica quais produtos ou serviços uma determinada empresa vende. |
| 5 | ReconciliationAgreement | Documento que especifica que contém permissão para acessar EDI. |

## DocumentFileType

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Cnpj | Principal documento jurídico da empresa. |
| 2 | OwnerLegalDocument | Documento jurídico principal do proprietário da empresa. |
| 3 | ProofOfAddress | Documento que comprova o endereço da empresa. |
| 4 | CompanyActivity | Documento que especifica quais produtos ou serviços uma determinada empresa vende. |
| 5 | ReconciliationAgreement | Documento que especifica que contém permissão para acessar EDI. |

## DocumentType

Atenção: Não fazer o envio da pontuação do número dos documentos.

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Cpf | CPF |
| 2 | Cnpj | CNPJ |
| 3 | Passport | Passaporte |

## EntityType

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | IndividualMerchant | Pessoa Física |
| 2 | Company | Pessoa Jurídica |

## EntryMode

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | MagneticStripe | Fita Magnética |
| 2 | Emv | EMV |
| 3 | ContactlessMagneticStripe | Fita Magnética sem contato |
| 4 | ContactlessEmv | EMV sem contato |
| 5 | Typed | Digitado |

## EstablishmentStatusEnum

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Pending | Validação pendente e envio para registro. |
| 2 | Active | Ativo no registro e com adquirentes ativos. |
| 3 | Inactive | O estabelecimento não possui transações a serem pagas e não é capaz de efetuar transações no Gateway. |
| 4 | Canceled | O estabelecimento foi cancelado pela matriz. |
| 5 | Suspended | Estabelecimento foi desativado pela matriz e contém transações a serem pagas. |
| 6 | InactiveByRegister | Estabelecimento foi enviado para registro e, em seguida, retornou erro. |

## EventType

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Created | Evento disparado quando uma cobrança é feita. |
| 2 | Updated | Evento disparado quando uma atualização na cobrança é feita, ou seja, captura, cancelamento, etc. |

## Frequency

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Daily | Diário |
| 2 | Weekly | Semanal |
| 3 | Monthly | Mensal |
| 6 | Annual | Anual |

## Gender

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Female | Mulher |
| 2 | Male | Homem |
| 3 | Other | Outro |

## InstallmentType

| Valor | Nome | Descrição |
| --- | --- | --- |
| 0 | None | Transação a vista. |
| 1 | Merchant | Transação parcelada pelo lojista, ou seja, sem juros . |
| 2 | Issuer | Transação parcelada pelo emissor do cartão, ou seja, com juros . |

## MerchantType

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Upsell | O comerciante que terá impostos predefinidos e fará upsell para um estabelecimento, também pode gerenciar o portal. |
| 2 | Establishment | Comerciante que não pode vender, mas terá impostos definidos por um comerciante de upsell. Normalmente, esse tipo de comerciante vende produtos aos clientes e não adiciona novos comerciantes. |
| 3 | ISO | Comerciante que é o parceiro que usa nossa plataforma e gerencia todos os impostos para seus parceiros. |

## NotificationMethod

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Email | As notificações são enviadas por e-mail. |

## PaymentSource

| Valor | Nome | Descrição |
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

## PaymentType

| Valor | Nome | Descrição |
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

## Phone

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Residencial | Telefone Residencial |
| 2 | Commercial | Telefone Comercial |
| 3 | Voicemail | Correio de Voz |
| 4 | Temporary | Telefone Temporário |
| 5 | Mobile | Celular |

## ReceivableMode

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Default | Usado para recebíveis comuns. D + 30. |
| 2 | NextDay | Usado para recebíveis do dia seguinte. D + 1. |

## ReceiverType

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Distributor | Distribuidor |
| 2 | Seller | Vendedor |
| 3 | MerchantReceiver | Comerciante Destinatário |

## ReconciliationAdjustment

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Credit | O ajuste de crédito adicionará mais dinheiro para a conta do comerciante. |
| 2 | Debit | O ajuste de débito subtrairá o dinheiro das contas a receber do comerciante. |

## ReconciliationAdjustmentReason

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Payment | Valor de crédito que se refere a uma transação. |
| 2 | Chargeback | Valor de débito que vem de uma transação estornada. |
| 3 | Cancellation | Valor de débito que se refere a uma transação cancelada. |
| 4 | POSRent | Debit value that refers to a POS rent. |
| 5 | Antecipation | Valor de crédito referente a antecipação de transação. |
| 6 | ChargebackRefund | Valor de crédito que se refere a um estorno que foi refutado. |
| 999 | Others | Outros motivos que não são mapeados. |

## ReconciliationSettingsStatus

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Enabled | Quando EDI está disponível para obter registros. |
| 2 | Disabled | O comerciante desativa as configurações de reconciliação ou o EDI não está habilitado. |
| 3 | PendingTerm | O comerciante não enviou termo assinado para Safrapay. |
| 4 | WaitingActivation | O termo foi enviado para o adquirente, mas o EDI ainda não estava habilitado. |

## ReconciliationTransactionsStatus

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | PendingPayment | Pendente de Pagamento. |
| 2 | Paid | Pago |
| 3 | Anticipated | Antecipado. |
| 4 | Canceled | Cancelado. |
| 5 | Chargeback | Chargeback. |
| 6 | PendingAnticipation | Pendente de antecipação. |

## ReconciliationType

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Sale | Tipo relacionado a conciliações com base na data de venda / transação. |
| 2 | Receivable | Tipo relacionado a conciliações com base na data de pagamento. |

## RolesEnum

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Master | Usuário com nível absoluto de permissões. |
| 2 | Administrator | Usuário pode gerenciar e criar outros usuários. Deve ser capaz de cancelar e capturar cobranças. |
| 3 | Operator | Usuário com permissões básicas, como visualização de cobranças. Não é possível gerenciar outros usuários nem criar novos usuários. |
| 4 | Affiliator | Usuário com permissão apenas para adicionar comerciante dentro de um comerciante pai e ver comerciantes que adicionaram comerciante. |
| 5 | Manager | Usuário com permissão para gerenciar apenas seu comerciante, sem adquirente ou qualquer capacidade para adicionar novo comerciante. |
| 6 | Attendant | Usuário com permissão para visualizar informações no portal mas não pode executar nenhuma ação, como cancelar, criar ou atualizar. |

## SafrapayProduct

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Ecommerce | Representa o produto de comércio eletrônico |
| 2 | Pos | Representa o produto PDV |
| 3 | Tef | Representa o produto TEF |
| 4 | BankSlip | Representa o produto Boleto Bancário |
| 5 | Voucher | Representa processo de transações VAN, integrando-se diretamente com as bandeiras e adquirentes de cartões voucher. |

## SmartCheckoutStatus

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Pending | Pendente de pagamento, nenhuma cobrança foi feita ainda. |
| 2 | Activated | Alguma cobrança foi feita, porém não atingiu ainda o limite ou expiração. |
| 3 | Canceled | Cancelado. |
| 100 | ExpiredByMaximumApprovals | Expirado, porque o numero de cobranças atingiu o máximo. |
| 101 | ExpiredByDate | Expirado, porque atingiu a data de expiração. |
| 102 | ExpiredByTooManyDenials | Expirado / bloqueado, devido a muitas tentativas não aprovadas. |

## SmartCheckoutType

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | PaymentLink | SmartCheckout do tipo Link de Pagamento, criado via endpoint /paymentlink. |
| 2 | Checkout | SmartCheckout do tipo Checkout, criado via endpoint /smartcheckout. |

## SortDirection

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Ascending | Usado para classificação crescente. |
| 2 | Descending | Usado para classificação decrescente. |

## TransactionStatus

| Valor | Nome | Descrição |
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

## TransactionStatus

| Valor | Nome | Descrição |
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

## TransferInterval

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Day | Dia |
| 2 | Week | Semana |
| 3 | Month | Mês |
| 4 | Year | Ano |

## TransferOrderStatus

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Ordered | Quando a transferência é solicitada. |
| 2 | Transferred | Quando o pedido de transferência é feito, ou seja, pago. |
| 3 | Cancelled | Status de quando o usuário cancela o pedido de transferência. |
| 4 | NotTransferred | Situação de quando o pedido de transferência não é realizada por motivos internos. |
| 5 | Processing | Status de quando a transferência está sendo processada. |
| 6 | InsufficientBalanceAtExecuteTed | Saldo total no inferior ao solicitado no momento da TED. Como as transferências podem ser agendadas e não é necessário prever o saldo no horário agendado, visto que muitas operações podem ocorrer naquele horário, então no momento do TED é feita uma verificação para ver se o saldo da conta é maior que o valor de TED solicitado. |
| 7 | BankAccountInexistent | Acontece quando a conta bancária não é encontrada antes do envio do TED. |
| 8 | BankAccountInvalid | Acontece quando a conta bancária encontrada é inválida antes do envio do TED. |

## WebhookStatus

| Valor | Nome | Descrição |
| --- | --- | --- |
| 1 | Pending | Webhook pendente, ou seja, eventos não serão enviados para ele nesse momento. |
| 2 | Active | Webhook está ativo, ou seja, os eventos configurados serão entregues. |
| 3 | Failed | Limite máximo de falhas atingidos. |
| 4 | Canceled | Webhook cancelado pelo usuário. |
