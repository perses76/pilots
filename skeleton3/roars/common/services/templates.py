from pl import services
from .. import templates


class TemplateDoesNotExists(RuntimeError):
    pass


class Templates(services.Templates):
    def __init__(self, services):
        self.servives = services
        self.cache = services.cache

    def get_template(self, name):
        if name == 'hello_world.xml':
            return templates.UserTemplate(self.servives)
        raise TemplateDoesNotExists(name)
