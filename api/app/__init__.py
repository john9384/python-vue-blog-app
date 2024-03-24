from dotenv import load_dotenv
load_dotenv()
 
from flask import Flask, jsonify
from app.config import Config
from app.database import create_db_instance

app = Flask(__name__)
app.config.from_object(Config)  
db = create_db_instance(app, Config.SQLALCHEMY_DATABASE_URI)

@app.route('/')
def index():
    return jsonify({'message': 'Hello World'})

# Register blueprints
from app.components.users.routes import users_bp
from app.components.posts.routes import posts_bp
from app.components.auth.routes import auth_bp

app.register_blueprint(users_bp, url_prefix='/api/users')
app.register_blueprint(posts_bp, url_prefix='/api/posts')
app.register_blueprint(auth_bp, url_prefix='/api/auth')

# with app.app_context():
#   db.create_all()

# Global error handler
@app.errorhandler(Exception)
def handle_error(error):
    response = {
        'error': str(error),
        'status_code': 500  # Internal Server Error
    }
    return jsonify(response), 500


if __name__ == '__main__':
    app.run()