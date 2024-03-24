from app import db
from app.database.base_model import BaseModel

class Post(BaseModel):
    __tablename__ = 'posts'
    creator_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    image = db.Column(db.String(100))

    def __repr__(self):
        return f"Post '{self.id}"