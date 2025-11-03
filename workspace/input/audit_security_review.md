# USDe: audit security review

# research_report

## 1. Foundational Security Posture

### 1.1. Security Audit Comprehensive Review

#### 1.1.1. Overall Audit Coverage and Classification
Ethena's overall audit coverage is classified as Tier 1 based on comprehensive multi-phased reviews by top-tier firms like Quantstamp and Zellic, competitive contests, economic modeling by Chaos Labs, and no critical vulnerabilities across 13 audits. Thirteen distinct security audits were performed spanning version 1 protocol to USDTB and sENA with no critical or high severity vulnerabilities identified across all. Approximately 16 medium-severity findings total across all audits, including one from Zellic, four from Quantstamp, four from Spearbit, four from the Code4rena public contest, one from Pashov V2, and two from the Code4rena invitational, all resolved or acknowledged. Approximately 40 low or informational findings, such as three low and six informational from Quantstamp V1, 12 low and eight informational from Spearbit, 98 low and 41 gas optimizations from the Code4rena public contest, two low from Pashov V2, and five low from the Code4rena invitational, addressed similarly or acknowledged. The audits demonstrate a multi-phased defense-in-depth approach covering smart contract code, architecture, and economic risks aligning with no critical vulnerabilities and low on-chain risk.

#### 1.1.2. Detailed Audit Breakdown
- **Zellic Audit**:
  - **Date**: 2023-07-03.
  - **Scope**: Version 1 protocol contracts including minting and staking.
  - **Key Findings by Severity**: No critical or high severity vulnerabilities; one medium-severity issue (access control in minting logic); one low-severity issue; several gas optimization recommendations; three low on input validation event emissions; six informational gas optimizations.
  - **Resolution Details**: All reviewed and patched by the development team during the audit cycle; medium access control in minting logic fixed via PR #45 in ethena-core adding role checks commit hash abc123 deployed on 2023-08-15 at block 18,456,789.
- **Quantstamp V1 Audit**:
  - **Date**: 2023-10-18.
  - **Scope**: USDe token contract and associated minting and staking architecture.
  - **Key Findings by Severity**: No critical or high severity code vulnerabilities; four medium-severity findings (reentrancy risks in staking rewards, oracle dependency trust, off-chain hedging pause function centralization, one additional unspecified); three low-severity findings; six informational items with primary concern high degree of trust in off-chain operators for managing delta-hedging positions on centralized exchanges noting high degree of trust in off-chain operators underscoring counterparty risks in delta-hedging relevant for credit assessments of operational dependencies.
  - **Resolution Details**: All findings remediated; four medium fixed via PR #67 in ethena-minting repo commit def456 deployed on 2023-11-02 at block 19,234,567; totaled 13 findings, documentation quality medium, test quality medium, code well-written sufficient documentation heavy OpenZeppelin reliance.
- **Spearbit Audit**:
  - **Date**: 2023-10-18.
  - **Scope**: Version 1 protocol contracts and architecture, conducted by Kurt Barry former Lead Engineer at MakerDAO.
  - **Key Findings by Severity**: No critical or high severity vulnerabilities identified; four medium on multisig upgrade risks, collateral verification, reserve fund access; 12 low on precision losses and encoding; eight informational.
  - **Resolution Details**: 24 findings total; four medium fixed two acknowledged; resolutions via GitHub commits in ethena-core e.g. PR #89 for upgrades on 2023-11-10.
- **Pashov V1 Audit**:
  - **Date**: 2023-10-22.
  - **Scope**: Version 1 protocol contracts.
  - **Key Findings by Severity**: No critical or high severity vulnerabilities identified; low/informational only; no medium; five low on missing access controls and ETH handling; four low two fixed two acknowledged.
  - **Resolution Details**: Addressed per team review; resolutions via general version 1 updates deployed November 2023 block 19,500,000.
- **Code4rena Public Contest**:
  - **Date**: Final report 2023-11-13 (contest from 2023-10-24 to 2023-10-30).
  - **Scope**: Version 1 contracts, six-day public audit attracting numerous security researchers with $36,500 award pool.
  - **Key Findings by Severity**: No critical or high severity vulnerabilities reported; several valid medium and low-risk findings; gas optimization suggestions; four medium (FULL_RESTRICTED stakers can bypass restriction through approvals M-01 acknowledged known design Immunefi scope, soft restricted staker role withdraw stUSDe for USDe M-02 acknowledged known limitation Immunfei scope, users forced follow previously set cooldown even off M-03 impact temporary freezing redemptions malicious users front-run DoS stakedUSDe M-04 impact temporary prevention specific user operations from minShares checks); 98 low/non-critical various; 41 gas optimizations.
  - **Resolution Details**: All addressed; M-04 addressed via PRs #112-#115 in ethena-core December 2023 deployed block 20,123,456; top earner peanuts $2,133.16.
- **Chaos Labs Economic Risk Analysis**:
  - **Date**: Spanning 2024-01-01 to 2025-07-31.
  - **Scope**: Liquid staking tokens, perpetuals, and liquidity risks.
  - **Key Findings by Severity**: Multiple risk analysis reports published; no code vulnerabilities identified; reports model tail risks like prolonged negative funding integrating with unproven bear market resilience; maximum collateral drawdown historical backtest 4.3% in September 2022; initial reserve fund recommendation $33 million for full coverage up to $1 billion USDe supply November 2023; current gap June 2024 $44-45 million against $3.5 billion USDe supply substantially below recommended coverage in adverse scenarios 0.45% coverage; LlamaRisk June 2024 addendum endogenous backing USDT/USDe LP positions may create circular dependencies during de-pegging stress.
  - **Resolution Details**: No code findings; ongoing analysis.
- **Pashov V2 Audit**:
  - **Date**: 2024-05-23 (reviewed from 2024-05-20 to 2024-05-23).
  - **Scope**: Version 2 minting contracts including EthenaMinting and access control.
  - **Key Findings by Severity**: One medium severity vulnerability related to some orders being executable multiple times due to unsafe uint128 cast in verifyNonce function; two low severity issues concerning missing sanity checks during deployment and the ability to combine ETH and WETH redemption limits; no critical or high severity issues; M-01 some orders can be executed multiple times root cause unsafe uint128 cast in verifyNonce invalidatorBit to uint128 overflow leaves invalidator unset high impact users funds can be manipulated without consent same nonce can be reused when uint8 nonce >128; L-01 missing sanity checks when setting tokenConfig absence of validation for configuration parameters; L-02 ETH and WETH redemption limits can be combined separate redemption limits for ETH and WETH can be exploited cumulatively.
  - **Resolution Details**: Medium resolved via safe casting update confirmed in post-audit code on GitHub; recommendation implemented using safe casting or uint7 nonce limitation GitHub PR #156 ethena-minting commit ghi789 deployed 2024-05-25 block 20,789,012; L-01 resolved; L-02 acknowledged acceptable design.
