from django.db import models
from django_extensions.db.fields import AutoSlugField
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, MultiFieldPanel, InlinePanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet


class MenuItem(Orderable):
    link_title = models.CharField(max_length=15, blank=True, null=True)
    link_url = models.CharField(max_length=500, blank=True, null=True)

    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.CASCADE,
    )

    open_in_new_tab = models.BooleanField(default=False, blank=True)

    menu = ParentalKey("Menu", related_name="menu_items")

    panels = [
        FieldPanel('link_title'),
        FieldPanel('link_url'),
        PageChooserPanel('link_page'),
        FieldPanel('open_in_new_tab')
    ]

    @property
    def link(self):
        if self.link_url:
            return self.link_url
        if self.link_page:
            return self.link_page.url
        return '#'

    @property
    def title(self):
        if self.link_title:
            return self.link_title
        if self.link_page:
            return self.link_page.title
        return "Missing Title"

    @property
    def page(self):
        if self.link_page:
            return self.link_page
        return None


@register_snippet
class Menu(ClusterableModel):
    title = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from='title', editable=True)

    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('slug')
        ], heading='Menu'),
        InlinePanel("menu_items", label="Menu Items")
    ]

    def __str__(self):
        return self.title


@register_snippet
class FooterAboutUs(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    text = RichTextField(blank=False)

    panels = [
        FieldPanel('title'),
        FieldPanel('text'),
    ]

    class Meta:
        verbose_name_plural = "Footer About Us"

    def __str__(self):
        return "Footer About Us"


@register_snippet
class FooterText(models.Model):
    text = RichTextField(blank=False)

    panels = [
        FieldPanel('text'),
    ]

    class Meta:
        verbose_name_plural = 'Footer Text'

    def __str__(self):
        return "Footer Text"
