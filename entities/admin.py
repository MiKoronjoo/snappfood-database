from entities.entity import Entity
from exception import LoginError


class Admin(Entity):
    def __init__(self, username, password, shopId):
        self.username = username
        self._password = password
        self.shopId = shopId

    @classmethod
    def add(cls, username, password):
        cls.insert_tuple('Admin', ['username', 'password'],
                         [username, password])

    def change_password(self, password):
        # TODO: hash password
        Admin.update_tuple('Admin', 'password', password, f'"username" = \'{self.username}\'')
        self._password = password

    @classmethod
    def login(cls, username, password):
        this_user = cls.select_tuples('Admin', ['username', 'password'], [username, password])
        if not this_user:
            raise LoginError('Invalid username or password.')
        un, pw, si = this_user[0]
        return Admin(un, pw, si)
