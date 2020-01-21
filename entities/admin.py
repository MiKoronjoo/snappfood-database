from entities.entity import Entity
from exception import LoginError


class Admin(Entity):
    def __init__(self, username, password, shopId):
        self.username = username
        self.password = password
        self.shopId = shopId

    @classmethod
    def add(cls, username, password):
        cls.insert_tuple('Admin', ['username', 'password'],
                         [username, password])
        # userId = cls.get_user_id(phone_number)
        # Wallet.add(userId)

    @classmethod
    def login(cls, username, password):
        this_user = cls.select_tuples('Admin', ['username', 'password'], [username, password])
        if not this_user:
            raise LoginError('Invalid username or password.')
        print(this_user[0])
