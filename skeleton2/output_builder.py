class OutputBuilder(object):
    def __init__(self):
        self.__buffer = ''

    def write(self, text):
        self.__buffer += text

    def get_value(self):
        return  self.__buffer
