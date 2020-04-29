from django.contrib.syndication.views import Feed

from aqui_carattino.blog.models import ArticlePage


class BlogsFeed(Feed):
    title = "Python for the lab blog articles"
    link = "/feed/"
    description = "All the articles as they are published"

    def items(self):
        return ArticlePage.objects.live().order_by('-first_published_at')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.introduction
