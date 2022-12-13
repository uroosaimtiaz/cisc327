from qbay.models import create_booking, register
from os import path
import random

file_path = path.abspath(__file__)  # full path of your script
dir_path = path.dirname(file_path)  # full path of the directory of your script
zip_file_path = path.join(dir_path,
                          'Generic_SQLI.txt')  # absolute zip file path

# create_booking(email, password, listing_id, start_date, duration)


user = register("user25", "test@test.com", "goodPass.123")


def test_email():
    exception_counter = 0
    f = open(zip_file_path, "r")
    for payload in f:
        try:
            create_booking(payload, "goodPass.123", "id", "01-02-1000", "5")
        except Exception:
            exception_counter += 1
    assert exception_counter is 0


def test_password():
    exception_counter = 0
    f = open(zip_file_path, "r")
    for payload in f:
        try:
            create_booking('test@test.com', payload, "id", "01-02-1000", "5")
        except Exception:
            exception_counter += 1
    assert exception_counter is 0


def test_listing_id():
    exception_counter = 0
    f = open(zip_file_path, "r")
    for payload in f:
        try:
            create_booking('test@test.com', "goodPass.123", payload,
                           "01-02-1000", "5")
        except Exception:
            exception_counter += 1
    assert exception_counter is 0


def test_start_date():
    exception_counter = 0
    f = open(zip_file_path, "r")
    for payload in f:
        try:
            create_booking('test@test.com', "goodPass.123", "id", payload, "5")
        except Exception:
            exception_counter += 1
    assert exception_counter is 0


def test_duration():
    exception_counter = 0
    f = open(zip_file_path, "r")
    for payload in f:
        try:
            create_booking('test@test.com', "goodPass.123", "id", "01-02-1000",
                           payload)
        except Exception:
            exception_counter += 1
    assert exception_counter is 0
