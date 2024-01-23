# app/components/auth/routes.py

from flask import Blueprint, request, jsonify, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager
from app.components.users.models import User
from app.lib.error_handler import handle_route_errors
from app.components.users.repository import user_repository

auth_bp = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(str(user_id))

@auth_bp.route('/signup', methods=['POST'])
@handle_route_errors
def signup():
    data = request.get_json()
    
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

    return jsonify({'message': 'User created successfully!'}), 201

@auth_bp.route('/login', methods=['POST'])
@handle_route_errors
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        login_user(user)
        return jsonify({'message': 'Login successful!'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

@auth_bp.route('/logout')
@login_required
@handle_route_errors
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful!'}), 200

@auth_bp.route('/user', methods=['GET'])
@login_required
def get_user():
    return jsonify({'id': current_user.id, 'username': current_user.username, 'email': current_user.email}), 200
