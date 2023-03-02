from flask import Blueprint, jsonify, redirect, request
from flask_login import login_required, current_user
from datetime import date, datetime, timedelta
from app.models.db import db
from app.models.parks import Park
from app.forms.park_form import CreateParkForm

parks_routes = Blueprint('parks', __name__)

## get all profiles of current user
@parks_routes.route('/all', methods=["GET"])
@login_required
def get_all_parks():
    parks = Park.query.all()
    if parks:
        parkobj = [park.to_dict() for park in parks]
        return jsonify(parkobj)
    return jsonify({'errors': 'No parks available right now'}, 404)

##get one park by id
@parks_routes.route('/<int:parkId>/one', methods=["GET"])
@login_required
def get_one_park(parkId):
    park = Park.query.get(parkId)
    if park:
        return jsonify(park.to_dict())
    return jsonify({'errors': 'No park found'}, 404)

# make a park 
@parks_routes.route('/create', methods=["POST"])
@login_required
def make_park():
    form = CreateParkForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    data = form.data
    if form.validate_on_submit():
        newpark = Park(
            name = data['name'],
            location = data['location'],
            amenities = data['amenities'],
            image = data['image'],
            lat = data['lat'],
            lng = data['lng']
            )
        db.session.add(newpark)
        db.session.commit()
        return jsonify(newpark.to_dict())
    return jsonify(form.errors)

##edit profile
@parks_routes.route('/<int:parkId>/edit', methods=["PUT"])
@login_required
def edit_park(parkId):
    form = CreateParkForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    data = form.data
    park = Park.query.get(parkId)

    if park and form.validate_on_submit():
        park.name = data['name']
        park.location = data['location']
        park.amenities = data['amenities']
        park.image = data['image']
        park.lat = data['lat']
        park.lng = data['lng']
        db.session.commit()
        return jsonify(park.to_dict())
    if not park:
        return {'errors': ['That park does not exist']}, 404
    else:
        return jsonify(form.errors)

##delete a park 
@parks_routes.route('/<int:parkId>/delete', methods=["DELETE"])
@login_required
def delete_park(parkId):
    park = Park.query.get(parkId)
    if park:
        db.session.delete(park)
        db.session.commit()
        return jsonify('Successfully deleted profile')
    return jsonify({'errors': 'Park not found'}, 404)
