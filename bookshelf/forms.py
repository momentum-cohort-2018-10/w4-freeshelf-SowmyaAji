from django.forms import ModelForm
from bookshelf.models import BookForm


class BookForm(ModelForm):

    class Meta:

        model = BookForm
        fields = ('comment',)
