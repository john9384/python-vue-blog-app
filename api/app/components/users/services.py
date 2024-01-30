class UserService:
  def read(query):
    user = user_repository.find_one(query)
    if user is None:
      return None
    
    return UserPresenter(user).serialize()
  
  def read_many(query):
    users = user_repository.find_all(query)
    return [UserPresenter(user).serialize for user in users]

  def update(query, data):
    payload = {
        'firstname': data.get('firstname'),
        'lastname': data.get('lastname'),
    }

    user = user_repository.update(query, payload)   

    return UserPresenter(user).serialize()

  def delete(query):
    user = user_repository.delete(query)   

    return UserPresenter(user).serialize()