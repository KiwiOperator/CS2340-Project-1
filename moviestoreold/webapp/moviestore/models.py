from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model


class Movie(models.Model):
    title = models.CharField(max_length = 200)
    genre = models.TextField()
    overview = models.TextField()
    release_date = models.DateField()
    image_url = models.URLField(max_length = 200)
    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links the review to a user
    movie_title = models.CharField(max_length=200)  # Title of the movie being reviewed
    review_text = models.TextField()  # The review itself
    rating = models.IntegerField(default=1, choices=[(i, i) for i in range(1, 6)])  # Rating (1-5)
    created_at = models.DateTimeField(auto_now_add=True)  # When the review was created
    updated_at = models.DateTimeField(auto_now=True)  # When the review was last updated

    def __str__(self):
        return f"{self.movie_title} - {self.user.username} ({self.rating}/5)"

class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie)