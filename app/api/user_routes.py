from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models.db import db
from app.models import User
from app.forms.user_form import EditUserForm

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

#SECTION - edit username and/or profile image
@user_routes.route('/<int:userId>/edit', methods=["PUT"])
@login_required
def edit_user(userId):
    form = EditUserForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    # data = form.data
    user = User.query.get(userId)

    if form.validate_on_submit() and user:
        req = User()
        form.populate_obj(user)
        db.session.commit()
        return jsonify(user.to_dict(), 200)
    return jsonify({'errors': 'No user found'}, 404)

def adminauthorized():
    """
    Returns unauthorized not admin JSON when flask-login authentication fails
    """
    if current_user.is_authenticated:
        if current_user.email == "abel10@gmail.com" or current_user.email == "alexis@gmail.com":
            return current_user.to_dict()
        else:
            return {'errors': ['Unauthorized']}, 401
    return {'errors': ['Unauthorized']}, 401
