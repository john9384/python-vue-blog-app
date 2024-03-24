
from app import db
import uuid

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()), unique=True, nullable=False)

    def __repr__(self):
      pass

    # Flask-Login required methods
    def get_id(self):
        return str(self.id)

