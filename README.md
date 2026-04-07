# 🚛 Profleet Backend

A production-ready backend system for managing trucks, trips, and logistics operations, built with FastAPI and powered by Supabase (PostgreSQL).

## 🚀 Features
- Truck Management (CRUD)
- Trip / Booking Management
- Expense & Revenue Tracking
- Driver & Agent Management
- Consignor & Consignee Management
- File Upload Support

## 🏗️ Tech Stack
- FastAPI
- Supabase (PostgreSQL)
- SQLAlchemy / SQLModel
- Pydantic

## ⚙️ Setup

```bash
git clone https://github.com/your-username/profleet_backend.git
cd profleet_backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create .env:

```
DATABASE_URL=your_database_url
SUPABASE_URL=your_url
SUPABASE_KEY=your_key
```

Run:

```bash
uvicorn main:app --reload
```

## 📖 API Docs
- http://127.0.0.1:8000/docs

## 👨‍💻 Author
Mitesh Tiwary
