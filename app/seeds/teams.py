from app.models import db
from app.models.teams import Team


# Adds a demo user, you can add other users here if you want
def seed_teams():
    team1 = Team(
        game_id=1, winner=True)
    team2 = Team(
        game_id=1, winner=False)
    team3 = Team(
        game_id=2, winner=False)
    team4 = Team(
        game_id=2, winner=False)

    db.session.add(team1)
    db.session.add(team2)
    db.session.add(team3)
    db.session.add(team4)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_teams():
    db.session.execute('TRUNCATE teams RESTART IDENTITY CASCADE;')
    db.session.commit()
