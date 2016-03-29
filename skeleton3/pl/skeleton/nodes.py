NODE_TYPE_COLLECTION = '_node_collection'


class SkeletonAtom(object):
    def __init__(self, node_type):
        self.node_type = node_type


class SkeletonNode(SkeletonAtom):
    def __init__(self, attrs=None, children=None, text='', *args, **kwargs):
        super(SkeletonNode, self).__init__(*args, **kwargs)
        self.attrs = attrs or {}
        self.children = children or NodeCollection()
        self.text = text


class NodeCollection(SkeletonAtom):
    def __init__(self, items=None):
        super(NodeCollection, self).__init__(NODE_TYPE_COLLECTION)
        self.items = items

    def __iter__(self):
        return self.items.__iter__()
