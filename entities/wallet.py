from entities.entity import Entity


class Wallet(Entity):
    def __init__(self, userId):
        Wallet.insert_tuple('Wallet', ['userId'], [userId])
        tbl = Wallet.select_tuples('Wallet', ['userId'], [userId])[0]
        self.walletId = tbl[0]
        self.userId = tbl[1]
