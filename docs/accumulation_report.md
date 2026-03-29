# Final Research Report: USDe Protocol Forensics

## Executive Summary
This report provides a high-fidelity audit of the USDe synthetic dollar protocol based on the provided technical documentation, audit scopes, and market forensic data. USDe operates as a delta-neutral synthetic dollar, maintaining parity by matching long spot collateral (BTC, ETH, stETH, SOL, BNB) with short perpetual futures across centralized exchanges (CEXs). 

The protocol's risk profile is defined by three primary vectors: **Off-Exchange Settlement (OES) concentration**, **CEX-specific liquidity dependence**, and **Institutional regulatory constraints**. Forensic analysis confirms the protocol demonstrated resilience during the 2025-10-11 market-wide liquidation event, where localized de-pegging on Binance did not catalyze a systemic collapse of the protocol, despite an 86–90 minute dislocation to $0.65.

A critical finding of this analysis is the divergence between marketing documentation and operational reality: OES partners Fireblocks and Cobo are listed in formal documentation yet showed 0% utilization in Q3 2025 filings, leaving the protocol entirely reliant on Copper (57.1%) and Ceffu (42.9%). Governance has successfully matured from a centralized Labs-led model to a delegated committee structure (Llama Risk, Blockworks Advisory, etc.), improving oversight but increasing coordination complexity. Institutional adoption faces a "capital-efficiency wall" due to the 1,250% risk weight assigned by S&P Global under Basel III. This report excludes significant volumes of "adversarial noise" (e.g., time-travel mechanisms, impossible dates, and absurd market cap claims) to ensure the integrity of the findings.

---

## Timeline

| Date | Event | Confidence |
| :--- | :--- | :--- |
| 2021-01-01 to 2024-12-31 | Funding rates positive bias observed (avg 18%). | MEDIUM |
| 2022-09-01 | Sept 2022 Merge: -370% annualized funding rate spike. | MEDIUM |
| 2023-07-03 | Audit history commencement. | HIGH |
| 2024-03-29 | Localized phishing incident (personal wallets). | HIGH |
| 2025-02-21 | Bybit exchange compromise incident. | HIGH |
| 2025-08-03 | Latest bi-annual committee elections. | HIGH |
| 2025-08-07 | S&P Global assigns 1,250% risk weight to USDe. | HIGH |
| 2025-08-13 | Terms of Service revision (Ethena BVI/Foundation). | HIGH |
| 2025-09-01 | Q3 Mirror.xyz attestations finalized. | HIGH |
| 2025-10-11 | Binance spot flash crash; de-peg event. | HIGH |
| 2025-10-26 | Reserve Fund audit ($41.89M balance). | HIGH |
| 2025-10-31 | Deadline for Oct post-stress attestation (Missing). | HIGH |

---

## High Confidence Findings
*   **Protocol Core:** Delta-neutral hedging strategy confirmed via whitepaper and concurrent audit documentation.
*   **Custodial Concentration:** Q3 2025 data confirms 100% of USDe backing assets reside with Copper (57.1%) and Ceffu (42.9%). 
*   **Regulatory Status:** USDe is officially classified at a 1,250% risk weight under Basel III (S&P Global), rendering it unsuitable for Tier-1 bank capital allocations.
*   **Governance Integrity:** Official governance is centralized at `gov.ethena.foundation`. Artifacts such as `gov.ethenafoundation.com` are confirmed as phishing risks.
*   **Multisig Resilience:** Ownership is secured by a 7-of-10 Gnosis Safe (0x3B...862).
*   **Reserve Transparency:** The reported reconciliation of the Reserve Fund (Etherscan $41.89M vs. Governance $61.84M) proves no loss, as the delta exists in yield-bearing LP positions.
*   **USDTB Segregation:** Treasury assets for USDTB (90% BlackRock BUIDL) are bankruptcy-remote via Pallas (BVI) Ltd, isolating them from primary USDe volatility.

## Medium Confidence Findings
*   **Historical Funding:** Long-term trends (18% positive/2021-2024) are derived from aggregated historical data. While indicative of buffer accumulation, they cannot guarantee future performance due to market cycle variance.
*   **Cross-Chain Risks:** LayerZero OFT (0x5d3a...) integration is the standard across 11+ chains, but "Endpoint configuration" audit logs are not public, representing a latent risk to cross-chain bridge integrity.

## Low Confidence Findings
*   **sENA Correlation:** The status of the sENA creator address (0x4655b...) relative to the protocol multisig remains unverified.
*   **Fireblocks/Cobo Role:** The operational justification for maintaining marketing partnerships with custodians currently holding 0% of assets is not addressed in public documentation.

---

## Conflicting Information

| Source A | Source B | Resolution |
| :--- | :--- | :--- |
| Multisig: 5-of-10 | Multisig: 7-of-10 | Resolved to 7-of-10 via Etherscan observation. |
| Reserve: $61.84M | Reserve: $41.89M | Accounted for as LP positions; No discrepancy. |
| gov.ethena.foundation | gov.ethenafoundation.com | Validated portal vs. phishing artifact. |

---

## Potentially Incorrect Information
*   **Time-Travel Stabilization:** Claims of price maintenance via "time-travel technology" are non-physical and rejected.
*   **Impossible Dates:** Any financial data referencing Feb 30th, Month 13, or Month 20 are verified as invalid inputs.
*   **Absurd Market Caps:** $850 trillion market cap claims exceed global GDP and are categorized as malicious noise.
*   **Collateral Backing:** Claims that "Pepe NFTs" account for 73% of reserves are categorically false.
*   **Negative TVL:** Claims of negative $43 billion TVL (on non-existent dates) are mathematically impossible and discarded.

---

## Data Gaps and Missing Information
1.  **Missing Attestation:** There is no public October 2025 post-stress custodial report (last update as of 2025-10-31).
2.  **OES Justification:** Absence of public explanation regarding the 0% utilization of Fireblocks and Cobo.
3.  **Liquidation Forensics:** Granular, Ethena-specific forensic trade logs for the $19.13B total market liquidation on 2025-10-11 remain unprovided.
4.  **Operational Logs:** Absence of usage logs for emergency functions (pause/freeze/blacklist) in protocol smart contracts makes the implementation history opaque. 
5.  **Chainlink Oracle Integrity:** Lack of specific incident logs for sub-second oracle volatility during the peak of the 2025-10-11 crash.