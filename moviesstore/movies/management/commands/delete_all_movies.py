# delete_all_movies.py
from django.core.management.base import BaseCommand
from movies.models import Movie

class Command(BaseCommand):
    help = 'Delete all movies from the database'

    def handle(self, *args, **kwargs):
        Movie.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all movies'))