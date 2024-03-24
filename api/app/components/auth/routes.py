from flask import Blueprint, request
from app.components.users.models import User
from app.lib.error_handler import handle_route_errors
from app.components.users.presenter import UserPresenter
from app.components.auth.services import AuthService
from app.components.users.services import UserService
from app.lib.response import SuccessResponse, OK, CREATED, BAD_REQUEST
from app.lib.authenticate import is_authenticated

auth_bp = Blueprint('auth', __name__)
auth_service = AuthService()
user_service = UserService()


@auth_bp.route('/signup', methods=['POST'])
@handle_route_errors
def signup():
    data = request.get_json()
    outcome = auth_service.signup(data)

    return SuccessResponse("User created successfully", outcome, CREATED).send()

@auth_bp.route('/login', methods=['POST'])
@handle_route_errors
def login():
    data = request.get_json()
    outcome = auth_service.login(data)

    return SuccessResponse("User logged in successfully", outcome, OK).send()

@auth_bp.route('/logout')
@is_authenticated
@handle_route_errors
def logout():
    auth_service.login(request.user['id'])
    return SuccessResponse("User logged out").send()

@auth_bp.route('/user', methods=['GET'])
@is_authenticated
def get_user():
    outcome = user_service.read({'id': request.user['id']})

    return SuccessResponse("User fetched successfully", outcome).send()
