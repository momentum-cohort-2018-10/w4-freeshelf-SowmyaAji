from django.forms import ModelForm
from bookshelf.models import Book, Comment


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class BookForm(ModelForm):

    class Meta:

        model = Book
        fields = ('comment',)
