from app import db
import uuid

class Post(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()), unique=True, nullable=False)
    creator_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    image = db.Column(db.String(100))

    def to_dict(self):
        return {
            'id': self.id,
            'creator_id': self.creator_id,
            'title': self.title,
            'content': self.content,
            'image': self.image,
        }
