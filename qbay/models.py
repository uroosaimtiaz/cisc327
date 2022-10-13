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
    """
    Register a new user
      Parameters:
        name (string):     user name
        email (string):    user email
        password (string): user password
      Returns:
        True if registration succeeded otherwise False
    """
    # check if the email has been used:
    existed = User.query.filter_by(email=email).all()
    if len(existed) > 0:
        print("existed1")
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
        print("not long enough")
        return False

    # checking username requirements
    # getting rid of all whitespace to use .isalnum properly
    temp_name = name.replace(" ", "")

    if name[0] == " " or name[-1] == " " or temp_name.isalnum() is not True:
        print("name error")
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


def update_user(old_email, password, new_email, new_name, new_billing_address,
                new_postal_code):
    """
    Update User Profile
      Parameters:
        old_email (string):     existing user email
        password (string):      existing user password
        new_email (string):     new user email
        new_name (string):      new username
        new_billing_address (string):   user billing address
        new_postal_code (string):   user postal code
      Returns:
        The user object if user is able to login and make changes
        to email, username, billing address, and postal code.
    """
    # user must provide correct credentials to login
    user = login(old_email, password)

    # if user fails to login no changes can be made
    if user is None:
        print("User does not exist or login unsuccessful.")
        return None

    if new_email != " ":
        # the new email requested cannot already be in use
        existed = User.query.filter_by(email=new_email).all()
        if len(existed) > 0:
            print("This email already is taken.")
            return None

        # the new email requested must follow RFC 5322 style
        try:
            validate_email(new_email).email
        except EmailNotValidError as errorMsg:
            print(str(errorMsg))
            return None

        # new user email is updated
        user.email = new_email

    # new username must be between 2 and 20 characters long
    if 20 <= len(new_name) <= 2:
        print("New username cannot be empty or incorrect length.")
        return None

    # remove all spaces in new username to use isalnum()
    temp_name = new_name.replace(" ", "")

    # new username cannot have a " " as prefix or suffix
    # new username cannot contain non-alphanumeric characters besides " "
    if new_name == " ":
        print("username not updated")
    elif len(new_name) >= 2 and new_name[0] == " " or new_name[-1] == " " or \
            temp_name.isalnum() is not True:
        print("New username cannot contain spaces as prefix or suffix.")
        return None
    else:
        # new username is updated
        user.username = new_name

    # new user billing address is updated
    user.billing_address = new_billing_address

    # new postal code but be valid CDN postal code
    if new_postal_code == " ":
        print("postal code not changed")
    elif len(new_postal_code) != 7:
        print("Postal code must be 7 characters.")
        return None
    elif not new_postal_code[0] in upper_characters:
        print("invalid postal code")
        return None
    elif not new_postal_code[1] in "0123456789":
        print("invalid postal code")
        return None
    elif not new_postal_code[2] in upper_characters:
        print("invalid postal code")
        return None
    elif new_postal_code[3] != " ":
        print("invalid postal code")
        return None
    elif not new_postal_code[4] in "0123456789":
        print("invalid postal code")
        return None
    elif not new_postal_code[5] in upper_characters:
        print("invalid postal code")
        return None
    elif not new_postal_code[6] in "0123456789":
        print("invalid postal code")
        return None

    else:
        # new user postal code is updated
        user.postal_code = new_postal_code

    # all user changes are committed to database
    db.session.commit()
    return user
