import streamlit as st
import requests

st.set_page_config(page_title="Smartawreed Demo", layout="wide")
st.title("🧠 Smartawreed – Demo (Streamlit)")
st.caption("كتالوج منتجات (من FastAPI)")

API_URL = st.sidebar.text_input("API URL (e.g. http://127.0.0.1:8000)", value="http://127.0.0.1:8000")

if not API_URL:
    st.error("Please set API URL in the sidebar.")
else:
    try:
        r = requests.get(f"{API_URL}/products", timeout=10)
        r.raise_for_status()
        products = r.json()
    except Exception as e:
        st.error(f"Failed to load products: {e}")
        products = []

    if products:
        for p in products:
            with st.container():
                st.subheader(p.get("product_name"))
                cols = st.columns([1,3])
                with cols[1]:
                    st.write(f"**SKU:** {p.get('sku')}  •  **Category:** {p.get('category')}")
                    st.write(f"**Price (EGP):** {p.get('unit_price_egp')}")
                    st.write(f"**Lead time (days):** {p.get('lead_time_days')}")
                    st.button("Add to cart", key=p.get('product_id'))
    else:
        st.info("No products to show.")
