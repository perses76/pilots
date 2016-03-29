from core.rtm_base import Lib
from skeleton import SkeletonNode


class NodeHandlers(Lib):

    def posts_handler(self, node):
        posts_source = self.load_lib('PostsSources')
        posts_renders = self.load_lib('PostsRenders')
        posts = posts_source.load_frontpage_posts(node.attrs.get('section_url'), node.attrs['limit'])
        return posts_renders.render(posts, node.attrs['format'])

    def posts_handler_match(self):
        return isinstance(self.last, SkeletonNode) and (self.last.node_type == 'posts')

    def process(self, node):
        raise NotImplementedError()
