import re
import sqlite3
from typing import List

from entities import *
from exception import *

DBTuple = List[str]


def is_in_db(value, table, attribute):
    con_obj = sqlite3.connect(DB_PATH)
    cursor = con_obj.execute(f'SELECT "{attribute}" FROM {table} WHERE "{attribute}" = \'{value}\';')
    selected_table = cursor.fetchall()
    con_obj.close()
    return bool(selected_table)


def check_phone_number_format(phone_number: str) -> None:
    match = re.match(r'09\d{9}', phone_number)
    if not match or match.group() != phone_number:
        raise PhoneNumberFormatError


def check_username_format(username: str) -> None:
    match = re.match(r'\w{5,32}', username)
    if not match or match.group() != username:
        raise UsernameFormatError


def check_email_format(email: str) -> None:
    match = re.match(r'(\w+)([._])?(\w*)@(\w+)(\.(\w+))+', email)
    if not match or match.group() != email:
        raise EmailFormatError


def login(username, password, is_admin=False):
    if is_admin:
        check_username_format(username)
        Admin.login(username, password)
    else:
        check_phone_number_format(username)
        this_user = User.login(username, password)
        return this_user


def signup(phone_number: str, password: str):
    check_phone_number_format(phone_number)
    if is_in_db(phone_number, 'User', 'phone-number'):
        raise SignupError('Phone number is already used.')
    # if is_in_db(email, 'User', 'email'):
    #     raise SignupError('Email is already used.')
    User.add(phone_number, password)


def admin_signup(username, password):
    check_username_format(username)
    if is_in_db(username, 'Admin', 'username'):
        raise SignupError('Username is already taken.')
    Admin.add(username, password)


if __name__ == '__main__':
    DB_PATH = 'db.sqlite'
    # signup('09171767788', 'sf@fs.dsf', 'ppargregrgra', 'mom', 'gh')
    # login('09171767788', 'ppargregrgra')
    # admin_signup('mikor', 'hassan')
    login('mikor', 'hassan', True)
    # login('09777777747', 'd7d@bfdg.fd')
