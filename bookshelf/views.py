
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from bookshelf.forms import BookForm, CommentForm

from bookshelf.models import Book, Category


from django.conf import settings
from django.conf.urls.static import static
from django.core.files import File
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required


def index(request):

    books = Book.objects.order_by('-date')

    return render(request, 'index.html', {

        'books': books,
        'categories': Category.objects.all(),

    })


def book_detail(request, slug):

    book = Book.objects.get(slug=slug)

    return render(request, 'books/book_detail.html', {
        'book': book,
    })


def category_more(request, slug):

    category = Category.objects.get(slug=slug)
    return render(request, 'categories/category_more.html', {
        'category': category,
        'books': Book.objects.filter(categories__slug=category.slug)
    })


def browse_by_name(request, initial=None):
    if initial:
        books = Book.objects.filter(
            name__istartswith=initial).order_by('name')
    else:
        books = Book.objects.all().order_by('name')

    return render(request, 'search/search.html', {
        'books': books,
        'initial': initial,

    })

@login_required
def add_comment_on_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.save()
            return redirect('book_detail', slug=book.slug)
    else:
        form = CommentForm()
    return render(request, 'books/add_comment_on_book.html', {'form': form})


