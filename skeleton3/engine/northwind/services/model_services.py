from roars.common.services import ModelServices as CommonModelServices
from users import Users


class ModelServices(CommonModelServices):
    def __init__(self, srv):
        super(ModelServices, self).__init__(srv)
        self._users = Users(self)
