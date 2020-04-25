from django import template

from aqui_carattino.base.models import Menu
from aqui_carattino.blog.models import ArticlePage

register = template.Library()


@register.simple_tag()
def get_menu(slug):
    try:
        return Menu.objects.get(slug=slug)
    except Menu.DoesNotExist:
        return None


@register.simple_tag()
def get_latest_posts():
    posts = ArticlePage.objects.live().order_by(
            '-first_published_at')[:5]
    print(posts)
    return posts
