from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from datetime import date
from django.core.files import File
from django.template.defaultfilters import slugify

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    #book = models.ForeignKey(to="Book", on_delete=models.CASCADE)


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    categories = models.ManyToManyField(to="bookshelf.Category")
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


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
