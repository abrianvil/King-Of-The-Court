from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, DecimalField, validators, FloatField
from wtforms.validators import DataRequired
# import requests #pip install requests
from app.models.user import User

class EditUserForm(FlaskForm):
    username = StringField('name', validators=[DataRequired()])
    profile_img = StringField('amenities')
