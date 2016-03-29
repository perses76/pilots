from core.rtm_base import Lib

from libs.node_handlers import NodeHandlers
from libs.posts_source import PostsSource
from libs.posts_renders import PostsRenders


class MainLib(Lib):
    pass


def process_html(node):
    lib = MainLib({
        'NodeHandlers': NodeHandlers,
        'PostsSources': PostsSource,
        'PostsRenders': PostsRenders,
    })
    handlers = lib.load_lib('NodeHandlers')
    return handlers.posts_handler(node)
