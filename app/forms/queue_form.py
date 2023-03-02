from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class New_Queue(FlaskForm):
    position = IntegerField('position', validators=[DataRequired()])
