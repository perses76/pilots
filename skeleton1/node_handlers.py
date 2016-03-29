from lib_factory import LibFactory


def posts_handler(node, env):
    # source handlers
    # posts_source_handlers = env.handlers.get_posts_source_handlers()
    # posts = posts_source_handlers.process(node, env)  # if we need to pass env?????
    # new_data = env.data.extend(posts=posts)

    # filters and others 
    # posts_general_handlers = env.handlers.get_general_handlers()
    # posts_general_handlers.process(node, new_data)
    
    # format handlers
    # posts_format_handers = env.handlers.get_posts_format_handlers()
    # posts_format_handlers.process(node, data=new_data)

    posts_lib = env.libs.get_posts_lib()
    posts = posts_lib.get_posts(node.attrs['source'], node.attrs['limit'], node.attrs.get('section_url'))
    posts_renderes_lib = env.libs.get_posts_renders_lib()
    env.output.write(
        posts_renderes_lib.render(posts, node.attrs['format'])
    )

# @hadlers.register('posts/@source[. == "frontpage"]')
def posts_source_handler(node, env):
    pass


# @hadlers.register('posts/@source[. == "search"]')
def posts_source_handler(node, env):
    pass
