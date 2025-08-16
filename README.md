Smartawreed Demo - Simple Package
--------------------------------
Structure:
- backend/: FastAPI app (main.py) + Products.xlsx sample
- frontend/: Streamlit app (app.py) + landing.html

Quick local run:
1) Backend:
   cd backend
   pip install -r requirements.txt
   uvicorn main:app --reload --port 8000

2) Frontend:
   cd frontend
   pip install -r requirements.txt
   streamlit run app.py

In Streamlit sidebar set API URL: http://127.0.0.1:8000
