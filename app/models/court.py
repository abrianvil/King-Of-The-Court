from .db import db, environment, SCHEMA, add_prefix_for_prod

class Court(db.Model):
    __tablename__ = 'courts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    park_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('parks.id')), nullable=False)
    num_of_hoops = db.Column(db.Integer, nullable=False)
    surface_type = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    #relationships
    courts_to_parks = db.relationship('Park', back_populates='parks_to_courts')
    

    def to_dict(self):
        return {
            'id': self.id,
            'park_id': self.park_id,
            'num_of_hoops': self.num_of_hoops,
            'surface_type': self.surface_type
        }
