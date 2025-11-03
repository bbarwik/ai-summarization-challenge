# USDe: incident financial depeg

# incident_report

## A. Basic Facts

**Incident Date/Time**: 2025-10-10 21:36 UTC. The severe window extended from 2025-10-10 21:36 UTC to 22:16 UTC, as detailed in the Binance announcement dated 2025-10-10 to 2025-10-12. The overall de-pegging occurred on October 10-11, 2025, with any local date confusion resolved to October 10 in Coordinated Universal Time (UTC).

**Incident Type**: Financial.

**Specific Sub-Type**: Depeg event. This was a localized liquidity flash crash, not a protocol failure but an exchange-specific oracle issue.

**Brief Description**: USDe temporarily de-pegged to $0.65, which is 35% below the peg, on the Binance spot USDe/USDT pair due to thin order book and internal oracle reliance amid a $19.13-19.37 billion crypto liquidation cascade triggered by U.S. President Donald Trump's announcement of an additional 100% tariff on all imports from China, effective November 1, 2025. Bitcoin dropped to $104,782 with a 12-14% decline, and Ethereum fell to $3,437 with a 12-20% decline. The immediate impact included a 40-minute severe window with a $60-90 million USDe dump, $500 million-$1 billion in USDe-specific liquidations, 780 million USDe tokens traded, and approximately 1.6 million traders affected in the broader market cascade, as reported in exchange post-mortems and media coverage dated 2025-10-11. Over $2 billion in redemptions were processed in 24 hours without protocol downtime. The peg remained stable on other venues with less than 0.3% deviation on Bybit, Curve, and Uniswap, while Chainlink and Aave oracles maintained a $1.00 valuation. ENA dropped approximately 40-43% to a low of $0.32-$0.40 (with one disputed report of $0.1858 all-time low). The current status is fully repegged by 2025-10-13, with USDe supply growing to $12-13 billion by late October 2025, exceeding the pre-incident $9.65 billion. Binance distributed $283 million in compensation, and post-incident whale accumulation in ENA increased 600% month-over-month. Post-incident, Ethereal DEX, the Ethena-incubated decentralized exchange, launched its mainnet alpha from 2025-10-20 to 2025-10-21 with $280 million in total value locked from pre-deposits and USDe-native perpetuals trading, driving a 4% rise in ENA and demonstrating ecosystem resilience.

---

## B. Impact Metrics

### Financial Impact:
- **Amount Lost/Affected**: No direct protocol losses occurred; Binance provided $283 million in compensation to affected users for trades during the 21:36-22:16 UTC window on 2025-10-10, as announced on 2025-10-12. Estimated USDe-specific liquidations on Binance ranged from $500 million to $1 billion. Initial USDe outflows reached $1.25 billion during the panic, later stabilizing after the Proof of Reserves (PoR) release. sUSDe loop trades (recursive yield farming positions involving staked USDe) had approximately $1 billion in exposure at risk due to negative carry conditions post-crash, though no realized losses were reported as of 2025-10-29 (medium-low reliability per analytical reports dated 2025-10-27). ENA experienced a 40-43% drop from $0.68 pre-event to $0.32-$0.40 low (with one disputed report of $0.1858 all-time low), implying approximately $1-2 billion in market cap loss at a 15 billion token cap, depending on circulating supply at the time.
- **Total TVL at Time of Incident**: Approximately $9.65 billion USDe supply and Total Value Locked (TVL) at incident onset.
- **Percentage of TVL Affected**: Approximately 5-10% of TVL was impacted through $500 million-$1 billion in liquidations and $1.25 billion in outflows relative to $9.65 billion. ENA market cap dropped about 40%, though this was not direct TVL impact; sUSDe exposure represented about 10% of TVL at risk.
- **TVL Before/After Incident**: Before the incident, TVL stood at $9.65-9.829 billion. After the incident in late October 2025, USDe supply and TVL reached $12-13 billion post-recovery.
- **TVL Change**: Initial -13% dip via $1.25 billion outflows on 2025-10-11, followed by +24-35% growth ($2.35-3.35 billion increase) by late October 2025, indicating recovery and inflows.

### User Impact:
- **Number of Users Affected**: Approximately 1.6-1.66 million traders were impacted in the broader crypto market liquidation cascade including USDe positions, with Binance-specific affected users eligible for the $283 million compensation.
- **User Value at Risk**: $283 million in direct compensation represented value at risk for affected Binance users. Up to $1.25 billion in outflows signified user positions at risk during the panic.