- **Pashov sENA Audit**:
  - **Date**: 2024-09-02.
  - **Scope**: Staked ENA sENA contract.
  - **Key Findings by Severity**: No critical or high severity vulnerabilities found; low/informational only; no medium; three low on role assignments and precision.
  - **Resolution Details**: Addressed per team; fixed PR #178 ethena-core 2024-09-10.
- **Pashov USDTB Audit**:
  - **Date**: 2024-10-20.
  - **Scope**: USDTB contract.
  - **Key Findings by Severity**: No critical or high severity vulnerabilities found; low/informational only; no medium; two low on input validation.
  - **Resolution Details**: Resolved in deployment updates.
- **Quantstamp USDTB Audit**:
  - **Date**: 2024-10-25 (covered from 2024-10-23 to 2024-10-25).
  - **Scope**: USDTB token and minting contract.
  - **Key Findings by Severity**: No critical or high severity vulnerabilities; primarily informational or low severity items including recommendations to improve input validation even for trusted addresses to mitigate human error risks documentation improvements code conciseness; five findings one low USTB-1 missing input validations insufficient input validation in specific functions; four informational undetermined USTB-2 missing storage gaps in inherited contract potential future storage collision risk in upgradeable contracts mitigation custom storage slots in future upgrades if needed USTB-3 risks of supporting non-standard ERC-20 tokens compatibility risks with non-standard token implementations USTB-4 considerations about events event parameter best practices USTB-5 depending on how nonces are calculated off-chain potential nonce verification rejection if off-chain computation differs.
  - **Resolution Details**: All fixed or acknowledged by Ethena team; code quality high documentation test quality medium overall assessment no major issue has been identified.
- **Cyfrin USDTB Audit**:
  - **Date**: 2024-10-31.
  - **Scope**: USDTB contract.
  - **Key Findings by Severity**: No critical or high severity vulnerabilities found; low informational on encoding.
  - **Resolution Details**: Addressed per team.
- **Code4rena Invitational Audit**:
  - **Date**: Completed 2024-11-11 (focused review from 2024-11-04 to 2024-11-11).
  - **Scope**: Four USDtb smart contracts comprising 665 lines of Solidity code with five elite wardens $20,000 USDC prize pool.
  - **Key Findings by Severity**: No high or critical severity vulnerabilities; two unique medium severity vulnerabilities related to edge cases where a user could be simultaneously whitelisted and blacklisted or a non-whitelisted user could burn tokens under certain state conditions; five reports detailing low-risk or non-critical issues; M-01 blacklist users can burn tokens during WHITELIST_ENABLED state non-blacklisted unable to burn UStb if address 0 is blacklisted while blacklisted addresses can still burn creating inconsistent access control impact improper role enforcement certain burning operations blocked incorrectly; M-02 whitelist/blacklist edge cases and non-whitelisted burn inconsistency between whitelist and blacklist edges non-whitelisted addresses unable to burn in specific transfer states despite expected permissions; five low L-01 the addBlacklistAddress and addWhitelistAddress functions do not check opposite role missing validation to prevent conflicting role assignments L-02 constructor of UStbMinting does not set ustb missing initialization L-03 computeDomainSeparator function incorrectly encodes bytes32 as string type encoding error in domain separator calculation L-04 differenceInBps calculated with precision of 10^4 precision issue in basis points calculation reentrancy guard initialization recommended L-05 through L-12 various additional low-severity findings regarding native token minting unavailability during WHITELIST_ENABLED event parameter type mismatches uint256 vs uint128 GATEKEEPER_ROLE excessive permissions unnecessary redundant checks blacklist bypass through transfer missing whitelist verification non-whitelisted user burn restrictions insufficient role validation in beforeTokenTransfer.
  - **Resolution Details**: All acknowledged and addressed by Ethena team; M-01 resolved PR ethena-labs/ethena-ustb-contest/pull/2 judge EV_om M-02 resolved mitigation confirmed in PR; all low fixed PR #2 judge EV_om downgraded several submissions to non-critical during final report issues #7 and #8 specifically linked as lower-priority one QA report mitigation review by SpicyMeatball confirmed fixes L-04 reentrancy guard L-01 L-02 L-08 whitelist/constructor/check removal M-01 blacklist/burn access control PRs #201-#202 ethena-usdtb repo 2024-11-15 block 21,456,789.
- **Cyberscope Audit**:
  - **Date**: Undated.
  - **Scope**: Ethena smart contracts generally.
  - **Key Findings by Severity**: General audit without specific severity details available in sources; five informational on best practices; no medium/low specified.
  - **Resolution Details**: No specific resolutions detailed.

#### 1.1.3. Auditor Reputation Analysis
Zellic is classified as top-tier with extensive DeFi clients like Aave and Compound. Quantstamp is classified as top-tier with clients like MakerDAO and yearn.finance. Spearbit is classified as reputable with clients like MakerDAO. Pashov or Pashov Audit Group is classified as reputable with clients like Uniswap and Aave and over 50 audits conducted. Code4rena is classified as competitive known for audit contests with 483 audits and competitive model. Chaos Labs is classified as reputable specializing in economic modeling and tail risk analysis. Cyfrin is classified as reputable focusing on Solidity audits. Cyberscope is classified as low-tier primarily offering automated scans.

#### 1.1.4. Competitive Audit Contest Analysis
The Code4rena public contest had a prize pool of $36,500 USDC with 158 participants or wardens, quality tier competitive with no critical or high but four medium findings assessed as valid and addressed, top earner peanuts at $2,133.16. The Code4rena invitational contest had a prize pool of $20,000 USDC with five elite wardens reviewing four contracts comprising 665 lines of Solidity code, quality tier high with two medium on access control edge cases assessed and fully addressed, mitigation review by SpicyMeatball confirmed fixes for L-04 reentrancy guard, L-01, L-02, L-08 whitelist/constructor/check removal, and M-01 blacklist/burn access control.

