from pl.services.handlers import NodeHandlers
from .nodes import NODE_TYPE_COLLECTION


handlers = NodeHandlers()


def node_collection_handler(node, env):
    return [env.srv.handlers(item, env) for item in node]


handlers.register_handler(node_collection_handler, node_type=NODE_TYPE_COLLECTION)
