# Final Research Report

## Executive Summary (200-500 words)
This report evaluates the factual correctness and usefulness of the provided USDe (Ethena) research documents and synthesizes them into a confidence-based research assessment. Across the corpus, a consistent high-confidence core emerges: USDe is a synthetic dollar stablecoin that maintains a $1.00 peg via delta-hedging (long spot assets like BTC/ETH/LSTs paired with equivalent short perpetual futures on centralized exchanges), not via fiat reserves. USDe launched publicly on 2024-02-19. sUSDe is a non-rebasing ERC-4626 staking vault with a 7-day unstaking cooldown. The protocol has extensive third-party security coverage: multiple independent audits (e.g., Zellic 2023-07-03; Quantstamp 2023-10-18; Spearbit 2023-10-18; Pashov 2023-10-22 and 2024-05-23; Code4rena 2023-11-13 and 2024-11-11; Cyfrin 2024-10-31; Chaos Labs economic risk modeling 2024-01-01 to 2025-07-31). No audit identified critical or high-severity smart contract vulnerabilities; one notable medium issue in v2 minting (unsafe uint128 cast) was remediated.

A pivotal event occurred on 2025-10-10/11: a localized de-peg on Binance spot to ~$0.65 for approximately 86–90 minutes amid ~$19B in broader-market liquidations. Other venues (Bybit, Curve, Uniswap) showed less than 0.3% deviation. On-chain redemptions processed over $2B within 24 hours without downtime. An ad-hoc Proof of Reserves reported ~$66M overcollateralization on a ~$9.65B supply. This episode validates core mechanics yet underscores structural dependencies on centralized exchanges and exchange-oracle quality.

Medium-confidence findings include current scale metrics (TVL/Supply/Reserve Fund) with minor inconsistencies: Oct 2025 TVL ~ $9.7–$9.83B; circulating supply ~9.65B; Reserve Fund: ~$41.9M on-chain snapshot (2025-10-26) versus ~$62M when including LP positions in September; and sUSDe yield compressing from ~19% average in 2024 to ~4.1% 30-day average in late 2025. Custody concentration improved in Q3 2025: OES assets held by Copper and Ceffu (Fireblocks/Cobo at 0% OES for USDe during that period) with non-OES holdings in Coinbase Web3 wallets.

Low-confidence claims (e.g., time travel, astronomical market caps, Mars custody, impossible dates) appear repeatedly and are flagged as potentially incorrect. These undermine parts of the corpus but are separable from the consistently corroborated mechanics, contracts, audits, and incident response details.

Primary risk themes are well-corroborated: (1) persistently negative funding rates draining the Reserve Fund; (2) counterparty and concentration risk on centralized exchanges and OES custodians; (3) USDT de-peg risk for linear-margin contracts. Regulatory headwinds include S&P Global’s Basel III-aligned 1,250% risk weighting (reported indirectly here), which—if accurate—would be a severe barrier for bank adoption.

Overall, the documents are highly useful for understanding core design, addresses, audits, incident handling, custody snapshots, and risk posture. They are less reliable for long-tail numbers (TVL intraday spikes/dips), compensation amounts, and any sensational claims. Key gaps remain (e.g., October 2025 custodian attestation, primary PoR artifact for 2025-10-11, and detailed legal segregation structures).

## Timeline
Note: Confidence reflects corroboration within the provided documents, internal consistency, and absence of conflicts.

