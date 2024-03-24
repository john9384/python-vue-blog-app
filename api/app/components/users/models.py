from app.database.base_model import BaseModel
from sqlalchemy import Column, String, DateTime

class User(BaseModel):
    __tablename__ = 'users'
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(1000), nullable=False)
    is_active = Column(DateTime, default=False)

    def __repr__(self):
        return f"User '{self.id}" 

