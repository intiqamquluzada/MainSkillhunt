# Generated by Django 4.1.3 on 2022-12-02 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='slug',
            field=models.SlugField(default='r'),
            preserve_default=False,
        ),
    ]