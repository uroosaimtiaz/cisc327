from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent


# read expected in/out
expected_in_1 = open(current_folder.joinpath(
    'test_update_listing.in'))
expected_out_1 = open(current_folder.joinpath(
    'test_update_listing.out')).read()

expected_in_2 = open(current_folder.joinpath(
    'test_update_listing_2.in'))
expected_out_2 = open(current_folder.joinpath(
    'test_update_listing_2.out')).read()

expected_in_4 = open(current_folder.joinpath(
    'test_update_listing_4.in'))
expected_out_4 = open(current_folder.joinpath(
    'test_update_listing_4.out')).read()


def test_r5_1_update_listing():
    """Functionality testing:
        checks that all attributes can be modified.
        except owner_id and last_modified date"""

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_1,
        capture_output=True,
    ).stdout.decode()

    print('test_update_listing_r1')
    assert output.strip() == expected_out_1.strip()


def test_r5_2_update_listing():
    """ R5-2: Price can be only increased but cannot 
        be decreased
        Input Partitioning:
            1. price is the same
            2. price is greater
            3. price is lower
            4. price is empty

        R5-3: last_modified_date should be updated 
        when the update operation is successful.

        This can be seen in test 2 (functionality)

        This is not done in any other test where
        the price was not successfully changed.
        """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_2,
        capture_output=True,
    ).stdout.decode()

    print('test_update_listing_r2_3')
    assert output.strip() == expected_out_2.strip()


def test_r5_2_4_update_listing():
    """checks that inputs meet requirements above
    Output Partitioning
        test title:
            - incorrect title length
            - title contains illegal characters
            - User already has a listing with same title
            - The listing title was longer than description.
        test description:
            - Description is incorrect length.
            - Description must be longer than title.
        test price:
            - Price out of range
        """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_4,
        capture_output=True,
    ).stdout.decode()

    print('test_update_listing_4')
    assert output.strip() == expected_out_4.strip()