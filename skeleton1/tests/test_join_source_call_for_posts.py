import unittest
from skeleton import SkeletonNode


class JoinSourceCallForPostsNode(unittest.TestCase):
    def runTest(self):
        root = SkeletonNode(
            node_type='root',
            children=(
                SkeletonNode(node_type='posts', attrs={'name': 'posts1', 'source': 'frontpage', 'limit': 1})
            )
        )

