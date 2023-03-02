from app.models import db
from app.models.court import Court


# Adds a demo user, you can add other users here if you want
def seed_courts():
    court1 = Court(
        park_id=1, num_of_hoops=2, surface_type='cement')
    court2 = Court(
        park_id=2, num_of_hoops=2, surface_type='cement')

    db.session.add(court1)
    db.session.add(court2)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_courts():
    db.session.execute('TRUNCATE courts RESTART IDENTITY CASCADE;')
    db.session.commit()
