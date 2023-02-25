from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Parks(db.Model):
    __tablename__ = 'parks'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amenities = db.Column(db.String(1000), nullable=False)
    image = db.Column(db.String, default='https://womeninendo.org/wp-content/uploads/2021/11/no-image.png', nullable=False)
    location = db.Column(db.String(255), nullable=False)
    #for google maps api
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    #relationships
    # user = db.relationship('User', back_populates='parks')
    # user_parks = db.relationship('UserPark', back_populates='parks')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'amenitites': self.description,
            'image': self.image,
            'location': self.location,
            'lat': self.lat,
            'lng': self.lng,
            'user_id': self.user_id
        }
