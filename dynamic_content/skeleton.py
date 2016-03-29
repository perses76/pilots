import xml.etree.ElementTree as ET


def load_skeleton(path):
    tree = ET.parse(path)
    return _get_skeleton_from_xml(tree.getroot())


def _get_skeleton_from_xml(node):
    children = [_get_skeleton_from_xml(child) for child in node]
    return SkeletonNode(node.tag, children=children, attrs=node.attrib.copy(), text=node.text)


class SkeletonNode(object):
    def __init__(self, node_type, children=None, attrs=None, text=None):
        self.node_type = node_type
        self.children = []
        if children:
            for child in children:
                self.add_child(child)
        self.attrs = attrs if not attrs is None else []
        self.text = text

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return '<{} {}>{}</{}>'.format(
            self.node_type,
            ', '.join(['{}={}'.format(key, value) for key, value in self.attrs.iteritems()]),
            self.text,
            self.node_type
        )


class SkeltonRoot(SkeletonNode):
    pass
