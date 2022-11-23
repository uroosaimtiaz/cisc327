from qbay.models import register
from os import path
import random

file_path = path.abspath(__file__)  # full path of your script
dir_path = path.dirname(file_path)  # full path of the directory of your script
zip_file_path = path.join(dir_path,
                          'Generic_SQLI.txt')  # absolute zip file path


def test_name():
    exception_counter = 0
    f = open(zip_file_path, "r")

    for payload in f:
        try:
            register(payload, "test@test.com", "goodPass.123")
        except Exception:
            exception_counter += 1
    assert exception_counter is 0


def test_email():
    exception_counter = 0
    f = open(zip_file_path, "r")
    for payload in f:
        try:
            register("name", payload, "goodPass.123")
        except Exception:
            exception_counter += 1
    assert exception_counter is 0


def test_password():
    exception_counter = 0
    f = open(zip_file_path, "r")
    used_numbers_first_part = []
    used_numbers_second_part = []
    num_used = True
    for payload in f:
        rand_email_first_part = ''
        rand_email_second_part = ''
        num_used = True
        while num_used:
            rand_email_first_part = str(random.randint(0, 100))
            rand_email_second_part = str(random.randint(0, 100))
            if rand_email_first_part not in used_numbers_first_part and \
                    rand_email_second_part not in used_numbers_second_part:
                num_used = False
        rand_email = str(rand_email_first_part) + str(rand_email_second_part) \
            + "@test.com"
        try:
            register("name", rand_email, payload)
        except Exception:
            exception_counter += 1
    assert exception_counter is 0
