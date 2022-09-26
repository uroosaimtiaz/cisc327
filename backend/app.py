from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Booking(db.Model):
    """Booking Entity. Stores which listing a user wants to book and other
    information.
    """

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(200), nullable=False)  # booking address

    # Listing reference number to refer to the listing
    listing_ref_number = db.Column(db.Integer, nullable=False)  

    lenth_of_stay = db.Column(db.Integer, nullable=False)  # Duration of stay
    cost = db.Column(db.Integer, nullable=False)  # How much it costs to stay

    # approval to book from owner
    approval = db.Column(db.Boolean, nullable=False)  

class Listing(db.Model):
    # Data Entity for Listing will store the location and description
    # of a specific listing; the images will be stored somewhere else.
   street_address = db.Column(db.String(150)) #store street address
   postal_code = db.Column(db.String(60)) #store postal code
   state = db.Column(db.String(80)) #store the state or province
   country = db.Column(db.String(80)) #stores country
   house_type = db.Column(db.String(80)) #eg. apartment, bangalow, room, van
   rental_cost = db.Column(db.Integer) #cost per night
   description = db.Column(db.String(2000)) #ad description of property and amenities

class Review(db.Model):
    """Review Enitity. Structure for leaving user reviews."""
    review_type = db.Column(db.String(100), nullable=False) # type of review, profile or listing
    star_number = db.Column(db.Integer, primary_key=True) # number of stars the user rates
    review_title = db.Column(db.String(150), nullable=False) # the title of the review
    review_description = db.Column(db.String(500), nullable=False) # the review description



   def __repr__(self):
       return '< Listing at %r>' % self.street_address