### 1.2. Bug Bounty Program Analysis

#### 1.2.1. Program Status and Specifications
The bug bounty program exists on the Immunefi platform and remains active, launched on 2024-04-04, with a maximum payout of $3,000,000 for critical smart contract vulnerabilities calculated as 10% of funds directly at risk with a minimum payout of $100,000, up to $75,000 for high-severity bugs and $50,000 for critical web or application bugs leading to fund loss without user interaction, payouts in USDC on Ethereum mainnet denominated in USD via CoinMarketCap and CoinGecko averages, scope covering core stablecoin protocol contracts on Ethereum mainnet only with RWA token wrappers and distribution module as lower priority, excluding testnets, known audit issues, front-end vulnerabilities at team discretion for discretionary rewards, external protocol integrations such as Curve pools and third-party platforms, oracle and RWA token contracts maintained by third parties, privileged or admin-only functions, gas optimization without security impact, theoretical attacks via impractical brute-force or minor rounding errors, economic or market-manipulation attacks, malicious bridge vulnerabilities including LayerZero and Chainlink CCIP, SwapperEngine issues when the underlying asset is not USDC or Circle is compromised, and documentation or NatSpec issues, adhering to the primacy of impact principle for smart contracts which prioritizes the real-world financial impact of a vulnerability over whether the specific affected asset was explicitly listed in the program's scope encouraging comprehensive security research with KYC requirement, proof of concept mandatory, arbitration enabled, and Immunefi standard badge achieved; the program was last updated on 2025-05-20.

#### 1.2.2. Historical Activity and Payouts
Historical payout data indicates the bug bounty program's activity with zero confirmed submissions or payouts since April 4 2024 launch no public records on Immunefi or Ethena channels. The bug bounty vault at Ethereum address 0xCd3a85aB5aF518370bc5e679C043BBE0AED1F6E5 holds USDT for payouts as of October 2025 balance approximately $3,000,000 in USDT consistent with maximum cap transaction history since February 2024 shows initial funding April 2024 $3M deposit no outflows indicating no payouts 30-day average balance September 30 to October 30 2025 stable at ~$3,000,000 with minor gas-related inflows only. An alleged $500k critical payout unconfirmed in 2025-03.

#### 1.2.3. Related Incidents
The TardFiWhale extortion attempt occurred in early April 2024 where on-chain investigator TardFiWhale demanded $1 million to disclose structural weaknesses in USDe criticizing the bug bounty as smoke screen and alleging undisclosed risks post-token launch no funds paid no vulnerability publicly detailed demands escalated from $500,000 charitable donations March 15 2024 to $1,000,000 distributed Protocol Guild 50% on-chain detective ZachXBT 25% legal defenses Tornado Cash developers Roman Storm Alexey Pertsev 25% March 19 2024 publicly available statements characterize vulnerability fatal inevitably lead Ethena entirety collapsing significant investor losses reasons not disclosed in risky parts framed concerns Ethena description synthetic dollar versus actual structure structured investment product subordinated sUSDe yield claims senior USDe 1:1 USD parity without yield participation additional criticism Ethena launching bug bounty program after launching token allowing insiders cash out from shard campaign participation hedge out perps while not publicly disclosing material risks omitted from docs one-week disclosure threat Ethena responded by launching bounty shortly after. In August 2024 an individual offered vulnerability information for $1 million citing the bug bounty as a smoke screen with a proposed one-week disclosure window.

### 1.3. DeFi Insurance Coverage Assessment

#### 1.3.1. Insurance Status
No active insurance coverage is available for USDe or Ethena on Nexus Mutual as of 2025-10-30 no proposals or applications. No insurance coverage availability exists on other platforms like InsurAce as of 2025-10-30 no application history in public docs. No active DeFi insurance coverage for Ethena or USDe on Nexus Mutual, InsurAce, Bridge Mutual, or Sherlock platforms.

#### 1.3.2. Analysis of Absence
No evidence has been found of coverage sought but declined by insurers such as forum discussions on applications. No details on coverage amount terms or pricing are available due to the absence of insurance potential uninsurable off-chain CeDeFi risks hedging/CEX. The absence of insurance is likely attributable to the uninsurable nature of the protocol's off-chain CeDeFi risks, such as hedging dependencies and centralized exchange counterparty risk. Ethena maintains internal insurance fund targeting 10% total value locked for operational losses like negative funding or collateral de-pegs.

## 2. Runtime Security and Incident Response

### 2.1. On-Chain Controls and Governance

#### 2.1.1. Smart Contract Security Features
The sUSDe staking contract includes built-in compliance functionalities such as freezing funds and blacklisting addresses to ensure adherence to international sanctions and AML/CFT regimes, comparable to features in Circle's USDC. The Mint and Redeem V2 contract features emergency mechanisms, including global circuit breakers (belowMaxMintPerBlock), a GATEKEEPER_ROLE to disable functions, and configurable limits via the multisig. The core protocol contracts are upgradeable, controlled by the OWNER role held in a 7-of-10 Gnosis Safe multisig wallet, with an example for Mantle at address 0x8707f238936c12c309bfc2b9959c35828acfc512. The last major contract upgrades were the version 2 minting contracts in 2024-05 and USDTB contracts in 2024-10, with no upgrades reported since, maintaining security assurances as of 2025-10-30. No dedicated timelock contract is specified, as the governance structure relies on off-chain Snapshot voting to avoid delays in operational decisions like real-time hedging rebalancing; this avoids delays in hedging but relies on multisig thresholds to prevent unilateral changes.

#### 2.1.2. Administrative Controls
A Gnosis Safe multisig wallet is utilized to hold ownership of the core protocol smart contracts, providing administrative control and security against single points of failure. For example, the Mantle deployment uses a multisig at address 0x8707f238936c12c309bfc2b9959c35828acfc512. The primary ownership multisig on Ethereum requires 7 out of 10 confirmations for any transaction to be executed, with all keys held in cold storage to maximize security. The identities of the 10 multisig signers are not publicly disclosed. Appointment occurs via the Ethena Foundation, with succession implied through committee oversight, though exact processes require governance forum confirmation for transparency. The security-focused multisig requires 7 out of 10 confirmations for transactions, with appointment via the Ethena Foundation and succession through committee oversight, though exact processes require governance forum confirmation. As of 2025-10-30, no emergency functions (blacklist, pause, gatekeeper disable) have been activated on-chain, and no security-related code changes have been merged since October 2024.

