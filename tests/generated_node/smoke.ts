/**
 * Smoke test for the generated Node/TypeScript client (generated/node), produced
 * by Orval (`npm run generate:client`) from the bundled spec.
 *
 * Not a full contract test — just enough to catch codegen/spec regressions that
 * break compilation or basic construction: missing exports, broken $refs, oneOf
 * enums that stop accepting both variants.
 *
 * Orval's plain-fetch output (no custom mutator) exports one function per
 * operation plus a `getXxxUrl()` helper returning the OpenAPI path template —
 * relative, with no host baked in. Most operations resolve against the spec's
 * default servers (prod/hml), but Chargeback and the v1 Autenticação operations
 * have a per-operation `servers:` override adding a `/chargeback` prefix that
 * Orval's generated code does not account for — callers must prepend the right
 * origin (and `/chargeback` where applicable) themselves; see openapi/paths/.
 *
 * Run via `mise run openapi:test` or directly with `npx tsx tests/generated_node/smoke.ts`
 * once `generated/node` has been (re)built with `npm run generate:client`.
 */
import {
  getPostV2MerchantAuthUrl,
  postV2MerchantAuth,
  getPostV2RefreshtokenUrl,
  postV2Refreshtoken,
  getGetV2ChargeChargeIdUrl,
  getPostV1MerchantAuthUrl,
} from "../../generated/node/main";
import type { Payer, Receiver, PatchV2SubscriptionSubscriptionIdBody } from "../../generated/node/main.schemas";

let failures = 0;

function check(description: string, fn: () => void): void {
  try {
    fn();
    console.log(`OK   ${description}`);
  } catch (err) {
    failures += 1;
    console.log(`FAIL ${description}: ${String(err)}`);
  }
}

check("operation functions are exported and callable-shaped", () => {
  if (typeof postV2MerchantAuth !== "function") throw new Error("postV2MerchantAuth missing");
  if (typeof postV2Refreshtoken !== "function") throw new Error("postV2Refreshtoken missing");
});

check("getXxxUrl() helpers return the documented relative path template", () => {
  if (getPostV2MerchantAuthUrl() !== "/v2/merchant/auth") {
    throw new Error(`unexpected URL: ${getPostV2MerchantAuthUrl()}`);
  }
  if (getPostV2RefreshtokenUrl() !== "/v2/refreshtoken") {
    throw new Error(`unexpected URL: ${getPostV2RefreshtokenUrl()}`);
  }
  if (getGetV2ChargeChargeIdUrl("abc-123") !== "/v2/charge/abc-123") {
    throw new Error(`unexpected URL: ${getGetV2ChargeChargeIdUrl("abc-123")}`);
  }
});

check("hml base URL composes correctly with a plain (no-servers-override) operation", () => {
  const url = `https://payment-hml.safrapay.com.br${getPostV2MerchantAuthUrl()}`;
  if (!url.startsWith("https://payment-hml.safrapay.com.br/v2/merchant/auth")) {
    throw new Error(`unexpected composed URL: ${url}`);
  }
});

check("Chargeback's /chargeback server-override prefix is NOT baked into the plain path (documented caveat)", () => {
  const url = getPostV1MerchantAuthUrl();
  if (url !== "/v1/merchant/auth") {
    throw new Error(`expected the raw path template, got ${url}`);
  }
  // Callers must manually prepend '/chargeback' for this operation — see openapi/paths/v1_merchant_auth.yaml's servers override.
});

check("Payer/Receiver schema types accept the documented shape (compile-time)", () => {
  const payer: Payer = {
    document: "71877920002",
    name: "Ester Patrícia",
    ispbCode: "60701190",
    bankCode: "341",
    branch: "0001",
    account: "12345-6",
  };
  const receiver: Receiver = {
    document: "31232517000130",
    ispbCode: "60701190",
    bankCode: "341",
    branch: "0001",
    account: "98765-4",
  };
  if (!payer.document || !receiver.document) throw new Error("unreachable");
});

check("PATCH /v2/subscription/{id} request body type exists (compile-time)", () => {
  const body: PatchV2SubscriptionSubscriptionIdBody = {
    amount: 1000,
    isActive: true,
    nextDayExecution: 10,
    planItems: [{ description: "Plano mensal" }],
  };
  if (!body.planItems?.length) throw new Error("unreachable");
});

console.log();
if (failures > 0) {
  console.log(`${failures} smoke check(s) FAILED`);
  process.exit(1);
}
console.log("ALL NODE SMOKE CHECKS PASSED");
