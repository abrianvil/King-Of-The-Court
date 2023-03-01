from app.models import db
from app.models.userTeams import UserTeam


# Adds a demo user, you can add other users here if you want
def seed_user_teams():
    userteam1 = UserTeam(
        user_id=1, team_id=2)
    userteam2 = UserTeam(
        user_id=2, team_id=2)
    userteam3 = UserTeam(
        user_id=4, team_id=1)
    userteam4 = UserTeam(
        user_id=5, team_id=1)
    userteam5 = UserTeam(
        user_id=7, team_id=3)
    userteam6 = UserTeam(
        user_id=8, team_id=3)
    userteam7 = UserTeam(
        user_id=9, team_id=4)
    userteam8 = UserTeam(
        user_id=10, team_id=4)

    db.session.add(userteam1)
    db.session.add(userteam2)
    db.session.add(userteam3)
    db.session.add(userteam4)
    db.session.add(userteam5)
    db.session.add(userteam6)
    db.session.add(userteam7)
    db.session.add(userteam8)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_user_teams():
    db.session.execute('TRUNCATE user_teams RESTART IDENTITY CASCADE;')
    db.session.commit()
