import sqlite3
from flask import Blueprint, jsonify, request
from app.components.posts.models import Post
from app.lib.error_handler import handle_route_errors

posts_bp = Blueprint('posts', __name__)

@posts_bp.route('', methods=['GET'])
def get_all_posts():
    posts = Post.query.all()
    return jsonify({'posts': [post.to_dict() for post in posts]})

@posts_bp.route('/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.get(post_id)
    if post:
        return jsonify({'post': post.to_dict()})
    else:
        return jsonify({'error': 'Post not found'}), 404

@posts_bp.route('', methods=['POST'])
@login_required
@handle_route_errors
def create_post():
    data = request.json
    new_post = Post(
        creator_id=data['creator_id'],
        title=data['title'],
        content=data['content'],
        image=data['image']
    )

    db.session.add(new_post)
    db.session.commit()

    return jsonify({'post': new_post.to_dict()}), 201

@posts_bp.route('/<int:post_id>', methods=['PUT'])
@login_required
@handle_route_errors
def update_post(post_id):
    data = request.json
    post = Post.query.get(post_id)

    if post:
        post.creator_id = data['creator_id']
        post.title = data['title']
        post.content = data['content']
        post.image = data['image']

        db.session.commit()

        return jsonify({'post': post.to_dict()})
    else:
        return jsonify({'error': 'Post not found'}), 404

@posts_bp.route('/<int:post_id>', methods=['DELETE'])
@login_required
@handle_route_errors
def delete_post(post_id):
    post = Post.query.get(post_id)

    if post:
        db.session.delete(post)
        db.session.commit()

        return jsonify({'message': 'Post deleted successfully'})
    else:
        return jsonify({'error': 'Post not found'}), 404
