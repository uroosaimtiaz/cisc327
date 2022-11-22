from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent


# read expected in/out
expected_in_1 = open(current_folder.joinpath(
                     'test_update_profile.in'))
expected_out_1 = open(current_folder.joinpath(
                      'test_update_profile.out')).read()
expected_in_2 = open(current_folder.joinpath(
                     'test_update_profile_2.in'))
expected_out_2 = open(current_folder.joinpath(
                      'test_update_profile_2.out')).read()
expected_in_3 = open(current_folder.joinpath(
                     'test_update_profile_3.in'))
expected_out_3 = open(current_folder.joinpath(
                      'test_update_profile_3.out')).read()


def test_update_profile_r1():
    """ R3-1: A user is only able to update his/her
         user name, user email, billing address, 
         and postal code.        

         Functionality testing.
         Will register user and successfully change
         details.
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_1,
        capture_output=True,
    ).stdout.decode()

    print('test_update_profile_r1')
    assert output.strip() == expected_out_1.strip()


def test_update_profile_r2_3():
    """ R3-2: postal code should be non-empty,
        alphanumeric-only, and no special 
        characters such as !.

        R3-3: Postal code has to be a valid 
        Canadian postal code.

        Output partitioning:
        test description:
            - Postal code must be 7 characters.
            - Invalid postal code:
            Postal code must follow pattern
            capital letter-number-capital letter
            space repeat
            - Postal code correctly updated
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_2,
        capture_output=True,
    ).stdout.decode()

    print('test_update_profile_2_3')
    assert output.strip() == expected_out_2.strip()


def test_update_profile_r4():
    """ R3-4: User name follows the 
        requirements above.

        Input partitioning:
            - empty username
            - username with non-alphanumeric characters
            - username with space as prefix or suffix
            - username 1-2 characters
            - username longer than 20 characters
            - username between 3-19 chars with alphanumeric
              characters and no space as prefix and suffix
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_3,
        capture_output=True,
    ).stdout.decode()

    print('test_update_profile_r4')
    assert output.strip() == expected_out_3.strip()