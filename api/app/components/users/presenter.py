class UserPresenter:
  def __init__(self, user):
    self.user = user

  def serialize(self):
    return {
      'firstname': self.user.firstname,
      'lastname': self.user.firstname,
      'email': self.user.email,
      'username': self.user.username,
    }