from django.contrib import messages
from django.db import models
from django.shortcuts import redirect, render
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase, Tag
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, RichTextFieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.fields import StreamField, RichTextField
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
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Overlay logo for the list of projects'
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

    parent_page_types = ['ProjectIndexPage']

    @property
    def get_tags(self):
        """
        """
        tags = self.tags.all()
        for tag in tags:
            tag.url = '/' + '/'.join(s.strip('/') for s in [
                self.get_parent().url,
                'tags',
                tag.slug
            ])
        return tags


class ProjectIndexPage(RoutablePageMixin, Page):
    subtitle = models.CharField(max_length=250, blank=False, null=False)
    footer = RichTextField(help_text='Content to appear at the end of the page', null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        RichTextFieldPanel('footer')
    ]

    subpage_types = ['ProjectPage']

    def children(self):
        return self.get_children().specific().live()

    def get_context(self, request, *args, **kwargs):
        context = super(ProjectIndexPage, self).get_context(request)
        context['projects'] = ProjectPage.objects.descendant_of(self).live()
        return context

    def serve_preview(self, request, mode_name):
        return self.serve(request)

    def get_projects(self, tag=None):
        projects = ProjectPage.objects.descendant_of(self)
        if tag:
            projects = projects.filter(tag=tag)
        return projects

    def get_child_tags(self):
        tags = []
        for project in self.get_projects():
            tags += project.get_tags
        tags = sorted(set(tags))
        return tags

    @route(r'^tags/$', name='tag_archive')
    @route(r'^tags/([\w-]+)/$', name='tag_archive')
    def tag_archive(self, request, tag=None):
        try:
            tag = Tag.objects.get(slug=tag)
        except Tag.DoesNotExist:
            if tag:
                msg = f'There are no blog posts tagged with {tag}'
                messages.add(msg)
            return redirect(self.url)

        projects = self.get_projects(tag=tag)
        context = {
            'tag': tag,
            'projects': projects
        }

        return render(request, 'projects/project_index_page.html', context=context)