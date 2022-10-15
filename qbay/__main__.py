from qbay import *
from qbay.cli import login_page, register_page

'''
    This main file will create a main menu that takes
    user input to navigate to the screens in qbay.cli
    that a user can use to register, login, create
    listings, view profile, edit profile, etc.
'''


def main():
    '''
        This screen prompts the user to register by providing
        a valid username, email, and password.
    '''
    while True:
        selection = input(
            '\nWelcome to qb&b! \n \n'
            '1. Register \n' 
            '2. Login \n'
            '3. Exit \n \n'
            'Please select one of the options above: ')
        selection = selection.strip()
        if selection == '1':
            register_page()
        elif selection == '2':
            user = login_page()
            if user:
                print(f'welcome {user.username}')
                break
            else:
                print('Login failed. ')
        elif selection == '3':
            print('Thanks for visiting!')
            break


if __name__ == '__main__':
    main()