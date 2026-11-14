# python-backend

Project **orchid** · Python / FastAPI · created by Backstage.

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
pytest                      # tests
uvicorn app.main:app --reload --port 8080   # http://localhost:8080/health
```

CI (`.github/workflows/ci.yml`) runs on every push and pull request; images go to
`ghcr.io/everesto-inc/python-backend` (linux/arm64).
