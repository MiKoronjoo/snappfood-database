class Shop:
    def __init__(self, shopId, name, addressId, minimum_bill_value, about_text=None):
        self.shopId = shopId
        self.name = name
        self.addressId = addressId
        self.minimum_bill_value = minimum_bill_value
        self.about_text = about_text
