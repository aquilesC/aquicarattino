from wagtail.core import blocks


class RelatedItemsBlock(blocks.StructBlock):
    items = blocks.ListBlock(blocks.PageChooserBlock(page_type='blog.ArticlePage'))

    class Meta:
        icon = 'text'
        template = 'blocks/related_item.html'
