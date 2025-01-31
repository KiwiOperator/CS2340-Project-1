import csv
from django.core.management.base import BaseCommand
from moviestore.models import Movie

class Command(BaseCommand):
    help = 'Import movies from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The Path of CSV file to be imported')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Title'] and row['Genre'] and row['Overview'] and row['Release_Date'] and row['Poster_Url']:
                    Movie.objects.create(
                        title = row['Title'],
                        genre = row['Genre'],
                        overview = row['Overview'],
                        release_date = row['Release_Date'],
                        image_url = row['Poster_Url']
                    )
                else :
                    self.stdout.write(self.style.WARNING(f"Skipping row with missing data: {row}"))
            self.stdout.write(self.style.SUCCESS('Successfully imported movies'))