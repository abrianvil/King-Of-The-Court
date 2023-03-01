from app.models import db
from app.models.queues import Queue


# Adds a demo user, you can add other users here if you want
def seed_queues():
    queue1 = Queue(
        game_id=2, team_id=3, position=1)
    queue2 = Queue(
        game_id=2, team_id=4, position=1)

    db.session.add(queue1)
    db.session.add(queue2)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_queues():
    db.session.execute('TRUNCATE queues RESTART IDENTITY CASCADE;')
    db.session.commit()
