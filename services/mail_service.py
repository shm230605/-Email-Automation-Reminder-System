import aiosmtplib
from email.message import EmailMessage
from backend.config import settings

class MailService:

    async def send_email(self, to_email, subject, body):
        
        if settings.DRY_RUN:
            print(f"[DRY RUN] To: {to_email} | Subject: {subject}")
            return True

        msg = EmailMessage()
        msg["From"] = settings.SMTP_USER
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.set_content(body, subtype="html")

        try:
            smtp = aiosmtplib.SMTP(
                hostname=settings.SMTP_HOST,
                port=settings.SMTP_PORT,
                use_tls=True
            )

            await smtp.connect()
            await smtp.login(settings.SMTP_USER, settings.SMTP_PASS)
            await smtp.send_message(msg)
            await smtp.quit()

            return True

        except Exception as e:
            print("EMAIL ERROR:", e)
            return False