# Azure Functions - simple calc APIs

This repository provides two HTTP Azure Functions endpoints (GET): `/api/mul` and `/api/div`.

Quick notes:
- Runtime: Python 3.11
- Plan: Consumption
- Region: East Japan (to be set during deployment)

Local run:

1. Install Azure Functions Core Tools and Python 3.11.
2. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

3. Run locally:

```bash
func start
```

GitHub Actions deployment:
- Set the following repository secrets:
  - `FUNCTION_APP_NAME` — your Function App name
  - `FUNCTION_PUBLISH_PROFILE` — publish profile XML content (or use Azure credentials)
- Push to `main` to trigger CI/CD.

Do not commit `local.settings.json` (it's ignored by `.funcignore`).
