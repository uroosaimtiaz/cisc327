from qbay.models import register, login, User, update_user
from qbay.models import Listing, create_listing, update_listing


def test_r1_1_user_register():
    """
    Testing R1-1: If the email or password is empty, opeation failed.
    """

    assert register('user1', 'test2@test.com', 'goodPass.123') is True
    assert register('user2', 'test3@test.com', '') is False
    assert register('user2', '', 'goodPass.123') is False
    assert register('user2', '', '') is False


def test_r1_2_user_register():
    """
    Testing R1-2: Checking that the user id is unique.
    """

    register('user20', 'test20@test.com', 'goodPass.123')

    register('user21', 'test21@test.com', 'goodPass.123')

    register('user22', 'test22@test.com', 'goodPass.123')

    register('user23', 'test23@test.com', 'goodPass.123')

    user20 = User.query.filter_by(username='user20').first()

    user21 = User.query.filter_by(username='user21').first()

    user22 = User.query.filter_by(username='user22').first()

    user23 = User.query.filter_by(username='user23').first()

    if user20.id == user21.id == user22.id == user23.id:
        assert False, "The id's are not unique"
    else:
        assert True, "ID's are unique"


def test_r1_3_user_register():
    """
    Testing R1-3: email has to follow RFC-5322
    """

    assert register('user2', 'test42@test.com', 'goodPass.123') is True
    assert register('user2', 'test4@test.', 'goodPass.123') is False
    assert register('user2', 'te@st5@test.com', 'goodPass.123') is False


def test_r1_4_user_register():
    """
    Testing R1-4: password must meet certain requirements
    """

    assert register('user3', 'test51@test.com', 'goodPass.123') is True
    assert register('user3', 'test6@test.com', 'goodPass') is False
    assert register('user3', 'test6@test.com', 'gggg') is False
    assert register('user3', 'test6@test.com', 'grand.444') is False


def test_r1_5_user_register():
    """
    Testing R1-5: username must meet certain requirements
    """

    assert register('good 123 name', 'test61@test.com', 'goodPass.123') is True
    assert register('badusername ', 'test7@test.com', 'goodPass.123') is False
    assert register(' badusername', 'test7@test.com', 'goodPass.123') is False
    assert register(' badusername ', 'test7@test.com', 'goodPass.123') is False
    assert register('', 'test7@test.com', 'goodPass.123') is False
    assert register('bad$%ername', 'test7@test.com', 'goodPass.123') is False


def test_r1_6_user_register():
    """
    Testing R1-6: username must be more than 2 character and less than 20
    otherwise failure
    """

    assert register('user6', 'test7@test.com', 'goodPass.123') is True
    assert register('u0', 'test8@test.com', 'goodPass.123') is False
    assert register('123456789012345678910',
                    'test8@test.com', 'goodPass.123') is False


def test_r1_7_user_register():
    """
    Testing R1-7: If the email has been used, the operation failed.
    """

    assert register('user0', 'test0@test.com', 'goodPass.123') is True
    assert register('user0', 'test1@test.com', 'goodPass.123') is True
    assert register('user1', 'test0@test.com', 'goodPass.123') is False


def test_r1_8_user_register():
    """
    Testing R1-8: billing address must be empty at registration.
    """

    register('user9', 'test9@test.com', 'goodPass.123')

    register('user10', 'test10@test.com', 'goodPass.123')

    user9 = User.query.filter_by(username='user9').first()

    if user9.billing_address is None:
        assert True, "billing address is empty"

    user10 = User.query.filter_by(username='user10').first()
    if user10.billing_address is not None:
        assert False, "billing address is not empty"


def test_r1_9_user_register():
    """
    Testing R1-9: Postal code must be empty at time of registration
    """

    register('user11', 'test11@test.com', 'goodPass.123')

    register('user12', 'test12@test.com', 'goodPass.123')

    user11 = User.query.filter_by(username='user11').first()

    user12 = User.query.filter_by(username='user11').first()

    if user11.postal_code is None:
        assert True, "postal code is empty"

    if user12.postal_code is not None:
        assert False, "postal code is not empty"


def test_r1_10_user_register():
    """
    Testing R1-10: balance must be 100.00 at time of registration
    """

    register('user13', 'test13@test.com', 'goodPass.123')

    register('user14', 'test14@test.com', 'goodPass.123')

    user13 = User.query.filter_by(username='user13').first()
    user14 = User.query.filter_by(username='user14').first()

    if user13.postal_code is None:
        assert True, "Balance is 100 upon registration"

    if user14.postal_code is not None:
        assert False, "Balance is not 100 upon registration"


