
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
    outcome = user_service.read({'id': current_user.id})
    return SuccessResponse("User fetched successfully", outcome, OK).send()

@users_bp.route('/<string:user_id>', methods=['GET'])
@login_required
@handle_route_errors
def get_user(user_id):
    outcome = user_service.read({'id': user_id})
    return SuccessResponse("User fetched successfully", outcome, OK).send()


@users_bp.route('/<string:user_id>', methods=['PUT'])
@login_required
@handle_route_errors
def update_user(user_id):
    data = request.json
    outcome = user_service.update({'id': user_id}, data)

    return SuccessResponse("User updated successfully", outcome, OK).send()

@users_bp.route('/<string:user_id>', methods=['DELETE'])
@login_required
@handle_route_errors
def delete_user(user_id):
    outcome = user_service.delete({ "id": user_id})
    return SuccessResponse("User deleted successfully", outcome, OK).send()
