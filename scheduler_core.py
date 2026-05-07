import time
from email_engine import send_email

# =========================
# SIMPLE SCHEDULER ENGINE
# =========================

def run_scheduler(df):

    logs = []

    for _, row in df.iterrows():

        time.sleep(1)  # simulate delay (real-world queue behavior)

        result = send_email(
            row["email"],
            row["subject"],
            row["body"]
        )

        logs.append({
            "email": row["email"],
            "status": result["status"]
        })

    return logs