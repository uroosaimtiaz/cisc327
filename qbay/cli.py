from qbay.models import get_listings, register, get_users, create_listing
from qbay.models import login, return_user_listings, update_listing, \
    update_user

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
    '''
        This screen prompts the user to create a listing by providing
        a valid title, description, and price.
    '''
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
    '''
        This screen prompts the user to update their listing by providing
        a valid title, description, and price.
    '''
    listings = return_user_listings(email)
    if len(listings) == 0:
        print("This user has no existing listings")
    else:
        print('Here are all the listings associated with this user: \n')
        for i in range(len(listings)):
            print(f'{(i + 1)}. {listings[i].title}')
        selection = int(input('Please select the listing you want to update:'))
        if selection > 0 and selection <= len(listings):
            print(f'you selected {listings[(selection - 1)].title}')
            
            utitle = input('if you wish to modify the title, enter here '
                           '(if you leave it blank it wont change):')
            udesc = input('if you wish to modify the description, enter here'
                          ' (if you leave it blank it wont change):')
            uprice = input('if you wish to modify the price, enter here '
                           '(if you leave it blank it wont change):')
            if len(utitle.strip) == 0:
                utitle = None
            if len(udesc.strip) == 0:
                udesc = None
            if len(uprice.strip) == 0:
                uprice = None
            else:
                uprice = int(uprice)

            update_listing(email, password, listings[(selection - 1)].id, 
                           listings[(selection - 1)].title, utitle, 
                           listings[(selection - 1)].description, udesc, 
                           listings[(selection - 1)].price, uprice)

        else:
            print("\nInvalid input.\n")


def print_all_users():
    '''
        function to assist with testing the database.
        it will print all current users in the database
    '''
    get_users()


def print_all_listings(owner_id=None):
    '''
        function to assist with testing the database.
        it will print all current listings in the database
    '''
    get_listings(owner_id)


def update_profile_page():
    """
        This screen prompts the user to update their information.
    """

    new_name = " "
    new_email = " "
    new_billing_address = " "
    new_postal_code = " "

    print("Welcome to the update profile page!\n")

    # User login required for update_user from models.py for validation
    print("Provide your login information. If it is wrong, we will not be"
          "able to update your account.")

    # getting the current email
    old_email = input("Please enter your current email: ")

    # getting the corresponding password to that account
    password = input("Please enter your password: ")

    print("Welcome to the update profile page!\n")
    print("**********************************")
    print("*         UPDATE MENU            *")
    print("*   1 - Update Username          *")
    print("*   2 - Update Email             *")
    print("*   3 - Billing address          *")
    print("*   4 - Update Postal Code       *")
    print("**********************************\n\n")

    continue_updating = True  # used to check if user wants to update more

    while continue_updating:
        selection = input("Which information would you like to update: ")

        if selection == '1':
            # updating username
            new_name = input(
                "Please enter a valid new username: ")
        elif selection == '2':
            # updating email
            new_email = input(
                "Please enter a valid new email: ")
        elif selection == '3':
            # updating Billing Address
            new_billing_address = input(
                "Please enter a valid new billing address: ")
        else:
            # updating postal code
            new_postal_code = input("Please enter a valid new postal code: ")

        # prompting the user if they would like to update a different option
        add_option = input("\nWould you like to update another option "
                           "('y'/'n')?: ")
        if add_option == 'y':
            # will allow user to choose another option to update
            continue_updating = True
        else:
            # user has finished updating
            continue_updating = False

    #  updating the profile
    update_user(old_email, password, new_email, new_name,
                new_billing_address,
                new_postal_code)
