from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
import csv
from bookshelf.models import Book, Category
from django.core.files import File
from django.template.defaultfilters import slugify
import pdb


def get_path(file):
    return os.path.join(settings.BASE_DIR, 'initial_data', file)


class Command(BaseCommand):
    help = "Load books from initial_data/book_data.csv"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):

        Book.objects.all().delete()

        with open(get_path('book_data.csv'), 'r') as file:
            reader = csv.DictReader(file, delimiter=',')

            for row in reader:

                book = Book(
                    name=row['name'],
                    author=row['author'],
                    description=row['description'],
                    url=row['url'],
                    date=row['date'].strip()
                )

                book.save()
                book.picture.save(row['picture'],
                                  File(open(get_path(row['picture'].strip()), 'rb')))
                categories = row['categories'].split('|')

                for category in categories:
                    title = category.strip()
                    slug = slugify(title)
                    try:
                        cat = Category.objects.get(slug=slug)
                    except:
                        cat = Category(title=title)
                        cat.slug = slug
                        cat.save()

                    if cat not in book.categories.all():
                        book.categories.add(cat)

                book.save()
