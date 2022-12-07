from qbay.models import get_listings, register, get_users, create_listing
from qbay.models import login, return_user_listings, update_listing, \
    update_user, create_booking, update_balance, return_all_listings, \
    get_listing

'''
    This file creates the different screens or pages a user
    will use to interact with the database, including
    creating an account, logging in, creating a listing
    and more.
'''


def login_page():
    """
        This screen prompts the user to login to their
        account by entering their username and password.
    """
    #  get email from user input
    email = input('Please enter your email: ')
    #  get password from user input
    password = input('Please enter your password: ')
    #  calls login function which returns a User
    return login(email, password)


def register_page():
    """
        This screen prompts the user to register by providing
        a valid username, email, and password.
    """
    print('\nThank you for registering with qb&b.\n')
    #  get username from user input
    name = input('Please enter a valid username: ')
    #  get email from user input
    email = input('Please enter a valid email address: ')
    #  get password from user input
    password = input('Please enter a valid password: ')
    #  get the same password again
    password_twice = input('Please enter the password again: ')
    #  if both passwords match, registration successful
    if password != password_twice:
        print('Password entered not the same.')
    #  calls the register function which will return True if successful
    elif register(name, email, password):
        print('Registration successful.')
    #  if register returns False then registration failed
    else:
        print('Registration failed.')


def create_listing_page(email, password):
    """
        This screen prompts the user to create a listing by providing
        a valid title, description, and price.
    """
    print('\nThank you for creating a listing with qb&b.\n')
    
    title = ""
    while len(title) < 1:
        title = input('Please enter a valid title for the listing: ')
    
    desc = input('Please enter a valid description for the listing: ')
    while len(desc) < 20:
        desc = input('Description must be over 20 characters.\n'
                     'Please enter a valid description for the listing: ')
    
    price = int(input('Please enter a valid price for the listing: '))
    while price < 10:
        price = int(input('Price must be at least 10.\n'
                          'Please enter a valid price for the listing: '))
    
    if create_listing(email, password, title, desc, price):
        print("Listing created successfully")
    else:
        print("Listing creation FAILED")


def update_listing_page(email, password):
    """
        This screen prompts the user to choose a listing and decide
        what attributes of the listing they would like to change and
        make updates by providing a valid title, description, and price.
    """
    listings = return_user_listings(email)
    if len(listings) == 0:
        print("This user has no existing listings")
    else:
        print('Here are all the listings associated with this user: \n')
        for i in range(len(listings)):
            print(f'{(i + 1)}. {listings[i].title}')
        selection = int(input('Please select the listing you want to update:'))
        if 0 < selection <= len(listings):
            print(f'you selected {listings[(selection - 1)].title}')
            
            utitle = input('Modify Title? Enter 1 [Yes] or 2 [No]: ')
            if int(utitle.strip()) == 1:
                newTitle = input('Enter new Title: ')
                update_listing(email, password, listings[(selection - 1)].id,
                               newTitle, True, '', False, '', False)

            udesc = input('Modify Description? Enter 1 [Yes] or 2 [No]: ')
            if int(udesc.strip()) == 1:
                newDesc = input('Enter new description: ')
                update_listing(email, password, listings[(selection - 1)].id,
                               '', False, newDesc, True, '', False)

            uprice = input('Modify Price? Enter 1 [Yes] or 2 [No]: ')
            if int(uprice.strip()) == 1:
                while True:
                    newPrice = input('Enter new Price: ')
                    if len(newPrice) != 0:
                        update_listing(email, password, 
                                       listings[(selection - 1)].id,
                                       '', False, '', False, 
                                       int(newPrice.strip()), True)
                        break
                    else:
                        print("Please enter a price.")

        else:
            print("\nInvalid input.\n")


def print_all_users():
    """
        function to assist with testing the database.
        it will print all current users in the database
    """
    get_users()


