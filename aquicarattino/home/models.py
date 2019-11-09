from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, PageChooserPanel
from wagtail.core.fields import RichTextField

from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Profile photo for header'
    )

    intro = RichTextField(null=True,
                          blank=False,
                          help_text='Information in header')

    featured_section_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )

    featured_section = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='This is what will be shown below the navbar (e.g. latest articles)',
        verbose_name='Featured Section'
    )

    featured_section_2_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )

    featured_section_2 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='This is what will be shown below the navbar (e.g. latest articles)',
        verbose_name='Featured Section'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('image'),
            FieldPanel('intro', classname="full"),
        ], heading="Hero section"),
        MultiFieldPanel([
            FieldPanel('featured_section_title'),
            PageChooserPanel('featured_section'),
            FieldPanel('featured_section_2_title'),
            PageChooserPanel('featured_section_2'),
        ])
    ]
