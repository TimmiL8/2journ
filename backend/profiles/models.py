from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #makes the email field unique so two people can't use the same one
    email = models.EmailField(unique=True)
    
    #tells Django to use the email for logging in
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] # Django still needs this internally
class Profile(models.Model):
    # This links the Profile to exactly one User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    displayed_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return f"Profile for {self.user.email}"