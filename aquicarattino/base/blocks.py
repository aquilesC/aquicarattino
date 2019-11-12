from wagtail.core.blocks import StructBlock, TextBlock, CharBlock, URLBlock, ListBlock, StreamBlock, RichTextBlock, \
    ChoiceBlock
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


class CarouselBlock(StructBlock):
    image_items = ListBlock(
        ImageChooserBlock(required=True),
        label="Image Item"
    )

    class Meta:
        icon = "fa-images"
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


class ContentBlock(StreamBlock):
    text = RichTextBlock(
        icon='fa fa-paragraph',
        template='blocks/paragraph_block.html'
    )
    alert_block = AlertBlock(required=False)
    button_block = ButtonBlock(required=False)
    carousel_block = CarouselBlock()
    testimonial = TestimonialBlock()
    class Meta:
        icon = 'fa fa-scroll'
        template = 'blocks/content_block.html'


class ProjectStreamBlock(StreamBlock):
    content = ContentBlock()