from app.database.base_model import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey, Text

class Post(BaseModel):
    __tablename__ = 'posts'
    creator_id = Column(String(150), nullable=False)
    title = Column(String(100), nullable=False)
    content = Column(String(Text), nullable=False)  
    image = Column(String(500), nullable=False)

    def __repr__(self):
        return f"Post '{self.id}" 