from entities.entity import Entity


class Discount(Entity):
    def __init__(self, discountId):
        tbl = Discount.select_tuples('Discount', ['discountId'], [discountId])[0]
        self.discountId = tbl[2]
        self.percent = tbl[0]
        self.text = tbl[1]