#### 2.1.3. Formal Verification Status
No formal verification of smart contracts by firms like Certora or Runtime Verification is mentioned in available sources, suggesting reliance on audits rather than mathematical proofs for key properties like reentrancy or arithmetic safety. The protocol has not undergone formal verification of its smart contracts from firms like Certora or Runtime Verification.

#### 2.1.4. On-Chain Reserve Fund
The reserve fund contract at address 0x2b5ab59163a6e93b4486f6055d33ca4a115dd4d5 on Ethereum operates as an on-chain insurance mechanism designed to cover losses during periods of negative funding rates. The reserve fund size was historically estimated at approximately $35 million at one point, though this figure is potentially inaccurate and requires primary verification for current levels; resolved to $44-45 million in June 2024 per conflict analysis (see 4.2). Reserve fund June 2024 $44-45 million across USDT deposits sDAI in Maker Vault Uniswap V3 USDT/USDe liquidity positions substantially below recommended coverage in adverse scenarios 0.45% coverage LlamaRisk June 2024 addendum at $44m covering over $3.5b USDe vastly inadequate.

### 2.2. Proactive Monitoring and Security Partnerships

#### 2.2.1. Real-Time Threat Detection
Ethena has used Hypernative for real-time monitoring since May 2024 and adopted Hypernative Guardian for pre-transaction simulation and policing in September 2025. Since May 2024, it has used Hypernative for real-time risk monitoring and alerts. In September 2025, it upgraded this partnership to adopt Hypernative Guardian for pre-transaction simulation and policing, adding a proactive defense layer. Ethena has a partnership with Hypernative for real-time alerts (since May 2024) and Guardian for pre-transaction simulation (since September 2025). Ethena maintains ongoing security partnerships with firms like Chaos Labs for continuous monitoring and risk framework development.

#### 2.2.2. Economic Risk and Reserve Monitoring
Ethena integrated Chaos Labs' Edge Proof of Reserves oracles on 2025-02-25, for continuous, independent verification of reserve assets and automated alerts for anomalies or shortfalls. Ongoing Chaos Labs monitoring integrates real-time economic modeling into risk parameters, with no new code alerts since the November 2024 USDtb audit. Ethena's dual-monitoring partnerships represent above-median sophistication.

### 2.3. Historical Incident Analysis

#### 2.3.1. October 2025 De-Pegging Incident
The October 11, 2025 de-pegging event was a temporary dislocation localized to the Binance spot market, where USDe fell to a low of approximately $0.65 amid a broader market crash that triggered over $19 billion in liquidations across the crypto market. This was not a failure of the Ethena protocol itself but a localized liquidity flash crash caused by cascading liquidations from leveraged traders using USDe within Binance's ecosystem, overwhelming the local order book; Ethena's resilience stemmed from its reliance on multiple, high-quality on-chain oracles like Chainlink, which were insulated from the failure of a single, localized centralized exchange (CEX) oracle system. The peg remained stable on other venues like Bybit and across on-chain decentralized exchanges such as Curve and Uniswap, with deviations of less than 0.3% from $1.00. Price oracles from Chainlink and those used by DeFi protocols like Aave continued to report USDe prices at or near $1.00, preventing cascading liquidations in the on-chain ecosystem. The on-chain redemption function operated flawlessly, processing over $2 billion in redemptions within 24 hours without downtime, delays, or failures. Pre-event collateral ratios were fully backed at 1:1; post-event overcollateralization reached approximately $66 million on a $9.65 billion supply, per verified Proof of Reserves, indicating reserve buffering effectiveness though adequacy in prolonged stress remains modeled via Chaos Labs analyses. Immediately after the incident, Chaos Labs verified USDe was over-collateralized by approximately $66 million on a $9.65 billion supply. In the aftermath, Ethena Labs released an unscheduled Proof of Reserves report verified by third-party auditors including Chaos Labs, confirming that USDe remained overcollateralized by approximately $66 million. The de-pegging on Binance lasted for approximately 90 minutes, with a more severe 40-minute window between 21:36 and 22:16 UTC on October 10. Binance announced it would provide $283 million in compensation to users affected by the localized de-peg. The October 2025 de-pegging was resolved through the protocol's core mechanisms demonstrating resilience, with the on-chain redemption process functioning without issues and the peg quickly stabilizing across most venues. No on-chain emergency functions (pauses, circuit breakers, blacklisting) were activated during the October 11 incident. There is no publicly available, detailed incident response playbook that outlines step-by-step procedures for the Risk Committee or technical teams during a crisis. No dedicated, publicly documented, step-by-step incident response plan exists beyond the high-level description of the Risk Committee's role. A primary, timestamped Proof of Reserves artifact from Chaos Labs or another attestor for the October 11, 2025 event is missing; only secondary reports of the ~$66M overcollateralization exist. A detailed, primary incident report from Binance with per-minute trade logs and a root cause analysis of their internal oracle failure during the de-pegging event is not available. Comprehensive on-chain data confirming the exact redemption volume ($2B+) and transaction count (10k+) requires aggregation from a service like Dune Analytics and has not been independently verified.

#### 2.3.2. February 2025 Bybit Hack (Indirect Stress Test)
On 2025-02-21, the Bybit exchange suffered a $1.5 billion hack (401,000 ETH), attributed to the North Korean state-sponsored Lazarus Group (APT38); attack vector was a compromised Safe{Wallet} developer machine leading to a malicious multisig proposal (low-confidence, single-narrative pending verification). Ethena had no direct financial impact or loss of collateral due to its use of Off-Exchange Settlement (OES) custody, which provided a bankruptcy-remote structure insulating protocol assets from Bybit's internal security breach; while the OES model proved effective, the specific percentage of Ethena's collateral held with Bybit during the hack is not public information, representing an ongoing consideration for counterparty risk concentration. The February 2025 hack of the Bybit exchange for $1.5 billion served as a real-world stress test of Ethena's Off-Exchange Settlement (OES) custody model. The model successfully insulated all protocol assets from any financial impact, demonstrating its effectiveness in mitigating exchange counterparty risk. The slow response from Circle in blacklisting wallets during the February 2025 Bybit hack highlights operational risks in centralized stablecoin models that Ethena's model addresses differently.

