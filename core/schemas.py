from pydantic import BaseModel, EmailStr

class ContactSchema(BaseModel):
    name: str
    email: EmailStr

class TemplateSchema(BaseModel):
    name: str
    subject: str
    body: str