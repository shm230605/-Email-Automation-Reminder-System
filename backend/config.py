import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SMTP_HOST = os.getenv("SMTP_HOST")
    SMTP_PORT = int(os.getenv("SMTP_PORT"))
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_PASS = os.getenv("SMTP_PASS")
    DRY_RUN = os.getenv("DRY_RUN", "True") == "True"

settings = Settings()