def print_all_listings(owner_id=None):
    """
        function to assist with testing the database.
        it will print all current listings in the database
    """
    get_listings(owner_id)


def update_profile_page():
    """
        This screen prompts the user to update their information.
    """

    new_name = " "
    new_email = " "
    new_billing_address = " "
    new_postal_code = " "
    menuItem = 0

    print("Welcome to the update profile page!\n")

    # User login required for update_user from models.py for validation
    print("Provide your login information. If it is wrong, we will not be "
          "able to update your account.")

    # getting the current email
    old_email = input("Please enter your current email: ")

    # getting the corresponding password to that account
    password = input("Please enter your password: ")

    # checking if user exists in the first part of update_user
    # returns None if user does not exist
    user_info = update_user(old_email, password, new_email, new_name,
                            new_billing_address, new_postal_code, 5)

    if user_info is not None:
        print("Welcome to the update profile page!\n")
        print("**********************************")
        print("*         UPDATE MENU            *")
        print("*   1 - Update Username          *")
        print("*   2 - Update Email             *")
        print("*   3 - Billing address          *")
        print("*   4 - Update Postal Code       *")
        print("**********************************\n\n")

        continue_updating = True  # used to check if user wants to update more
        menuItems = [False, False, False, False]
        
        while continue_updating:
            selection = input("Which information would you like to update: ")
            if selection == '1':
                # updating username
                menuItems[0] = True
                new_name = input(
                    "Please enter a valid new username: ")
            elif selection == '2':
                # updating email
                menuItems[1] = True
                new_email = input(
                    "Please enter a valid new email: ")
            elif selection == '3':
                menuItems[2] = True
                # updating Billing Address
                new_billing_address = input(
                    "Please enter a valid new billing address: ")
            elif selection == '4':
                # updating postal code
                menuItems[3] = True
                new_postal_code = input("Please enter a valid new postal "
                                        "code: ")
            else:
                print("Invalid Menu Item.")

            # prompting the user if they would like to update different option
            add_option = input("\nWould you like to update another option "
                               "('y'/'n')?: ")
            if add_option == 'y':
                # will allow user to choose another option to update
                continue_updating = True
            else:
                # user has finished updating
                continue_updating = False

        #  updating the profile
        if menuItems[0] is True and menuItems[1] is True and \
           menuItems[2] is True and menuItems[3] is True:
            menuItem = 0
            update_user(old_email, password, new_email, new_name,
                        new_billing_address,
                        new_postal_code, menuItem)
        else:
            for i in range(4):
                if menuItems[i] is True:
                    menuItem = i + 1
                    update_user(old_email, password, new_email, new_name,
                                new_billing_address,
                                new_postal_code, menuItem)


def create_booking_page(email, password):
    """
    This screen prompts the user to create a booking by providing a valid
    listing id.
    """
    listings = return_all_listings()

    if (len(listings) == 0):
        print("There are currently no active listings.")
        return

    print('Here are all the listings: \n')
    for i in range(len(listings)):
        print(f'{(i + 1)}. {listings[i].title}')
    
    try:
        selection = int(input('Please select the listing you want to book:'))
    except Exception:
        print("Input could not be resolved into number.")
        return
   
    if selection < 1 or selection > len(listings):
        print("Invalid number.")
        return

    print(f'you selected {listings[(selection - 1)].title}')
    
    listing = get_listing(listings[(selection - 1)].id)

    # listing_id = input('Enter the listing id: ')
    start_date = input('Enter the start date (MM-DD-YYYY): ')
    duration = input('Enter the duration (in days): ')
    if create_booking(email, password, listing.id, 
                      start_date, duration):
        print('Booking created successfully!')
    else:
        print('Booking creation failed.')


def update_balance_page(email, password):
    """
    This screen prompts the user to update their balance.
    """
    amount = input('Enter the amount you want to add to your balance: ')
    if update_balance(email, password, amount):
        print('Your balance has been updated.')
    else:
        print('Your balance could not be updated.')