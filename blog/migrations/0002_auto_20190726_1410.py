# Generated by Django 2.2.3 on 2019-07-26 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish_time',
            field=models.DateTimeField(null=True),
        ),
    ]
