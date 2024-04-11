from app.components.posts.repository import post_repository
from app.components.posts.presenter import PostPresenter

class PostService:
  def create(self, creator_id, data):
    payload = {
      'creator_id': creator_id,
      'title': data.get('title'),
      'content': data.get('content'),
      'image': data.get('image'),
    }

    post = post_repository.create(payload)
    return PostPresenter(post).serialize()

  def read(self, query):
    post = post_repository.find_one(query)
    if post is None:
      return None
    
    return PostPresenter(post).serialize()
  
  def read_many(self, query):
    posts = post_repository.find_all(query)
    return [PostPresenter(post).serialize for post in posts]

  def update(self, query, data):
    post = post_repository.find_one(query)
    if post is None:
      raise Exception('Post not found')

    if post.creator_id != query['creator_id']:
      raise Exception('You are not authorized to update this post')

    payload = {
      'title': data.get('title'),
      'content': data.get('content'),
      'image': data.get('image'),
    }

    post = post_repository.update(query, payload)   

    return PostPresenter(post).serialize()

  def delete(self, query):
    post = post_repository.find_one(query)
    if post is None:
      raise Exception('Post not found')

    if post.creator_id != query['creator_id']:
      raise Exception('You are not authorized to update this post')
      
    post = post_repository.delete(query)   

    return PostPresenter(post).serialize()