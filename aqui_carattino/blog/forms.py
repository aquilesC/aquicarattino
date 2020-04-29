from django.contrib.syndication.views import Feed

from aqui_carattino.blog.models import ArticlePage


class BlogsFeed(Feed):
    title = "Aquiles Carattino"
    link = "/feed/"
    description = "Follow my path from science to entrepreneurship"

    description_template = 'feed/item_description.html'

    def items(self):
        return ArticlePage.objects.live().order_by('-first_published_at')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return item.url
