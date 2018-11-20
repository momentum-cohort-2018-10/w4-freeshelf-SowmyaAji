from django.db import models
from datetime import date


# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    date = models.DateField(auto_now=False, auto_now_add=False)
    slug = models.SlugField(unique=True)
    picture = models.ImageField(upload_to='books/', null=False)


class BookForm(models.Model):

    comment = models.CharField(max_length=255, blank=True)
