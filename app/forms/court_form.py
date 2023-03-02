from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class new_Court (FlaskForm):
    num_of_hoops = IntegerField('num_of_hoops', validators=[DataRequired()])
    surface_type = StringField('surface_type')
