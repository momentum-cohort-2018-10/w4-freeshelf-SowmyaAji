from django.shortcuts import render, redirect
from bookshelf.forms import BookForm

from bookshelf.models import Book


from django.conf import settings
from django.conf.urls.static import static

# Create your views here.


def index(request):
    return render(request, 'index.html')
