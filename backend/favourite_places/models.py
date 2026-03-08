from django.db import models
from profiles.moedls import UserProfile
from places.models import Place
# Create your models here.
class FavouritePlace(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="favourite_places")
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)