import os

class Config:
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = os.getenv('MYSQL_DATABASE_URI')
  SECRET_KEY = os.getenv('SECRET_KEY')