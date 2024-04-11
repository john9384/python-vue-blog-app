
class PostPresenter:
  def __init__(self, post):
    self.post = post

  def serialize(self):
    return {
      'id': self.post.id,
      'creator_id': self.post.creator_id,
      'title': self.post.title,
      'content': self.post.content,
      'image': self.post.image,
    }