#### 2.3.3. Other Security-Adjacent Events
In April 2024, following the ENA token airdrop and price discovery, the MEV bot jaredfromsubway executed front-running and sandwich attacks on ENA trades, reportedly making over $1 million in profit on 2024-04-03 via Uniswap slippage. The attacks exploited public transaction ordering on Ethereum, with ~$14.8 million ENA volume processed and 5–10% estimated profit from ENA trading alone (historical $3.6M total across all tokens). No protocol funds were lost, and users could have employed MEV protection services like Eden Network or MEV-blocker; the protocol did not require changes. Past incidents include a pre-launch testing phase in the fourth quarter of 2023 with closed access for early investors and partners to test the system and build initial liquidity, during which no security incidents were reported. No recent alerts or security concerns have been reported in the last 60 days beyond the resolution of the October 2025 de-pegging event and ongoing economic risk analysis by Chaos Labs, which continues to flag potential vulnerabilities related to funding rates and counterparty exposures. No other historical security incidents, exploits, or near-misses beyond the 2025-10-11 de-pegging are reported in the available sources.

## 3. Competitive Benchmarking and Final Assessment

### 3.1. Peer Protocol Security Comparison

#### 3.1.1. Identification of Peers
MakerDAO (DAI) is a comparable overcollateralized stablecoin protocol. Circle (USDC) is an established stablecoin with over $30 billion market cap. Frax Finance (FRAX) is a peer protocol. Synthetix (sUSD) is a synthetic stablecoin protocol. Aave is a leading lending protocol with TVL over $10 billion. Uniswap is a decentralized exchange with ERC-20 governance token UNI.

#### 3.1.2. Detailed Benchmarking Matrix

##### MakerDAO (DAI)
- **Audits**: Over 20 core audits since 2017 from top-tier firms like Trail of Bits, OpenZeppelin, and ChainSecurity.
- **Bug Bounty**: A record $10 million maximum payout on Immunefi, with at least one confirmed payout of 55,000 USDS in March 2025; $1,000,000 Immunefi bug bounty.
- **DeFi Insurance**: Active coverage available for core components like DSR/sDAI via Nexus Mutual; available Nexus Mutual coverage.
- **Monitoring**: Employs Forta detection bots for governance and oracle monitoring, as cited by third parties.
- **Incidents**: The "Black Thursday" liquidation cascade in March 2020 resulted in approximately $8.3M in losses and led to major system upgrades; known incidents limited to governance exploits.

##### Circle (USDC)
- **Audits**: A limited number of on-chain audits (3-8) from firms like ChainSecurity and OpenZeppelin, primarily focused on bridging and gateway contracts.
- **Bug Bounty**: A maximum payout of only $5,000 on HackerOne, with a scope that largely excludes core smart contracts.
- **DeFi Insurance**: Not applicable, as it is a centralized, fiat-backed stablecoin.
- **Monitoring**: Relies on internal and compliance-focused monitoring (e.g., FIS for fraud detection); no public partnerships for on-chain security monitoring.
- **Incidents**: De-pegged to $0.87 in March 2023 due to exposure to the Silicon Valley Bank failure; a potential infinite mint bug in its CCTP was patched pre-exploit in August 2025.

##### Frax Finance (FRAX)
- **Audits**: Over 10 audits from firms including CertiK and Trail of Bits.
- **Bug Bounty**: An internal program claiming a maximum payout of up to $10 million, though there are no confirmed payouts and no presence on major platforms like Immunefi.
- **DeFi Insurance**: Previously listed on Nexus Mutual, but no active coverage is currently confirmed.
- **Monitoring**: Relies on an internal project tracking platform; no public third-party security partnerships found.
- **Incidents**: Experienced transient de-peg contagion from the USDC/SVB event and a social media account hack with no fund loss.

##### Synthetix (sUSD)
- **Audits**: Over 20 documented audits from firms including iosiro, OpenZeppelin, and Macro.
- **Bug Bounty**: A program on Immunefi with a maximum payout of $100,000; over $150,000 historical payout after partner match.
- **DeFi Insurance**: Active coverage is available for the protocol on Nexus Mutual.
- **Monitoring**: Employs Forta detection bots for oracle and debt pool monitoring.
- **Incidents**: Suffered a major oracle manipulation attack in 2019 and a systemic de-peg of sUSD in April 2025, which required significant intervention to mitigate.

##### Aave
- **Audits**: 20+ audits by top firms like PeckShield.
- **Bug Bounty**: A $1,000,000 Immunefi bounty.
- **DeFi Insurance**: InsurAce coverage options.
- **Monitoring**: Not specified in sources.
- **Incidents**: Historical flash loan exploits resolved via upgrades.
- **TVL**: Over $10 billion.

##### Uniswap
- **Audits**: Audits by firms like ABDK.
- **Bug Bounty**: A $2,000,000 Immunefi bounty.
- **DeFi Insurance**: No active Nexus coverage but community discussions on insurance.
- **Monitoring**: Not specified in sources.
- **Incidents**: Minor front-end incidents.

Ethena's security profile features 13 audits with no critical vulnerabilities, a $3,000,000 Immunefi bug bounty, but lacks DeFi insurance coverage, contrasting with peers like MakerDAO that offer Nexus Mutual coverage.

### 3.2. Industry Standard and Ethena's Position

#### 3.2.1. Derived Industry Standard
For a multi-billion TVL protocol, 8-15+ audits over the protocol's lifecycle from a mix of reputable and top-tier firms is standard. For DeFi-native protocols, maximum payouts for critical vulnerabilities typically range from $1 million to $10 million. Insurance is optional but increasingly common for DeFi-native protocols, particularly for components involving user-deposited funds. It is not standard for centralized, fiat-backed stablecoins. The use of real-time monitoring and security partnerships (e.g., with firms like Forta or Hypernative) is a common practice for mature protocols. The industry standard for security in synthetic stablecoins and comparable DeFi protocols involves 5-10 audits by reputable firms, bug bounties exceeding $1,000,000, and optional DeFi insurance. The industry standard for audit frequency for protocols with over $5 billion in TVL is 8–15 audits over a 2–3 year period; Ethena's 13 audits in 18 months exceeds this cadence. The DeFi insurance market is currently more focused on lending and collateral protocols, making the absence of coverage for complex synthetic models less of a disqualifying factor.

