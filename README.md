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
- `report/` — final PDF report

## Module Tracking

Use one of these values: `Not started`, `In progress`, `Done`

| Module | What it should include | Status |
|---|---|---|
| M1 | Proof of Work Monitor | Done |
| M2 | Block Header Analyzer | Done |
| M3 | Difficulty History | Done |
| M4 | AI Component | Done |

## Current Progress

- Implemented M1 with live Bitcoin mining metrics, including difficulty, leading zero bits, estimated hash rate, target interpretation, and recent block-time analysis.
- Implemented M2 to reconstruct the 80-byte Bitcoin block header and verify Proof of Work locally using double SHA-256.
- Implemented M3 to analyse real Bitcoin difficulty adjustment periods and compare actual block times against the 600-second protocol target.
- Implemented M4 as an anomaly detector for unusual Bitcoin inter-block times using z-scores and visualised the anomalous intervals in the dashboard.
- Improved the Streamlit interface with a cleaner layout, overview page, styled metrics, and more polished charts.


## Main Problem or Blocker

- The main remaining task is completing the final written report and checking that the whole project is ready for submission.

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py