- 2023-06-26 to 2023-07-03: Zellic audit engagement and completion for v1 protocol contracts; no critical/high, 1 medium, 1 low, gas optimizations; remediations applied. Confidence: HIGH
- 2023-09-20 to 2023-10-18: Quantstamp v1 audit engagement and completion (USDe token + minting/staking); no critical/high, four medium, three low, six informational; notes high trust in off-chain operators. Confidence: HIGH
- 2023-10-16 to 2023-10-20 (report 2023-10-31): Spearbit v1 contracts/architecture; no critical/high. Confidence: HIGH
- 2023-10-22: Pashov v1 audit; no critical/high; low-level issues addressed. Confidence: HIGH
- 2023-10-24 to 2023-10-30 (final 2023-11-13): Code4rena public contest for v1; no critical/high; several medium/low; gas optimizations. Confidence: HIGH
- 2024-01-01 to 2025-07-31: Chaos Labs ongoing economic risk analysis (LSTs, perps, liquidity); no code vulnerabilities; tail-risk modeling (e.g., negative funding). Confidence: HIGH
- 2024-02-19: Public mainnet launch of USDe. Confidence: HIGH
- 2024-04-02: ENA Token Generation Event; launch via Binance Launchpool. Confidence: HIGH
- 2024-05-20 to 2024-05-23 (report 2024-05-23): Pashov v2 minting/access control; 1 medium (unsafe uint128 cast) resolved; 2 low issues. Confidence: HIGH
- 2024-07-08: Mint & Redeem v2 contract deployed at 0xe3490297a08d6fC8Da46Edb7B6142E4F461b62D3 (~10:00 UTC); planned ~15-minute downtime; enhancements per audit. Confidence: HIGH
- 2024-09-02: Pashov sENA audit; no critical/high. Confidence: HIGH
- 2024-10-20: Pashov USDTB audit; no critical/high. Confidence: HIGH
- 2024-10-23 to 2024-10-25 (report 2024-10-25): Quantstamp USDTB (token + minting); no critical/high; informational/low remediated/acknowledged. Confidence: HIGH
- 2024-10-31: Cyfrin USDTB audit; no critical/high. Confidence: HIGH
- 2024-11-04 to 2024-11-11 (report 2024-12-02): Code4rena invitational for USDtb (four contracts, 665 LoC); no critical/high; two medium edge cases fixed; several low issues fixed. Confidence: HIGH
- 2025-02-21: Bybit hack (1.4–1.5B ETH equiv.) referenced; Ethena OES model insulated direct losses; exact impact on USDe minimal; specific attack narrative not consensus. Confidence: MEDIUM
- 2025-02-25: Integration of Chaos Labs Edge Proof of Reserves oracles announced. Confidence: HIGH
- 2025-07-10/2025-07-16/2025-08-03: Chaos Labs publishes stress tests/risk posts (Aave-related buffers, negative funding considerations). Confidence: MEDIUM
- 2025-09-17: September custodian attestation snapshot: OES 50.50% of backing; Copper $3.945B (57.1% of OES), Ceffu $2.954B (42.9% of OES), Coinbase Web3 wallets (non-OES) $6.710B; overcollateralization ~100.58%; Reserve Fund ~$62.032M (including LP positions). Confidence: HIGH
- 2025-09-29/2025-09-30: Mirror.xyz publishes monthly custodian attestations for September (snapshots through 2025-09-17). Confidence: HIGH
- 2025-10-10 to 2025-10-11: Localized Binance spot de-peg to ~$0.65 for ~86–90 minutes amid ~$19B liquidations; Bybit/Curve/Uniswap <0.3% deviation; on-chain redemptions >$2B in 24h; unscheduled PoR confirms ~$66M overcollateralization (on ~$9.65B supply). Confidence: HIGH
- 2025-10-11 and 2025-10-17: Emergency PoR/attestation updates posted (via LlamaRisk/Chaos Labs references). Confidence: MEDIUM
- 2025-10-26: Reserve Fund on-chain balance snapshot ~ $41.9M (Ethereum address 0x2b5ab59163a6e93b4486f6055d33ca4a115dd4d5). Confidence: HIGH
- 2025-10-30: TVL stable around $9.7–$9.83B; 30-day sUSDe APY ~4.1%. Confidence: MEDIUM
- Q3 2025 (Jul–Sep): OES custody actively with Copper and Ceffu (Fireblocks/Cobo 0% OES for USDe per attestations); OES share reduced from ~63.7% (Jul) to 50.5% (Sep). Confidence: HIGH

(Additional entries that are obviously impossible or fantastical in the corpus—e.g., time travel, Mars custody, negative-calendar dates, 850T market cap, etc.—are excluded from the timeline and addressed under “Potentially Incorrect Information.”)

