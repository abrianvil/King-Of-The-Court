from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import Court, db