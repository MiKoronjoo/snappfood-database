import re

from entities.entity import Entity
from entities.wallet import Wallet
from exception import LoginError, EmailIsAlreadyUsed, PhoneNumberFormatError, EmailFormatError, SignupError


class User(Entity):
    def __init__(self, userId, first_name, last_name, phone_number, email, password, walletId):
        self.userId = userId
        self._first_name = first_name
        self._last_name = last_name
        self.phone_number = phone_number
        self._email = email
        self._password = password
        self.walletId = walletId

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        User.update_tuple('User', 'first-name', value, f'"userId" = \'{self.userId}\'')
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        User.update_tuple('User', 'last-name', value, f'"userId" = \'{self.userId}\'')
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        User.check_email_format(value)
        if User.select_tuples('User', ['email'], [value]):
            raise EmailIsAlreadyUsed('Email is already used.')
        User.update_tuple('User', 'email', value, f'"userId" = \'{self.userId}\'')
        self._email = value

    def change_password(self, password):
        # TODO: hash password
        User.update_tuple('User', 'password', password, f'"userId" = \'{self.userId}\'')
        self._password = password

    @classmethod
    def add(cls, phone_number, password):
        cls.check_phone_number_format(phone_number)
        if cls.select_tuples('User', ['phone-number'], [phone_number]):
            raise SignupError('Phone number is already used.')
        cls.insert_tuple('User', ['phone-number', 'password'], [phone_number, password])
        userId = cls.get_user_id(phone_number)
        Wallet.add(userId)

    @classmethod
    def get_user_id(cls, phone_number):
        tbl = cls.select_tuples('User', ['phone-number'], [phone_number])
        userId = tbl[0][-2]
        return userId

    @classmethod
    def login(cls, phone_number, password):
        this_user = cls.select_tuples('User', ['phone-number', 'password'], [phone_number, password])
        if not this_user:
            raise LoginError('Invalid username or password.')
        fn, ln, pn, em, pw, ui, wi = this_user[0]
        return User(ui, fn, ln, pn, em, pw, wi)

    @classmethod
    def check_phone_number_format(cls, phone_number: str) -> None:
        match = re.match(r'09\d{9}', phone_number)
        if not match or match.group() != phone_number:
            raise PhoneNumberFormatError

    @classmethod
    def check_email_format(cls, email: str) -> None:
        match = re.match(r'(\w+)([._])?(\w*)@(\w+)(\.(\w+))+', email)
        if not match or match.group() != email:
            raise EmailFormatError
