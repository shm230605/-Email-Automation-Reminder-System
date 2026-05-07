from sqlalchemy import Column, String, Boolean
from core.database import Base
import uuid

def gen_id():
    return str(uuid.uuid4())

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(String, primary_key=True, default=gen_id)
    name = Column(String)
    email = Column(String, unique=True)
    active = Column(Boolean, default=True)

class Template(Base):
    __tablename__ = "templates"
    id = Column(String, primary_key=True, default=gen_id)
    name = Column(String)
    subject = Column(String)
    body = Column(String)