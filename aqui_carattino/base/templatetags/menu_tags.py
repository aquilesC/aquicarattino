from django import template

from aqui_carattino.base.models import Menu

register = template.Library()


@register.simple_tag()
def get_menu(slug):
    try:
        return Menu.objects.get(slug=slug)
    except Menu.DoesNotExist:
        return None
