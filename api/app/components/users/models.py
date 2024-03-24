from app import db
from app.database.base_model import BaseModel

class User(BaseModel):
    __tablename__ = 'users'
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(1000))

    def __repr__(self):
        return f"User '{self.id}"

