from qbay.models import create_booking, register, create_listing, login
from datetime import date


def test_r1_1_create_booking():
    """
        Testing R1-1: Checking to see if booking can be made when done properly
    """
    #  create listing
    seller = register("sellerr1", "sellerr1@test.com", "Password123!")
    listing = create_listing("sellerr1@test.com", "Password123!",
                             "This is an example title",
                             "This is an example description", 50)
    
    #   create buyer
    buyer = register("buyerr1", "buyerr1@test.com", "Password123!")

    #   book
    booking = create_booking("buyerr1@test.com", "Password123!", listing.id,
                             "11-11-2022", 1)

    assert booking is not None


def test_r1_2_create_booking():
    """
        Testing R1-2:   Checking to see if booking cannot be made when its the
                        user's listing
    """
    #  create listing
    seller = register("sellerr2", "sellerr2@test.com", "Password123!")
    listing = create_listing("sellerr2@test.com", "Password123!",
                             "This is an example title",
                             "This is an example description", 50)

    #   book
    booking = create_booking("sellerr2@test.com", "Password123!", listing.id,
                             "11-11-2022", 1)

    assert booking is None


def test_r1_3_create_booking():
    """
        Testing R1-3:   Checking to see if booking cannot be made when it costs
                        more than the user's balance
    """
    #  create listing
    seller = register("sellerr3", "sellerr3@test.com", "Password123!")
    listing = create_listing("sellerr3@test.com", "Password123!",
                             "This is an example title",
                             "This is an example description", 500)

    #   create buyer
    register("buyerr3", "buyerr3@test.com", "Password123!")
    buyer = login("buyerr3@test.com", "Password123!")

    assert buyer.balance is not None
    assert buyer.balance < listing.price

    #   book
    booking = create_booking("sellerr2@test.com", "Password123!", listing.id,
                             "11-11-2022", 1)

    assert booking is None


def test_r1_4_create_booking():
    """
        Testing R1-4:   Checking to see if booking cannot be made when it is
                        already booked on the requested dates
    """
    #  create listing
    seller = register("sellerr4", "sellerr4@test.com", "Password123!")
    listing = create_listing("sellerr4@test.com", "Password123!",
                             "This is an example title",
                             "This is an example description", 50)

    #   create buyer 1
    register("buyerr4b1", "buyerr4b1@test.com", "Password123!")

    #   book with buyer 1
    booking1 = create_booking("buyerr4b1@test.com", "Password123!", listing.id,
                              "11-11-2022", 1)
    
    #   create buyer 2
    register("buyerr4b2", "buyerr4b2@test.com", "Password123!")

    #   book with buyer 2
    booking2 = create_booking("buyerr4b2@test.com", "Password123!", listing.id,
                              "11-11-2022", 1)

    assert booking1 is not None        
    assert booking2 is None