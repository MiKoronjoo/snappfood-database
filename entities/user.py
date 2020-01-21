from entities.entity import Entity
from entities.wallet import Wallet
from exception import LoginError


class User(Entity):
    def __init__(self, userId, first_name, last_name, phone_number, email, password, walletId):
        self.userId = userId
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.password = password
        self.walletId = walletId

    @classmethod
    def add(cls, first_name, last_name, phone_number, email, password):
        cls.insert_tuple('User', ['first-name', 'last-name', 'phone-number', 'email', 'password'],
                         [first_name, last_name, phone_number, email, password])
        userId = cls.get_user_id(phone_number)
        Wallet.add(userId)

    @classmethod
    def get_user_id(cls, phone_number, password):
        tbl = cls.select_tuples('User', ['phone-number'], [phone_number])
        userId = tbl[0][-2]
        return userId

    @classmethod
    def login(cls, phone_number, password):
        this_user = cls.select_tuples('User', ['phone-number', 'password'], [phone_number, password])
        if not this_user:
            raise LoginError('Invalid username or password.')
        print(this_user[0])
