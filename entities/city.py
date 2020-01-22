from entities.entity import Entity


class City(Entity):
    def __init__(self, cityId):
        self.cityId = cityId

    @property
    def name(self):
        tbl = City.select_tuples('City', ['cityId'], [self.cityId])
        return tbl[0][0]
