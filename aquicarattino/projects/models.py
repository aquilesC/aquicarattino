from django.db import models
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from base.blocks import ProjectStreamBlock
from wagtail.images.edit_handlers import ImageChooserPanel


class ProjectTag(TaggedItemBase):
    content_object = ParentalKey('ProjectPage', on_delete=models.CASCADE, related_name='tagged_items')


class ProjectPage(Page):
    summary = models.TextField(help_text='Short summary to show on cards')
    category = models.CharField(max_length=50, help_text='Bold title to appear under card')
    tags = ClusterTaggableManager(through=ProjectTag, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Image for cards and header image for page'
    )
    body = StreamField(
        ProjectStreamBlock(), verbose_name="Page body", blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('summary', classname='full'),
        FieldPanel('category', classname='full'),
        FieldPanel('tags'),
        ImageChooserPanel('image'),
        StreamFieldPanel('body')
    ]