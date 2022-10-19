from qbay import *
from qbay.cli import login_page, register_page, print_all_listings
from qbay.cli import login_page, create_listing_page, update_listing_page, \
    update_profile_page

'''
    This main file will create a main menu that takes
    user input to navigate to the screens in qbay.cli
    that a user can use to register, login, create
    listings, view profile, edit profile, etc.
'''


def main():
    user = None
    '''
        This screen prompts the user to register by providing
        a valid username, email, and password.
    '''
    while user is None:
        selection = input(
            '\nWelcome to qb&b! \n \n'
            '1. Register \n' 
            '2. Login \n'
            '3. Update Profile \n'
            '4. Exit \n \n'
            'Please select one of the options above: ')
        selection = selection.strip()
        if selection == '1':
            register_page()
        elif selection == '2':
            temp_user = login_page()
            if temp_user:
                user = temp_user
                print(f'welcome {user.username}')
                break
            else:
                print('Login failed. ')
        elif selection == '3':
            user = None
            update_profile_page()
        elif selection == '4':
            print('Thanks for visiting!')
            break

    while user is not None:
        selection = input(
            f'You are signed in as {user.username}\n \n'
            '1. Log out \n'
            '2. Home Page \n'
            '3. Exit \n \n'
            'Please select one of the options above: ')
        selection = selection.strip()
        if selection == '1':
            user = None
            main()
            break
        elif selection == '2':
            home_page(user)
        elif selection == '3':
            user = None
            print('Thanks for visiting!')
            break


def home_page(user):
    while True:
        selection = input(
            f'Welcome to the home page!\n \n'
            '1. View all listings \n'
            '2. View all of your listings \n'
            '3. Create listing \n'
            '4. Update listing \n'
            '5. Exit home page \n \n'
            'Please select one of the options above: ')
        selection = selection.strip()
        if selection == '1':
            print_all_listings()
        elif selection == '2':
            print_all_listings(user.email)
        elif selection == '3':
            create_listing_page(user.email, user.password)
        elif selection == '4':
            update_listing_page(user.email, user.password)
        elif selection == '5':
            break


if __name__ == '__main__':
    main()