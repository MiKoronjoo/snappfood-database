from typing import List

from entities.entity import Entity


class Shop(Entity):
    def __init__(self, shopId):
        tbl = Shop.select_tuples('Shop', ['shopId'], [shopId])[0]
        self.name = tbl[0]
        self.about_text = tbl[1]
        self.minimum_bill_value = tbl[2]
        self.shopId = tbl[3]
        self.addressId = tbl[4]

    @property
    def foods(self):
        from entities.food import Food
        tbl = Shop.exe_query(f'SELECT foodId FROM Food WHERE shopId = {self.shopId} ORDER BY categoryId;')
        return [Food(foodId[0]) for foodId in tbl]

    @property
    def rate(self):
        tbl = Shop.exe_query('SELECT avg(rate) FROM Comment C JOIN Invoice I on C.commentId = I.commentId '
                             'JOIN IsInInvoice III on I.invoiceId = III.invoiceId '
                             'JOIN Food F on III.foodId = F.foodId '
                             'JOIN Shop S on F.shopId = S.shopId '
                             f'WHERE S.shopId = {self.shopId} GROUP BY rate;')
        return tbl[0][0]

    @classmethod
    def add(cls, name, addressId, minimum_bill_value=0):
        cls.insert_tuple('Shop', ['name', 'addressId', 'minimum-bill-value'],
                         [name, addressId, str(minimum_bill_value)])
        tbl = cls.select_tuples('Shop', ['name', 'addressId'], [name, addressId])
        return tbl[-1][3]  # shopId

    @classmethod
    def get_near_shops(cls, lat, lon):
        tbl = cls.exe_query('SELECT shopId FROM Shop S JOIN Address A ON S.addressId = A.addressId '
                            'JOIN Location L ON A.locationId = L.locationId '
                            f'WHERE ABS(lat - {lat}) < 100 AND ABS(lon - {lon}) < 100;')
        for shop in tbl:
            yield Shop(shop[0])

    def __str__(self):
        return f'{self.name}, {self.shopId}'
