from django.urls import path
from places.views import *


urlpatterns = [
    path('search/', PlaceSearchList.as_view(), name='index'),
    path('place/<str:place_id>/', PlaceDetailView.as_view(), name='detail'),
    path('favourites/', ListFavouritePlaces.as_view(), name='favourites'),
    path('<str:place_id>/toggle_favourite/', PlaceToggleFavouriteView.as_view(), name='add-favourite'),
]