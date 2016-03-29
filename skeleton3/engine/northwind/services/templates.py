from roars.common.services import Templates as CommonTemplates
from .. import templates


class Templates(CommonTemplates):
    def get_template(self, name):
        return templates.UserTemplate()
