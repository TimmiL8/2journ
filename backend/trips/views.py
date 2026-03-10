from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Trip
from .serializers import TripSerializer

class TripViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing trip instances.
    """
    queryset = Trip.objects.all()
    serializer_class = TripSerializer