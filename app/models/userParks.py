from .db import db, environment, SCHEMA, add_prefix_for_prod

class UserPark(db.Model):
    __tablename__ = 'user_parks'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    park_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('parks.id')), nullable=False)

    #relationships 

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'park_id': self.park_id
        }
