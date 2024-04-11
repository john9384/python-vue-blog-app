
class UserPresenter:
  def __init__(self, user):
    self.user = user

  def serialize(self):
    return {
      'id': self.user.id,
      'firstname': self.user.firstname,
      'lastname': self.user.lastname,
      'email': self.user.email,
      'username': self.user.username,
    }