### Duration Impact:
- **Incident Start Time**: 2025-10-10 21:36 UTC on Binance.
- **Service Disruption Duration**: The severe de-peg window lasted 40 minutes (21:36-22:16 UTC on 2025-10-10), during which prices fell below $0.90 for 23 minutes and below $0.95 for 53 minutes, with total deviation greater than 2% spanning approximately 90 minutes.
- **Core Functions Affected**: No core Ethena functions were affected; minting and redeeming remained operational, processing over $2 billion in redemptions in 24 hours without downtime. Binance spot trading was disrupted by oracle and thin order book issues, while on-chain stability was maintained via external oracles.

### Price/Peg Impact:
- **Target/Peg Price**: $1.00 USD.
- **Worst Deviation Observed**: $0.65 low on Binance spot USDe/USDT, representing a 35% de-peg. Less than 0.3% deviation occurred on Bybit, Curve, and Uniswap.
- **Duration at Worst Deviation**: A few minutes at the $0.65 low during 21:20-21:21 UTC on 2025-10-10; the overall severe window lasted 40 minutes.
- **Current Status**: Fully repegged across all venues by 2025-10-13, remaining stable near $1.00 as of late October 2025.

---

## C. Verification

### Official Source:
- **Link**: x.com/ethena_labs/status/1976988523598385528 for confirmation of systems normal and off-cycle Proof of Reserves; binance.com/en/support/announcement/detail/0989d6c7f32545bfb019e3249eaabc3f for the de-peg window from 21:36 to 22:16 UTC and $283 million compensation; chaoslabs.xyz/posts/proof-of-reserve-as-risk-infrastructure for Proof of Reserves validation.
- **Quote/Summary**: As quoted in the Ethena X thread dated 2025-10-10 22:13 UTC, "Due to turbulent market conditions... USDe experienced volatility. We can confirm the mint & redeem functionality has remained operational... USDe remains overcollateralised." The 2025-10-11 X post states, "Systems normal; off-cycle Proof of Reserves confirms ~$66 million overcollateralization." The Chaos Labs analysis dated 2025-10-16 notes, "Incident as risk infrastructure validation; PoR verified intact." This aligns with third-party reports by confirming the localized nature.
- **Date Published**: 2025-10-10 22:13 UTC for the initial X post; 2025-10-11 12:29 UTC for the Proof of Reserves release; 2025-10-10 to 2025-10-12 for the Binance announcement; 2025-10-16 for the Chaos Labs analysis.
- **Source Type**: Social media (X/Twitter) for Ethena; exchange announcement for Binance; research and analysis for Chaos Labs.

### Third-Party Source:
- **Link**: coindesk.com/markets/2025/10/11/ethena-s-usde-briefly-loses-peg-during-usd19b-crypto-liquidation-cascade for localized de-peg details; bloomberg.com/news/articles/2025-10-11/third-largest-stablecoin-briefly-loses-dollar-peg-in-crypto-rout for the $0.65 low; coinmetrics.substack.com/p/state-of-the-network-issue-335 for resilience validation.
- **Publication**: CoinDesk; Bloomberg; Coin Metrics.
- **Quote/Summary**: As reported by CoinDesk on 2025-10-11, "Ethena's USDe briefly loses peg during $19B crypto liquidation cascade; localized to Binance, protocol normal." Bloomberg on 2025-10-11 stated, "Third-largest stablecoin briefly loses dollar peg in crypto rout, hitting ~$0.65 on Binance." Coin Metrics on 2025-10-27 noted, "Validates Ethena resilience, highlights exchange risks."
- **Date Published**: 2025-10-11 for CoinDesk and Bloomberg; 2025-10-27 for Coin Metrics.

### Verifiable Evidence:
- **Type**: On-chain transaction data; exchange charts and logs; oracle feeds; custodian attestations.
- **Link/Reference**: etherscan.io/address/0xe3490297a08d6fC8Da46Edb7B6142E4F461b62D3 for the mint and redeem contract; governance.aave.com/t/arfc-ethena-usde-risk-oracle-and-automated-freeze-guardian/23303 for oracle stability; Binance spot charts for the $0.65 low during the window; docs.ethena.fi/resources/custodian-attestations for off-exchange custody.
- **What it shows**: Over $2 billion in redemptions processed from 2025-10-10 to 2025-10-11 without delays via the v2 contract, with block explorer data confirming no downtime. The Aave oracle maintained a $1.00 USDe valuation during the event. Binance charts verify the drop to $0.65 at 21:20-21:21 UTC and recovery by 22:45 UTC. Off-exchange settlement (OES) custody with providers like Copper and Anchorage Digital mitigated liquidation exposure by holding collateral separately from exchange balance sheets, explaining the absence of direct protocol losses. Confirming less than 0.3% deviation on Bybit, Curve, and Uniswap (noting one disputed report of ~$0.92 dip on Bybit, pending verification).

