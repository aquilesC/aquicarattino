from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core.blocks import CharBlock
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page

from .blocks import SocialProfileBlock, WorkExperienceBlock, WorkBlock, SkillsetBlock, OtherSkillBlock, EducationBlock, \
    MiscellaneousStreamBlock, LanguageStreamBlock
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class ResumePage(Page):
    name = models.CharField(max_length=250, blank=False, null=False, help_text='Your name')
    subtitle = models.CharField(max_length=250, blank=False, null=False, help_text='Subtitle, under the name')
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    career_summary = models.TextField()

    work_experience = StreamField(
        WorkBlock(),
        help_text='Work Experience',
        null=True,
        blank=True
    )

    skills_tools = StreamField([
        ('skills_tools', SkillsetBlock()),
    ],
        help_text='Skills and Tools',
        null=True,
        blank=True,
    )

    other_skills = StreamField([
        ('other_skills', OtherSkillBlock()),
    ],
        help_text='Other Skills',
        null=True,
        blank=True,
    )

    education = StreamField([
        ('education', EducationBlock()),
    ],
        help_text='Education',
        null=True,
        blank=True
    )

    miscellaneous = StreamField(MiscellaneousStreamBlock(), blank=True, null=True)

    languages = StreamField(LanguageStreamBlock(), blank=True, null=True)

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
        StreamFieldPanel('work_experience'),
        StreamFieldPanel('skills_tools'),
        StreamFieldPanel('other_skills'),
        StreamFieldPanel('education'),
        StreamFieldPanel('miscellaneous'),
        StreamFieldPanel('languages'),
        DocumentChooserPanel('pdf_link'),
        ImageChooserPanel('profile_image'),
        StreamFieldPanel('social_profiles')
    ]
