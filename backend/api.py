from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter()

# -------------------
# MODELS
# -------------------

class Contact(BaseModel):
    name: str
    email: EmailStr

class Template(BaseModel):
    name: str
    subject: str
    body: str


# -------------------
# STORAGE (temporary)
# -------------------
contacts = []
templates = []


# -------------------
# ROUTES
# -------------------

@router.get("/")
def home():
    return {"message": "API running"}

@router.post("/contact")
def add_contact(c: Contact):
    contacts.append(c.dict())
    return {"message": "contact saved", "data": c}

@router.post("/template")
def add_template(t: Template):
    templates.append(t.dict())
    return {"message": "template saved", "data": t}

@router.get("/contact")
def get_contacts():
    return contacts

@router.get("/template")
def get_templates():
    return templates