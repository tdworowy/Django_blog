from django.contrib.syndication.views import  Feed
from django.template.defaultfilters import truncatewords

from Example.Example1.blog.models import Post


class LatestPostsFeed(Feed):
    title = 'My blog'
    link = '/blog/'
    description = 'Newest posts on blog'

    @staticmethod
    def items():
        return Post.published.all()[:5]

    def item_title(self,item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body,30)
