from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.filters import OrderingFilter
from rest_framework import status
from rest_framework.exceptions import NotFound
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http.response import JsonResponse
from places.filters import PlacesFilter
from places.models import Place
from places.serializers import PlaceListSerializer, PlaceDetailSerializer
from dotenv import load_dotenv

import requests
import os


import json
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
        
class PlaceSearchList(APIView):
    def post(self, request):
        load_dotenv()
        API_KEY = os.getenv("GOOGLE_PLACES_API")
       
        search_query = request.data.get("searchQuery")
        if not search_query:
            return Response({"error": "searchQuery is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        url = "https://places.googleapis.com/v1/places:searchText"
        headers = {
            "Content-Type":"application/json",
            "X-Goog-FieldMask":"places.displayName,places.formattedAddress,places.priceLevel",
            "X-Goog-Api-Key": API_KEY,
        }
        payload = {
            "textQuery": search_query
        }

        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status() 
        data = response.json()

        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        return JsonResponse(data)


