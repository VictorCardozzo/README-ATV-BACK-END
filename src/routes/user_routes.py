from flask import Blueprint
from src.controllers.user_controller import UserController

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/users', methods=['GET'])(UserController.list_users)
user_bp.route('/users', methods=['POST'])(UserController.create_user)

from flask import Blueprint
from src.controllers.user_controller import UserController

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/users', methods=['GET'])(UserController.list_users)
user_bp.route('/users', methods=['POST'])(UserController.create_user)
user_bp.route('/users/<int:user_id>', methods=['GET'])(UserController.get_user_by_id)