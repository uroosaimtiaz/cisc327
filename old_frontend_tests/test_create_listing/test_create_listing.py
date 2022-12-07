from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent


# read expected in/out
expected_in_1 = open(current_folder.joinpath(
                     'test_create_listing.in'))
expected_out_1 = open(current_folder.joinpath(
                      'test_create_listing.out')).read()
expected_in_2 = open(current_folder.joinpath(
                     'test_create_listing_2.in'))
expected_out_2 = open(current_folder.joinpath(
                      'test_create_listing_2.out')).read()
expected_in_3 = open(current_folder.joinpath(
                     'test_create_listing_3.in'))
expected_out_3 = open(current_folder.joinpath(
                      'test_create_listing_3.out')).read()
expected_in_4 = open(current_folder.joinpath(
                     'test_create_listing_4.in'))
expected_out_4 = open(current_folder.joinpath(
                      'test_create_listing_4.out')).read()


def test_create_listing_r1_2():
    """ R4-1: The title of the product has to be 
        alphanumeric-only, and space allowed only if it 
        is not as prefix and suffix.
        R4-2: The title of the product is no longer 
        than 80 characters.

        Output Partitioning
        test title:
            - incorrect title length
            - title contains illegal characters
            - User already has a listing with same title
            - The listing title was longer than description.          
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_1,
        capture_output=True,
    ).stdout.decode()

    print('test_update_listing_r1_2')
    assert output.strip() == expected_out_1.strip()


def test_create_listing_r3_4():
    """ R4-3: The description of the product can be 
        arbitrary characters, with a minimum length of 
        20 characters and a maximum of 2000 characters.
        R4-4: Description has to be longer than the 
        product's title.

        Output partitioning:
        test description:
            - Description must be over 20 characters.
            - Description is incorrect length.
            - Description must be longer than title
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_2,
        capture_output=True,
    ).stdout.decode()

    print('test_update_listing_r3_4')
    assert output.strip() == expected_out_2.strip()


def test_create_listing_r5_6_7():
    """ R4-5: Price has to be of range [10, 10000].
        R4-6: last_modified_date must be after 
        2021-01-02 and before 2025-01-02.
        R4-7: owner_email cannot be empty. 
        The owner of the corresponding product 
        must exist in the database.

        R4-6 and R4-7 cannot be tested on the
        frontend because the conditions to create
        test cases with different outcomes are not
        possible.

        Input partitioning:
        test price:
            - price is less than 10
            - price is greater than 10000
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_3,
        capture_output=True,
    ).stdout.decode()

    print('test_update_listing_r5')
    assert output.strip() == expected_out_3.strip()


def test_create_listing_r8():
    """ R4-8: A user cannot create products 
        that have the same title.

        Functionality testing:
        attempt to create identical products
    """

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in_4,
        capture_output=True,
    ).stdout.decode()

    print('test_update_listing_r8')
    assert output.strip() == expected_out_4.strip()