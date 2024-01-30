from app.database.base_repository import BaseRepository
from app.components.posts.models import Post

class PostRepository(BaseRepository):
  def __init__(self, _model):
    self._model = _model
    super().__init__(_model)

post_repository = PostRepository(Post)