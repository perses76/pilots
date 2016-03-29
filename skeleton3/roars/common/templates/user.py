from pl.templates import Template


class UserTemplate(Template):
    def __init__(self, services):
        self._services = services
