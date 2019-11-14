# Generated by Django 2.2.7 on 2019-11-14 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('projects', '0003_projectindexpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='logo',
            field=models.ForeignKey(blank=True, help_text='Overlay logo for the list of projects', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
