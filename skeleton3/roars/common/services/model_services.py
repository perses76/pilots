from pl import services
from users import Users


class ModelServices(services.ModelServices):
    def __init__(self, services=None):
        self._users = Users(services)

    @property
    def users(self):
        return self._users
