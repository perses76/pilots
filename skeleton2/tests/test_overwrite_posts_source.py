from unittest import TestCase
from skeleton import SkeletonNode
from skeleton_processor import process_html
from lib_factory import LibFactory
from libs.posts_source import PostsSourceLib


class CustomLibFactory(LibFactory):
    def get_posts_source_lib(self):
        return CustomPostsSourceLib(self)


class CustomPostsSourceLib(PostsSourceLib):
    def load_frontpage_posts(self, section_url, limit):
        return [1]


class OverwriteMethodInLib(TestCase):
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
        value = process_html(node, libs_factory=CustomLibFactory())
        self.assertEqual(value, 'news: [1]')