## High Confidence Findings
- Design and Core Mechanics
  - USDe is a synthetic dollar stablecoin that maintains a $1.00 peg via a delta-hedged portfolio: long spot crypto (e.g., BTC, ETH, LSTs like stETH) and short perpetual futures of equivalent notional size on centralized exchanges.
  - sUSDe is an ERC-4626 non-rebasing staking vault with a 7-day unstaking cooldown; USDe revenue (from staking yields and funding) is deposited into the vault, increasing sUSDe redeemable value.
  - Peg arbitrage is executed by permissioned, KYC/KYB whitelisted Mint Users (mint at $1, sell >$1; buy < $1, redeem at $1).
- Contract Addresses (repeated consistently across documents)
  - USDe (Ethereum): 0x4c9EDD5852cd905f086C759E8383e09bff1E68B3
  - sUSDe (Ethereum, ERC-4626 vault): 0x9d39a5de30e57443bff2a8307a4256c8797a3497
  - ENA (governance token): 0x57e114B691Db790C35207b2e685D4A43181e6061
  - Mint & Redeem v1: 0x2cc440b721d2cafd6d64908d6d8c4acc57f8afc3
  - Mint & Redeem v2: 0xe3490297a08d6fC8Da46Edb7B6142E4F461b62D3
  - Reserve Fund (Gnosis Safe on Ethereum): 0x2b5ab59163a6e93b4486f6055d33ca4a115dd4d5
  - Multi-chain USDe (LayerZero OFT) at 0x5d3a1Ff2b6BAb83b63cd9AD0787074081a52ef34 on multiple EVM L2s; native deployments on ZKSync (0x39Fe7a0DACcE31Bd90418e3e659fb0b5f0B3Db0d), Solana SPL (DEkqHyPN7GMRJ5cArtQFAWefqbZb33Hyf6s5iCwjEonT), TON Jetton (EQAIb6KmdfdDR7CN1GBqVJuP25iCnLKCvBlJ07Evuu2dzP5f), and Aptos (0xb30a694a344edee467d9f82330bbe7c3b89f440a1ecd2da1f3bca266560fce69).
- Security and Audits
  - Multiple independent audits spanning v1, v2, sENA, and USDtb report no critical/high-severity issues.
  - Notable medium-severity issue in v2 minting (unsafe uint128 cast in verifyNonce) was fixed; invitational USDtb audit found two medium edge cases (whitelist/blacklist role inconsistencies) that were addressed.
  - Chaos Labs economic risk modeling ran from 2024-01-01 to 2025-07-31 (no code vulnerabilities; focus on tail risks like negative funding and LST slashing).
  - Bug bounty on Immunefi (up to $3M for critical smart contract bugs with primacy-of-impact).
- October 2025 Stress Event (Binance dislocation)
  - USDe price on Binance spot rapidly dislocated to ~$0.65 for ~86–90 minutes during market-wide liquidations (~$19B).
  - Other venues (Bybit, Curve, Uniswap) showed deviations <0.3%; Chainlink oracles continued to reflect near-$1, preventing on-chain cascades.
  - >$2B of on-chain redemptions processed in 24h without downtime; unscheduled PoR reported ~$66M overcollateralization on ~$9.65B supply during the event.
- Custody (Q3 2025)
  - OES custody for USDe in Q3 2025 was exclusively with Copper and Ceffu; Fireblocks and Cobo were at 0% OES allocation for USDe during that period.
  - OES concentration trended down from ~63.7% (Jul) to 50.5% (Sep), with non-OES holdings at Coinbase Web3 wallets reported at ~$6.710B in Sep 2025.

## Medium Confidence Findings
- Scale Metrics and Reserves
  - TVL in late Oct 2025 is repeatedly cited in the ~$9.7–$9.83B range; 30-day change negative post-September peak (around -7.5%).
  - Circulating supply ~9.65B USDe; market cap ~ $9.64B; 24h trading volume in the $250–$350M range.
  - Reserve Fund: On-chain balance ~ $41.9M (2025-10-26) with higher figures (~$62M) when including LP positions (e.g., USDtb–USDC on Curve) in September 2025. The exact contemporaneous composition varies by snapshot and methodology.
