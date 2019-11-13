from django.db import models
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting
from wagtail.snippets.models import register_snippet


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
