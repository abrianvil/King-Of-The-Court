from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class New_game(FlaskForm):
    team_size = IntegerField('team_size', validators=[DataRequired()])
