from flask import Blueprint, jsonify, redirect, request
from flask_login import login_required, current_user
from app.models import Court, db
from app.forms.court_form import New_Court

courts_routes = Blueprint('courts', __name__)


#SECTION - View Court By id
@courts_routes.route('/<int:courtId>/one', methods=["GET"])
@login_required
def get_one_court(courtId):
    court = Court.query.get(courtId)
    if court:
        return court.to_dict()
    return {'errors': 'No court found'}, 404

#SECTION - View All Courts of a Park
@courts_routes.route('/park/<int:parkId>/all', methods=["GET"])
@login_required
def get_all_court(parkId):
    courts = Court.query.filter(Court.park_id == parkId).all()
    if courts:
        courtsobj = [court.to_dict() for court in courts]
        return jsonify(courtsobj)
    return {'errors': 'No courts available for this park'}, 404

#!SECTION Create a Court for a Park
@courts_routes.route('/park/<int:parkId>/create', methods=["POST"])
@login_required
def make_court(parkId):
    form = New_Court()
    form['csrf_token'].data = request.cookies['csrf_token']
    
    if form.validate_on_submit():
        court = Court()
        form.populate_obj(court)
        court.park_id = parkId
        db.session.add(court)
        db.session.commit()
        return jsonify(court.to_dict())
    else:
        return jsonify(form.errors)

#!SECTION Delete a Court
@courts_routes.route('/<int:courtId>/delete', methods=["DELETE"])
@login_required
def delete_court(courtId):
    court = Court.query.get(courtId)
    if court:
        db.session.delete(court)
        db.session.commit()
        return jsonify("Successfully deleted court")
    else:
        return jsonify({"errors": "Court not found"}, 404)
