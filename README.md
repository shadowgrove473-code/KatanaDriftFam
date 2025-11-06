 python -m venv .venv
 Windows: .venv\Scripts\activate
 Linux/macOS: source .venv/bin/activate


 pip install -r requirements.txt


 uvicorn app.main:app --reload --port 8000

 http://127.0.0.1:8000
