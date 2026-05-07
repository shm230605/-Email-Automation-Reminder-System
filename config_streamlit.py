import os

# =========================
# EMAIL CONFIG
# =========================

EMAIL_MODE = "DRY_RUN"   # change to "LIVE" when ready

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL_USER = os.getenv("EMAIL_USER", "your_email@gmail.com")
EMAIL_PASS = os.getenv("EMAIL_PASS", "your_app_password")

# =========================
# APP SETTINGS
# =========================

APP_NAME = "Email Automation System"
TIMEZONE = "Asia/Kolkata"