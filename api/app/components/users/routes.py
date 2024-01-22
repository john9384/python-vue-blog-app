
import sqlite3
from flask import Blueprint, jsonify, request
from app.components.users.models import User
from app import db
from flask_login import login_required, current_user
from app.lib.error_handler import handle_route_errors

users_bp = Blueprint('users', __name__)

@users_bp.route('', methods=['GET'])
@login_required
@handle_route_errors
def get_all_users():
    users = User.query.all()
    return jsonify({'users': [user.to_dict() for user in users]})

@users_bp.route('/current-user', methods=['GET'])
@login_required
@handle_route_errors
def get_current_user():
    return jsonify({'id': current_user.id, 'username': current_user.username, 'email': current_user.email}), 200

@users_bp.route('/<int:user_id>', methods=['GET'])
@login_required
@handle_route_errors
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({'user': user.to_dict()})
    else:
        return jsonify({'error': 'User not found'}), 404


@users_bp.route('/<int:user_id>', methods=['PUT'])
@login_required
@handle_route_errors
def update_user(user_id):
    data = request.json
    user = User.query.get(user_id)

    if user:
        user.firstname = data['firstname']
        user.lastname = data['lastname']
        user.email = data['email']
        user.username = data['username']
        user.password = data['password']

        db.session.commit()

        return jsonify({'user': user.to_dict()})
    else:
        return jsonify({'error': 'User not found'}), 404

@users_bp.route('/<int:user_id>', methods=['DELETE'])
@login_required
@handle_route_errors
def delete_user(user_id):
    user = User.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()

        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'error': 'User not found'}), 404
