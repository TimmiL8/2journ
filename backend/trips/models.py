from django.db import models
from uuid import uuid4
# Create your models here.
class Trip(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)   
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    # Fields to be added later
    # places = models.ManyToManyField('places.Place', related_name='trips')
    # owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='trips')
    # participants = models.ManyToManyField('auth.User', related_name='participating_trips', blank=True)

    def __str__(self):
        return f"{self.title} {self.start_date} - {self.end_date} by \
        {self.owner.username if hasattr(self, 'owner') else 'Unknown'}"
