class BaseCache(object):
    def get(self, key, default=None):
        raise NotImplementedError()

    def set(self, key, vaue):
        raise NotImplementedError()


class DictCache(object):
    def __init__(self, data=None):
        self._data = data if data is not None else {}

    def get(self, key, default=None):
        return self._data.get(key, default)

    def set(self, key, value):
        self._data[key] = value


class CacheWithPrefix(BaseCache):
    def __init__(self, base_cache, prefix):
        self._prefix = prefix
        self._base_cache = base_cache

    def get_full_key(self, key):
        return u'{}_{}'.format(self._prefix, key)

    def get(self, key, default=None):
        return self._base_cache.get(self.get_full_key(key), default=default)

    def set(self, key, value):
        self._base_cache.set(self.get_full_key(key), value)
