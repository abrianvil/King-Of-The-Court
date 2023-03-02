from flask import Blueprint, jsonify, redirect, request
from flask_login import login_required, current_user
from datetime import date, datetime, timedelta
from app.models.db import db
from app.models.teams import Team
from app.models.userTeams import UserTeam
from app.forms.team_form import New_team
from app.forms.user_team_form import New_user_team


teams_routes= Blueprint('teams', __name__)


##SECTION - CREATE A TEAM FOR A GAME
@teams_routes.route('/game/<int:gameId>', methods=['POST'])
@login_required
def create_a_team(gameId):
    # print('this \n \n is a \n \n test')
    form=New_team()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        team=Team()
        form.populate_obj(team)
        team.game_id= gameId
        # print("""GAMEID \n \n \n""", team)
        db.session.add(team)
        db.session.commit()
        return jsonify(team.to_dict())
    else:
        return jsonify(form.errors)


##SECTION - VIEW TEAM BY ID
@teams_routes.route('/<int:teamId>/', methods=['GET'])
@login_required
def view_a_team(teamId):
    team= Team.query.get(teamId)

    if team:
        return jsonify(team.to_dict())
    else:
        return jsonify({'errors':'team not found'}, 404)


##SECTION - JOIN TEAM
@teams_routes.route('/<int:teamId>/join', methods=['POST'])
@login_required
def join_a_team(teamId):
    form=New_user_team()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user_team=UserTeam()
        form.populate_obj(user_team)
        user_team.user_id=current_user.id
        db.session.add(user_team)
        db.session.commit()
        return jsonify(user_team.to_dict())
