from werkzeug.security import generate_password_hash, check_password_hash
from app.components.users.repository import user_repository
from app.components.users.presenter import UserPresenter
from app.lib.jwt import JWT

class AuthService:
  def signup(self, data):
  
    if user_repository.find_one({ 'email' : data.get('email') }) or user_repository.find_one({ 'username' : data.get('username') }):
      raise Exception("User with email or username already exist")

    password = data.get('password')
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    payload = {
        'firstname': data.get('firstname'),
        'lastname': data.get('lastname'),
        'email': data.get('email'),
        'username': data.get('username'),
        'password': hashed_password
    }

    new_user = user_repository.create(payload)
    return UserPresenter(new_user).serialize()

  def login(self, data):
    email = data.get('email')
    password = data.get('password')
    user = user_repository.find_one({ 'email' : email})

    if not user or not check_password_hash(user.password, password):
      raise Exception("Invalid username or password")

    auth_token = JWT().encode_auth_token(user.id)
    user_repository.update({'id': user.id} ,{'is_active': True})
    return {'token': auth_token, 'user': UserPresenter(user).serialize()}
  
  def logout(self, user_id):
    user = user_repository.find_one({ 'id' : user_id})

    if not user or not check_password_hash(user.password, password):
      raise Exception("Invalid username or password")

    user_repository.update({'id': user.id} , {'is_active': False})
    return {'token': auth_token, 'user': UserPresenter(user).serialize()}
        
