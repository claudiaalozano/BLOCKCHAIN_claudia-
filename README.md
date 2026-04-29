# Blockchain Dashboard Project

<!-- student-repo-auditor:teacher-feedback:start -->
## Teacher Feedback

### Kick-off Review

Review time: 2026-04-29 20:44 CEST
Status: Green

Strength:
- I can see the dashboard structure integrating the checkpoint modules.

Improve now:
- The checkpoint evidence is strong: the dashboard and core modules are visibly progressing.

Next step:
- Keep building on this checkpoint and prepare the final AI integration.
<!-- student-repo-auditor:teacher-feedback:end -->

Use this repository to build your blockchain dashboard project.
Update this README every week.

## Student Information

| Field | Value |
|---|---|
| Student Name | CLAUDIA LOZANO |
| GitHub Username | claudiaalozano |
| Project Title | CryptoChain Analyzer Dashboard |
| Chosen AI Approach | Anomaly detector for abnormal inter-block times |

## Repository Structure

- `app.py` — dashboard entry point
- `api/` — blockchain API connection code
- `modules/` — project modules
- `requirements.txt` — Python dependencies

## Module Tracking

Use one of these values: `Not started`, `In progress`, `Done`

| Module | What it should include | Status |
|---|---|---|
| M1 | Proof of Work Monitor | Done |
| M2 | Block Header Analyzer | Done |
| M3 | Difficulty History | Done |
| M4 | AI Component | In progress |

## Current Progress

- Implemented M1 with live Bitcoin mining metrics, including difficulty, leading zero bits, estimated hash rate, and recent block-time analysis.
- Implemented M2 to reconstruct the 80-byte block header and verify Proof of Work locally using double SHA-256.
- Implemented M3 to analyse Bitcoin difficulty adjustment periods and compare actual block times against the 600-second target.
- Defined the M4 AI approach as an anomaly detector for unusual Bitcoin inter-block times.
- Tested the Streamlit dashboard and confirmed that M1, M2, M3, and the M4 skeleton are visible in the app.

## Next Step

- Implement anomaly scoring in M4 and display flagged unusual block intervals in a chart and table.

## Main Problem or Blocker

- The main remaining task is to turn the M4 anomaly detector from a planned skeleton into a working AI analysis module.

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