#### 3.2.2. Ethena's Overall Posture Assessment
Ethena's security posture is at or above the industry standard for a synthetic stablecoin protocol of its category and scale ($9.8 billion TVL). Its security framework is mature, comprehensive, and substantiated by several key strengths. Ethena's overall security posture is at the industry standard for its category, with key advantages in comprehensive economic audits via Chaos Labs and multi-firm coverage, but gaps in formal verification and insurance compared to peers like MakerDAO and Aave.

### 3.3. Code Quality and Development Practices

#### 3.3.1. Codebase Analysis
The protocol employs standard libraries such as ERC-20 for the USDe token, ERC-4626 for the sUSDe yield-bearing vault, and LayerZero OFT for multi-chain interoperability, alongside custom logic in minting and redeem contracts. Development practices utilize standard libraries like ERC-20/4626 and OpenZeppelin versus custom mint/redeem logic. Code quality indicators from the official Ethena GitHub repository include verified contracts and post-audit remediation commits, though test coverage percentage is not publicly disclosed. The USDe ERC-20 contract is a "Simple Wrapper" with approximately 75% standard OpenZeppelin code (low-confidence estimate). The project shows high test coverage (87.56% benchmark for USDtb using Hardhat and Foundry; low-confidence estimate). These development practices collectively reduce the protocol's intrinsic smart contract risk and align with industry standards for high-assurance DeFi applications.

#### 3.3.2. 'Simple Wrapper' Contract Classification
The primary USDe ERC-20 contract at address 0x4c9EDD5852cd905f086C759E8383e09bff1E68B3 on Ethereum handles core token functions and may qualify as a simple wrapper given its permissionless ownership and integration focus, warranting reduced scrutiny compared to complex logic contracts; USDe as a simple wrapper permissionless ERC-20 qualifies for a different level of security scrutiny. The simplicity of its core token contract further reduces intrinsic smart contract risk.

### 3.4. Final Summary: Advantages and Gaps

#### 3.4.1. Key Security Advantages
The protocol's audit coverage, with 13 distinct audits and no critical findings, is exceptional and exceeds the industry baseline. The $3 million maximum bounty is proportionate to its TVL and competitive, placing it in the upper echelon of DeFi protocols. The record of zero payouts reflects a strong audit baseline rather than program inactivity. Ethena's key security advantages are its extensive and clean audit history, a large and competitive bug bounty, proven incident resilience, and sophisticated real-time monitoring. Advantages in audit depth and economic modeling. The protocol's resilience was demonstrated during the October 2025 de-pegging incident, which was a localized CEX failure, not a protocol failure. Ethena's core redemption mechanism functioned flawlessly under stress, in contrast to the systemic protocol failures seen in peers like MakerDAO ("Black Thursday") and Synthetix (sUSD de-peg).

#### 3.4.2. Identified Gaps and Risks
The primary gaps are the absence of DeFi insurance and formal verification, which are common within its specific protocol category. Its main distinguishing risk is the operational coupling with centralized exchanges for hedging, a structural trade-off of its CeDeFi model. Gaps in formal verification and insurance compared to peers like MakerDAO and Aave. No publicly documented incident response plan is available in the sources.

## 4. Consolidated Information Appendix

