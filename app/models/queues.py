from .db import db, environment, SCHEMA, add_prefix_for_prod

class Queue(db.Model):
    __tablename__ = 'queues'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    court_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('courts.id')), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id')), nullable=False)
    position = db.Column(db.Integer, nullable=False)

    #relationships
    queue_to_court = db.relationship('Court', back_populates='courts_to_queue')
    queue_to_team = db.relationship('Team', back_populates='team_to_queue')


    def to_dict(self):
        return {
            'id': self.id,
            'court_id': self.court_id,
            'team_id': self.team_id,
            'position': self.position
        }
