from turtle import up
from qbay import app
from flask_sqlalchemy import SQLAlchemy
import string
from email_validator import validate_email, EmailNotValidError
import uuid
from datetime import date

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


class Listing(db.Model):
    id = db.Column(db.String, unique=True, primary_key=True)
    title = db.Column(
        db.String(80), nullable=False)
    description = db.Column(
        db.String(2000), nullable=False)
    price = db.Column(
        db.Integer, nullable=False)
    last_modified_date = db.Column(
        db.Date)
    owner_id = db.Column(
        db.String, nullable=False)

    def __repr__(self):
        return '<Listing %r>' % self.title


class Booking(db.Model):
    id = db.Column(db.String, unique=True, primary_key=True)
    price = db.Column(
        db.Integer, nullable=False)
    listing_id = db.Column(
        db.String, nullable=False)
    user_id = db.Column(
        db.String, nullable=False)
    date = db.Column(
        db.Date)

    def __repr__(self):
        return '<Booking %r>' % self.id


class Review(db.Model):
    id = db.Column(db.String, unique=True, primary_key=True)
    review_text = db.Column(
        db.String(2000), nullable=False)
    listing_id = db.Column(
        db.String, nullable=False)
    user_id = db.Column(
        db.String, nullable=False)
    date = db.Column(
        db.Date)

    def __repr__(self):
        return '<Review %r>' % self.review_text


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
        print("User with email already exists.")
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
        print("Password must be at least 6 characters long, and inlude an"
            "uppercase character, lowercase character, and a special character. \n")
        return False

    # length username
    if len(name) <= 2 or len(name) >= 20:
        print("Username must be between 3-19 characters long.\n")
        return False

    # checking username requirements
    # getting rid of all whitespace to use .isalnum properly
    temp_name = name.replace(" ", "")

    if name[0] == " " or name[-1] == " " or temp_name.isalnum() is not True:
        print("Username can only contain alphanumeric characters and"
        " cannot begin or end with a ' '. \n")
        return False

    # create a new user
    user = User(username=name, email=email, password=password)
    # add it to the current database session
    db.session.add(user)
    # generate random ID for user
    user.id = str(uuid.uuid1())
    user.balance = 100
    print("\nRegistration Gift: We have given you a credit of $100 dollars.")

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
        print("Password invalid.")
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


def create_listing(owner_email, password, title, description, price):
    """
    Create a new listing
      Parameters:
        owner_email (string):   email of the owner
        password (string):      password of the owner
        title (string):         listing title
        description (string):   listing description
        price (integer):        listing price
      Returns:
        Listing if successfully created or None
    """

    # user must provide correct credentials to login
    user = login(owner_email, password)

    # if user fails to login no changes can be made
    if user is None:
        print("User does not exist or login unsuccessful.")
        return None

    # title must be between 1 and 80 characters
    if len(title) > 80:
        print("Incorrect Title length.")
        return None
    if len(title) == 0:
        print("Incorrect Title length.")
        return None

    # title must contain only alphanumeric chars
    temp_title = title.replace(" ", "")

    # title cannot have " " prefix or suffix
    if title[0] == " " or title[-1] == " " or temp_title.isalnum() is not True:
        print("Title contains illegal characters.")
        return None

    # description must be between 20 and 2000 characters
    if len(description) > 2000:
        print("Description is incorrect length.")
        return None
    if len(description) < 20:
        print("Description is incorrect length.")
        return None

    # description must be longer than title
    if len(description) < len(title):
        print("Description must be longer than title.")
        return None

    # price has to be between 10 and 10000
    if price > 10000:
        print("Price out of range")
        return None
    if price < 10:
        print("Price out of range")
        return None

    # today date must be after 2021-01-02
    # and before 2025-01-02
    today = date.today()
    print(today)
    if 2025 < today.year < 2021:
        print("Year out of range.")
        return None
    if today.year == 2021:
        if today.month == 1 and today.day < 3:
            print("Cannot be before 2021-01-03")
            return None
    if today.year == 2025:
        if today.month > 1 and today.day > 1:
            print("Cannot be after 2025-01-01")
            return None

    # user cannot have more than one listing
    # with the same title
    existing_listing = Listing.query.filter_by(owner_id=owner_email,
                                               title=title).all()
    if len(existing_listing) != 0:
        print("User already has a listing with same title.")
        return None

    # create listing
    listing = Listing(title=title, description=description, price=price,
                      owner_id=owner_email)
    db.session.add(listing)
    print("Listing created: ", listing.title)

    # set unique id for listing
    listing.id = str(uuid.uuid1())
    print("Listing id created: ", listing.id)

    # set last modified date for listing
    listing.last_modified_date = today
    print("Listing date: ", listing.last_modified_date)

    db.session.commit()

    return listing


