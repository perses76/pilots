from roars.common.models import User as CommonUser


class User(CommonUser):
    def __init__(self, age=None, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.age = age
