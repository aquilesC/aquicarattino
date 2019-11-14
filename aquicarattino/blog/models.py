""" A lot of the code here was adapted from Wagtail backery
"""
from django.db import models
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.core.models import Orderable, Page
from wagtail.snippets.edit_handlers import SnippetChooserPanel


class BlogPeopleRelationship(Orderable, models.Model):
    """ We have created a two way relationship between BlogPage and People using
    the ParentalKey and ForeignKey
    """
    page = ParentalKey(
        'BlogPage', related_name='blog_person_relationship', on_delete=models.CASCADE
    )
    people = models.ForeignKey(
        'base.People', related_name='person_blog_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('people')
    ]


class BlogPageTag(TaggedItemBase):
    """ Many-to-many relationship to be able to tag Blog articles """
    content_object = ParentalKey('BlogPage', related_name='tagged_items', on_delete=models.CASCADE)


class BlogPage(Page):
    """ This is a Blog Article, the core of the blog app.
    """
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='This image will be used for social media and in the cards while listing articles'
    )

    subtitle = models.CharField(max_length=250, null=False, blank=False)

