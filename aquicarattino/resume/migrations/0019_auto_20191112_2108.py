# Generated by Django 2.2.7 on 2019-11-12 21:08

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0018_resumepage_miscelaneous'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resumepage',
            old_name='miscelaneous',
            new_name='miscellaneous',
        ),
        migrations.AddField(
            model_name='resumepage',
            name='languages',
            field=wagtail.core.fields.StreamField([('language', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('proficiency', wagtail.core.blocks.CharBlock(max_length=50, required=True))]))], blank=True, null=True),
        ),
    ]
