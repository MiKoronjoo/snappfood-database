class Food:
    def __init__(self, foodId, name, price, shopId, categoryId, discount, about=None):
        self.foodId = foodId
        self.name = name
        self.price = price
        self.shopId = shopId
        self.categoryId = categoryId
        self.discount = discount
        self.about = about
