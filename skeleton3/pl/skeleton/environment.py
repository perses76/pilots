from data import SkeletonData


class SkeletonEnvironment(object):
    def __init__(self, data=None, srv=None, output=None):
        self.data = data
        self.srv = srv
        self.output = output

    def copy(self, data=None, srv=None, output=None):
        return SkeletonEnvironment(
            data=self.data if data is None else SkeletonData(data, base_data=self.data),
            srv=srv or self.srv,
            output=output or self.output
        )
