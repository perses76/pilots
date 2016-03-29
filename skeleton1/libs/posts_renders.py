from base_lib import BaseLib


class PostsRendersLib(BaseLib):
    def render(self, posts, format_name):
        return '{}: {}'.format(
            format_name,
            ','.join(['[{}]'.format(post) for post in posts])
        )
