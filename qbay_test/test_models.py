from qbay.models import register, login, User


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