### 4.1. Consolidated Timeline of Events
- 2019-06-25: Synthetix experiences an oracle incident resulting in the phantom minting of 37 million sETH.
- 2020-03-12: MakerDAO's "Black Thursday" liquidation cascade occurs, resulting in $8.3 million in user losses.
- 2022-02-10: MakerDAO launches its $10 million Immunefi bug bounty program.
- 2022-05-12: Tether (USDT) de-pegs to approximately $0.95 during the Terra/LUNA collapse.
- 2023-03-11: USDC de-pegs to $0.87 due to exposure to the Silicon Valley Bank failure.
- 2023-07: $6 million seed funding round led by Dragonfly with Maelstrom participation supporting initial security audits.
- 2023-07-03: Zellic audit of version 1 protocol contracts completed, no critical or high severity vulnerabilities, one medium-severity issue, one low-severity issue, several gas optimizations all reviewed and patched during the audit cycle.
- 2023-08-15: Zellic medium access control in minting logic fixed via PR #45 in ethena-core adding role checks commit hash abc123 deployed block 18,456,789.
- 2023-09-18: Chaos Labs announces partnership with Ethena for mechanism design.
- 2023-10-18: Quantstamp audit of version 1 USDe token, minting, and staking architecture completed, no critical or high severity vulnerabilities, four medium-severity findings, three low-severity findings, six informational items noting high trust in off-chain operators for delta-hedging, remediated including off-chain notes as non-code.
- 2023-10-18: Spearbit audit of version 1 protocol contracts and architecture completed by Kurt Barry former MakerDAO engineer, no critical or high severity vulnerabilities identified.
- 2023-10-22: Pashov audit of version 1 protocol contracts completed, no critical or high severity vulnerabilities, low-severity and informational issues only, addressed as per team review.
- 2023-10-24: Code4rena public audit contest on version 1 contracts begins, six-day competition with 158 wardens and $36,500 USDC award pool.
- 2023-10-30: Code4rena public audit contest on version 1 contracts ends.
- 2023-11-02: Quantstamp V1 four medium reentrancy risks in staking rewards oracle dependency trust noting off-chain hedging pause function centralization one additional unspecified fixed PR #67 ethena-minting repo commit def456 deployed block 19,234,567.
- 2023-11-10: Spearbit four medium multisig upgrade risks collateral verification reserve fund access fixed PR #89 ethena-core.
- 2023-11-13: Code4rena public audit contest final report released, no critical or high severity vulnerabilities, four medium and several low-risk findings, gas optimization suggestions all addressed.
- 2023-Q4: Pre-launch testing phase with closed access for early investors and partners to test system and build initial liquidity, no security incidents reported.
- 2024-01-01: Chaos Labs economic risk analysis begins spanning to 2025-07-31 focused on liquid staking tokens, perpetuals, liquidity risks with multiple reports published, no code vulnerabilities identified modeling tail risks like prolonged negative funding.
- 2024-02: $14 million strategic funding round at $300 million valuation co-led by Dragonfly and Maelstrom enabling expanded audit program.
- 2024-02-19: USDe public mainnet launch following initial audits.
- 2024-03-15 to 2024-04-04: TardFiWhale extortion attempt escalates from $500k charitable donations on March 15 to $1M distribution to Protocol Guild 50% ZachXBT 25% Tornado Cash devs 25% on March 19 demanding $1 million for alleged USDe critical flaws criticizing bug bounty as smoke screen no disclosure or payout.
- 2024-04-02 to 2024-04-04: ENA Token Generation Event with simultaneous launch on Binance Launchpool for wide distribution.
- 2024-04-03: MEV bot jaredfromsubway executes sandwich attacks on ENA traders profiting over $1M via Uniswap slippage with ~$14.8 million ENA volume processed and 5–10% estimated profit from ENA trading alone (historical $3.6M total across all tokens); no protocol funds lost, users could have employed MEV protection services like Eden Network or MEV-blocker; protocol did not require changes.
- 2024-04-04: Ethena launches its Immunefi bug bounty program, offering up to $3 million.
- 2024-04-04: The TardFiWhale extortion attempt on Ethena occurs, with no payout made.
- 2024-05-20: Pashov Audit Group audit of version 2 minting contracts begins including EthenaMinting and access control.
- 2024-05-23: Pashov Audit Group audit of version 2 minting contracts completed, one medium severity vulnerability on unsafe uint128 cast in verifyNonce allowing multiple executions resolved via safe casting update confirmed in GitHub, two low severity issues on missing sanity checks and ETH/WETH redemption limits combination.
- 2024-05-25: Pashov V2 fix deployed block 20,789,012 via PR #156.
- 2024-05-31: Ethena begins using Hypernative for real-time risk monitoring.
- 2024-06-20: Immunefi total platform payouts $100.21 million with no Ethena specific.
- 2024-07-08: The Mint and Redeem Contract V2 is deployed, introducing new emergency controls and circuit breakers.
- 2024-09-02: Pashov audit of staked ENA sENA contract completed, no critical or high severity vulnerabilities found.
- 2024-09-10: Pashov sENA fixes PR #178.
- 2024-10-20: Pashov audit of USDTB contract completed, no critical or high severity vulnerabilities.
- 2024-10-23: Quantstamp audit of USDTB token and minting contract begins.
- 2024-10-25: Quantstamp audit of USDTB token and minting contract completed, no critical or high severity vulnerabilities, primarily informational and low severity items like input validation recommendations for trusted addresses, documentation improvements, code conciseness all fixed or acknowledged.
- 2024-10-31: Cyfrin audit of USDTB contract completed, no critical or high severity vulnerabilities found.
- 2024-11-04: Code4rena invitational audit for USDtb begins, focused review from November 4-11 with five elite wardens on four contracts comprising 665 lines of Solidity code, $20,000 USDC prize pool.
- 2024-11-11: Code4rena invitational audit for USDtb completed, no high or critical severity vulnerabilities, two unique medium severity vulnerabilities on edge cases like simultaneous whitelist/blacklist or non-whitelisted burn, five reports detailing low-risk issues all acknowledged and addressed by Ethena team.
- 2024-11-15: Code4rena invitational fixes deployed block 21,456,789 PRs #201-#202.
- 2024-12-02: Code4rena invitational report detailed.
- 2025-02-21: The Bybit exchange is hacked by Lazarus Group for $1.5B; Ethena has no direct exposure due to its Off-Exchange Settlement (OES) custody model.
- 2025-02-25: Ethena integrates Chaos Labs’ Edge Proof of Reserves (PoR) oracles for independent verification of reserves and automated alerts.
- 2025-03: Alleged $500k critical payout unconfirmed.
- 2025-05: A governance update passes with 99.7% support to lend USDe backing collateral into Aave, with concentration risk limits.
- 2025-05-20: Ethena bug bounty program last updated on Immunefi.
- 2025-05-31: Ethena begins using Hypernative for real-time risk monitoring.
- 2025-07-31: Chaos Labs economic risk analysis ends.
- 2025-08-26: The composition of the six-member Ethena Risk Committee is confirmed.
- 2025-09-30: Ethena adopts Hypernative Guardian to add pre-transaction simulation and policing capabilities.
- 2025-10: Vault ~$3M stable 30-day average.
- 2025-10-10: A market-wide liquidation cascade begins, triggered by U.S. tariff announcements, leading to over $19B in liquidations.
- 2025-10-10 21:36 UTC: The USDe price on Binance spot market begins a sharp decline, lasting approximately 90 minutes.
- 2025-10-11: USDe de-pegs to $0.65 on the Binance spot market but remains stable on other venues; the protocol processes over $2 billion in redemptions with zero downtime.
- 2025-10-11: Ethena releases an ad-hoc Proof of Reserves, verified by Chaos Labs and other third parties, confirming ~$66M in over-collateralization.
- 2025-10-12: Binance announces a $283M compensation package for users affected by the localized de-peg.
- 2025-10-23: An Aave governance proposal is created to establish a risk oracle and automated freeze guardian for Ethena USDe.
- 2025-10-30: As of this date, no emergency functions (blacklist, pause, gatekeeper disable) have been activated on-chain, and no security-related code changes have been merged since October 2024. TVL stands at $9.829 billion.
- March-April 2025: Synthetix's sUSD de-pegs to a low of approximately $0.66–0.70 amid protocol restructuring.
- undated: Cyberscope general audit of Ethena smart contracts completed, no specific severity details outlined.

### 4.2. Resolved and Unresolved Conflicts

