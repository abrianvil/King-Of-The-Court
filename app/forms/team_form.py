from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms.validators import DataRequired

class New_team(FlaskForm):
    winner= BooleanField('winner')
    