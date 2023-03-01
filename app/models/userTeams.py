from .db import db, environment, SCHEMA, add_prefix_for_prod

class UserTeam(db.Model):
    __tablename__ = 'user_teams'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id')), nullable=False)

    #relationships
    user_teams_to_user = db.relationship('User', back_populates='user_to_user_teams', foreign_keys=[user_id]) 
    user_teams_to_team = db.relationship('Team', back_populates='team_to_user_teams', foreign_keys=[team_id])


    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'team_id': self.team_id
        }
