# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    from app.components.users.routes import users_bp
    from app.components.posts.routes import posts_bp
    from app.components.auth.routes import auth_bp  # Add this line

    app.register_blueprint(users_bp, url_prefix='/api/users')
    app.register_blueprint(posts_bp, url_prefix='/api/posts')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    # Create database tables
    with app.app_context():
        db.create_all()

        # Global error handler
    @app.errorhandler(Exception)
    def handle_error(error):
        response = {
            'error': str(error),
            'status_code': 500  # Internal Server Error
        }
        return jsonify(response), 500

    return app
