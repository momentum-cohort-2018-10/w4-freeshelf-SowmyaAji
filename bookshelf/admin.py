from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from bookshelf.models import Book, Category


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('name', 'author', 'description',
                    'url', 'picture',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Book, BookAdmin)
admin.site.register(Category)
