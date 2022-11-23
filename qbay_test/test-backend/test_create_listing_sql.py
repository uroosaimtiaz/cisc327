from qbay.models import create_listing


def test_email():
    flag = 0
    f = open("Generic_SQLI.txt", "r")
    for payload in f:
        try:
            create_listing(payload, "goodPass.123", "listing title",
                           "description of the listing to be tested", 600)
        except Exception:
            flag += 1
    assert flag is 0


def test_password():
    flag = 0
    f = open("Generic_SQLI.txt", "r")
    for payload in f:
        try:
            create_listing("test@test.com", payload, "listing title",
                           "description of the listing to be tested", 600)
        except Exception:
            flag += 1
    assert flag is 0


def test_title():
    flag = 0
    f = open("Generic_SQLI.txt", "r")
    for payload in f:
        try:
            create_listing("test@test.com", "goodPass.123", payload,
                           "description of the listing to be tested", 600)
        except Exception:
            flag += 1
    assert flag is 0


def test_description():
    flag = 0
    f = open("Generic_SQLI.txt", "r")
    for payload in f:
        try:
            create_listing("test@test.com", "goodPass.123", "listing title",
                           payload, 600)
        except Exception:
            flag += 1
    assert flag is 0


def test_price():
    flag = 0
    f = open("Generic_SQLI.txt", "r")
    for payload in f:
        try:
            create_listing("test@test.com", "goodPass.123", "listing title",
                           "description of the listing to be tested", payload)
        except Exception:
            flag += 1
    assert flag is 0
