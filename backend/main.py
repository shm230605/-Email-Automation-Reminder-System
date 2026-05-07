from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from utils.mailer import send_email

app = FastAPI()

class EmailRequest(BaseModel):
    email: EmailStr
    subject: str
    message: str


@app.post("/send-email")
def send(req: EmailRequest):
    success, msg = send_email(req.email, req.subject, req.message)
    return {"success": success, "message": msg}