class SkeletonNode(object):
    # TODO should be unmutiable
    def __init__(self, node_type, attrs=None, text=None, children=None):
        self.node_type = node_type
        self.attrs = attrs  # Make it frozen
        self.test = text
        self.children = children


class SkeletonData(dict):
    pass


class Environment(object):
    def __init__(self, data, output, libs):
        self.data = data
        self.output = output
        self.libs = libs
