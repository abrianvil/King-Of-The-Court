from .db import db, environment, SCHEMA, add_prefix_for_prod

class Game(db.Model):
    __tablename__ = 'games'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    court_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('courts.id')), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    #relationships
    game_to_team = db.relationship('Team', back_populates='team_to_game', cascade="all,delete")
    game_to_court = db.relationship('Court', back_populates='courts_to_game')

    def to_dict(self):
        return {
            'id': self.id,
            'court_id': self.court_id,
            'created_at': self.created_at
        }
