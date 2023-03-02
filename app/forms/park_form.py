from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, DecimalField, validators, FloatField
from wtforms.validators import DataRequired
# import requests #pip install requests
from app.models.parks import Park

class CreateParkForm(FlaskForm):
    # name = db.Column(db.String(100), nullable=False)
    name = StringField('name', validators=[DataRequired()])
    # location = db.Column(db.String(255), nullable=False)
    location = StringField('location', validators=[DataRequired()])
    # amenities = db.Column(db.String(1000), nullable=False)
    amenities = StringField('amenities', validators=[DataRequired()])
    # image = db.Column(db.String, default='https://womeninendo.org/wp-content/uploads/2021/11/no-image.png', nullable=False)
    image = StringField('image', validators=[DataRequired()])
    #for google maps api
    # lat = db.Column(db.Float, nullable=False)
    # lng = db.Column(db.Float, nullable=False)
    lat = FloatField('lat', validators=[DataRequired()])
    lng = FloatField('lng', validators=[DataRequired()])

# def validate_picture_url(self, field):
#         # Check if the URL points to an image file
#         response = requests.head(field.data)
#         content_type = response.headers.get('content-type')
#         if content_type is None or 'image' not in content_type:
#             raise validators.ValidationError('The URL must point to an image file.')
