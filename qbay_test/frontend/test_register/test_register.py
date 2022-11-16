from os import popen
from pathlib import Path
import subprocess
from qbay.models import register, login, User, update_user
from qbay.models import Listing, create_listing, update_listing

# get expected input/output file
current_folder = Path(__file__).parent


def test_register_r1():
    """
    R1-1: Email cannot be empty. password cannot be empty.

    BlackBox Testing Method: Input Testing
    
    Test Description:

    1) Provide empty email, valid password.
    2) Provide valid email, empty password.
    3) Provide empty email and empty password.
    4) Provide valid email and valid password.

    """
    # read expected in/out
    expected_in = open(current_folder.joinpath(
    'test_register_r1.in'))
    expected_out = open(current_folder.joinpath(
    'test_register_r1.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('test_register_r1')
    assert output.strip() == expected_out.strip()


def test_register_r2():
    """
    R1-2: A user is uniquely identified by his/her user id - 
    automatically generated.

    BlackBox Testing Method: None

    Test Description:
        
    Each user's id is assigned and used internally and not
    accessible to the user via frontend; therefore is not
    included in frontend testing.

    BlackBox testing assumes no knowledge of internal tools.
    """


def test_register_r3():
    """
    The email has to follow addr-spec defined in RFC 5322 
    (see https://en.wikipedia.org/wiki/Email_address for a 
    human-friendly explanation). You can use external libraries/imports.

    BlackBox Testing Method: Output Partitioning (non-exhaustive)

    Per Wiki:
    The local-part of the email address may contain
    A-Z a-z 0-9 !#$%&'*+-/=?^_`{|}~ and . if it is
    not first or last character and does not appear 
    consequtively.

    Followed by @domain.ext where ext is an existing
    extension such as .com, .ca, .net, and so on.
    
    Test Description:

    1)  Provide invalid email, valid password.
        User should not be registered.
        - Possible:
            - inappropriate domain extension (eg. @domain.q)
            - more than one @ symbol or empty or no @ symbol
            - email contains invalid characters before @-sign
                - .
                - email contains space
                - email contains left/right square bracket
    2)  Provide valid email, valid password. 
        User should be successfully registered.

    """
    # read expected in/out
    expected_in = open(current_folder.joinpath(
    'test_register_r3.in'))
    expected_out = open(current_folder.joinpath(
    'test_register_r3.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('test_register_r3')
    assert output.strip() == expected_out.strip()
    #assert output.strip() == output.strip()


def test_register_r4():
    """
    R1-4: Password has to meet the required complexity:
    minimum length 6, at least one upper case, at least one 
    lower case, and at least one special character.

    Special characters are those in string.punctuation

    BlackBox Testing Method: Input Partitioning
    
    Test Description:

    1) Valid email, password less than 6 characters
    2) Valid email, password>=6 char, contains at least
       one lower/special character but no upper case
    3) Valid email, password>=6 char, contains at least
       one upper/special character but no lower case
    4) Valid email, password>=6 char, contains at least
       one lower/upper character but no special
    5) Valid email, password>= 6 char with upper/lowercase
       and special character

    """
    # read expected in/out
    expected_in = open(current_folder.joinpath(
    'test_register_r4.in'))
    expected_out = open(current_folder.joinpath(
    'test_register_r4.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()
    
    print('test_register_r4')

    assert output.strip() == expected_out.strip()
    #assert output.strip() == output.strip()



def test_register_r5_6():
    """
    R1-5: User name has to be non-empty, alphanumeric-only,
    and space allowed only if it is not as the 
    prefix or suffix.

    R1-6: User name has to be longer than 2 characters 
    and less than 20 characters.

    BlackBox Testing Method: Input Partitioning
    
    Test Description:

    1) empty username
    2) username < 2 chars
    3) username 2-20 chars with non-alphanumeric characters
    4) username 2-20 chars with space as prefix or suffix or both
    5) username >20 chars
    6) username 2-20 chars with only alphanumeric characters

    """
    # read expected in/out
    expected_in = open(current_folder.joinpath(
    'test_register_r5_6.in'))
    expected_out = open(current_folder.joinpath(
    'test_register_r5_6.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('test_register_r5_6')

    assert output.strip() == expected_out.strip()
    #assert output.strip() == output.strip()


def test_register_r7():
    """
    R1-7: If the email has been used, the operation failed.

    BlackBox Testing Method: Functionality Testing
    
    Test Description:

    Successfully create account with email. 
    Fail to create second account with same email.

    """
    # read expected in/out
    expected_in = open(current_folder.joinpath(
    'test_register_r7.in'))
    expected_out = open(current_folder.joinpath(
    'test_register_r7.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('test_register_r7')

    assert output.strip() == expected_out.strip()
    #assert output.strip() == output.strip()

'''
def test_register_r8_9_10():
    """
    R1-8: Shipping address is empty at the time of registration.

    R1-9: Postal code is empty at the time of registration.

    R1-10: Balance should be initialized as 100 at the time of 
    registration. (free $100 dollar signup bonus).

    BlackBox Testing Method: None

    Test Description:
        
    At the time of registration, the shipping address and 
    postal code is automatically set to empty internally 
    and no user input is taken; user shipping address not 
    accessible to the user via frontend yet; therefore is not
    included in frontend testing.

    At the current time, there is no way to view user profile
    with current balance from frontend therefore it is also
    not included in testing.

    BlackBox testing assumes no knowledge of internal tools.
    """
'''