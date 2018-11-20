from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
import csv
from bookshelf.models import Book
from django.core.files import File


def get_path(file):
    return os.path.join(settings.BASE_DIR, 'initial_data', file)


class Command(BaseCommand):
    help = "Load books from book_data.csv"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):

        with open(get_path('book_data.csv'), 'r') as file:
            reader = csv.DictReader(file)
            i = 0
            for row in reader:
                i += 1
                book = Book(
                    name=row['name'],
                    author=row['author']
                    description=row['description'],
                    category=row['category'],
                    url=row['url'],
                    date=row['date'],

                )
                book.picture.save(row['picture'],
                                  File(open(get_path(row['picture']), 'rb')))
                book.save()
        print(f"{i} dogs loaded!")
