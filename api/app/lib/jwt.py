from app.config import Config
from datetime import datetime
import os
import jwt
from datetime import datetime, timedelta


class JWT:
    @staticmethod
    def encode_auth_token(user_id):
        """
        Generates the Auth Token
        :return: string
        """
        secret_key = Config.SECRET_KEY
    
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1, seconds=3600),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        try:
            return jwt.encode(payload, secret_key, algorithm='HS256')
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        secret_key = Config.SECRET_KEY
        try:
            payload = jwt.decode(auth_token, secret_key, algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