### Verification Level:
- **CONFIRMED** (All 3 sources present). Medium confidence applies to unresolved conflicts such as the Bybit dip (approximately $0.92 versus less than 0.3%) and coordinated attack evidence due to lack of Nansen proof.

---

## D. Timeline Reconstruction

**T-0 (Incident Occurred)**: 2025-10-10 21:36 UTC: De-pegging started on Binance, and the severe window opened.
1. Preceding events: 2025-10-10 13:30 UTC: Trump tariff announcement.
2. 2025-10-10 21:03 UTC: Reuters wire on the announcement.
3. 2025-10-10 21:20 UTC: Initial lows with market maker liquidation.

**T+[X] (Protocol Response)**: T+37 minutes (2025-10-10 22:13 UTC): Ethena issued the initial X acknowledgment of volatility, confirming mint and redeem operations remained operational and USDe was overcollateralized.
1. T+1 day +12 hours (2025-10-11 09:18 UTC): Guy Young published a detailed oracle thread with a cross-venue chart.
2. T+1 day +15 hours (2025-10-11 12:29 UTC): The unscheduled Proof of Reserves release confirmed $66 million excess.

**T+[X] (Resolution Efforts Began)**: T+ immediate (2025-10-10 22:16 UTC): The severe window ended, and prices began recovering via arbitrage.
1. T+1 day +19 hours (2025-10-11 16:23 UTC): Binance announced the compensation plan and risk enhancements.
2. T+2 days (2025-10-12 09:18 UTC): Guy Young posted an X clarification on oracle design with a chart.
3. T+3 days (2025-10-12): The founder clarified the oracle issue, and $283 million compensation was announced.
4. T+10 days (2025-10-20 to 2025-10-21): The Ethereal DEX launched with $280 million in TVL. The timeline highlights rapid response within hours, leading to full resolution in days.

**T+[X] (Resolution Complete OR Current Status)**: T+3 days (2025-10-13): The peg was fully restored across venues, and $1.25 billion in outflows stabilized.
1. T+4 days (2025-10-14): Binance completed the external oracle transition.
2. T+6 days (2025-10-16): Chaos Labs published the Proof of Reserves analysis.
3. Current as of late October 2025 (current date: 2025-10-30): USDe supply reached $12-13 billion, ENA recovered to $0.46 (230% from low), and no recurrence has occurred.

**Summary Timeline**:
- **Days Since Incident**: 20 days as of late October 2025 (current date: 2025-10-30).
- **Days Since Resolution**: 17 days since the full repeg on 2025-10-13; resolution is complete, with ongoing monitoring via Chaos Labs.

---

## E. Resolution Quality Assessment

### Response Speed:
- **Classification**: Hours.
- **Assessment**: Good monitoring is indicated by the initial acknowledgment within 37 minutes of the severe window start. The Proof of Reserves release in less than 24 hours addressed community concerns in a timely manner, outperforming typical DeFi response delays (often 24-48 hours for disclosures in decentralized finance incident responses).

### Communication Quality:
- **Classification**: Transparent.
- **Assessment**: This classification is chosen due to high transparency, evidenced by more than three communications in the first 24 hours (22:13 UTC initial post, 09:18 UTC thread, and 12:29 UTC Proof of Reserves). Detailed explanations of oracle mechanics and specifics on the $66 million excess built trust, consistent with the handling of prior events like the Bybit incident.

### Fix/Resolution:
- **Has Fix Been Implemented?**: Yes. Binance completed the oracle transition on 2025-10-14, and arbitrage restored the peg.
- **Root Cause Identified?**: Yes. The root cause was Binance's internal oracle reliance on a thin order book, which amplified volatility.
- **Fix Verification**: Partial. Chaos Labs audited the Proof of Reserves integrity; prior audits such as Zellic on 2023-07-03 and Quantstamp on 2023-10-18 confirmed no critical vulnerabilities, supporting overall resilience. Binance enhancements, including redemption weights and price thresholds, were self-reported without mention of a third-party audit.

