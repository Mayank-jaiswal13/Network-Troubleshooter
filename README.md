# NetSage AI

An explainable troubleshooting dashboard for Cisco-style Packet Tracer labs. NetSage turns network symptoms and command output into a structured diagnosis, suggested verification command, and practical next steps.

## Features

- 32 sample troubleshooting scenarios across routing, VLANs, DHCP, DNS, ACLs, NAT, wireless, and more
- Rule-based diagnosis with visible evidence and recommended checks
- Deterministic checks for common network configuration issues
- A responsive Flask dashboard with severity and issue summaries
- Human review guidance for validating every suggested fix

> NetSage is an educational decision-support demo. Its diagnosis logic is rule-based and should not be treated as an authoritative production network configuration.

## Quick start

Requires Python 3.10 or newer.

```bash
python -m venv .venv
```

Activate the environment:

```powershell
.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Install the app dependencies and start Flask:

```bash
pip install -r requirements.txt
python app.py
```

Open [http://localhost:5000](http://localhost:5000).

## Diagnose a network issue

1. Select a matching symptom or describe a different one.
2. Paste relevant Cisco `show` command output.
3. Review the suggested root cause, evidence, and next command.
4. Verify the recommendation in Packet Tracer or with a network administrator before changing a configuration.

## Project layout

```text
NetSageAI/
├── app.py                 # Flask routes and diagnosis flow
├── dashboard.py           # Summary statistics from the case catalog
├── rule_checker.py        # Deterministic configuration checks
├── cases.csv              # Sample troubleshooting cases
├── requirements.txt       # Runtime dependencies
├── requirements-research.txt # Optional research and document packages
├── static/
│   └── style.css
└── templates/
    └── index.html
```

## Deployment

The Flask application is compatible with Vercel's Python runtime. Import this repository into Vercel and use the repository root as the project root. Vercel will install the packages in `requirements.txt` and detect `app.py` as the Flask entry point.

## Data and privacy

The included case catalog is sample data. The app does not persist submitted symptoms or command output. Avoid pasting credentials, secrets, or sensitive production network details into a public demo.

## License

No license has been added yet. Contact the repository owner before reusing this project.
