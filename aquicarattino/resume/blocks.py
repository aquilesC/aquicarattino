from wagtail.core import blocks


class SocialLink(blocks.StructBlock):
    social_network = blocks.URLBlock(required=True, label='Profile to link to')
    name = blocks.CharBlock(required=True, label='Name to show on website')
    fa_icon = blocks.CharBlock(required=True, label='Font Awesome Icon to use, for example fa-linkedin-in')

    class Meta:
        icon = 'fa-linkedin'
        template = 'resume/social_link_block.html'


class SocialProfileBlock(blocks.StreamBlock):
    social_link = SocialLink()

    class Meta:
        icon = 'fa-linkedin-in'
        template = 'resume/social_profile_block.html'


class WorkExperienceBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    start_date = blocks.DateBlock(required=True)
    end_date = blocks.DateBlock(required=False)
    description = blocks.RichTextBlock(required=True)
    tags = blocks.ListBlock(blocks.CharBlock())

    class Meta:
        template = 'resume/work_experience_block.html'