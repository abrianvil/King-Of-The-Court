from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password')
    marnie = User(
        username='marnie', email='marnie@aa.io', password='password')
    bobbie = User(
        username='bobbie', email='bobbie@aa.io', password='password')
    abel = User(
        username='abel10', email='abel10@gmail.com', password='password')
    alexis = User(
        username='alexis24', email='alexis@gmail.com', password='password')
    ella = User(
        username='ella', email='ella@gmail.com', password='password')
    jordan = User(
        username='jpoole', email='jpoole@gmail.com', password='password')
    melo = User(
        username='melo', email='melo@gmail.com', password='password')
    damian = User(
        username='damiam', email='damian@gmail.com', password='password')
    giannis = User(
        username='giannis', email='giannis@gmail.com', password='password')

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(abel)
    db.session.add(alexis)
    db.session.add(ella)
    db.session.add(jordan)
    db.session.add(melo)
    db.session.add(damian)
    db.session.add(giannis)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
