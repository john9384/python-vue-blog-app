from flask_login import UserMixin
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(120))
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def to_dict(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'username': self.username,
            'password': self.password,
        }

    def __repr__(self):
        return f"User('{self.firstname}', '{self.lastname}', '{self.email}', '{self.username}')"

    # Flask-Login required methods
    def get_id(self):
        return str(self.id)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
