from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length = 200)
    genre = models.TextField()
    overview = models.TextField()
    release_date = models.DateField()
    image_url = models.URLField(max_length = 200)

    def __str__(self):
        return self.title


