from django.db import models
from django.contrib.syndication.views import Feed

from blog.models import BlogPage


class BlogsFeed(Feed):
    title = "My blog articles"
    link = "/blogs-feed/"
    description = "All of my articles as they are published"

    def items(self):
        return BlogPage.objects.live().order_by('-date_published')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.introduction