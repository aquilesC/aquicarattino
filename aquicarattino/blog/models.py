""" A lot of the code here was adapted from Wagtail backery
"""
from django.contrib import messages
from django.db import models
from django.shortcuts import redirect, render
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase, Tag
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, PageChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.fields import StreamField
from wagtail.core.models import Orderable, Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from base.blocks import ContentBlock
from base.choices import LANGUAGES


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
    introduction = models.TextField(help_text='Text to describe the page')
    date_published = models.DateField('Date article published', blank=True, null=True)
    body = StreamField(
        ContentBlock(),
        verbose_name='Page body',
        blank=True
    )
    language = models.CharField(max_length=2, choices=LANGUAGES, default='En')

    # Using translations as ForeignKeys is very limiting (it is only useful when dealing with 2 languages)
    translated = models.ForeignKey('wagtailcore.Page', related_name='+', null=True, blank=True, on_delete=models.SET_NULL)

    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('introduction', classname='full'),
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
        FieldPanel('date_published'),
        InlinePanel('blog_person_relationship', label='Author (s)', panels=None, min_num=1),
        FieldPanel('tags'),
        PageChooserPanel('translated')
    ]

    parent_page_types = ['BlogIndexPage']
    subpage_types = []

    def is_translated(self):
        # If the translation exists we simply return it
        if self.translated:
            return self.translated
        # If a translation exists, let's update our page and return the translation
        try:
            self.translated = BlogPage.objects.filter(translated=self).get()
            self.save()
            return self.translated
        except Page.DoesNotExist:
            return None

    def get_context(self, request):
        context = super(BlogPage, self).get_context(request)
        print(context)
        context['translated'] = self.is_translated()
        print(context)
        return context


class BlogIndexPage(RoutablePageMixin, Page):
    subtitle = models.TextField(help_text='Subtitle to display below the title')
    image = models.ForeignKey(
        'wagtailimages.Image',
        help_text='Image to show next to the title',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    featured_article = models.ForeignKey(BlogPage, related_name='+', null=True, blank=True, on_delete=models.SET_NULL)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle', classname='full'),
        ImageChooserPanel('image'),
        PageChooserPanel('featured_article'),
    ]

    subpage_types = ['BlogPage']


    def children(self):
        return self.get_children().specific().live()

    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)
        context['posts'] = BlogPage.objects.descendant_of(
            self).live().order_by(
            '-date_published')
        return context

    @route(r'^tags/$', name='tag_archive')
    @route(r'^tags/([\w-]+)/$', name='tag_archive')
    def tag_archive(self, request, tag=None):
        try:
            tag = Tag.objects.get(slug=tag)
        except Tag.DoesNotExist:
            if tag:
                msg = 'There are no blog posts tagged with "{}"'.format(tag)
                messages.add_message(request, messages.INFO, msg)
            return redirect(self.url)

        posts = self.get_posts(tag=tag)
        context = {
            'tag': tag,
            'posts': posts
        }
        return render(request, 'blog/blog_index_page.html', context)

    def get_posts(self, tag=None):
        posts = BlogPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            # Not tags.append() because we don't want a list of lists
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags