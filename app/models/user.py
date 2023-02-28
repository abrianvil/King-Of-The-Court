from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    profile_image = db.Column(db.String, default='https://cdn.shopify.com/s/files/1/0464/8386/5759/products/cc19f74538a0d099a4e4f76de967fddfb3e245dd5229b2ab26d9a8c23f61b746_grande.jpg', nullable=False)
    wins = db.Column(db.Integer, default=0, nullable=False)
    losses = db.Column(db.Integer, default=0, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    #relationships
    users_to_members = db.relationship('Member', back_populates='members_to_users', primaryjoin='User.id == Member.user_id')
    user_to_user_teams = db.relationship('Team', back_populates='user_teams_to_user', primaryjoin='User.id == UserTeam.user_id')

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'profimg': self.profile_image,
            'wins': self.wins,
            'losses': self.losses,
            'created_at': self.created_at
        }