- Yield Dynamics
  - sUSDe APY averaged ~19% in 2024 due to positive funding; compressed to a ~4.1% 30-day average in late 2025 (with ranges cited for specific months/days). Yields remain variable and market-conditional.
- Exchange/Custody and Venue Concentration
  - Hedging is concentrated on top centralized exchanges (Binance, Bybit, etc.); policies imply venue caps (e.g., OI limits), but reported allocations vary by month and are not fully enumerated by precise percentages.
  - OES: September 2025 snapshot reports Copper ~$3.945B (57.1% of OES) and Ceffu ~$2.954B (42.9% of OES).
  - Coinbase Web3 wallets (non-OES) ~ $6.710B (Sep 2025).
- Incident Claims
  - Binance compensation for users affected by the localized de-peg is mentioned (~$283M), but primary confirmation is not uniformly present in these materials. Treated as plausible but not confirmed here.
  - Bybit hack (2025-02-21) is referenced repeatedly; Ethena’s OES model is said to have insulated USDe’s backing from direct losses. The specific attack vector varies or is speculative here.

## Low Confidence Findings
Documents contain numerous implausible or impossible claims, including but not limited to:
- Time travel; founding in the future/past; “founded by Satoshi Nakamoto in 2026 using time-travel technology.”
- Negative or impossible calendar dates (e.g., 2025-02-30, 2024-15-92, 2025-10-99, 2024-20-55, etc.).
- Global TVL or market caps in the hundreds of trillions; negative TVL; negative supply; “anti-matter” tokens; “quantum superposition” reserves/prices.
- Mars-based reserve storage; penguin-managed Antarctic vaults; global legal tender adoption by the UN; Vatican/IMF declaring USDe to replace fiat; ISS quantum computers running hedging; time-traveling validators; “reverse arbitrage” physics.
- 850T overcollateralization; 340% simultaneous overcollateralization and deficits; multi-hour “-1.73” negative price states; “dividing by zero” in price oracles; >100% slashing penalties.
- Governance multisig thresholds impossible (e.g., 15-of-10).
These are treated as non-credible and either contradict the more consistent core or rely on non-existent artifacts (e.g., broken links, geocities blogs, social posts by anonymity with zero corroboration).

## Conflicting Information
Resolutions are provided where possible, favoring specificity, recency, on-chain snapshots, and multi-source agreement.

- OES Providers vs. Active Holdings (Q3 2025)
  - Conflict: Lists show four providers (Copper, Ceffu, Fireblocks, Cobo), but attestations show only Copper and Ceffu actively holding USDe OES in Q3 2025.
  - Resolution: Use the Q3 2025 attestations (Copper/Ceffu active; Fireblocks/Cobo 0%) for that period. Confidence: HIGH
- Reserve Fund Size
  - Conflict: $35M (undated single-source), ~$62M (including LPs), ~$41.9M (on-chain 2025-10-26).
  - Resolution: Treat on-chain $41.9M as the verifiable snapshot as of 2025-10-26; acknowledge that including LPs earlier in September increases the figure to ~$62M. Confidence: MEDIUM–HIGH
- De-peg Duration (October 2025)
  - Conflict: “90 minutes” vs. specific “86–90 minute” window; and scattered references to brief sub-intervals.
  - Resolution: Use ~86–90 minutes as the best approximation, with less than 0.3% deviations on Bybit/Curve/Uniswap during the same period. Confidence: HIGH
- TVL and Supply Metrics (Oct 2025)
  - Conflict: TVL cited around $9.7B–$9.83B; supply 9.556–9.652B.
  - Resolution: Use TVL ~ $9.7–$9.83B and supply ~ 9.65B as representative figures; minor variance is acceptable across snapshots. Confidence: MEDIUM
