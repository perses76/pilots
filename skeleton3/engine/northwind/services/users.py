from roars.common.services import Users as CommonUsers
from .. import models


class Users(CommonUsers):
    def get_by_id(self, id):
        return models.User(id=id, name='name{}'.format(id), age=id)
