from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.filters import OrderingFilter
from rest_framework.exceptions import NotFound
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from places.filters import PlacesFilter
from places.models import Place
from places.serializers import PlaceListSerializer, PlaceDetailSerializer


# Create your views here.

class PlacesListView(generics.ListAPIView):
    # authentication_classes = (SessionAuthentication, )
    # authentication_classes = (AllowAny,)
    queryset = Place.objects.all()
    filter_backends = (OrderingFilter, DjangoFilterBackend,)
    filterset_class = PlacesFilter
    ordering_fields = ['price', 'name', 'rating']
    ordering_field = ['-name']
    serializer_class = PlaceListSerializer


class PlaceDetailView(generics.RetrieveAPIView):
    serializer_class = PlaceDetailSerializer

    def get_object(self):
        place_id = self.request.query_params.get('id')

        if not place_id:
            raise NotFound("ID query parameter is required.")

        try:
            return Place.objects.get(id=place_id)
        except (Place.DoesNotExist, ValueError):
            raise NotFound("Place not found.")
