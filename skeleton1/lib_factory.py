import libs


class LibFactory(object):
    def get_posts_lib(self):
        return libs.posts.PostsLib(self)

    def get_posts_source_lib(self):
        return libs.posts_source.PostsSourceLib(self)

    def get_posts_renders_lib(self):
        return libs.posts_renders.PostsRendersLib(self)
