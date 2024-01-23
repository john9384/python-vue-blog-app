
import sqlite3
from flask import Blueprint, jsonify, request
from app.components.users.models import User
from app import db
from flask_login import login_required, current_user
from app.lib.error_handler import handle_route_errors
from app.components.users.repository import user_repository

users_bp = Blueprint('users', __name__)

@users_bp.route('', methods=['GET'])
@login_required
@handle_route_errors
def get_all_users():
    query_params = request.args
    users = user_repository.find_all(query_params)
    return jsonify({'users': users})

@users_bp.route('/current-user', methods=['GET'])
@login_required
@handle_route_errors
def get_current_user():
    return jsonify({'id': current_user.id, 'username': current_user.username, 'email': current_user.email}), 200

@users_bp.route('/<string:user_id>', methods=['GET'])
@login_required
@handle_route_errors
def get_user(user_id):
    user = user_repository.find_one({"id": user_id})
    if user is None:
        raise Exception("User not found")
   
    return jsonify({'user': user})


@users_bp.route('/<string:user_id>', methods=['PUT'])
@login_required
@handle_route_errors
def update_user(user_id):
    data = request.json
    payload = {
        'firstname': data.get('firstname'),
        'lastname': data.get('lastname'),
    }

    user = user_repository.update({'id': user_id}, payload)

    return jsonify({'user': user})

@users_bp.route('/<string:user_id>', methods=['DELETE'])
@login_required
@handle_route_errors
def delete_user(user_id):
    user_repository.delete({ "id": user_id})
    return jsonify({'message': 'User deleted successfully'})
