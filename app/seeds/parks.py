from app.models import db
from app.models.parks import Park


# Adds a demo user, you can add other users here if you want
def seed_parks():
    park1 = Park(
        name='McKibben Park', location='5500 Trekell St, North Port, FL 34287', amenities='Bathroom, Lake, Parking, Alligators', image='https://www.courtsoftheworld.com/upload/courts/1840/0/COTW-Veterans-Park-1556740907.jpg', lat=27.040380, lng=-82.210160)
    park2 = Park(
        name='Gellert Park', location='50 Wembley Dr, Daly City, CA 94015', amenities='Open 24hr, Bathroom, Soccer Field', image='https://lh5.googleusercontent.com/p/AF1QipMo8uCUlg55Mkuwf0cejTn5MpOQrzFw5MRyWawf', lat=37.663840, lng=-122.472340)

    db.session.add(park1)
    db.session.add(park2)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_parks():
    db.session.execute('TRUNCATE parks RESTART IDENTITY CASCADE;')
    db.session.commit()
