from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import User

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict()


# def adminauthorized():
#     """
#     Returns unauthorized JSON when flask-login authentication fails
#     """
#     if current_user.is_authenticated:
#         if current_user.email not "abel10@gmail.com" or current_user.email not "alexis@gmail.com":
#             return {'errors': ['Unauthorized']}, 401
#         else:
#             return current_user.to_dict()
#     return {'errors': ['Unauthorized']}, 401
