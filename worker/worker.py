import asyncio
from core.database import SessionLocal
from core.models import Contact, Template
from services.mail_service import MailService
from services.template_engine import render

mail = MailService()

async def run_worker():

    while True:
        db = SessionLocal()

        contacts = db.query(Contact).all()
        template = db.query(Template).first()

        if template:

            for c in contacts:
                subject, body = render(
                    template.subject,
                    template.body,
                    {"name": c.name}
                )

                await mail.send_email(c.email, subject, body)

        db.close()
        await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(run_worker())