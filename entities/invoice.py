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
