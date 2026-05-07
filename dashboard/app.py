import streamlit as st
import requests

API = "http://127.0.0.1:8000"

st.title("Email Automation System")

# -------------------
# HEALTH CHECK FIRST
# -------------------
try:
    r = requests.get(API + "/health", timeout=3)
    backend_ok = True
except:
    backend_ok = False

if not backend_ok:
    st.error("❌ Backend is NOT running. Start FastAPI first.")
    st.stop()


# -------------------
# CONTACT
# -------------------
st.header("Add Contact")

name = st.text_input("Name")
email = st.text_input("Email")

if st.button("Add Contact"):
    res = requests.post(API + "/contact", json={"name": name, "email": email})
    st.success(res.json())


# -------------------
# TEMPLATE
# -------------------
st.header("Add Template")

tname = st.text_input("Template Name")
subject = st.text_input("Subject")
body = st.text_area("Body")

if st.button("Add Template"):
    res = requests.post(API + "/template", json={
        "name": tname,
        "subject": subject,
        "body": body
    })
    st.success(res.json())