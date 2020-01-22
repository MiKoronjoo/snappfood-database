from entities.entity import Entity


class Category(Entity):
    @classmethod
    def add(cls, name):
        cls.insert_tuple('Category', ['name'], [name])
        tbl = cls.select_tuples('Category', ['name'], [name])
        return tbl[-1][0]  # CategoryId

    @classmethod
    def name(cls, CategoryId):
        tbl = cls.select_tuples('Category', ['CategoryId'], [CategoryId])
        return tbl[0][1]
