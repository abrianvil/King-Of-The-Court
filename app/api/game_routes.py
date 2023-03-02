from flask import Blueprint, jsonify, redirect, request
from flask_login import login_required, current_user
from datetime import date, datetime, timedelta
from app.models.db import db
from app.models.games import Game
from app.forms.game_form import New_game


games_routes= Blueprint('games', __name__)

##SECTION - GET GAME BY ID
@games_routes.route('/<int:gameId>', methods=['GET'])
@login_required
def view_a_game(gameId):
    game= Game.query.get(gameId)
    if game:
        return jsonify(game.to_dict())
    else:
        return jsonify({'errors':'game not found'}, 404)


##SECTION - CREATE A GAME
@games_routes.route('/court/<int:courtId>', methods=['POST'])
@login_required
def create_game(courtId):
    form= New_game()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        game=Game()
        form.populate_obj(game)
        game.court_id= courtId
        db.session.add(game)
        db.session.commit()
        return jsonify(game.to_dict())
    else:
        return jsonify(form.errors)


##SECTION - EDIT A GAME
@games_routes.route('/<int:gameId>', methods=['PUT'])
@login_required
def edit_game(gameId):
    game=Game.query.get(gameId)
    if game:
        form= New_game()
        form['csrf_token'].data = request.cookies['csrf_token']
        if form.validate_on_submit():
            form.populate_obj(game)
            db.session.commit()
            return jsonify(game.to_dict())
        else:
            return jsonify(form.errors)
    else:
        return jsonify({'errors':'game not found'}, 404)


##SECTION - DELETE A GAME
@games_routes.route('/<int:gameId>/delete',methods=['DELETE'])
@login_required
def delete_game(gameId):
    game=Game.query.get(gameId)
    if game:
        db.session.delete(game)
        db.session.commit()
        return jsonify('Successfully deleted')
    else:
        return jsonify({'errors':'game not found'}, 404)
