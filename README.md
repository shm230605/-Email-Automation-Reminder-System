# 🚀 SmartMail Pro — Email Automation & Scheduling Platform

Professional Email Automation and Scheduling Platform built with Python and Streamlit. 
It supports real SMTP email sending, contact management, scheduling, smart business routing, and a modern dashboard interface.

---

# ✨ Features

## 📧 Real Email Sending
- Gmail SMTP integration
- Real inbox delivery
- Secure App Password authentication

## 👥 Contact Management
- Add contacts
- Delete contacts
- Store recipient database

## 📤 Instant Email Sender
- Send emails instantly
- Professional email interface

## ⏰ Email Scheduler
- Schedule emails
- Set date & time
- AM/PM support
- Re-send scheduled emails
- Delete scheduled emails

## 🧠 Smart Business Mail
Automatically classifies emails:
- Finance
- Marketing
- Meeting
- General

## 📊 Professional Dashboard
- Modern Streamlit UI
- Metrics cards
- SaaS-like layout

---

# 🖥️ Tech Stack
```
| Technology |         Usage         |
|------------|-----------------------|
|   Python   |      Core Backend     |
|  Streamlit |      Dashboard UI     |
|   Pandas   |      Data Handling    |
|    SMTP    |    Real Email Sending |
|   dotenv   | Environment Variables |
```
---

# 📁 Project Structure

```
Email-Automation-System/
│
├── app_streamlit.py                # Main professional Streamlit dashboard
├── email_engine.py                 # Real SMTP email sender
├── utils_streamlit.py              # CSV utility/helper functions
├── run.bat                         # One-click launcher
├── requirements.txt                # Python dependencies
├── README.md                       # Professional documentation
├── .gitignore                      # Git ignore rules
├── .env                            # Gmail credentials (PRIVATE)
│
├── data/
│   ├── contacts.csv                # Saved contacts
│   └── schedule.csv                # Scheduled emails
│
├── assets/                         # Optional logos/images/icons
│
├── backend/                        
│   ├── main.py
│   ├── api.py
│   └── __pycache__/
│
├── core/                           
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── __pycache__/
│
├── dashboard/                      
│   ├── app.py
│   └── __pycache__/
│
├── worker/                         
│   ├── worker.py
│   └── __pycache__/
│
├── venv/                           # Virtual environment
│
└── __pycache__/
```

---


# 🚀 Future Improvements

- Background Scheduler
- Email Tracking
- Open Rate Analytics
- Login Authentication
- Cloud Deployment
- AI Email Generator

---

# 👨‍💻 Author

Shresthaa Maiti