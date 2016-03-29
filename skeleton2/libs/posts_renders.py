from core.rtm_base import Lib


class PostsRenders(Lib):
    def render(self, posts, format_name):
        return '{}: {}'.format(
            format_name,
            ','.join(['[{}]'.format(post) for post in posts])
        )
