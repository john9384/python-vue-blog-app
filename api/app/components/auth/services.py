from werkzeug.security import generate_password_hash, check_password_hash

class AuthService:
  def signup(data):
    password = data.get('password')
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    payload = {
        'firstname': data.get('firstname'),
        'lastname': data.get('lastname'),
        'email': data.get('email'),
        'username': data.get('username'),
        'password': hashed_password
    }

    new_user = user_repository.create(payload)
    user_data = UserPresenter(new_user).serialize()

  def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = user_repository.find_one({ 'email' : email})
  
    if user and check_password_hash(user.password, password):
        login_user(user)
        return UserPresenter(user).serialize() 
    else:
        raise Exception("Invalid username or password")
