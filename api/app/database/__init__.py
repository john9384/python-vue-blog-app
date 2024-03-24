from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

def create_db_instance(app, db_uri='sqlite:///database.db'):
  db = SQLAlchemy(app)

  engine = create_engine(db_uri)
  if not database_exists(engine.url):
      create_database(engine.url)
      print("New Database Created")
  else:
      print("Database Already Exists")

  return db
