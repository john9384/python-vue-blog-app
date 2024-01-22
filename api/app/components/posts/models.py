# app/posts/models.py

from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer)
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
