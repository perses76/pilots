from skeleton import SkeletonNode, SkeletonData, Environment
from node_handlers import posts_handler
from output_builder import OutputBuilder
from lib_factory import LibFactory


def process_html(node, libs_factory=None, data=None):
    output = OutputBuilder()
    if not libs_factory:
        libs_factory = LibFactory()
    env = Environment(data=data, output=output, libs=libs_factory)
    posts_handler(node, env)
    return output.get_value()
