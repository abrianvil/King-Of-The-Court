# from .db import db, environment, SCHEMA, add_prefix_for_prod

# class Team(db.Model):
#     __tablename__ = 'teams'

#     if environment == "production":
#         __table_args__ = {'schema': SCHEMA}
    
#     id = db.Column(db.Integer, primary_key=True)
#     # name = db.Column(db.String(100))
#     # game_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('games.id')), nullable=False)
#     winner = db.Column(db.Boolean, nullable=False)

#     #relationships

#     def to_dict(self):
#         return {
#             'id': self.id,
#             #'name': self.name,
#             # 'game_id': self.game_id,
#             'winner': self.winner
#         }   
