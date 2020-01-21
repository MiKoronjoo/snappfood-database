from entities.entity import Entity


class Wallet(Entity):
    def __init__(self, walletId, userId):
        self.walletId = walletId
        self.userId = userId

    @classmethod
    def add(cls, userId):
        cls.insert_tuple('Wallet', ['userId'], [userId])
