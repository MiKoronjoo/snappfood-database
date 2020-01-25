from entities.entity import Entity


class Food(Entity):
    def __init__(self, foodId):
        tbl = Food.select_tuples('Food', ['foodId'], [foodId])[0]
        self.foodId = tbl[4]
        self.name = tbl[1]
        self.price = tbl[0]
        self.shopId = tbl[5]
        self.categoryId = tbl[6]
        self.discount = tbl[3]
        self.about = tbl[2]

    @classmethod
    def add(cls, name, price, shopId, categoryId, about):
        cls.insert_tuple('Food', ['name', 'price', 'shopId', 'categoryId', 'about'],
                         [name, price, shopId, categoryId, about])
        tbl = cls.select_tuples('Food', ['name', 'shopId'], [name, shopId])
        return Food(tbl[-1][4])

    def __str__(self):
        from entities.shop import Shop
        if self.discount:
            part = f'{self.price} -> {self.price * (100 - self.discount) / 100}'
        else:
            part = str(self.price)
        return f'{self.name}, {Shop(self.shopId)}, {part}, {self.shopId}'
