from app.models import db
from app.models.members import Member


# Adds a demo user, you can add other users here if you want
def seed_memberss():
    member1 = Member(
        user_id=1, park_id=1)
    member2 = Member(
        user_id=2, park_id=2)

    db.session.add(member1)
    db.session.add(member2)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_members():
    db.session.execute('TRUNCATE members RESTART IDENTITY CASCADE;')
    db.session.commit()
