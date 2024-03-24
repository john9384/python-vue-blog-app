from app import db
import uuid

class BaseRepository:
  def __init__(self, _model):
    self._model = _model

  def create(self, payload):
    '''
    Args:query (dict): A dictionary containing payload for creating a new row.
    Returns: object: The newly created object.
    '''
    new_model = self._model(**{key: value for key, value in payload.items() if key != "id"})

    db.session.add(new_model)
    db.session.commit()

    return new_model

  def find_all(self, query=None):
    '''
    Args:query (dict): A dictionary containing key-value pairs for filtering.
    Returns: list: A list of matching user objects or an empty list if none found.
    '''
    if not query:
        base_query = self._model.query
    else:
        # Build the query dynamically based on the given dictionary
        filters = [getattr(self._model, key) == value for key, value in query.items()]
        base_query = self._model.query.filter(*filters)

    results = base_query.all()

    return results

  def find_one(self, query):
    '''
    Args: query (dict): A dictionary containing key-value pairs for filtering.
    Returns: object or None: The first matching item or None if not found.
    '''
    if not query:
        return None

    filters = [getattr(self._model, key) == value for key, value in query.items()]
    base_query = self._model.query.filter(*filters)

    result = base_query.first()

    if not result: return None

    return result
  
  def get_by_id(self, id):
    if not id:
        return None

    return self._model.query.get(id)

  def update(self, query,  payload):
    if not query:
        return None

    filters = [getattr(self._model, key) == value for key, value in query.items()]
    base_query = self._model.query.filter(*filters)
    
    instance = base_query.first()

    if not instance:
      raise Exception("Resource not found")

    for key, value in payload.items():
      if value is not None:
        setattr(instance, key, value)

    db.session.commit()

    return instance

  def delete(self, query):
    '''
    Args: query (dict): A dictionary containing key-value pairs for filtering.
    Returns:object or None: returns the id of the deleted item.
    '''
    if not query:
        return None

    filters = [getattr(self._model, key) == value for key, value in query.items()]
    base_query = self._model.query.filter(*filters)
    
    instance = base_query.first()
    
    if not instance:
      raise Exception("Resource not found")
    
    id = instance.to_dict()['id']

    db.session.delete(instance)
    db.session.commit()

    return id

    