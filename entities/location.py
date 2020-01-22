from pprint import pprint

from entities.entity import Entity


class Location(Entity):
    def __init__(self, locationId, lat, lon):
        self.locationId = locationId
        self.lat = lat
        self.lon = lon

    @classmethod
    def add(cls, lat: float, lon: float):
        cls.insert_tuple('location', ['lat', 'lon'], [str(lat), str(lon)])
        tbl = cls.select_tuples('location', ['lat', 'lon'], [str(lat), str(lon)])
        return tbl[-1][2]
