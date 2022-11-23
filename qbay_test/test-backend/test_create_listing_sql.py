from qbay.models import create_listing, register
from os import path

file_path = path.abspath(__file__)
dir_path = path.dirname(file_path)
zip_file_path = path.join(dir_path, 'Generic_SQLI.txt')


def test_create_listing():
    """
        Testing R4-1: Title of the product has to be alphanumeric only
        and space only allowed if it is not suffix or prefix.
    """
    #  create user for testing
    user = register("user24", "test@test.com", "goodPass.123")

    assert user is not None


def test_email():
    flag = 0
    f = open(zip_file_path, "r")
    for payload in f:
        try:
            create_listing(payload, "goodPass.123", "listing title",
                           "description of the listing to be tested", 600)
        except Exception:
            flag += 1
    assert flag is 0


def test_password():
    flag = 0
    f = open(zip_file_path, "r")
    for payload in f:
        try:
            create_listing("test@test.com", payload, "listing title",
                           "description of the listing to be tested", 600)
        except Exception:
            flag += 1
    assert flag is 0


def test_title():
    flag = 0
    f = open(zip_file_path, "r")
    for payload in f:
        try:
            create_listing("test@test.com", "goodPass.123", payload,
                           "description of the listing to be tested", 600)
        except Exception:
            flag += 1
    assert flag is 0


def test_description():
    flag = 0
    f = open(zip_file_path, "r")
    for payload in f:
        try:
            create_listing("test@test.com", "goodPass.123", "listing title",
                           payload, 600)
        except Exception:
            flag += 1
    assert flag is 0


def test_price():
    flag = 0
    f = open(zip_file_path, "r")
    for payload in f:
        try:
            create_listing("test@test.com", "goodPass.123", "listing title",
                           "description of the listing to be tested", payload)
        except Exception:
            flag += 1
    assert flag is 0
