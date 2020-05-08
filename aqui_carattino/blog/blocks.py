from wagtail.core.blocks import StreamBlock, RichTextBlock, StructBlock, TextBlock, CharBlock, URLBlock, ListBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class TestimonialBlock(StructBlock):
    text = TextBlock(required=True)
    author = CharBlock(
        required=True,
        label="Who said this?"
    )
    author_title = CharBlock(
        required=False,
        label="Role of this person"
    )
    image = ImageChooserBlock(required=False)

    link = URLBlock(required=False, label="Link to the person website")

    class Meta:
        icon = "fa-quote-left"
        template = "blocks/testimonial_block.html"


class QuotableShare(StructBlock):
    text = TextBlock(required=True)

    class Meta:
        icon = 'fa-twitter'
        template = 'blocks/quotable_share.html'


class CarouselBlock(StructBlock):
    image_items = ListBlock(
        ImageChooserBlock(required=True),
        label="Image Item"
    )

    class Meta:
        icon = "image"
        template = "blocks/carousel_block.html"


class ButtonBlock(StructBlock):
    url = URLBlock(required=True)
    text = CharBlock(required=True)

    class Meta:
        icon = "fa-mouse"
        template = "blocks/button_block.html"


class AlertBlock(StructBlock):
    text = RichTextBlock(required=True)

    class Meta:
        icon = "fa-exclamation"
        template = "blocks/alert_block.html"


class CodeBlock(StructBlock):
    language = CharBlock(required=True, max_length=20, help_text='In which language this is written')
    code = TextBlock(required=True, help_text='The actual code')

    class Meta:
        icon = 'fa-code'
        template = 'blocks/code_block.html'


class FullWidthImageBlock(StructBlock):
    image = ImageChooserBlock(required=True)

    class Meta:
        icon = 'image'
        template = 'blocks/full_width_image.html'


class SideBySideImages(StructBlock):
    images = ListBlock(
        ImageChooserBlock(required=True),
        label="Image Item"
    )

    class Meta:
        icon = "image"
        template = 'blocks/side_by_side_images.html'



class ContentBlock(StreamBlock):
    text = RichTextBlock(
        icon='fa-paragraph',
        template='blocks/paragraph_block.html'
    )
    embed_block = EmbedBlock()
    alert_block = AlertBlock(required=False)
    button_block = ButtonBlock(required=False)
    carousel_block = CarouselBlock()
    testimonial = TestimonialBlock()
    quotable_share = QuotableShare()
    code_block = CodeBlock()
    full_width_image = FullWidthImageBlock()
    side_by_side_images = SideBySideImages()

    class Meta:
        icon = 'fa fa-scroll'
        template = 'blocks/content_block.html'
