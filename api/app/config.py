import os

class Config:
  print(os.getenv('MYSQL_DATABASE_URI'))
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = os.getenv('MYSQL_DATABASE_URI')
  SECRET_KEY = os.getenv('SECRET_KEY')