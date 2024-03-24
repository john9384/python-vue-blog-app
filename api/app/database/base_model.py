from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
import uuid
from app import db

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(String(150), primary_key=True, default=str(uuid.uuid4()), unique=True, nullable=False)

    created_at = Column(db.DateTime(timezone=True), default=db.func.now())
    updated_at = Column(db.DateTime(timezone=True), onupdate=db.func.now(), default=db.func.now())
    def __repr__(self):
      pass

