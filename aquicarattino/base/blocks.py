from wagtail.core.blocks import StructBlock, TextBlock, CharBlock, URLBlock, ListBlock, StreamBlock, RichTextBlock
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


class ProjectStreamBlock(StreamBlock):
    paragraph_block = RichTextBlock(
        icon='fa fa-paragraph',
        template='blocks/paragraph_block.html'
    )
    carousel_block = CarouselBlock()
    testimonial = TestimonialBlock()