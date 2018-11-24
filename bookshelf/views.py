from django.shortcuts import render, redirect
from bookshelf.forms import BookForm

from bookshelf.models import Book


from django.conf import settings
from django.conf.urls.static import static
from django.core.files import File
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):

    books = Book.objects.order_by('-date')

    return render(request, 'index.html', {

        'books': books,
    })


def book_detail(request, slug):

    book = Book.objects.get(slug=slug)

    return render(request, 'books/book_detail.html', {
        'book': book,
    })


@login_required
def comment_book(request, slug):

    book = Book.objects.get(slug=slug)
    if request.method == 'POST':

        form = BookForm(data=request.POST)

        form.save()

        return redirect('book_detail', slug=book.slug)

    else:
        form = BookForm(instance=book)

    return render(request, 'books/comment_book.html', {
        'book': book,
        'form': form,
    })


def suggest_book(request):

    if request.method == 'POST':

        form = BookForm(data=request.POST)

        book = form.save(commit=False)
        book.user = request.user
        book.slug = slugify(book.name)

        book.save()

        return redirect('book_detail', slug=book.slug)

    else:
        form = BookForm()

    return render(request, 'books/create_book.html', {
        # 'book': book,
        'form': form,
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

# def browse_by_author(request, initial=None):
#     if initial:
#         authors = Book.objects.filter(
#             book.author__istartswith=initial).order_by('book.author')
#     else:
#         authors = Book.objects.all().order_by('')

#     return render(request, 'search/search.html', {
#         'authors': book.authors,
#         'initial': initial,
#     })
