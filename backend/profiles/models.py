from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(models.Model):
    displayed_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return f"Profile for {self.user.email}"

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='user')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']