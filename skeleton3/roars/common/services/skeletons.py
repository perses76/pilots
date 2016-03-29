from pl.skeleton import nodes
from ..skeleton_templates import SkeletonHtmlTemplate


class Skeletons(object):
    def __init__(self, srv):
        self._srv = srv

    def get_skeleton(self, name):
        if name == 'hello_world.xml':
            return nodes.SkeletonNode(
                node_type='h1',
                text='Hello: {{ user_name }}',
                children=nodes.NodeCollection([nodes.SkeletonNode(node_type='div', text='#######')])
            )

    def get_html_template(self, skeleton):
        return SkeletonHtmlTemplate(skeleton=skeleton, services=self._srv)
