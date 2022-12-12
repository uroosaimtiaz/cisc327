from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent


def test_booking_r1():
    """
    R2-1: A user can book a listing.
    
    Test Description:

    Successfully register seller account and buyer account.
    Create listing from seller account.
    Buyer is able to book the listing.

    """

    # read expected in/out
    expected_in = open(current_folder.joinpath(
                       'test_booking.in'))
    expected_out = open(current_folder.joinpath(
                        'test_booking.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('test_booking_r1')
    assert output.strip() == expected_out.strip()


def test_booking_r2():
    """
    R2-2: A user cannot book a listing for his/her listing.
    
    Test Description:

    Login to seller account and attempt to book
    his own listing. Booking cannot be created.

    """

    # read expected in/out
    expected_in = open(current_folder.joinpath(
                       'test_booking_r2.in'))
    expected_out = open(current_folder.joinpath(
                        'test_booking_r2.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('test_booking_r2')
    assert output.strip() == expected_out.strip()


def test_booking_r3():
    """
    R2-3: A user cannot book a listing that is 
    already booked with the overlapped dates.
    
    Test Description:

    Successfully register a new buyer account.
    New buyer attempts to book listing from
    seller with overlapping dates. Booking
    is unavailable.

    """

    # read expected in/out
    expected_in = open(current_folder.joinpath(
                       'test_booking_r3.in'))
    expected_out = open(current_folder.joinpath(
                        'test_booking_r3.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbay'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('test_booking_r3')
    assert output.strip() == expected_out.strip()