def test_r2_1_login():
    """
    Testing R2-1: A user can log in using her/his email address
      and the password.
    (will be tested after the previous test, so we already have test2,
         in database)
    """

    user = login('test2@test.com', 'goodPass.123')
    assert user is not None
    assert user.username == 'user1'

    user = login('test2@test.com', "1234567")
    assert user is None


def test_r2_2_login():
    """
    Testing R2-2: Login requirements meet same email/password requirements
    as register function before checking database.
    """
    user = login("", "")
    assert user is None

    user = login("test0@test.com", "")
    assert user is None

    user = login("", "123456")
    assert user is None

    user = login("test0@test.com", "")
    assert user is None

    user = login("test@@test.com", "1234")
    assert user is None

    user = login('test2@test.com', 'goodPass.123')
    assert user is not None


def test_r3_1_user_update():
    """
    Testing R3-1: A user is only able to update their username, user address,
    email or postal code.
    """

    user = update_user("test2@test.com", "goodPass.123", "test91@test.com",
                       "newUser", "8 Songwood Drive", "M9M 1X3", 0)
    assert user is not None


def test_r3_2_user_update():
    """
        Testing R3-2: A postal code should be non-empty, alphanumeric only,
        and no special characters such as !.
    """
    user = update_user("test9@test.com", "goodPass.123", "",
                       "", "", "", 4)
    assert user is None

    user = update_user("test9@test.com", "goodPass.123", "",
                       "", "", "M9M !X3", 4)
    assert user is None


def test_r3_3_user_update():
    """
        Testing R3-3: Postal code has to be a valid Canadian postal code.
    """
    user = update_user("test9@test.com", "goodPass.123", " ",
                       "", "", "m9M 1X3", 4)
    assert user is None

    user = update_user("test9@test.com", "goodPass.123", " ",
                       "", "", "M9M 2X3", 4)
    assert user is not None


def test_r3_4_user_update():
    """
        Testing R3-4: User name follows the requirements above.
    """
    user = update_user("test91@test.com", "goodPass.123", "test912@test.com",
                       " u!8", "8 Songwood Drive", "M9M 1X3", 1)
    assert user is None

    user = update_user("test91@test.com", "goodPass.123", " ",
                       "user81", "8 Songwood Drive", "M9M 1X3", 1)
    assert user is not None

    user = update_user("test91@test.com", "goodPass.123", " ",
                       " ", "", "M9M 1X3", 1)
    assert user is None


def test_r4_1_create_listing():
    """
        Testing R4-1: Title of the product has to be alphanumeric only
        and space only allowed if it is not suffix or prefix.
    """
    #  create user for testing
    user = register("listuser", "list@test.com", "Password123!")

    #  create a succussful listing associated with user
    listing_1 = create_listing("list@test.com", "Password123!",
                               "This is an example title",
                               "This is an example description", 45)
    assert listing_1 is not None

    #  create a listing with special characters in title
    listing_2 = create_listing("list@test.com", "Password123!",
                               "Title!", "Description", 55)
    assert listing_2 is None

    #  create listing with " " as prefix
    listing_3 = create_listing("list@test.com", "Password123!",
                               " Title", "Description", 22)
    assert listing_3 is None

    #  create listing with " " as suffix
    listing_4 = create_listing("list@test.com", "Password123!",
                               "Title ", "Description", 44)
    assert listing_4 is None


def test_r4_2_create_listing():
    """
        Testing R4-2: Title of the product is no longer than
        80 characters.
    """
    #  create user for testing
    user = register("listuser", "list2@test.com", "Password123!")

    #  create listing with title > 80 characters
    listing_1 = create_listing("list2@test.com", "Password123!",
                               """komswywqqvtebilemnptxvtdwquydxjicytrjgufbrxbt
                lvupibxhweefktvijvvihuotjnjgqwgwzsw""",
                               "Description", 55)
    assert listing_1 is None

    #  create listing with empty title
    listing_2 = create_listing("list2@test.com", "Password123!",
                               "",
                               "Description", 55)
    assert listing_2 is None


def test_r4_3_create_listing():
    """
        Testing R4-3: The description of a product can be
        arbitrary characters, with a minimum length of 20
        characters and a maximum of 2000 characters
    """
    #  create user for testing
    user = register("listuser", "list3@test.com", "Password123!")

    #  create listing with description < 20 characters
    listing_1 = create_listing("list3@test.com", "Password123!",
                               "Title",
                               "f", 55)
    assert listing_1 is None


def test_r4_4_create_listing():
    """
        Testing R4-4: The description of a product must be
        longer than the title.
    """
    #  create user for testing
    user = register("listuser", "list4@test.com", "Password123!")

    #  create title longer than 20 characters and short description
    listing_1 = create_listing("list4@test.com", "Password123!",
                               "This is a very long title longer than "
                               "description",
                               "Only 23 characters here", 55)
    assert listing_1 is None


