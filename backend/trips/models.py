import uuid

from django.db import models
# from backend.profiles.models import User
from places.models import Place
# Create your models here.
class Trip(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    places = models.ManyToManyField(Place)
    