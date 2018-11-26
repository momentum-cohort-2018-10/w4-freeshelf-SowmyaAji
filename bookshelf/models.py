from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from datetime import date
from django.core.files import File
from django.template.defaultfilters import slugify
# from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def save(self):

        if not self.id:
            self.slug = slugify(self.title)
        super(Category, self).save()


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    categories = models.ManyToManyField(to="bookshelf.Category")
    description = models.TextField(null=True)
    url = models.URLField(max_length=255)
    date = models.DateField(auto_now=False, auto_now_add=False)
    slug = models.SlugField(unique=True)
    picture = models.ImageField(upload_to='books/', blank=True)
    comment = models.TextField(null=True)
    # user = models.OneToOneField(
    #     User, on_delete=models.CASCADE, blank=True, null=True)

    def save(self):

        if not self.id:
            self.slug = slugify(self.name)
        super(Book, self).save()


# class BookForm(models.Model):

#     comment = models.CharField(max_length=255, blank=True)
class Comment(models.Model):
    book = models.ForeignKey(
        'Book', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    # created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
