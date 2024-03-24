from functools import wraps
from flask import jsonify, request
from app.lib.jwt import JWT
from app.lib.response import BadRequestResponse
from app.config import Config
from app.components.users.services import UserService
import jwt

user_service = UserService()

def is_authenticated(func):
  @wraps(func)
  def decorated_function(*args, **kwargs):
    auth_header = request.headers.get('Authorization')
    if not auth_header:
      return BadRequestResponse('Invalid JWT token', None).send()

    token = auth_header.split()[1] 

    try:
      decoded_data = JWT.decode_auth_token(token)
      user = user_service.read({'id': decoded_data})
      if not user:
        raise Exception("Invalid credential")
      request.user = { 'id': user['id'], 'email': user['email'] }
    except jwt.exceptions.DecodeError:
      return BadRequestResponse('Invalid JWT token', None).send()
    except jwt.exceptions.ExpiredSignatureError:
      return BadRequestResponse('JWT token expired', None).send()
    return func(*args, **kwargs)
  return decorated_function


