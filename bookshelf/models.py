from django.db import models
from datetime import date
from django.core.files import File
from django.template.defaultfilters import slugify

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField(null=True)
    url = models.URLField(max_length=255)
    date = models.DateField(auto_now=False, auto_now_add=False)
    slug = models.SlugField(unique=True)
    picture = models.ImageField(upload_to='books/', blank=True)

    def save(self):

        if not self.id:
            self.slug = slugify(self.name)
        super(Book, self).save()


class BookForm(models.Model):

    comment = models.CharField(max_length=255, blank=True)
