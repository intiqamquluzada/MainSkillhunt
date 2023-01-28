# Generated by Django 4.1.3 on 2022-11-30 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField()),
                ('title2', models.CharField(max_length=100, verbose_name='Title 2')),
                ('description2', models.TextField()),
            ],
        ),
    ]
