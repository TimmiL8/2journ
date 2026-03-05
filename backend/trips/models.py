from datetime import date

from django.db import models
from uuid import uuid4
from places.models import Place
# Create your models here.
class Trip(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200, default='Trip')
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    places = models.ManyToManyField(Place)

    # owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='trips')


    def __str__(self):
        return f"{self.title} {self.start_date} - {self.end_date} by \
        {self.owner.username if hasattr(self, 'owner') else 'Unknown'}"


import uuid






