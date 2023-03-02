from flask import Blueprint, jsonify, redirect, request
from flask_login import login_required, current_user
from datetime import date, datetime, timedelta
from app.models.db import db
from app.models.members import Member
# from app.forms.mem_form import CreateParkForm

members_routes = Blueprint('members', __name__)

## get all members of current user
@members_routes.route('/all', methods=["GET"])
@login_required
def get_all_members():
    members = Member.query.all()
    if members:
        membersobj = [member.to_dict() for member in members]
        return jsonify(membersobj)
    return jsonify({'errors': 'No members available right now'}, 404)

##SECTION - delete membership
@members_routes.route('/<int:memberId>/delete', methods=["DELETE"])
@login_required
def delete_membership(memberId):
    member = Member.query.get(memberId)
    if member:
        db.session.delete(member)
        db.session.commit()
        return jsonify("Successfully deleted membership")
    return jsonify({'errors': 'No member found'}, 404)
