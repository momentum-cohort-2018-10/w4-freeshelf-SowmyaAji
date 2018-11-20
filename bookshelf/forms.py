from django.forms import ModelForm
from bookshelf.models import BookForm


class CommentForm(ModelForm):

    class Meta:

        model = BookForm
        fields = ('comment',)
