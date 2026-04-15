# Blockchain Dashboard Project

Use this repository to build your blockchain dashboard project.
Update this README every week.

## Student Information

| Field | Value |
|---|---|
| Student Name | CLAUDIA LOZANO |
| GitHub Username | claudiaalozano |
| Project Title | CryptoChain Analyzer Dashboard |
| Chosen AI Approach | Anomaly detector for abnormal inter-block times |

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

- Accepted the GitHub Classroom repository and reviewed the project structure.
- Read the project requirements and identified the four required modules.
- Started updating the README with the project plan and module status.
- Preparing the first API connection to retrieve live Bitcoin block data.

## Next Step

Write the next small step you will do before the next class.

- Create the first Python script in `api/blockchain_client.py` to fetch the latest Bitcoin block data.

## Main Problem or Blocker

Write here if you are stuck with something.

- Need to understand the API endpoints and how to parse the block fields correctly.

```md
## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```
## Project Structure 

template-blockchain-dashboard/
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- app.py
|-- api/
|   `-- blockchain_client.py
`-- modules/
    |-- m1_pow_monitor.py
    |-- m2_block_header.py
    |-- m3_difficulty_history.py
    `-- m4_ai_component.py