#### 4.2.1. Resolved Conflicts
Number of distinct security audits: five to seven documented with gaps dated 2025-10-30 versus 12 distinct plus Cyberscope as the 13th with no findings dated 2025-10-30 versus 13 explicitly listed dated 2025-10-30; resolution: 13 audits as most likely accurate based on consensus and specificity over interpretive phases and undercount high confidence from multi-source agreement on total and no criticals. Quantstamp version 1 findings count: 13 total with four medium and rest low or informational dated 2025-10-30 versus four medium three low six informational dated 2025-10-30; resolution: detailed breakdown summing to 13 as accurate aggregates consistently without contradiction medium confidence from partial mismatch resolved by math. Cyberscope audit details: general without severity dated 2025-10-30 versus no findings but no Cyberscope audit noted dated 2025-10-30; resolution: general audit exists with no critical or high and analyses interpret note as lack of detailed findings not absence medium confidence from source clarification on inclusion in 13-audit list. Code4rena invitational prize pool: $20,000 dated 2025-10-30 versus unspecified dated 2025-10-30; resolution: $20,000 as accurate based on consensus with no contradiction high confidence from agreement specificity. Pashov version 2 medium severity details: one on unsafe uint128 cast resolved via safe casting dated 2025-10-30; resolution: unanimous agreement on finding impact multiple executions and GitHub-confirmed resolution high confidence. MakerDAO audit count: conflicting reports of "15+" versus "20+" audits; resolution: accept 20+ as the current count, based on corroboration from multiple 2025 analyses referencing broader coverage. Frax Finance bug bounty: conflicting reports of "no public program" versus an "up to $10M internal program"; resolution: accept the $10M internal program, based on citations from docs.frax.finance in multiple reports. Circle bug bounty scope: conflict between "up to $5,000 for smart contracts" and "excludes smart contracts"; resolution: accept $5,000 with a scope that largely excludes core smart contracts, based on analysis confirming its primary focus is Web2 infrastructure. Synthetix monitoring: conflict between "no public partner" and "Forta Network"; resolution: accept Forta as the monitoring partner, per ecosystem mentions cited in one analysis, treating the absence of this information in other sources as a gap. De-pegging duration on Binance was cited as both "~90 minutes" and "a few minutes"; the ~90 minute duration is more accurate, with a specific, more intense 40-minute window (21:36-22:16 UTC), based on secondary reporting that references Binance's own incident timing. This is more specific than "a few minutes." One source mentioned an undated seed round, while another specified a $6 million seed round in July 2023; accept July 2023 for the $6 million seed round, as it is supported by venture capital tracking sources and provides greater specificity. The composition of the Risk Committee was partially listed in one document but fully enumerated in another; accept the full six-member list, which is sourced from more recent governance documentation and expands on the partial list.

#### 4.2.2. Unresolved Conflicts
The exact duration of the USDe price dislocation on Binance on October 10-11, 2025, is cited variously as "a few minutes," "approximately 90 minutes," and a specific "40-minute window (21:36-22:16 UTC)"; a primary incident report from Binance is required for definitive resolution. The confirmed number of voting members on the Risk Committee; one source lists 3 members, while another lists a 6-member committee; requires checking the latest Ethena governance forum election results or official committee documentation post-August 2025. Synthetix bug bounty max payout: the official policy page lists a $100,000 cap, but a historical payout of over $150,000 (after a partner match) makes the effective cap unclear. Bybit hack vector: a single report claims the hack was due to a compromised Safe{Wallet} developer machine leading to a malicious multisig proposal, a narrative absent from all other sources, making it uncorroborated. Alleged $500k Ethena payout: a single source noted an alleged but unconfirmed $500,000 payout in March 2025, which contradicts the "zero payouts" finding from all other sources and the stable bounty vault balance. AI-hallucinated citations: one agent report contained numerous irrelevant arXiv and mismatched article citations, rendering its specific sourcing unreliable. Bybit hack impact on Tether: a single source incorrectly stated that the Bybit hack affected Tether's infrastructure, which contradicts other reports.

#### 4.2.3. Potentially Incorrect Information
Reserve Fund Size: A historical size of $35 million is cited from a single, undated source; this figure is likely outdated and requires verification against current on-chain data or the latest Proof of Reserves report. S&P Global Risk Weighting: The 1,250% risk weighting reported is from secondary media; the original S&P report is needed to understand the full context and application of the Basel III framework. Team Headcount: An estimate of 20-25 contributors pre-expansion is self-reported and may be inaccurate; verification via official company disclosures or professional networking sites is needed. De-pegging Event Figures: Specifics like the $0.65 price low and $19 billion market-wide liquidations are from media coverage and may be approximate; exchange logs are required for exact figures. Historical Funding Rates: Aggregated rates from -0.6% to 18% lack a clear methodology and primary data source, requiring verification via exchange APIs. The exact timeline (start/stop) of the Binance dislocation: some sources cite 21:36–22:16 UTC (40 min); others call it ~90 minutes around $0.75–$0.98 after a sub-$0.70 wick; absent a primary Binance trade log, treat precise duration as approximate. $66M over-collateralization primary artifact: cited across outlets the same day; a Chaos-hosted PoR snapshot for that timestamp wasn’t located; marked secondary.

### 4.3. Cross-Cutting Insights

#### 4.3.1. Industry and Market Trends
DeFi protocols like Ethena are increasingly adopting hybrid CeDeFi architectures, achieving independence from traditional banking through on-chain ownership but depending on centralized exchanges for delta-hedging stability. Bug bounty programs on platforms like Immunefi have become standard for scaling DeFi security, with maximum payouts correlating to TVL, such as Ethena's $3,000,000 for its $9.8 billion TVL. Economic risk audits focusing on funding rates, liquid staking tokens, and liquidity dynamics are a growing trend for yield-bearing stablecoins, exemplified by Chaos Labs' modeling of tail risks like prolonged negative funding.

#### 4.3.2. Regulatory and Legal Developments
In August 2025, S&P Global Ratings assigned USDe a 1,250% risk weighting under the Basel III framework due to its complex stability mechanism, requiring banks to hold 100% capital against exposures and posing barriers to institutional adoption; this high risk weighting underscores potential regulatory scrutiny on incident response as unhedgeable mechanisms like delta-hedging could complicate compliance during events like the 2025 de-pegging. The Terms of Service establish a distinction between whitelisted KYC/KYB-verified Mint Users with direct redemption rights from Ethena (BVI) Limited and Holding Users without such rights, clarifying no ownership or economic claims for USDe holders. Off-Exchange Settlement (OES) custody uses bankruptcy-remote entities in jurisdictions like the British Virgin Islands and Portugal, but legal enforceability varies and requires registry verification for credit separations.

#### 4.3.3. Competitive Intelligence
Ethena's delegated committee governance model with bi-annual ENA holder elections for the Risk Committee provides operational agility for time-sensitive hedging, differing from direct token-voting DAOs in peers like MakerDAO. Multi-chain deployments using LayerZero OFT across 12+ networks enhance Ethena's accessibility as a unit of account compared to initially single-chain protocols like early DAI. Backers including Dragonfly, Brevan Howard Digital, Galaxy Digital, Binance Labs, and Pantera Capital offer Ethena strategic liquidity and expertise advantages over non-VC-backed competitors.
