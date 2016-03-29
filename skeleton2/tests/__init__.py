import unittest
from test_posts_node import PostsNodeTest
# from test_overwrite_posts_source import OverwriteMethodInLib
# from test_add_posts_source import PostsSourceSelection

suite = unittest.TestSuite()
suite.addTest(PostsNodeTest())
# suite.addTest(OverwriteMethodInLib())
# suite.addTest(PostsSourceSelection())
