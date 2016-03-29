import unittest
from tests import suite


def main():
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    main()
    print 'End'
