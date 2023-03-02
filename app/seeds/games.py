from app.models import db
from app.models.games import Game


# Adds a demo user, you can add other users here if you want
def seed_games():
    game1 = Game(
        court_id=1, team_size=2, isStarted=True)
    game2 = Game(
        court_id=1, team_size=4, isStarted=False)

    db.session.add(game1)
    db.session.add(game2)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_games():
    db.session.execute('TRUNCATE games RESTART IDENTITY CASCADE;')
    db.session.commit()
