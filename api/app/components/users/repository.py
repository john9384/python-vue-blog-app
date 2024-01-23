from app.database.base_repository import BaseRepository
from app.components.users.models import User

class UserRepository(BaseRepository):
  pass

user_repository = UserRepository(User)