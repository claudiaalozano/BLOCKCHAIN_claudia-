# Blockchain Dashboard Project

<!-- student-repo-auditor:teacher-feedback:start -->
## Teacher Feedback

### Kick-off Review

Review time: 2026-04-16 09:59 CEST
Status: Red

Strength:
- I can see more than one commit in your repository.

Improve now:
- The repository is missing part of the expected classroom structure.

Next step:
- Restore the expected template files and folders before continuing.
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
| M1 | Proof of Work Monitor | In progress |
| M2 | Block Header Analyzer | Not started |
| M3 | Difficulty History | Not started |
| M4 | AI Component | Not started |

## Current Progress

Write 3 to 5 short lines about what you have already done.

- Accepted the GitHub Classroom repository and updated the README.
- Connected the project to a public blockchain API and fetched real Bitcoin block data.
- Retrieved and displayed the latest block height, hash, bits, nonce, and transaction count.
- Ran the Streamlit app and tested the M1 module interface.

## Next Step

Write the next small step you will do before the next class.

- Improve M1 to show the latest block data more clearly and start the Block Header Analyzer module.

## Main Problem or Blocker

Write here if you are stuck with something.

- Need to calculate difficulty correctly from the available API fields and understand the block header structure.

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```
