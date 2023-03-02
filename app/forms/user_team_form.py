from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired

class New_user_team(FlaskForm):
    user_id= IntegerField('userId', validators=[DataRequired()])
    team_id= IntegerField('teamId', validators=[DataRequired()])

