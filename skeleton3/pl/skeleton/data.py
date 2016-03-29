class SkeletonData(object):
    def __init__(self, data=None, base_data=None):
        self.data = data or {}
        self.base_data = base_data

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        if self.base_data is None:
            raise Exception('key is not found {}'.format(key))
        return self.base_data[key]
