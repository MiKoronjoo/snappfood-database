from entities.city import City
from entities.location import Location
from entities.entity import Entity


class Address(Entity):
    def __init__(self, addressId):
        tbl = Address.select_tuples('Address', ['addressId'], [addressId])[0]
        self.addressId = tbl[3]
        self.userId = tbl[4]
        self.cityId = tbl[6]
        self.locationId = tbl[5]
        self._street = tbl[2]
        self._alley = tbl[1]
        self._plaque = tbl[0]

    @classmethod
    def add(cls, userId, cityId, lat, lon):
        locationId = Location.add(lat, lon)
        cls.insert_tuple('Address', ['userId', 'cityId', 'locationId'], [userId, cityId, locationId])
        tbl = cls.select_tuples('Address', ['locationId'], [locationId])
        return tbl[-1][3]  # addressId

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, value: str):
        Address.update_tuple('Address', 'street', value, f'"addressId" = \'{self.addressId}\'')
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

    def __str__(self):
        city_name = City(self.cityId).name
        return f'{city_name}, {self.street}, {self.alley}, {self.plaque}'.replace('null', '')