### Confidence in Resolution:
- **Level**: High.
- **Reasoning**: This level is appropriate due to the localized exchange fix via oracle upgrade, proven protocol resilience with $2 billion in redemptions without downtime, absence of recurrence post-2025-10-14, multi-venue stability, and ongoing Chaos Labs modeling. It contrasts with algorithmic failures like UST. High overall confidence despite partial verification, as the protocol's on-chain resilience ($2B redemptions without issues) and exchange-specific fix outweigh un-audited Binance enhancements.

---

## F. Severity Assessment

- **Classification**: MODERATE.
- **Justification**: This severity level is assigned because of the significant 35% price deviation and $1.25 billion in outflows, but no protocol loss or downtime occurred, with containment to one venue for less than 90 minutes and full recovery with intact overcollateralization. Thresholds were exceeded for financial impact (e.g., >10% temporary TVL dip via outflows) but not for systemic issues (e.g., no on-chain downtime or losses exceeding 20% TVL), per standard DeFi incident frameworks. It is lower than critical, like the Bybit exploit, due to no direct exposure. Amplification from the pre-incident S&P 1,250% weighting on 2025-08 highlights regulatory barriers, but the contained recovery prevents a HIGH classification. This isolation reduces contagion risk but highlights centralized exchange (CEX) dependencies.

---

## G. Pattern Detection

### Historical Context Check:
- **Are there OTHER incidents in the last 60-90 days?** Yes. The BaFin prohibition occurred on 2025-03-21 (prohibiting new USDe business in Germany due to regulatory non-compliance) and redemption activated on 2025-06-25 (42-day window ending 2025-08-06, affecting ~$500 million in German-held USDe, <5% of global supply, now resolved). The SEC informational meeting was on 2025-07-01 with no enforcement. No other material adverse events occurred in October 1-30, 2025, across security, financial, operational, governance, or regulatory categories beyond this de-peg. In the 60-90 days prior, none were reported; the BaFin redemption ended on 2025-08-06, and the S&P weighting in August 2025 was non-adverse.
- **Is this a RECURRING issue?** No. This was an isolated liquidity flash crash with no prior de-peg patterns; it contrasts with the systemic failure of UST in 2022.
- **Last known incident before this one**: 2025-02 Bybit $1.4 billion exploit with no exposure; prior regulatory incident was the BaFin resolution on 2025-08-06. The Bybit exploit in 2025-02 involved $1.4 billion in losses but no Ethena exposure due to OES custody.

### Red Flag Patterns Detected:
- [ ] **Cascading Failures**. No cascading occurred in a 7-day period; the incident was isolated to Binance without on-chain spread. No cascading failures occurred despite $19B market liquidations, as the incident remained isolated to Binance without spreading to on-chain protocols.
- [ ] **Recurring Incidents**. No recurrence or pattern of de-pegs or stability issues.
- [ ] **Communication Blackout**. No blackout occurred; updates were transparent within hours.
- [ ] **Permanent Impairment**. No permanent damage; TVL grew post-event.
- [ ] **Regulatory Shutdown**. No new actions in October; the prior BaFin issue resolved in August 2025.
- [X] **None detected** - This appears to be an isolated incident. Isolation is confirmed by multi-source consensus; the response was consistent with prior non-impacting events like Bybit. No regulatory shutdown recurrence followed the BaFin resolution in August 2025.

---

## H. Information Gaps