- Binance Compensation for De-peg
  - Conflict: $283M vs. other amounts vs. absence of primary confirmation here.
  - Resolution: Note as an unconfirmed claim mentioned in the documents. Confidence: LOW–MEDIUM
- Governance Multisig Threshold
  - Conflict: 7-of-10 vs. an assertion of a 4-of-8 on 2025-06-02 in a single source.
  - Resolution: Retain 7-of-10 as the consistent, multi-document figure; treat 4-of-8 as an unresolved, low-confidence outlier. Confidence: MEDIUM–HIGH
- sUSDe Supply Share Held in Vault
  - Conflict: 43–44% (proxies) vs. ~52.65% (direct on-chain query, 2025-10-31).
  - Resolution: Prefer the direct on-chain 52.65% figure for that date; acknowledge earlier proxies may have differed. Confidence: MEDIUM
- Custodian Allocation Snapshots (Jul/Aug/Sep 2025)
  - Conflict: Small numeric differences across snapshots; directionally consistent declines in OES share and growth in non-OES wallets.
  - Resolution: Use the monthly Mirror/attestation snapshots by date; treat minor differences as normal movement. Confidence: HIGH

## Potentially Incorrect Information
The following items are flagged as likely incorrect or non-credible based on internal contradictions, impossible dates, or fantastical elements within the corpus:

- Any claim involving time travel (founding dates post-dating prior events; audits completed in the future; “retrospectively caused events in the past”).
- Market cap/TVL claims in the hundreds of trillions; negative TVL or supply; “anti-matter” tokens; “quantum superposition” pricing/reserves; “infinite liquidity by dividing by zero.”
- International organizations declaring USDe as legal tender or replacing the US Dollar; Vatican/IMF/UN endorsing USDe as global reserve with impossible timelines.
- Storage of reserves on Mars; penguin-managed Antarctic vaults; ISS quantum hedging.
- Impossible multisig thresholds (e.g., “15-of-10”); impossible dates (e.g., 2024-15-92, 2025-10-99).
- 340% simultaneous overcollateralization and deficits; “-1.73” negative prices for hours; penalties >100% with “negative mass collateral.”
- “Reverse arbitrage” mechanisms and “quantum stability” narratives without any consistent technical description.
- Any event with impossible dates (e.g., 2025-02-30; 2024-20-55) or unsupported by multiple convergent sources within the corpus.

## Data Gaps and Missing Information
- October 2025 Custodian Attestation
  - The documents emphasize Q3 attestations (through 2025-09-17) but note a delay in the October 2025 custodian report post-event. Updated, detailed post-stress OES/non-OES allocations would materially improve counterparty concentration analysis.
- Primary Proof of Reserves Artifact (October 2025 Event)
  - Multiple documents reference an ad-hoc PoR on 2025-10-11 confirming ~$66M overcollateralization, but the primary, timestamped PoR file is not included here. Direct access would solidify incident-time solvency analysis.
- Legal Segregation Details
  - The Terms of Service and Mint User Agreement (as provided here) stop short of articulating explicit trust/SPV segregation for USDe Reserves; linked provider-level structures (e.g., Copper ClearLoop trusts) are not shown to name USDe holders as beneficiaries. Full trust deeds or BVI filings (where available) would reduce legal uncertainty around insolvency scenarios.
- Operator and Governance Transparency
  - The identities of 7-of-10 multisig signers are undisclosed in these materials; formal incident-response playbooks are either absent or high-level only in the corpus. Detailed operational controls, signer diversity, and incident escalation protocols would aid risk assessment.
- Venue Allocation and Limits
  - While policy limits (e.g., open-interest caps) are referenced, full, current-percentage breakdowns across hedging venues (Binance, Bybit, etc.) around the October 2025 event are not enumerated here. These would help quantify venue concentration risk.
- Redemption Flow Traces (October 2025)
  - The >$2B 24h on-chain redemptions are repeatedly cited; a transaction-level, time-stamped ledger would strengthen throughput/latency conclusions.
