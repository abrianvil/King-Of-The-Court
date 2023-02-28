# from .db import db, environment, SCHEMA, add_prefix_for_prod

# class Game(db.Model):
#     __tablename__ = 'games'

#     if environment == "production":
#         __table_args__ = {'schema': SCHEMA}
    
#     id = db.Column(db.Integer, primary_key=True)
#     court_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('courts.id')), nullable=False)

#     #NOTE FOR ABEL 
#     #Flask relationships get a little weird when you have two columns in a table that are foreign keys to the same table.
#     #I think it'd be better to have the Teams table have a game_id column and the boolean for winner

#     # team1_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id')), nullable=False)
#     # team2_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('teams.id')), nullable=False)
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
#     updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

#     #relationships

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'court_id': self.court_id,
#             'created_at': self.created_at
#         }
