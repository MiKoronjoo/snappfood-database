from pprint import pprint

from entities.entity import Entity


class Location(Entity):
    def __init__(self, locationId):
        tbl = Location.select_tuples('Location', ['locationId'], [locationId])[0]
        self.locationId = tbl[2]
        self.lat = tbl[1]
        self.lon = tbl[0]

    @classmethod
    def add(cls, lat: float, lon: float):
        cls.insert_tuple('location', ['lat', 'lon'], [str(lat), str(lon)])
        tbl = cls.select_tuples('location', ['lat', 'lon'], [str(lat), str(lon)])
        return tbl[-1][2]
