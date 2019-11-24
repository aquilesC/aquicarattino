from django import template


register = template.Library()


@register.inclusion_tag('tags/author.html', takes_context=False)
def render_author(person):
    return {'author': person}
