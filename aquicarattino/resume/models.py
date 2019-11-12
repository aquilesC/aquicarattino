from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page

from .blocks import SocialProfileBlock
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class ResumePage(Page):
    name = models.CharField(max_length=250, blank=False, null=False, help_text='Your name')
    subtitle = models.CharField(max_length=250, blank=False, null=False, help_text='Subtitle, under the name')
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    career_summary = models.TextField()


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

    social_profiles = StreamField(
        SocialProfileBlock(),
        help_text='Links to social profiles',
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('name'),
                FieldPanel('subtitle'),
                FieldPanel('email'),
                FieldPanel('phone')
            ],
            heading='Information for the header',
            classname='collapsible',
        ),
        FieldPanel('career_summary'),
        DocumentChooserPanel('pdf_link'),
        ImageChooserPanel('profile_image'),
        StreamFieldPanel('social_profiles')
    ]
