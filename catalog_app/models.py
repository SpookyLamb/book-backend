from django.db import models
from django.contrib.auth.models import User

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    email = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self) -> str:
        return self.user.username

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)
    user_rating = models.IntegerField(default=0)
    favorite = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"BOOK: {self.title}, by {self.author} in the {self.genre} genre."