from .. import models


class Users(object):
    def __init__(self, services):
        self._services = services

    def get_by_id(self, id):
        return models.User(id=id, name='Name{}'.format(id))
