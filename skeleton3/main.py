from roars.common.views import hello_world
from roars.common.services import EngineServices as CommonEngineServices
from engine.northwind.services import EngineServices as NorhtwindEngineServices


def main():
    print hello_world(Request(user_id=5, services=CommonEngineServices()))
    print hello_world(Request(user_id=5, services=NorhtwindEngineServices()))
    print 'End!'

from pl.skeleton.environment import SkeletonEnvironment
env = SkeletonEnvironment(srv=None, output=None, data=None)


def test_speed():
    env.copy(data={'ttt': 1})


class Request(object):
    def __init__(self, user_id=None, services=None):
        self.services = services
        self.user_id = user_id


if __name__ == '__main__':
    main()
    # import timeit
    # print(timeit.timeit("test_speed()", setup="from __main__ import test_speed", number=1000))
