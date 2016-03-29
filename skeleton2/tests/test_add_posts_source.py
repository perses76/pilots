import unittest
from skeleton import SkeletonNode, SkeletonData
from skeleton_processor import process_html


class PostsSourceSelection(unittest.TestCase):
    def runTest(self):
        node = SkeletonNode(
            node_type='posts',
            attrs={'name': 'name1', 'source': 'search', 'format': 'news', 'limit': '1'}
        )
        data = SkeletonData(search_txt='table')
        self.assertEqual(
            process_html(node, data=data),
            'news: [1]'
        )
