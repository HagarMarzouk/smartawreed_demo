# 🌟 SmartAwreed Demo Platform

SmartAwreed is a **digital distribution and payments platform** that connects suppliers, retailers, and small businesses in emerging markets.  
This demo project showcases the **core features** of SmartAwreed with a professional prototype for investors and competitions.

---

## 📌 Features

- **Supplier & Retailer Dashboards** – Easy onboarding and profile management  
- **Inventory Management** – Add, edit, and track products in real time  
- **Order Management** – Retailers can place orders; suppliers can confirm or reject  
- **Payment Integration (Demo)** – Simulated flow for digital payments  
- **Analytics Dashboard** – Sales & orders statistics (mock data for demo)  
- **Scalable Architecture** – Backend (FastAPI) + Frontend (Streamlit)

---

## 🏗️ Project Structure

smartawreed_demo/
│── backend/ # FastAPI backend (APIs for suppliers, retailers, orders)
│ ├── main.py
│ ├── models.py
│ ├── database.py
│ └── requirements.txt
│
│── frontend/ # Streamlit frontend (UI for suppliers & retailers)
│ ├── app.py
│ └── requirements.txt
│
│── README.md # Project documentation




---

## ⚡ Quick Start (Run Locally)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/smartawreed_demo.git
cd smartawreed_demo


###  2️⃣ Start the Backend (FastAPI)
cd backend
pip install -r requirements.txt
uvicorn main:app --reload



Backend will run at 👉 http://127.0.0.1:8000

Docs available at: http://127.0.0.1:8000/docs

### 3️⃣ Start the Frontend (Streamlit)

Open a new terminal:
cd frontend
pip install -r requirements.txt
streamlit run app.py


cd frontend
pip install -r requirements.txt
streamlit run app.py


Frontend will run at 👉 http://localhost:8501

🌍 Deployment (Demo)

For investor demos, you can deploy quickly:

Backend → Render or Railway (free tier)

Frontend → Streamlit Community Cloud (1-click deploy)

📊 Sample Accounts

Supplier
Username: supplier1
Password: password123

Retailer
Username: retailer1
Password: password123

🧭 Roadmap

Multi-language support (Arabic + English)

Mobile app version (React Native)

Real payment integration (Vodafone Cash, Fawry, Stripe)

AI-powered demand forecasting

👨‍💻 Tech Stack

Backend: FastAPI, SQLite

Frontend: Streamlit

Language: Python 3.10

Deployment: Streamlit Cloud + Render

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

📧 Contact

For questions, partnership, or investment opportunities:
Your Name – Founder, SmartAwreed
✉️ Email: your_email@example.com
🌐 Website: (coming soon)

✨ This is a demo project for competition & investor presentation purposes. The live platform will include advanced integrations and scalability features.