- **What information is missing or uncertain?** Exact UTC timestamp for the $0.65 low within 21:20-21:21 UTC on the Binance chart. **Why does each gap matter for risk assessment?** It assesses the duration and severity of the peak deviation, impacting liquidity risk quantification. **Where might this information be found?** Binance API or TradingView 1-minute candles for October 10, 2025.
- **What information is missing or uncertain?** Raw on-chain redemption ledger breakdown for over $2 billion volume (time, user, token-to-USD) from 2025-10-10 to 2025-10-11. **Why does each gap matter for risk assessment?** It verifies user impact and protocol throughput under stress, key for operational resilience. **Where might this information be found?** Dune Analytics or Etherscan export for redemptions.
- **What information is missing or uncertain?** Direct Chaos Labs Proof of Reserves certificate full text for October 2025. **Why does each gap matter for risk assessment?** It confirms the exact overcollateralization methodology, critical for backing credibility. **Where might this information be found?** Chaos Labs site or PDF download for the Proof of Reserves.
- **What information is missing or uncertain?** Cross-venue 1-minute price series for Bybit, Curve, and Uniswap during 21:36-22:16 UTC to confirm less than 0.3%. **Why does each gap matter for risk assessment?** It validates multi-venue stability claims, affecting diversification risk. **Where might this information be found?** TradingView multi-venue comparison for October 10, 2025.
- **What information is missing or uncertain?** Primary Trump tariff Truth Social post ID and timing (13:30 versus 14:57 UTC). **Why does each gap matter for risk assessment?** It clarifies macro trigger causality, informing external shock sensitivity. **Where might this information be found?** Truth Social archive for the tariff post.
- **What information is missing or uncertain?** On-chain wallet data for the $60-90 million dump (coordinated versus opportunistic). **Why does each gap matter for risk assessment?** It distinguishes attack from market panic, elevating risk if coordinated. **Where might this information be found?** Nansen or Arkham for dump wallets.
- **What information is missing or uncertain?** CoinGecko historical ENA charts for October 2025 to confirm $0.32-$0.40 low versus disputed $0.1858. **Why does each gap matter for risk assessment?** It resolves token volatility impact, relevant for governance token risk. **Where might this information be found?** CoinGecko API or historical charts for October 2025 for ENA.
- **What information is missing or uncertain?** Binance internal liquidation logs for $500 million-$1 billion USDe-specific. **Why does each gap matter for risk assessment?** It quantifies direct USDe exposure in cascades, for counterparty risk. **Where might this information be found?** Binance API liquidation export for USDe.
- **What information is missing or uncertain?** Exact X post ID and content for the 2025-10-10 22:13 UTC acknowledgment. **Why does each gap matter for risk assessment?** It ensures communication authenticity and timeliness for response quality. **Where might this information be found?** X archive or search for Ethena posts on October 10, 2025.
- **What information is missing or uncertain?** Timestamped DeFiLlama data for $1.25 billion outflows. **Why does each gap matter for risk assessment?** It measures flight risk magnitude and post-stress retention. **Where might this information be found?** DeFiLlama timestamped TVL or outflows.
- **What information is missing or uncertain?** Nansen or Arkham write-up for ENA 600% whale accumulation. **Why does each gap matter for risk assessment?** It gauges investor sentiment recovery as a long-term adoption signal. **Where might this information be found?** Nansen on-chain reports for ENA whales.
- **What information is missing or uncertain?** BaFin filing excerpts for approximately $500 million affected volume in Germany. **Why does each gap matter for risk assessment?** It assesses jurisdictional exposure and resolution impact. **Where might this information be found?** BaFin full filings for volume.
- **What information is missing or uncertain?** SEC April 2025 "Covered Stablecoins" exact quote and filing link. **Why does each gap matter for risk assessment?** It clarifies non-security status and regulatory overhang. **Where might this information be found?** sec.gov search for "Covered Stablecoins" April 2025.
- **What information is missing or uncertain?** Anchorage July 2025 USDtb press for GENIUS Act. **Why does each gap matter for risk assessment?** It verifies compliance path and expansion risk. **Where might this information be found?** anchorage.com press for July 2025.
- **What information is missing or uncertain?** StablecoinX $530 million financing primary announcement and investor confirmations. **Why does each gap matter for risk assessment?** It involves potential conflicts and valuation implications for the ecosystem. **Where might this information be found?** StablecoinX announcements or investor disclosures.
- **What information is missing or uncertain?** Guy Young 48 million ENA buyback on-chain evidence. **Why does each gap matter for risk assessment?** It verifies team alignment and liquidity support. **Where might this information be found?** On-chain ENA transfers or wallets for the buyback.
- **What information is missing or uncertain?** Aave proposal status and vote outcome for USDe oracle. **Why does each gap matter for risk assessment?** It involves integration risks with DeFi protocols. **Where might this information be found?** Aave governance forum thread updates.
- **What information is missing or uncertain?** Jupiter JupUSD partnership details and vote. **Why does each gap matter for risk assessment?** It validates competitive and multi-chain strategy. **Where might this information be found?** Jupiter governance for the partnership.
- **What information is missing or uncertain?** USDH Hyperliquid proposal outcome. **Why does each gap matter for risk assessment?** It involves perps expansion risks. **Where might this information be found?** Hyperliquid validators for USDH.
- **What information is missing or uncertain?** S&P August 15, 2025 Ethena versus Sky primary report. **Why does each gap matter for risk assessment?** It provides full Basel III context for institutional barriers. **Where might this information be found?** S&P archives for the August 2025 report.
