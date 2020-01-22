from entities.user import User
from entities.entity import Entity


class Invoice(Entity):
    def __init__(self, addressId, walletId):
        Invoice.insert_tuple('Invoice', ['addressId', 'walletId', 'statusId'], [addressId, walletId, 1])
        tbl = Invoice.select_tuples('Invoice', ['addressId', 'walletId', 'statusId'], [addressId, walletId, 1])[-1]
        self.invoiceId = tbl[5]
        self.addressId = tbl[0]
        self.walletId = tbl[1]
        self.statusId = tbl[2]
        self.commentId = tbl[3]
        self.discountId = tbl[4]
        tbl = Invoice.exe_query(f'SELECT userId From Wallet WHERE walletId = {walletId};')
        this_user = User(tbl[0][0])
        for foodId in this_user.cart:
            Invoice.insert_tuple('IsInInvoice', ['foodId', 'invoiceId'], [foodId, self.invoiceId])
        this_user.clear_cart()
