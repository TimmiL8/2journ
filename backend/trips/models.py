import uuid
from django.db import models
from profiles.models import User # Corrected import path
from places.models import Place

class Trip(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # The 'owner' is the User who created the trip
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')
    title = models.CharField(max_length=255, default="My Trip")
    places = models.ManyToManyField(Place)
    
    def __str__(self):
        return self.title