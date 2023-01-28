from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Blog(models.Model):
    image = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=100, verbose_name='Title')
    description = RichTextUploadingField()
    title2 = models.CharField(max_length=100, verbose_name='Title 2')
    description2 = RichTextUploadingField()
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Name')
    email = models.EmailField()
    website = models.CharField(max_length=150, verbose_name='Website')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return f'{self.name} --->>> {self.blog}'
