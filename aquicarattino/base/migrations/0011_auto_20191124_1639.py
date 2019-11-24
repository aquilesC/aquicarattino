# Generated by Django 2.2.7 on 2019-11-24 16:39

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_formfield_formpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formpage',
            name='body',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.RichTextBlock(icon='fa fa-paragraph', template='blocks/paragraph_block.html')), ('alert_block', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(required=True))], required=False)), ('button_block', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(required=True)), ('text', wagtail.core.blocks.CharBlock(required=True))], required=False)), ('carousel_block', wagtail.core.blocks.StructBlock([('image_items', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(required=True), label='Image Item'))])), ('testimonial', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(required=True)), ('author', wagtail.core.blocks.CharBlock(label='Who said this?', required=True)), ('author_title', wagtail.core.blocks.CharBlock(label='Role of this person', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(label='Link to the person website', required=False))])), ('code_block', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.CharBlock(help_text='In which language this is written', max_length=20, required=True)), ('code', wagtail.core.blocks.TextBlock(help_text='The actual code', required=True))])), ('markdown_block', wagtailmarkdown.blocks.MarkdownBlock())]),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='body',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.RichTextBlock(icon='fa fa-paragraph', template='blocks/paragraph_block.html')), ('alert_block', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(required=True))], required=False)), ('button_block', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(required=True)), ('text', wagtail.core.blocks.CharBlock(required=True))], required=False)), ('carousel_block', wagtail.core.blocks.StructBlock([('image_items', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(required=True), label='Image Item'))])), ('testimonial', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock(required=True)), ('author', wagtail.core.blocks.CharBlock(label='Who said this?', required=True)), ('author_title', wagtail.core.blocks.CharBlock(label='Role of this person', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(label='Link to the person website', required=False))])), ('code_block', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.CharBlock(help_text='In which language this is written', max_length=20, required=True)), ('code', wagtail.core.blocks.TextBlock(help_text='The actual code', required=True))])), ('markdown_block', wagtailmarkdown.blocks.MarkdownBlock())]),
        ),
    ]
