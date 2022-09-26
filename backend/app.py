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

# Data Entity for Listing will store the location and description
# of a specific listing; the images will be stored somewhere else. 
class Listing(db.Model):
    street_address = db.Column(db.String(150))
    postal_code = db.Column(db.String(60))
    state = db.Column(db.String(80))
    country = db.Column(db.String(80))
    house_type = db.Column(db.String(80))
    rental_cost = db.Column(db.Integer)
    description = db.Column(db.String(2000))

    def __repr__(self):
        return '< Listing at %r>' % self.street_address