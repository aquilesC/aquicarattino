from django.contrib.sites.models import Site
from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from .blocks import ContentBlock


@register_snippet(Site)

@register_snippet
class People(index.Indexed, ClusterableModel):
    """ Preparing for the future. This allows to have people added to pages, in order to be able to generate articles
    with different authors. May not be needed for a personal blog, but better be prepared for the future.
    """
    name = models.CharField("Name", max_length=254, blank=True, null=True)
    job_title = models.CharField("Job title", max_length=254)
    description = models.TextField("Short summary", null=True)

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('job_title'),
        FieldPanel('description'),
        ImageChooserPanel('image'),
    ]

    search_fields = [
        index.SearchField('name'),
    ]

    @property
    def thumb_image(self):
        # Returns an empty string if there is no profile pic or the rendition
        # file can't be found.
        try:
            return self.image.get_rendition('fill-50x50').img_tag()
        except:  # FIXME: remove bare 'except:'
            return ''

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'


@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(null=True, blank=True, help_text='Your Facebook page URL')
    instagram = models.URLField(null=True, blank=True, help_text='Your Instagram Profile')
    trip_advisor = models.URLField(null=True, blank=True, help_text='Your Trip Advisor page URL')
    youtube = models.URLField(null=True, blank=True, help_text='Your YouTube channel or user account URL')
    vimeo = models.URLField(null=True, blank=True, help_text='Your Vimeo channel')
    github = models.URLField(null=True, blank=True, help_text='Your Github profile')
    twitter = models.URLField(null=True, blank=True, help_text='Your Twitter Link')
    linkedin = models.URLField(null=True, blank=True, help_text='Your LinkedIn Link')
    stackoverflow = models.URLField(null=True, blank=True, help_text='Your Stack Overflow Profile')
    indiehackers = models.URLField(null=True, blank=True, help_text='Your Indie Hackers Profile')
    codepen = models.URLField(null=True, blank=True, help_text='Your Codepen Profile')
    orcid = models.URLField(null=True, blank=True, help_text='Your ORCID profile')


@register_setting
class GeneralSettings(BaseSetting):
    footer_text = models.TextField(null=False, blank=False, help_text='Text at the bottom of every page')


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


class FormField(AbstractFormField):
    """
    Wagtailforms is a module to introduce simple forms on a Wagtail site. It
    isn't intended as a replacement to Django's form support but as a quick way
    to generate a general purpose data-collection form or contact form
    without having to write code. We use it on the site for a contact form. You
    can read more about Wagtail forms at:
    http://docs.wagtail.io/en/latest/reference/contrib/forms/index.html
    """
    page = ParentalKey('FormPage', related_name='form_fields', on_delete=models.CASCADE)


class FormPage(AbstractEmailForm):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    body = StreamField(ContentBlock())
    thank_you_text = RichTextField(blank=True)

    # Note how we include the FormField object via an InlinePanel using the
    # related_name value
    content_panels = AbstractEmailForm.content_panels + [
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]