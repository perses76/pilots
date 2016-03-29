class Lib(object):
    def __init__(self, libs):
        self.libs = libs

    def load_lib(self, lib_name):
        return self.libs[lib_name](self.libs)

    def add_lib(self, lib_name, lib):
        self.libs[lib_name] = lib
