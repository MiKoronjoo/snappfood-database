class Address:
    def __init__(self, addressId, userId, cityId, locationId, street=None, alley=None, plaque=None):
        self.addressId = addressId
        self.userId = userId
        self.cityId = cityId
        self.locationId = locationId
        self.street = street
        self.alley = alley
        self.plaque = plaque
