from django.db import models
from django.utils.text import slugify


class BrowseJobs(models.Model):
    CHOICES_2 = (
        ('Full time', 'full_time'),
        ('Part time', 'part_time'),
        ('Freelance', 'freelance'),
        ('Internship', 'internship'),
        ('Termporary', 'termporary')
    )
    schedule = models.CharField(choices=CHOICES_2, max_length=100)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class JobPost(models.Model):
    CHOICES = (
        ('full_time', 'Full time'),
        ('part_time', 'Part time'),
        ('freelance', 'Freelance'),
        ('internship', 'Internship'),
        ('termporary', 'Termporary')
    )
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    job_type = models.CharField(choices=CHOICES, max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Candidates(models.Model):
    CHOICES = (
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('doctor', 'Doctorant'),
        ('noedu', 'No education')
    )
    location = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100, choices=CHOICES)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='media/')
    file = models.FileField(upload_to='cves/')
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.full_name

    def get_unique_slug(self):
        slug = slugify(self.full_name)
        unique_slug = slug
        counter = 1
        while Candidates.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug} -- {counter}'
            counter += 1
        return unique_slug

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None, *args, **kwargs
    ):
        if not self.slug:
            self.slug = self.get_unique_slug()
        return super(Candidates, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']


class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
