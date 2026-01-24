from django.urls import path
from places.views import *
urlpatterns = [
    path('', PlacesListView.as_view(), name='index'),
    path('<str:uuid>/', PlaceDetailView.as_view(), name='detail'),
]