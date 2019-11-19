from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldRowPanel, FieldPanel
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet


@register_snippet
class People(index.Indexed, ClusterableModel):
    """ Preparing for the future. This allows to have people added to pages, in order to be able to generate articles
    with different authors. May not be needed for a personal blog, but better be prepared for the future.
    """
    first_name = models.CharField("First name", max_length=254)
    last_name = models.CharField("Last name", max_length=254)
    job_title = models.CharField("Job title", max_length=254)

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('first_name', classname="col6"),
                FieldPanel('last_name', classname="col6"),
            ])
        ], "Name"),
        FieldPanel('job_title'),
        ImageChooserPanel('image')
    ]

    search_fields = [
        index.SearchField('first_name'),
        index.SearchField('last_name'),
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
        return '{} {}'.format(self.first_name, self.last_name)

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