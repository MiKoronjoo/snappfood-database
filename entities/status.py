from entities.entity import Entity


class Status(Entity):
    def __init__(self, statusId, name):
        self.statusId = statusId
        self.name = name
