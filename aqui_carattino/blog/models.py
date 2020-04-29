from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

from aqui_carattino.blog.blocks import ContentBlock


class StandardPage(Page):
    """ Page with the minimum components. It is ideal to add as child of the root for things like the privacy notice,
    etc.
    """

    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True
    )

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Image to appear on the header at the top of the page'
    )

    body = StreamField(
        ContentBlock()
    )

    content_panels = Page.content_panels + [
        FieldPanel('introduction'),
        StreamFieldPanel('body'),
        ImageChooserPanel('image')
    ]


class BlogPageTag(TaggedItemBase):
    """ Many-to-many relationship to be able to tag Blog articles """
    content_object = ParentalKey('ArticlePage', related_name='tagged_items', on_delete=models.CASCADE)


class ArticlePage(Page):
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Image to appear at the top of the page, before author information'
    )

    body = StreamField(
        ContentBlock()
    )

    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        ImageChooserPanel('header_image'),
        FieldPanel('tags'),
    ]

    @property
    def get_tags(self):
        tags = self.tags.all()
        return [tag.slug for tag in tags]

    @property
    def og_image(self):
        """ Used in the template for the Open Graph standard"""
        if self.header_image:
            url = self.header_image.get_rendition('fill-1200x800|jpegquality-60').url
            return url

    @property
    def square_header(self):
        """ Used in the template when showing the list of articles"""
        if self.header_image:
            url = self.header_image.get_rendition('fill-200x200|jpegquality-60').url
            return url


@register_snippet
class Sidebar(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Image to appear at the top of the page, before author information'
    )

    title = models.CharField(max_length=50, blank=False, null=False)
    text = models.TextField()
    cta = models.CharField(max_length=15, blank=True, null=True, verbose_name='Call to action text')
    sidebar_cta_target = models.CharField(max_length=255, blank=True, null=True, verbose_name='What does the CTA link')
    panels = [
        FieldPanel('title'),
        FieldPanel('text'),
        FieldPanel('cta'),
        FieldPanel('sidebar_cta_target'),
        ImageChooserPanel('image'),
    ]

    def __str__(self):
        return "Sidebar for Articles"


class IndexPage(Page):
    """ Index page for articles, so they can be nested """
    subpage_types = ['ArticlePage']

    def children(self):
        return self.get_children().specific().live().order_by(
            '-first_published_at')

    def get_context(self, request, **kwargs):
        context = super(IndexPage, self).get_context(request, **kwargs)
        posts = self.paginate(request, self.children())
        context['posts'] = posts
        return context

    def serve_preview(self, request, mode_name):
        # Needed for previews to work
        return self.serve(request)

    def paginate(self, request, *args):
        page = request.GET.get('page')
        paginator = Paginator(self.children(), 20)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages
