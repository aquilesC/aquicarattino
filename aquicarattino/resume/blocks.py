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
    where = blocks.CharBlock(required=True)
    start_date = blocks.DateBlock(required=True)
    end_date = blocks.DateBlock(required=False)
    description = blocks.RichTextBlock(required=True)
    tags = blocks.ListBlock(blocks.CharBlock())

    class Meta:
        template = 'resume/work_experience_block.html'


class WorkBlock(blocks.StreamBlock):
    work = WorkExperienceBlock()


class SkillBlock(blocks.StructBlock):
    name = blocks.CharBlock(max_length=25, required=True)
    percentage = blocks.IntegerBlock(min_value=0, max_value=100, help_text='Confidence in this skill', required=True)


class SkillsetBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    skills = blocks.ListBlock(SkillBlock())

    class Meta:
        template = 'resume/skill_tool_block.html'


class OtherSkillBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)

    class Meta:
        template = 'resume/other_skill_block.html'


class EducationBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=50, required=True)
    where = blocks.CharBlock(max_length=75, required=True)
    start_date = blocks.DateBlock(required=True)
    end_date = blocks.DateBlock(required=False)

    class Meta:
        template = 'resume/education_block.html'


class EducationStreamBlock(blocks.StreamBlock):
    education = EducationBlock()

    class Meta:
        template = 'resume/education_stream_block.html'


class MiscellaneousBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=50, required=True)
    description = blocks.TextBlock(required=True)

    class Meta:
        template = 'resume/miscellaneous_block.html'


class MiscellaneousStreamBlock(blocks.StreamBlock):
    content = MiscellaneousBlock()

    class Meta:
        template = 'resume/miscellaneous_stream_block.html'


class LanguageBlock(blocks.StructBlock):
    language = blocks.CharBlock(max_length=50, required=True)
    proficiency = blocks.CharBlock(max_length=50, required=True)

    class Meta:
        template = 'resume/language_block.html'


class LanguageStreamBlock(blocks.StreamBlock):
    language = LanguageBlock()

    class Meta:
        template = 'resume/language_stream_block.html'


class InterestBlock(blocks.StructBlock):
    name = blocks.CharBlock(max_length=20, required=True)

    class Meta:
        template = 'resume/interest_block.html'


class InterestsStreamBlock(blocks.StreamBlock):
    interest = InterestBlock()

    class Meta:
        template = 'resume/interests_stream_block.html'
