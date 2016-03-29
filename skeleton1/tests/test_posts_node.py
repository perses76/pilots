from unittest import TestCase
from skeleton import SkeletonNode
from skeleton_processor import process_html


class PostsNodeTest(TestCase):
    def runTest(self):
        node = SkeletonNode(
            node_type='posts',
            attrs={
                'name': 'posts1',
                'source': 'frontpage',
                'limit': '3',
                'format': 'news',
            },
        ) 
        value = process_html(node)
        self.assertEqual(value, 'news: [1],[2],[3]')
