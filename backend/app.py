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
    """Booking Entity. Stores which listing a user wants to bookand other
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