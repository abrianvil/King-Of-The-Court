from .db import db, environment, SCHEMA, add_prefix_for_prod

class Member(db.Model):
    __tablename__ = 'members'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    park_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('parks.id')), nullable=False)

    #relationships
    members_to_parks = db.relationship('Park', back_populates='parks_to_members', foreign_keys=[park_id])
    members_to_users = db.relationship('User', back_populates='users_to_members', foreign_keys=[user_id])

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'park_id': self.park_id
        }
