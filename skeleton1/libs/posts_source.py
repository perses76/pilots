from base_lib import BaseLib


class PostsSourceLib(BaseLib):
    def load_frontpage_posts(self, section_url, limit):
        return [1, 2, 3]

    def load_search_posts(self, search_txt, limit):
        return [5]
