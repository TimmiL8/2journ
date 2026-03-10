from django.urls import path
from .views import *
urlpatterns = [
    path('trips/', TripListDetailView.as_view(), name='trip-list'),
    path('trips/create/', TripCreateView.as_view(), name='trip-create'),
    path('trips/<str:id>/', TripDetailView.as_view(), name='trip-detail'),
    path('trips/<str:id>/update/', TripUpdateView.as_view(), name='trip-update'),
    path('trips/<str:id>/delete/', TripDeleteView.as_view(), name='trip-delete'),

]