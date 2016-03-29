from pl.skeleton.handlers import handlers as skeleton_handlers

handlers = skeleton_handlers


def h1_handler(node, env):
    new_env = env.srv.handlers(node, env, name='get_user')
    result = node.text.replace('{{ user_name }}', new_env.data['user'].name)
    env.output.write('<h1>' + result)
    env.srv.handlers(node.children, new_env)
    env.output.write('</h1>')


handlers.register_handler(h1_handler, node_type='h1')


def div_handler(node, env):
    env.output.write('<div>' + node.text + '</div>')


handlers.register_handler(div_handler, node_type='div')


def get_user(node, env):
    user_id = env.data['user_id']
    user = env.srv.models.users.get_by_id(user_id)
    return env.copy({'user': user})


handlers.register_handler(get_user, name='get_user')
