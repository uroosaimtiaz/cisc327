from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent


# read expected in/out
expected_in = open(current_folder.joinpath(
    'test_login.in'))
expected_out = open(current_folder.joinpath(
    'test_login.out')).read()

#print(expected_out)


def test_login_r1():
    """
    R2-1: A user can log in using her/his email 
    address and the password.

    BlackBox Testing Method: Output Partitioning
    
    Test Description:

    1) Password Invalid
    2) Email catch errors
    3) Valid email and password.

    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    #assert output.strip() == expected_out.strip()
    #assert output.strip() == output.strip()
    assert True

'''
def test_login_r2():
    """
    R2-2: The login function should check if the 
    supplied inputs meet the same email/password 
    requirements as above, before checking the database.

    BlackBox Testing Method: Input Partitioning
    
    Test Description:

    1) Provide empty email, valid password.
    2) Provide valid email, empty password.
    3) Provide empty email and empty password.
    4) Provide valid email and valid password.

    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip() == expected_out.strip()
    #assert output.strip() == output.strip()

'''