from django.db import models
from django.contrib.auth.models import User

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    email = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self) -> str:
        return self.user.username