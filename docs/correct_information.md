```markdown
# Correct Information for USDe Research Documents

## 1. asset_quality_analysis.md

### Correct Claims
- USDe is a synthetic dollar stablecoin that maintains stability via delta-hedging: long spot crypto assets paired with short perpetual futures, targeting a 1:1 backing ratio without fiat reserves.
- Mint-and-redeem arbitrage is available to permissioned, KYC/KYB-verified institutional Mint Users.
- Public mainnet launch occurred on 2024-02-19.
- Bitcoin was approved as collateral on 2024-04-02 to diversify beyond Ethereum-based assets.
- Solana was incorporated as an SPL Token at address DEkqHyPN7GMRJ5cArtQFAWefqbZb33Hyf6s5iCwjEonT.
- BNB was onboarded in August 2025 using LayerZero OFT at 0x5d3a1Ff2b6BAb83b63cd9AD0787074081a52ef34.
- Margin collateral includes USDC and USDT; USDT in linear contracts carries unhedged de-peg risk.
- Reserve Fund address: 0x2b5ab59163a6e93b4486f6055d33ca4a115dd4d5; balance about $41.9M as of 2025-10-26.
- Post-event overcollateralization reached ~$66M on a ~$9.65B supply on 2025-10-11.
- OES custody providers framework includes Copper, Ceffu, Fireblocks, and Cobo; Q3 2025 attestations show USDe OES assets held only by Copper and Ceffu.
- September 2025 OES snapshot: Copper $3.945B (57.1% of OES), Ceffu $2.954B (42.9% of OES); OES share of total backing 50.50%.
- Non‑OES holdings in Coinbase Web3 wallets totaled $6.710B in September 2025.
- Proof of Reserves moved to daily cadence on 2025-02-25 using Chaos Labs Edge oracles; Chainlink provides USD pricing feeds.
- Audits from 2023-07-03 to 2024-11-11 by multiple firms (e.g., Zellic, Quantstamp, Spearbit, Pashov, Code4rena, Cyfrin) reported no critical or high‑severity vulnerabilities; Pashov V2 (2024-05-23) found and fixed one medium (unsafe uint128 cast).
- 2025-10-10/11 event: USDe de-pegged to ~$0.65 on Binance for ~86–90 minutes amid ~$19B market liquidations; deviation <0.3% on Bybit, Curve, Uniswap; >$2B redemptions processed within 24 hours; Chainlink oracles near $1.00.
- Historical funding rates: ~18% average in 2021 and 2024; ~-0.6% average in 2022; an extreme of -370% annualized observed during Sep 2022 Ethereum Merge (consensus figure).
- sUSDe yields averaged ~19% in 2024; ~4.1% 30‑day average in late 2025.

## 2. audit_security_review.md

### Correct Claims
- Thirteen distinct security audits were performed across versions and components with no critical/high-severity vulnerabilities reported (Zellic, Quantstamp, Spearbit, Pashov, Code4rena, Cyfrin, etc.).
- Zellic audit (2023-07-03): v1 minting/staking; no critical/high; one medium and one low; issues patched.
- Quantstamp v1 (2023-10-18): no critical/high; four medium; three low; six informational; noted reliance on off-chain operators for hedging.
- Spearbit (2023-10-18): v1/architecture; no critical/high findings.
- Code4rena public contest (final 2023-11-13): no critical/high; several medium/low and gas suggestions; addressed.
- Pashov V2 (2024-05-23): one medium (unsafe uint128 cast in verifyNonce) fixed; two low; no critical/high.
- Pashov sENA (2024-09-02): no critical/high.
- Pashov USDTB (2024-10-20): no critical/high.
- Quantstamp USDTB (2024-10-25): no critical/high; primarily informational/low; recommendations addressed.
- Cyfrin USDTB (2024-10-31): no critical/high.
- Code4rena invitational USDtb (completed 2024-11-11): no critical/high; two medium edge cases; five low; addressed.
- Bug bounty on Immunefi active since 2024-04-04; up to $3M for critical smart contract issues (10% of funds at risk, $100k min); up to $50k for critical web/app issues.
- No active DeFi insurance coverage on Nexus Mutual or InsurAce as of 2025-10-30.
- Hypernative monitoring since May 2024; Hypernative Guardian added in September 2025.
- Chaos Labs Edge PoR oracles integrated 2025-02-25.
- October 11, 2025 incident: localized Binance de-peg to ~$0.65; deviations <0.3% elsewhere; Chainlink oracles near $1.00; >$2B redemptions processed; post-event PoR indicated ~$66M overcollateralization on ~$9.65B supply.
- Governance/ownership via 7-of-10 Gnosis Safe multisig; no dedicated on-chain timelock; off-chain Snapshot used for voting.
- No formal verification reported by Certora/Runtime Verification.

## 3. collateral_hedging_mechanisms.md

### Correct Claims
- USDe uses delta‑neutral hedging (long spot BTC/ETH/LSTs, short perpetuals) for a 1:1 backing model.
- As of 2025-10-30: circulating supply ~9.65B; market cap ~ $9.64B; 24h volume ~ $335M; TVL ~$9.829B (aggregator figures).
- 2025-10-11 event: Binance spot de-peg to ~$0.65 for ~86–90 minutes; <0.3% deviation on Bybit/Curve/Uniswap; >$2B redemptions within 24 hours; post-event PoR showed ~$66M surplus on ~$9.65B supply.
- sUSDe ERC‑4626 vault at 0x9d39a5de30e57443bff2a8307a4256c8797a3497 with 7‑day unstaking cooldown.
- Key Ethereum addresses: USDe 0x4c9EDD5852cd905f086C759E8383e09bff1E68B3; Mint/Redeem V2 0xE3490297A08d6fC8Da46Edb7B6142E4F461b62D3; ENA 0x57e114B691Db790C35207b2e685D4A43181e6061; Reserve Fund 0x2b5ab59163a6e93b4486f6055d33ca4a115dd4d5.
- Cross-chain deployments for USDe via LayerZero OFT at 0x5d3a1Ff2b6BAb83b63cd9AD0787074081a52ef34 across multiple EVM chains; ZKSync native 0x39Fe7a0DACcE31Bd90418e3e659fb0b5f0B3Db0d; Solana SPL DEkqHyPN7GMRJ5cArtQFAWefqbZb33Hyf6s5iCwjEonT; TON Jetton EQAIb6KmdfdDR7CN1GBqVJuP25iCnLKCvBlJ07Evuu2dzP5f; Aptos native 0xb30a694a344edee467d9f82330bbe7c3b89f440a1ecd2da1f3bca266560fce69.
- Audit set (Zellic, Quantstamp, Spearbit, Pashov, Code4rena, Cyfrin) found no critical/high issues; Pashov V2 medium fixed.

## 4. contract_maturity_analysis.md

### Correct Claims
- Public mainnet launch: 2024-02-19.
- ENA Token Generation Event on 2024-04-02 (Binance Launchpool).
- sUSDe ERC‑4626 deployed 2023-11-14 at 0x9d39a5de30e57443bff2a8307a4256c8797a3497; 7‑day unstaking cooldown.
- Reserve Fund contract deployed 2024-01-11 at 0x2b5ab59163a6e93b4486f6055d33ca4a115dd4d5.
- ENA governance token at 0x57e114B691Db790C35207b2e685D4A43181e6061.
- Mint & Redeem V2 deployed 2024-07-08 at 0xE3490297A08d6fC8Da46Edb7B6142E4F461b62D3.
- USDe ERC‑20 on Ethereum: 0x4c9EDD5852cd905f086C759E8383e09bff1E68B3.
- Mint & Redeem V1: 0x2cc440b721d2cafd6d64908d6d8c4acc57f8afc3.
- Multi-chain deployments (LayerZero OFT 0x5d3a1Ff2b6BAb83b63cd9AD0787074081a52ef34 across EVM L2s; ZKSync, Solana, TON, Aptos addresses as listed).
- Governance uses delegated committee model with Snapshot voting; core contracts controlled by a 7‑of‑10 Gnosis Safe multisig.
- Pashov V2 audit (2024-05-23) identified and Ethena fixed a medium-severity nonce/uint cast issue before V2 deployment.

## 5. delta_neutral_hedging.md

### Correct Claims
- USDe is a delta‑neutral synthetic dollar; yield derives from LST staking (3–4% baseline) plus funding rates (high in 2024; 30‑day ~4.1% in late 2025).
- TVL/AUM approximately $9.829B as of 2025-10-30 (aggregators).
- 2025-10-11 stress event: deviations <0.3% on-chain; >$2B redemptions in 24 hours; PoR confirmed ~$66M over‑collateralization.
- Reserve Fund balance ~$41.89M on-chain as of 2025-10-26 (0x2b5ab59163a6e93b4486f6055d33ca4a115dd4d5).
- Fee switch proposal submitted 2024-11-06; approved in principle 2024-11-15; thresholds reported met by 2025-09-15.
- September 17, 2025 custodian snapshot: Copper $3.945B, Ceffu $2.954B, Coinbase Web3 Wallets $6.710B; backing at 100.58%.
- Post-redemptions supply about 9.65B (down from 13.659B pre-event).
- Audits (Zellic 2023-07-03, Quantstamp 2023-10-18 and 2024-10-25, Spearbit 2023-10-18, Pashov 2023-10-22/2024-05-23/2024-09-02/2024-10-20, Code4rena 2023-11-13 & 2024-11-11, Cyfrin 2024-10-31) with no critical/high issues.
- Bug bounty: Immunefi up to $3M for critical smart contract vulns.

## 6. incident_financial_depeg.md

### Correct Claims
- Incident timeframe: October 10–11, 2025; severe window 2025-10-10 21:36–22:16 UTC on Binance.
- USDe fell to ~$0.65 on Binance spot during a broader crypto liquidation cascade (~$19B).
- On other venues (Bybit, Curve, Uniswap), deviations remained small (<0.3%).
- Chainlink/Aave oracles maintained valuations near $1.00, preventing DeFi cascades.
- On-chain redemptions exceeded $2B within 24 hours without downtime.
- Post‑event PoR indicated ~$66M over‑collateralization on ~$9.65B supply.
- Binance announced a $283M compensation program (2025-10-12).

## 7. infrastructure_centralization_vulnerabilities.md

### Correct Claims
- Audit history includes: Zellic (2023-07-03), Quantstamp (2023-10-18, 2024-10-25), Spearbit (2023-10-18), Pashov (2023-10-22; 2024-05-23; 2024-09-02; 2024-10-20), Code4rena (2023-11-13; 2024-11-11), Cyfrin (2024-10-31); no critical/high issues reported.
- Immunefi bug bounty launched 2024-04-04; critical payout up to $3M (10% funds at risk; $100k min).
- Hypernative monitoring since May 2024; Guardian added September 2025.
- LayerZero OFT is used for EVM cross-chain USDe transfers (canonical OFT address 0x5d3a1Ff2b6BAb83b63cd9AD0787074081a52ef34).
- October 2025: Binance-localized de-peg to ~$0.65 for ~90 minutes; deviations <0.3% elsewhere; >$2B redemptions processed; unscheduled PoR confirming ~$66M over‑collateralization.
- Governance via delegated committees and a multisig (no dedicated on-chain timelock).

## 8. protocol_governance_assessment.md

### Correct Claims
- Governance uses a delegated committee model; ENA holders vote via off‑chain Snapshot; Risk Committee includes firms such as Llama Risk, Blockworks Advisory, and Kairos Research.
- Primary governance multisig (Ethereum): 0x3B0AAf6e6fCd4a7cEEf8c92C32DFeA9E64dC1862; threshold 7‑of‑10.
- Key Ethereum addresses: USDe 0x4c9EDD5852cd905f086C759E8383e09bff1E68B3; sUSDe 0x9d39a5de30e57443bff2a8307a4256c8797a3497; ENA 0x57e114B691Db790C35207b2e685D4A43181e6061; Mint/Redeem V2 0xE3490297A08d6fC8Da46Edb7B6142E4F461b62D3; Reserve Fund 0x2b5ab59163a6e93b4486f6055d33ca4a115dd4d5.
- No dedicated on-chain timelock; governance relies on Snapshot voting and multisig execution.

## 9. reserves_audit_transparency.md

### Correct Claims
- Multi-firm audit program (Zellic 2023-07-03; Quantstamp 2023-10-18 and 2024-10-25; Spearbit 2023-10-18; Pashov 2023-10-22 & 2024-05-23 & 2024-09-02 & 2024-10-20; Code4rena 2023-11-13 & 2024-11-11; Cyfrin 2024-10-31) consistently reported no critical/high‑severity vulnerabilities; identified issues were medium/low/informational and addressed.
- Pashov V2 (2024-05-23): identified an unsafe uint128 cast in verifyNonce (medium) and two low-severity issues; all remediated.
- Quantstamp USDTB (2024-10-25): no critical/high; input validation and documentation improvements suggested and addressed.
- Code4rena invitational (2024-11-11) for USDtb: no critical/high; two medium edge cases; low-risk items addressed.

## 10. stability_track_record.md

### Correct Claims
- USDe typically exhibits low on-chain volatility, with on-chain deviations generally under 0.3%.
- Major CEX-specific depeg: 2025-10-11 on Binance to ~$0.65 for ~90 minutes; on-chain stability maintained (<0.3% deviation).
- Recovery supported by >$2B redemptions within 24 hours and Chainlink oracle prices near $1.00.
- Post‑event PoR indicated approximately $66M over‑collateralization.

## 11. stablecoin_derivatives_analysis.md

### Correct Claims
- USDe maintains its peg via delta-hedging: long spot (BTC/ETH/LSTs) and short perpetual futures.
- sUSDe is a yield-bearing ERC‑4626 vault; yield sources are LST staking rewards and derivatives funding rates.
- Primary smart contract addresses (Ethereum): USDe 0x4c9EDD5852cd905f086C759E8383e09bff1E68B3; sUSDe 0x9d39a5de30e57443bff2a8307a4256c8797a3497; Reserve Fund 0x2b5ab59163a6e93b4486f6055d33ca4a115dd4d5; ENA 0x57e114B691Db790C35207b2e685D4A43181e6061; Mint/Redeem V2 0xE3490297A08d6fC8Da46Edb7B6142E4F461b62D3.
- Cross‑chain deployments: LayerZero OFT (0x5d3a1Ff2b6BAb83b63cd9AD0787074081a52ef34 across EVM chains); ZKSync 0x39Fe7a0DACcE31Bd90418e3e659fb0b5f0B3Db0d; Solana SPL DEkqHyPN7GMRJ5cArtQFAWefqbZb33Hyf6s5iCwjEonT; TON Jetton EQAIb6KmdfdDR7CN1GBqVJuP25iCnLKCvBlJ07Evuu2dzP5f; Aptos native 0xb30a694a344edee467d9f82330bbe7c3b89f440a1ecd2da1f3bca266560fce69.
- October 2025 incident: Binance localized depeg to ~$0.65; on-chain venues near $1.00; >$2B redemptions in 24 hours; post‑event PoR confirmed ~$66M surplus.
- Extensive audits by multiple firms (Zellic, Quantstamp, Spearbit, Pashov, Code4rena, Cyfrin); no critical/high issues reported.
- Key backers include Dragonfly and Maelstrom (Arthur Hayes); a $14M strategic round at a $300M valuation closed in February 2024.

## 12. stablecoin_risk_analysis.md

### Correct Claims
- USDe’s peg mechanism uses delta‑neutral hedging; each minted USDe is backed by a long spot asset and an offsetting short perpetual futures position.
- Collateral composition includes ETH, BTC, and LSTs (e.g., stETH), plus stablecoins (USDC/USDT) for margin.
- Primary yield sources for sUSDe are LST staking rewards (~3–4% APR baseline) and derivatives funding rates (historically positive in contango).
- Off‑Exchange Settlement (OES) custodians are used to keep collateral off exchange balance sheets, reducing exchange failure risk.
- 2025-10-11 event: Binance-localized de-peg to ~$0.65; small deviations elsewhere; Chainlink/Aave oracles near $1.00; >$2B redemptions; post‑event PoR indicated ~$66M over‑collateralization.
- As of 2025-10-30 there is no specific Nexus Mutual coverage for Ethena/USDe.
- Multiple audits (Zellic, Quantstamp, Spearbit, Pashov, Code4rena, Cyfrin) reported no critical/high vulnerabilities.

## 13. synthetic_delta_hedging.md

### Correct Claims
- USDe is a synthetic dollar maintained via delta‑hedging; sUSDe is an ERC‑4626 vault; ENA is the governance token.
- Official links: ethena.fi; docs.ethena.fi; github.com/ethena-labs.
- Data aggregators list USDe/ENA on CoinMarketCap, CoinGecko, DeFiLlama.
- LayerZero OFT used for EVM cross‑chain transfers; native deployments on Solana (SPL), TON (Jetton), ZKSync (native), and Aptos (native).
- Core Ethereum addresses: USDe 0x4c9EDD5852cd905f086C759E8383e09bff1E68B3; sUSDe 0x9d39a5de30e57443bff2a8307a4256c8797a3497; Reserve Fund 0x2b5ab59163a6e93b4486f6055d33ca4a115dd4d5; Mint/Redeem V2 0xE3490297A08d6fC8Da46Edb7B6142E4F461b62D3; ENA 0x57e114B691Db790C35207b2e685D4A43181e6061.
- Audit set (Zellic, Quantstamp, Spearbit, Pashov, Code4rena, Cyfrin) found no critical/high issues.
- Governance: delegated committee model; Snapshot voting; 7‑of‑10 Gnosis Safe controls upgrades.

## 14. total_value_locked.md

### Correct Claims
- Verified TVL: ~$9.71B as of 2025-10-30 (DeFiLlama), broadly consistent with a ~$9.8B baseline.
- All‑time high USDe-only TVL ~ $13.88B on 2025-09-17.
- 30‑day change ~ -7.52%; 90‑day change ~ +38.71% (as of 2025-10-30).
- Ethereum accounts for ~99.69% of TVL; TON contributes a small share.
- USDe supply ~9.65B; market cap ~ $9.64B; 24h volume ~ $335M (late Oct 2025 aggregator data).
- sUSDe vault address: 0x9d39a5de30e57443bff2a8307a4256c8797a3497 (ERC‑4626, 7‑day cooldown).
- Audit set from 2023–2024 (Zellic, Quantstamp, Spearbit, Pashov, Code4rena, Cyfrin) reported no critical/high issues.
- Immunefi bug bounty offers up to $3M for critical smart contract vulnerabilities.

## 15. user_rights_assessment.md

### Correct Claims
- Redemption rights are limited to whitelisted, KYC/KYB-verified Mint Users; Holding Users lack direct redemption rights.
- Updated Terms of Service dated 2025-08-13 govern current framework under BVI law.
- Legal title to reserves is held by Ethena (BVI) Limited; the Company states it does not provide custody or fiduciary services.
- Holding USDe does not grant beneficial ownership, economic rights, or voting rights in Ethena BVI or its assets; holders are not entitled to reserve yield/interest.
- sUSDe incorporates compliance features such as freezing and blacklisting to meet sanctions/AML/CFT requirements.
- BaFin actions in 2025 included a prohibition order (2025-03-21) and a court‑approved redemption wind‑down window (2025-06-25 to 2025-08-06) for the German entity’s issuance.
- Off‑exchange custody solutions are referenced in documentation (e.g., Copper, Ceffu, Fireblocks), though specific trust beneficiary linkages for holders are not detailed in the ToS.

```