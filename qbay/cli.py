from qbay.models import login, register

'''
    This file creates the different screens a user
    will use to navigate the site.
'''

def login_page():
    '''
        This screen prompts the user to login to their
        account by entering their username and password.
    '''
    #  get email from user input
    email = input('Please enter your email: ')
    #  get password from user input
    password = input('Please enter your password: ')
    #  calls login function which returns a User
    return login(email, password)


def register_page():
    '''
        This screen prompts the user to register by providing
        a valid username, email, and password.
    '''
    print('\nThank you for registering with qb&b.\n')
    #  get username from user input
    name = input ('Please enter a valid username: ')
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