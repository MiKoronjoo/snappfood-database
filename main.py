import re
import sqlite3
from typing import List

from entities import *


def get_all(table: str, attributes: List[str] = None) -> List[tuple]:
    con_obj = sqlite3.connect(DB_PATH)
    if attributes is None:
        att = '*'
    else:
        att = ', '.join(attributes)
    cursor = con_obj.execute(f'SELECT {att} FROM {table};')
    selected_table = cursor.fetchall()
    con_obj.close()
    return selected_table


def check_phone_number_format(phone_number: str) -> bool:
    match = re.match(r'09\d{9}', phone_number)
    if not match:
        return False
    return match.group() == phone_number


def check_username_format(username: str) -> bool:
    match = re.match(r'\w{5,32}', username)
    if not match:
        return False
    return match.group() == username


def check_email_format(email: str) -> bool:
    match = re.match(r'(\w+)([._])?(\w*)@(\w+)(\.(\w+))+', email)
    if not match:
        return False
    return match.group() == email


def login(username, password, is_admin=False):
    if is_admin:
        check_username_format(username)
        # TODO: check database
    else:
        check_phone_number_format(username)
        # TODO: check database


def signup(phone_number, email, password, first_name, last_name):
    check_phone_number_format(phone_number)
    check_email_format(email)
    # TODO: check database


def admin_signup(username, password):
    check_username_format(username)


if __name__ == '__main__':
    DB_PATH = 'db.sqlite'
    print(get_all('User', ['"first-name"']))
