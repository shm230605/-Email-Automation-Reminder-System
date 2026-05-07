@echo off

cd /d I:\Email-Automation-System

call venv\Scripts\activate

start http://localhost:8501

streamlit run app_streamlit.py