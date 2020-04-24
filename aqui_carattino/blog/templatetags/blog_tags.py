from django import template

from aqui_carattino.blog.models import Sidebar, ArticlePage

register = template.Library()


@register.inclusion_tag('blog/includes/sidebar.html', takes_context=True)
def get_sidebar_info(context):
    sidebar_image = None
    sidebar_title = None
    sidebar_text = None
    sidebar_cta = None
    sidebar_cta_target = None

    try:
        sb = Sidebar.objects.first()
        sidebar_image = sb.image
        sidebar_title = sb.title
        sidebar_text = sb.text
        sidebar_cta = sb.cta
        # sidebar_cta_target = sb.cta_target

    except Sidebar.DoesNotExist:
        pass

    return {
        'sidebar_image': sidebar_image,
        'sidebar_title': sidebar_title,
        'sidebar_text': sidebar_text,
        'sidebar_cta': sidebar_cta,
        'sidebar_cta_target': sidebar_cta_target,
    }

@register.simple_tag()
def get_latest_posts():
    posts = ArticlePage.objects.all().order_by(
            '-first_published_at')[:5]
    print(posts)
    return posts