def get_listing(list_id):
    """
    Find an existing listing
        Parameters:
        list_id (string):       unique id of listing
        Returns:
        Listing if exists or None
    """
    valids = Listing.query.filter_by(id=list_id).all()
    if len(valids) != 1:
        return None
    return valids[0]


def update_listing(email, password, id, title, utitle, description,
                   udescription, price, uprice):
    """
    Update an existing listing
        Parameters:
        email (string):         email of the owner
        password (string):      password of the owner
        title (string):         listing title
        description (string):   listing description
        price (integer):        listing price
        Returns:
        Listing if successfully updated or None
    """
    # user must provide correct credentials to login
    user = login(email, password)

    # if user fails to login no changes can be made
    if user is None:
        print("User does not exist or login unsuccessful.")
        return None

    # find listing to be modified
    listing = get_listing(id)
    if listing is None:
        print("Listing was not found.")
        return None

    # code will only execute if request title update
    if utitle:
        print("Title update requested.")
        # title must be between 1 and 80 characters
        if len(title) > 80:
            print("Incorrect Title length.")
            return None
        if len(title) == 0:
            print("Incorrect Title length.")
            return None

        # title must contain only alphanumeric chars
        temp_title = title.replace(" ", "")

        # title cannot have " " prefix or suffix
        if title[0] == " " or title[-1] == " " or\
                temp_title.isalnum() is not True:
            print("Title contains illegal characters.")
            return None

        # user cannot have more than one listing
        # with the same title
        existing_listing_title = Listing.query.filter_by(owner_id=email,
                                                         title=title).all()
        if len(existing_listing_title) != 0:
            print("User already has a listing with same title.")
            return None

        #  check title length against description
        if not udescription and len(title) > len(listing.description):
            print("The listing title was longer than description.")
            return None

        # update title
        listing.title = title

    if udescription:
        print("Description update requested.")

        # description must be between 20 and 2000 characters
        if len(description) > 2000:
            print("Description is incorrect length.")
            return None
        if len(description) < 20:
            print("Description is incorrect length.")
            return None

        # description must be longer than title
        if len(description) < len(listing.title):
            print("Description must be longer than title.")
            return None

        #  check length of description against title
        if len(description) < len(listing.title):
            print("The listing title was longer than description.")
            return None

        # update description
        listing.description = description

    if uprice:
        print("Price update requested.")

        # price has to be between 10 and 10000
        if price > 10000:
            print("Price out of range")
            return None
        if price < 10:
            print("Price out of range")
            return None

        # price can only increase or stay same from listing amount
        if listing.price > price:
            print("Price can only increased, not decreased.")
            return None

        # update price
        listing.price = price

    # today date must be after 2021-01-02
    # and before 2025-01-02
    today = date.today()
    print(today)
    if 2025 < today.year < 2021:
        print("Year out of range.")
        return None
    if today.year == 2021:
        if today.month == 1 and today.day < 3:
            print("Cannot be before 2021-01-03")
            return None
    if today.year == 2025:
        if today.month > 1 and today.day > 1:
            print("Cannot be after 2025-01-01")
            return None

    # update last modified date
    if utitle or udescription or uprice:
        listing.last_modified_date = today

    db.session.commit()
    return listing
