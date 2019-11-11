from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.blocks import ListBlock
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page

from base.blocks import SocialProfileBlock
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class ResumePage(Page):
    pdf_link = models.ForeignKey(
        'wagtaildocs.Document',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='PDF version of the resume'
    )

    profile_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Profile photo to show at the top',
    )

    header_text = RichTextField(help_text='Header text')

    social_profiles = StreamField(
        SocialProfileBlock(),
        help_text='Links to social profiles',
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('header_text'),
        DocumentChooserPanel('pdf_link'),
        ImageChooserPanel('profile_image'),
        StreamFieldPanel('social_profiles')
    ]