def test_r4_5_create_testing():
    """
        Testing R4-5: Price has to be of range 10 to 10000.
    """
    #  create user for testing
    user = register("listuser", "list5@test.com", "Password123!")

    #  create listing with price less than 10
    listing_1 = create_listing("list5@test.com", "Password123!",
                               "Example Title",
                               "Only 23 characters here", 5)
    assert listing_1 is None

    #  create listing with price greater than 10000
    listing_2 = create_listing("list5@test.com", "Password123!",
                               "Anothher Example Title",
                               "Only 23 characters here", 12000)
    assert listing_2 is None


def test_r4_7_create_testing():
    """
        Testing R4-7: owner_email cannot be empty.
        The owner of a corresponding product must exist in
        the database.
    """
    #  create user for testing
    user = register("listuser", "list7@test.com", "Password123!")

    #  create listing with empty email
    listing_1 = create_listing("", "Password123!",
                               "Example Title",
                               "Only 23 characters here", 15)
    assert listing_1 is None

    #  create listing with non-existent user
    listing_2 = create_listing("list51@test.com", "Password123!",
                               "Anothher Example Title",
                               "Only 23 characters here", 33)
    assert listing_2 is None


def test_r4_8_create_listing():
    """
        Testing R4-8: User cannot have products that contain the 
        same title.
    """
    #  create listing with same title from same user already in db
    listing_1 = create_listing("list@test.com", "Password123!",
                               "This is an example title",
                               "This is an example description, copied from "
                               "above",
                               45)
    assert listing_1 is None


def test_r5_1_update_listing():
    """
        Testing R5-1: One can update all attributes of the listing, except
        owner_id and last_modified_date.
    """
    #  find an existing listing
    listing = Listing.query.filter_by(owner_id="list@test.com").first()

    #  update an existing listing title
    listing_1 = update_listing("list@test.com", "Password123!", listing.id,
                               "This is a new updated title", True, "", False,
                               0, False)
    assert listing_1 is not None

    #  update an existing listing title, but longer than description
    listing_2 = update_listing("list@test.com", "Password123!", listing.id,
                               "This is a new updated title but it will be "
                               "waaaaaaaay too long",
                               True, "", False, 0, False)
    assert listing_2 is None

    #  update an existing listing title, but title contains illegal characters
    listing_3 = update_listing("list@test.com", "Password123!", listing.id,
                               "This is a new updated title, but it will be "
                               "waaaaaaaay too long",
                               True, "", False, 0, False)
    assert listing_3 is None

    #  update an existing listing title, but don't update title
    listing_4 = update_listing("list@test.com", "Password123!", listing.id,
                               "This is a new updated title, but it will be "
                               "waaaaaaaay too long",
                               False, "", False, 0, False)
    assert listing_4 is not None


def test_r5_2_update_listing():
    """
        Testing R5-2: Price can only be increased not decreased.
    """
    #  find an existing listing
    listing = Listing.query.filter_by(owner_id="list@test.com").first()

    #  update only the price, subtract 1 from it
    listing_1 = update_listing("list@test.com", "Password123!", listing.id,
                               "", False, "", False, listing.price - 1, True)
    assert listing_1 is None

    #  update only the price, increase it
    listing_2 = update_listing("list@test.com", "Password123!", listing.id,
                               "", False, "", False, 1000, True)
    assert listing_2 is not None


def test_r5_4_update_listing():
    """
        Testing R5-4: When updating an attribute, one has to make sure
        that it follows the same requirements above.
    """
    #  find an existing listing
    listing = Listing.query.filter_by(owner_id="list@test.com").first()

    #  update the title and description 
    listing_1 = update_listing("list@test.com", "Password123!", listing.id,
                               "This is the new title it will be long", True,
                               "description short", True, 0, False)
    assert listing_1 is None

    #  update title but it contains " " prefix
    listing_2 = update_listing("list@test.com", "Password123!", listing.id,
                               " This is the new title it will be long", True,
                               "", False, 0, False)
    assert listing_1 is None

    #  update only the description, but it will be too short
    listing_3 = update_listing("list@test.com", "Password123!", listing.id,
                               " ", False, "d", True, 0, False)
    assert listing_1 is None

    #  update the price but it will be out of range
    listing_4 = update_listing("list@test.com", "Password123!", listing.id,
                               " ", False, " ", False, 120000, True)
    assert listing_4 is None

    #  update the price but it will be out of range
    listing_5 = update_listing("list@test.com", "Password123!", listing.id,
                               " ", False, " ", False, 1, True)
    assert listing_5 is None
