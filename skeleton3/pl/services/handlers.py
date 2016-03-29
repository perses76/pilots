class NodeHandlers(object):
    def __init__(self, base_handlers=None):
        self._items = {}
        self._data = {}

    def register_handler(self, func, node_type=None, name=None):
        if name:
            self._data[name] = func
        else:
            self._items[node_type] = func

    def __call__(self, node, env, name=None):
        if name:
            return self._data[name](node, env)
        return self._items[node.node_type](node, env)
