from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=255)

# Use Google Places API(New) to fetch objects
class Place(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    # Overview
    name = models.CharField(max_length=255)
    # ---To be decided. Depends on quota -----
    # picture =
    # description = models.TextField(blank=True)
    # -----------------------------------------
    display_name = models.CharField(max_length=255)
    primary_type = models.ForeignField(Type, on_delete=models.CASCADE)
    types = models.ManyToManyField(Type, on_delete=models.CASCADE, related_name="places")

    # picture = 
    # ------------------------------- #
    # Location (Parsed from address)
    address = models.TextField()
    region = models.TextField()
    country = models.TextField()
    # ------------------------------- #
    # Coordinates (For maps)
    # latitude = models.FloatField()
    # longitude = models.FloatField()
    # ------------------------------- #
    # Filtering
    # popularity = models.FloatField() # 0-1
    price = models.FloatField()
    rating = models.FloatField() # 0-10
    # Contact info
    telephone = models.TextField()
    website = models.URLField()
    # Amenities
    allows_dogs = models.BooleanField(default=False)
    allows_outdoor_seating = models.BooleanField(default=False)
    allows_reservations = models.BooleanField(default=False)
    serves_vegetarian_food = models.BooleanField(default=False)
    has_restroom = models.BooleanField(default=False)
    good_for_children = models.BooleanField(default=False)
    has_wi_fi = models.BooleanField(default=False)
    # ------------------------------- #

    def __str__(self):
        return self.name

class OpeningPeriod(models.Model):
    DAY_CHOICES = [
        (0, 'Sunday'),
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
    ]

    place = models.ForeignKey(Place, related_name='opening_periods', on_delete=models.CASCADE)
    
    open_day = models.IntegerField(choices=DAY_CHOICES)
    open_time = models.TimeField() 
    
    close_day = models.IntegerField(choices=DAY_CHOICES)
    close_time = models.TimeField() 

    class Meta:
        ordering = ['open_day', 'open_time']

    def __str__(self):
        return f"{self.get_open_day_display()}: {self.open_time} - {self.close_time}"