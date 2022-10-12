from qbay import app
from flask_sqlalchemy import SQLAlchemy
import string
from email_validator import validate_email, EmailNotValidError
import uuid

'''
This file defines data models and related business logics
'''

db = SQLAlchemy(app)

upper_characters = list(string.ascii_uppercase)
lower_characters = list(string.ascii_lowercase)
special_characters = list(string.punctuation)


class User(db.Model):
    id = db.Column(db.String)
    username = db.Column(
        db.String(80), nullable=False)
    email = db.Column(
        db.String(120), unique=True, nullable=False,
        primary_key=True)
    password = db.Column(
        db.String(120), nullable=False)
    billing_address = db.Column(
        db.String(300))
    postal_code = db.Column(
        db.String(300))
    balance = db.Column(
        db.Integer)

    def __repr__(self):
        return '<User %r>' % self.username


# create all tables
db.create_all()


def register(name, email, password):
    '''
    Register a new user
      Parameters:
        name (string):     user name
        email (string):    user email
        password (string): user password
      Returns:
        True if registration succeeded otherwise False
    '''
    # check if the email has been used:
    existed = User.query.filter_by(email=email).all()
    if len(existed) > 0:
        return False

    #  validating the email follows RFC 5322
    try:
        validate_email(email).email
    except EmailNotValidError as errorMsg:
        print(str(errorMsg))
        return False

    #  checking for password requirements
    upper_count = 0
    lower_count = 0
    special_count = 0
    for letter in password:
        if letter in upper_characters:
            upper_count += 1
        if letter in lower_characters:
            lower_count += 1
        if letter in special_characters:
            special_count += 1

    if upper_count <= 0 or lower_count <= 0 or special_count <= 0 or \
            len(password) < 6:
        print("not long enough")
        return False

    # length username
    if len(name) <= 2 or len(name) >= 20:
        return False

    # checking username requirements
    # getting rid of all whitespace to use .isalnum properly
    temp_name = name.replace(" ", "")

    if name[0] == " " or name[-1] == " " or temp_name.isalnum() is not True:
        return False

    # create a new user
    user = User(username=name, email=email, password=password)
    # add it to the current database session
    db.session.add(user)
    # generate random ID for user
    user.id = str(uuid.uuid1())
    print("Printing the user id: ", user.id)
    user.balance = 100
    print("added 100")

    # actually save the object
    db.session.commit()

    return True


def login(email, password):
    """
    Check login information
      Parameters:
        email (string):    user email
        password (string): user password
      Returns:
        The user object if login succeeded otherwise None
    """
    # validating the email follows RFC 5322
    try:
        validate_email(email).email
    except EmailNotValidError as errorMsg:
        print(str(errorMsg))
        return None

    # checking for password requirements
    upper_count = 0
    lower_count = 0
    special_count = 0

    password = str(password)
    for letter in password:
        if letter in upper_characters:
            upper_count += 1
        if letter in lower_characters:
            lower_count += 1
        if letter in special_characters:
            special_count += 1

    if upper_count <= 0 or lower_count <= 0 or special_count <= 0 or \
            len(password) < 6:
        print("password invalid")
        return None

    valids = User.query.filter_by(email=email, password=password).all()
    if len(valids) != 1:
        return None
    return valids[0]
