from base_lib import BaseLib


class PostsLib(BaseLib):

    def get_posts(self, source_name, limit, section_url=None):
        posts_sources_lib = self.libs.get_posts_source_lib()
        return posts_sources_lib.load_frontpage_posts(limit, section_url)
