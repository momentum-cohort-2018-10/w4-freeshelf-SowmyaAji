from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
import csv
from bookshelf.models import Book
from django.core.files import File

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
                    category=row['category'],
                    url=row['url'],
                    date=row['date'].strip(),

                )
                book.picture.save(row['picture'],
                                  File(open(get_path(row['picture'].strip()), 'rb')))

                book.save()
