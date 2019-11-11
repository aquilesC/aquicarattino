# Generated by Django 2.2.7 on 2019-11-11 20:58

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_resumepage_social_profiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumepage',
            name='social_profiles',
            field=wagtail.core.fields.StreamField([('social_link', wagtail.core.blocks.StructBlock([('social_network', wagtail.core.blocks.URLBlock(label='Profile to link to', required=True)), ('fa_icon', wagtail.core.blocks.CharBlock(label='Font Awesome Icon to use, for example fa-linkedin-in', required=True))]))], blank=True, help_text='Links to social profiles', null=True),
        ),
    ]