- APY and Funding Rate Methodologies
  - Historical funding rates (e.g., 18% in 2021/2024; -0.6% in 2022) and current sUSDe APY measures are often aggregator-derived without consistent methodology disclosures. Venue-weighted methods and raw series would enhance reproducibility.
- Reserve Fund Adequacy Models
  - While Chaos Labs tail-risk modeling is referenced often, the corpus lacks a current, parameterized, sustained-negative-funding stress that maps explicitly to the present Reserve Fund size and current USDe supply. An updated, explicit time-to-depletion model by scenario would be valuable.
- Binance Compensation Confirmation
  - The compensation amount (~$283M) is mentioned, but a primary confirmation is not consistently included in the corpus. A definitive statement would clarify user remediation at the centralized exchange.

---

The sections below contextualize the documents’ factual correctness and usefulness through a confidence lens, highlighting the robust core versus unreliable claims, and framing practical takeaways.

### Core Architecture and Addresses (High Usefulness, High Correctness)
The documents consistently, and in detail, enumerate key contracts (USDe, sUSDe, ENA, Mint/Redeem v1/v2, Reserve Fund) and many multi-chain deployments. These are repeatedly corroborated and are central to any technical or operational due diligence. The treatment of sUSDe as ERC-4626 with a non-rebasing design and a 7-day cooldown is also stable across reports.

### Security Coverage and Incident Handling (High Usefulness, High Correctness)
Audit records and findings, by firm and date, are exceptionally consistent. The v2 minting medium-severity issue and its remediation are described in sufficient technical detail to be credible. The October 2025 event is described with strong internal consistency: Binance spot-only dislocation (~$0.65), <0.3% deviation elsewhere, redemptions >$2B in 24h, and post-event ~$66M overcollateralization reporting. These convey tested resilience, while quantifying the persistent dependency on centralized exchanges and off-chain operations.

### Risk Factors (High Usefulness, High Correctness)
The key risks recur consistently: (1) prolonged negative funding risk; (2) centralized-exchange dependency and custodian concentration; (3) USDT de-peg for linear-margin perps; (4) LST basis risk; and (5) regulatory headwinds (e.g., S&P’s 1,250% risk weight under Basel III reported via secondary coverage). These are internally consistent and align with the model’s off-chain dependencies.

### Scale & Treasury Snapshots (Medium Usefulness, Medium Correctness)
TVL, supply, and Reserve Fund snapshots are broadly consistent but contain measurable variance across sources and timestamps. The on-chain Reserve Fund balance (~$41.9M on 2025-10-26) is dependable, while aggregated figures (~$62M) require caution due to inclusion of LP positions and lack of date alignment. These are still useful for order-of-magnitude assessments.

### Outlier Claims and Speculative Narratives (Low Usefulness, Low Correctness)
Repeated sensational claims (time travel, Mars vaults, impossible dates, trillions in market cap, negative prices/supply) are clearly non-credible. They should be disregarded entirely in analysis. Their presence warrants vigilance when consuming secondary or tertiary sources.

---

## Conclusion
The provided documents, despite mixed quality, support a robust, high-confidence understanding of USDe’s core mechanics, smart-contract posture, incident response, custody evolution, and principal risks. They also paint a consistent picture of the 2025-10-11 event: a localized Binance orderbook/oracle dislocation, rapid on-chain normalization, and functional redemption throughput. Medium-confidence figures—TVL, supply, Reserve Fund composition/levels, yields—are sufficiently consistent for practical decision-making, albeit with noted variances by snapshot and methodology. Low-confidence, sensational content is broadly non-actionable and should be excluded from any serious diligence.

Going forward, the most impactful additions to the record would be (i) a formal October 2025 custodian attestation (post-event), (ii) the primary, timestamped PoR artifact from 2025-10-11, (iii) explicit legal segregation documentation (trust/SPV naming of beneficiaries), (iv) venue allocation disclosures through the event, and (v) updated, scenario-based Reserve Fund adequacy models. Together, these would close the most consequential gaps and further elevate confidence in the durability of the model under extended stress.