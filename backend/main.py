from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

app = FastAPI(title="Smartawreed Demo API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_FILE = os.path.join(os.path.dirname(__file__), "Products.xlsx")

def load_products():
    if os.path.exists(DATA_FILE):
        return pd.read_excel(DATA_FILE)
    return pd.DataFrame([])

@app.get("/healthz")
def healthz():
    return {"status":"ok"}

@app.get("/")
def root():
    return {"message":"Smartawreed Demo API"}

@app.get("/products")
def get_products(q: str | None = Query(None), category: str | None = Query(None)):
    df = load_products()
    if df.empty:
        raise HTTPException(status_code=404, detail="No products available")
    if q:
        df = df[df['product_name'].astype(str).str.contains(q, case=False, na=False)]
    if category:
        df = df[df['category'] == category]
    return df.to_dict(orient="records")
