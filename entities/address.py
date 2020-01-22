from entities.location import Location
from entities.entity import Entity


class Address(Entity):
    def __init__(self, addressId, userId, cityId, locationId, street=None, alley=None, plaque=None):
        self.addressId = addressId
        self.userId = userId
        self.cityId = cityId
        self.locationId = locationId
        self._street = street
        self._alley = alley
        self._plaque = plaque

    @classmethod
    def add(cls, userId, cityId, lat, lon):
        locationId = Location.add(lat, lon)
        cls.insert_tuple('Address', ['userId', 'cityId', 'locationId'], [userId, cityId, locationId])

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, value: str):
        Address.update_tuple('Address', 'street', value,  f'"addressId" = \'{self.addressId}\'')
        self._street = value

    @property
    def alley(self):
        return self._alley

    @alley.setter
    def alley(self, value: str):
        Address.update_tuple('Address', 'alley', value, f'"addressId" = \'{self.addressId}\'')
        self._alley = value

    @property
    def plaque(self):
        return self._plaque

    @plaque.setter
    def plaque(self, value: str):
        Address.update_tuple('Address', 'plaque', value, f'"addressId" = \'{self.addressId}\'')
        self._plaque = value
