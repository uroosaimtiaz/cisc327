from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent


def test_login_r1():
    """
    R2-1: A user can log in using her/his email 
    address and the password.

    BlackBox Testing Method: Functionality Testing
    
    Test Description:

    Successfully register account and log in.

    Account with wrong password or doesn't exist
    cannot log in.

    """

    # read expected in/out
    expected_in = open(current_folder.joinpath(
                       'test_login.in'))
    expected_out = open(current_folder.joinpath(
                        'test_login.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('test_login_r1')
    assert output.strip() == expected_out.strip()


def test_login_r2():
    """
    R2-2: The login function should check if the 
    supplied inputs meet the same email/password 
    requirements as above, before checking the database.

    BlackBox Testing Method: Input Partitioning
    
    Test Description:

    We do not need to create any accounts to check
    this functionality as we want to ensure that 
    error messages are given based on inputs
    prior to actually checking the database
    whether the account actually exists.

    1) Provide empty email, empty password.
    2) Invalid email, valid password (3 from below):
        - inappropriate domain extension (eg. @domain.q)
        - more than one @ symbol or empty or no @ symbol
        - email contains invalid characters before @-sign
            - .
            - email contains space
            - email contains left/right square bracket
    2) Provide valid email, empty password.
    3) Provide valid email, password <6 chars
    4) Provide valid email, password >6chars no uppercase
    5) Provide valid email, password >6chars no lowercase
    6) Provide valid email, password >6chars no special char
    7) Provide empty email and valid password.

    """

    # read expected in/out
    expected_in = open(current_folder.joinpath(
                       'test_login_r2.in'))
    expected_out = open(current_folder.joinpath(
                        'test_login_r2.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('test_login_r2')
    assert output.strip() == expected_out.strip()
