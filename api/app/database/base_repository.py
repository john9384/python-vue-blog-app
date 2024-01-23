from app import db
import uuid

class BaseRepository:
  def __init__(self, _model):
    self._model = _model

  def create(self, payload):
    new_model = self._model(**{key: value for key, value in payload.items() if key != "id"})

    db.session.add(new_model)
    db.session.commit()

    return { "id" : new_model.id}

  def find_all(self, query):
    results = []
    if query:
      base_query = self._model.query

      for key, value in query.items():
          base_query = base_query.filter(getattr(self._model, key) == value)
      
      results = base_query.all()
    else:
      results = self._model.query.all()

    return [result.to_dict() for result in results]

  def find_one(self, query):
    if query:
      base_query = self._model.query

      for key, value in query.items():
          base_query = base_query.filter(getattr(self._model, key) == value)
      
      result = base_query.first()
      return result.to_dict()
    else:
      return None

  def update(self, query,  payload):
    base_query = self._model.query

    for key, value in query.items():
        base_query = base_query.filter(getattr(self._model, key) == value)
    
    instance = base_query.first()

    if not instance:
      raise Exception("Resource not found")

    for key, value in payload.items():
      if value is not None:
        setattr(instance, key, value)

    db.session.commit()

    return instance.to_dict()

  def delete(self, query):
    base_query = self._model.query

    for key, value in query.items():
        base_query = base_query.filter(getattr(self._model, key) == value)
    
    instance = base_query.first()
    
    if not instance:
      raise Exception("Resource not found")
    
    id = instance.to_dict()['id']

    db.session.delete(instance)
    db.session.commit()

    return { "id" : id }

    