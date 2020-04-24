from django import template

from aqui_carattino.base.models import FooterText, FooterAboutUs

register = template.Library()


@register.inclusion_tag('base/includes/footer_text.html', takes_context=True)
def get_footer(context):
    try:
        footer_text = FooterText.objects.first().text
    except AttributeError:
        footer_text = None
    return {'footer_text': footer_text}


@register.inclusion_tag('base/includes/footer_about.html', takes_context=True)
def get_footer_about(context):
    try:
        about_us_title = FooterAboutUs.objects.first().title
        about_us_text = FooterAboutUs.objects.first().text
    except AttributeError:
        about_us_title = None
        about_us_text = None
    return {
        'about_us_text': about_us_text,
        'about_us_title': about_us_title,
    }
