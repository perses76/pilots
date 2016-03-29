from pl.skeleton import SkeletonData, SkeletonEnvironment
from pl.templates import Template


class HtmlOutput(object):
    def __init__(self, header='', html=''):
        self.header = header
        self.html = html

    def write(self, text):
        self.html += text


class SkeletonHtmlTemplate(Template):
    def __init__(self, skeleton, services):
        self._skeleton = skeleton
        self._srv = services

    def render(self, data):
        output = HtmlOutput()
        env = SkeletonEnvironment(srv=self._srv, data=SkeletonData(data), output=output)
        self._srv.handlers(self._skeleton, env)
        return output.html
