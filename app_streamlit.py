import streamlit as st
import pandas as pd
import os
import uuid
from datetime import datetime

from email_engine import send_email
from utils_streamlit import load_csv, save_csv

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="SmartMail Pro - Email Automation Suite",
    page_icon="📧",
    layout="wide"
)

# =========================
# HEADER
# =========================

st.title("🚀 SmartMail Pro – Email Automation & Scheduling Suite")
st.caption("Professional SMTP-Based Email Automation Dashboard")

# =========================
# FILE SETUP
# =========================

os.makedirs("data", exist_ok=True)

CONTACT_FILE = "data/contacts.csv"
SCHEDULE_FILE = "data/schedule.csv"

# init CSV files safely
if not os.path.exists(CONTACT_FILE):
    pd.DataFrame(columns=["id", "name", "email"]).to_csv(CONTACT_FILE, index=False)

if not os.path.exists(SCHEDULE_FILE):
    pd.DataFrame(columns=["id", "email", "subject", "body", "datetime", "status"]).to_csv(SCHEDULE_FILE, index=False)

contacts = load_csv(CONTACT_FILE, ["id", "name", "email"])
schedules = load_csv(SCHEDULE_FILE, ["id", "email", "subject", "body", "datetime", "status"])

# =========================
# SIDEBAR MENU
# =========================

menu = st.sidebar.radio(
    "📌 Navigation",
    ["Dashboard", "Contacts", "Send Email", "Schedule Email", "Business Smart Mail"]
)

# =========================
# DASHBOARD
# =========================

if menu == "Dashboard":

    st.markdown("## 📊 System Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("👥 Total Contacts", len(contacts))

    with col2:
        st.metric("⏰ Scheduled Emails", len(schedules))

    st.success("✔ SMTP Email Engine Active")

# =========================
# CONTACTS (WITH DELETE)
# =========================

elif menu == "Contacts":

    st.markdown("## 👥 Contact Management")

    name = st.text_input("Full Name")
    email = st.text_input("Email Address")

    if st.button("➕ Add Contact", use_container_width=True):

        if name and email:

            new = pd.DataFrame([{
                "id": str(uuid.uuid4()),
                "name": name,
                "email": email
            }])

            contacts = pd.concat([contacts, new], ignore_index=True)
            save_csv(CONTACT_FILE, contacts)

            st.success("Contact Added")
            st.rerun()

    st.divider()

    st.markdown("### 📋 Contact List")

    for i, row in contacts.iterrows():

        col1, col2 = st.columns([4, 1])

        with col1:
            st.write(f"👤 {row['name']} — {row['email']}")

        with col2:
            if st.button("🗑 Delete", key=f"del_{row['id']}"):

                contacts = contacts[contacts["id"] != row["id"]]
                save_csv(CONTACT_FILE, contacts)

                st.warning("Contact Deleted")
                st.rerun()

# =========================
# SEND EMAIL
# =========================

elif menu == "Send Email":

    st.markdown("## 📤 Send Email (Instant Mode)")

    selected = st.selectbox(
        "Select Recipient",
        contacts["name"] + " <" + contacts["email"] + ">"
    )

    subject = st.text_input("📌 Subject")
    body = st.text_area("📧 Email Body")

    if st.button("🚀 Send Email", use_container_width=True):

        email = selected.split("<")[1].replace(">", "")

        result = send_email(email, subject, body)

        st.success("Email Sent")
        st.json(result)

# =========================
# SCHEDULE EMAIL (FULL CONTROL)
# =========================

elif menu == "Schedule Email":

    st.markdown("## ⏰ Email Scheduler")

    selected = st.selectbox(
        "Select Recipient",
        contacts["name"] + " <" + contacts["email"] + ">"
    )

    subject = st.text_input("📌 Subject")
    body = st.text_area("📧 Email Body")

    col1, col2 = st.columns(2)

    with col1:
        date = st.date_input("📅 Date")

    with col2:
        time = st.time_input("⏰ Time")

    am_pm = st.radio("AM / PM", ["AM", "PM"], horizontal=True)

    email = selected.split("<")[1].replace(">", "")

    # =========================
    # ADD SCHEDULE
    # =========================

    if st.button("➕ Schedule Email", use_container_width=True):

        schedule_time = f"{date} {time} {am_pm}"

        new = pd.DataFrame([{
            "id": str(uuid.uuid4()),
            "email": email,
            "subject": subject,
            "body": body,
            "datetime": schedule_time,
            "status": "PENDING"
        }])

        schedules = pd.concat([schedules, new], ignore_index=True)
        save_csv(SCHEDULE_FILE, schedules)

        st.success("Email Scheduled")
        st.rerun()

    st.divider()

    st.markdown("### 📋 Scheduled Emails")

    # =========================
    # LIST + RESEND + DELETE
    # =========================

    for i, row in schedules.iterrows():

        with st.container(border=True):

            st.write(f"📧 To: {row['email']}")
            st.write(f"📌 Subject: {row['subject']}")
            st.write(f"⏰ Time: {row['datetime']}")
            st.write(f"📊 Status: {row['status']}")

            col1, col2 = st.columns(2)

            # RESEND
            with col1:
                if st.button("🔁 Resend", key=f"resend_{row['id']}"):

                    result = send_email(
                        row["email"],
                        row["subject"],
                        row["body"]
                    )

                    st.success("Email Resent")
                    st.json(result)

            # DELETE
            with col2:
                if st.button("🗑 Delete", key=f"delete_{row['id']}"):

                    schedules = schedules[schedules["id"] != row["id"]]
                    save_csv(SCHEDULE_FILE, schedules)

                    st.warning("Deleted")
                    st.rerun()

# =========================
# SMART BUSINESS MAIL
# =========================

elif menu == "Business Smart Mail":

    st.markdown("## 🧠 Smart Email Router")

    st.info("Auto detects email type and sends instantly")

    email = st.text_input("Recipient Email")
    subject = st.text_input("Subject")
    body = st.text_area("Body")

    def classify(text):

        text = text.lower()

        if "invoice" in text or "payment" in text:
            return "Finance"
        elif "meeting" in text:
            return "Meeting"
        elif "offer" in text:
            return "Marketing"
        else:
            return "General"

    if st.button("Send Smart Email"):

        category = classify(subject + body)

        result = send_email(email, subject, body)

        st.success(f"Type: {category}")
        st.json(result)