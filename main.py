import os
from contextlib import contextmanager


class ChangeFolder(object):
    def __init__(self, new_folder):
        self.new_folder = new_folder

    def __enter__(self):
        self.cur_dir = os.getcwd()
        os.chdir(self.new_folder)
        print "Enter"
        return self

    def __exit__(self, *args):
        print 'Exit'
        os.chdir(self.cur_dir)
        pass


def change_folder1(folder):
    return ChangeFolder(folder)


@contextmanager
def change_folder(folder):
    cur_dir = os.getcwd()
    os.chdir(folder)
    try:
        yield
    finally:
        print 'Change directory back to = {}'.format(cur_dir)
        os.chdir(cur_dir)


def main():
    print 'Current Folder={}'.format(os.getcwd())
    try:
        with change_folder('..'):
            with open('pilots/main.py', 'r+') as f:
                raise NotImplementedError('Test')
                print f.name
        print 'Current Folder={}'.format(os.getcwd())
    except NotImplementedError:
        print 'Exeption: Current Folder={}'.format(os.getcwd())
    print 'End'


if __name__ == '__main__':
    main()
