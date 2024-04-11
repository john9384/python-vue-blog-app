import sqlite3
from flask import Blueprint, jsonify, request
from app.components.posts.models import Post
from app.lib.response import SuccessResponse, OK, CREATED, BAD_REQUEST
from app.lib.error_handler import handle_route_errors
from app.lib.authenticate import is_authenticated
from app.components.posts.services import PostService

posts_bp = Blueprint('posts', __name__)
post_service = PostService()

@posts_bp.route('', methods=['GET'])
def get_all_posts():
    query_params = request.args
    outcome = user_service.read_many(query_params)
    return SuccessResponse("User fetched successfully", outcome, OK).send()

@posts_bp.route('/<int:post_id>', methods=['GET'])
def get_post(post_id):
    outcome = user_repository.find_all({'id': post_id})
    return SuccessResponse("User fetched successfully", outcome, OK).send()

@posts_bp.route('', methods=['POST'])
@is_authenticated
@handle_route_errors
def create_post():
    data = request.json
    outcome = post_service.create(request.user['id'], data)
    return SuccessResponse("Post created successfully", outcome, CREATED).send()

@posts_bp.route('/<int:post_id>', methods=['PUT'])
@is_authenticated
@handle_route_errors
def update_post(post_id):
    data = request.json
    creator_id = request.user['id']
    outcome = post_service.update({'id': post_id, 'creator_id': creator_id}, data)
    return SuccessResponse("Post updated successfully", outcome, OK).send()

@posts_bp.route('/<int:post_id>', methods=['DELETE'])
@is_authenticated
@handle_route_errors
def delete_post(post_id):
    creator_id = request.user['id']
    outcome = post_service.delete({'id': post_id, 'creator_id': creator_id})
    return SuccessResponse("Post deleted successfully", outcome, OK).send()
