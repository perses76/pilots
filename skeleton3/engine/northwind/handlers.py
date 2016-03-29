from roars.common.handlers import handlers as common_handlers


handlers = common_handlers


def h1_handler(node, flesh, srv):
    result = node.text.replace('{{ user_name }}', flesh['user'].name)
    result += 'Northwind H1 Handler'
    return HtmlOutput(html=result)


# handlers.register_handler('h1', h1_handler)
