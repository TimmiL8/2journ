from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

class Attributes(models.Model):
    """
    A class to store additional info about the place. 
    """
    # class ThreeGradeScale(models.TextChoices):
    #     POOR = "P", _("Poor")
    #     AVERAGE = "A", _("Average")
    #     GREAT = "G", _("Great")

    atm = models.BooleanField(blank=True)
    bar = models.BooleanField(blank=True)
    byo = models.BooleanField(blank=True)
    essential_reservation = models.BooleanField(blank=True)

class Pictures(models.Model):
    """
    Picture ids for a place object
    1. To obtain the original size of the photo, combine
    prefix + original + suffix:
    https://fastly.4sqi.net/img/general/original/1049719_PiLE0Meoa27AkuLvSaNwcvswnmYRa0vxLQkOrpgMlwk.jpg
    2. To scale down this photo, 1) determine the size you want,
    paying close attention to not exceed the maximum width and height. 2) using your desired width (800px) &
    height (600px), convert this to a size (width x height) and combine
    prefix + size + suffix:
    https://fastly.4sqi.net/img/general/800x600/1049719_PiLE0Meoa27AkuLvSaNwcvswnmYRa0vxLQkOrpgMlwk.jpg
    3. To crop this photo, determine the size you would like (ie. 400x400) and combine
    prefix + size + suffix:
    https://fastly.4sqi.net/img/general/200x200/1049719_PiLE0Meoa27AkuLvSaNwcvswnmYRa0vxLQkOrpgMlwk.jpg

    """
    id = models.AutoField(primary_key=True)
    prefix = models.CharField(max_length=255)
    suffix = models.CharField(max_length=255)
    place_id = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    created_at = models.DateTimeField()


# Use foursquare API to fetch objects
class Place(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    # Overview
    name = models.CharField(max_length=255)
    description = models.TextField()
    short_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Pictures  Docs: https://docs.foursquare.com/fsq-developers-places/reference/place-photos
    pictures = models.ManyToManyField(Pictures)

    # ------------------------------- #
    # Location
    address = models.TextField()
    region = models.TextField()
    country = models.TextField()
    # ------------------------------- #
    # Coordinates (For maps)
    # latitude = models.FloatField()
    # longitude = models.FloatField()
    # ------------------------------- #
    # Filtering
    popularity = models.FloatField() # 0-1
    price = models.FloatField() # Range unknown
    rating = models.FloatField() # 0-10
    # Contact info
    email = models.EmailField()
    telephone = models.TextField()
    website = models.URLField()
    # Open/close (Find the way to store the "regular" object)
    # open = models.TimeField()
    # close = models.TimeField()
    # is_open = models.BooleanField()
    # Socials
    # facebook_id = models.CharField(max_length=255)
    # instagram = models.CharField(max_length=255)
    # twitter = models.CharField(max_length=255)
    # ------------------------------- #
