from .db import db, environment, SCHEMA, add_prefix_for_prod

class Team(db.Model):
    __tablename__ = 'teams'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('games.id')), nullable=False)
    winner = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    #relationships
    team_to_user_teams = db.relationship('UserTeam', back_populates='user_teams_to_team', primaryjoin='Team.id==UserTeam.team_id')
    team_to_game = db.relationship('Game', back_populates='game_to_team')
    team_to_queue = db.relationship('Queue', back_populates='queue_to_team', cascade="all,delete")

    def to_dict(self):
        return {
            'id': self.id,
            'game_id': self.game_id,
            'winner': self.winner,
            'created_at': self.created_at
        }   
