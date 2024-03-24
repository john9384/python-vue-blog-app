from flask_sqlalchemy import SQLAlchemy

def create_db_instance(app):
  db = SQLAlchemy(app)

  return db