from django.db.models.expressions import OuterRef, Exists
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.http.response import JsonResponse
from places.filters import PlacesFilter
from profiles.models import Place, FavouritePlace
from places.serializers import PlaceListSerializer, PlaceDetailSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import requests
import os


import json
# Create your views here.


class PlacesListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        favourite_subquery = FavouritePlace.objects.filter(
            user_profile=request.user.profile,
            place_id=OuterRef('pk')
        )
        places = Place.objects.annotate(is_favourite=Exists(favourite_subquery))
        serializer = PlaceListSerializer(places, many=True, context={'request': request})
        return Response(serializer.data)

class PlaceDetailView(APIView):
    def get(self, request, place_id):
        try:
            favourite_subquery = FavouritePlace.objects.filter(
                user_profile=request.user.profile,
                place_id=OuterRef('pk')
            )
            place = Place.objects.annotate(
                is_favourite=Exists(favourite_subquery)
            ).get(id=place_id)
        except Place.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PlaceDetailSerializer(place, context={'request': request})
        return Response(serializer.data)

class PlaceSearchList(APIView):

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'search_query',
                openapi.IN_QUERY,
                description="Search places by name",
                type=openapi.TYPE_STRING
            )
        ]
    )

    # def post(self, request, search_query):
    #     load_dotenv()
    #     API_KEY = os.getenv("GOOGLE_PLACES_API")
    #
    #
    #     if not search_query:
    #         return Response({"error": "searchQuery is required"}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     url = "https://places.googleapis.com/v1/places:searchText"
    #     headers = {
    #         "Content-Type":"application/json",
    #         "X-Goog-FieldMask":"places.displayName,places.formattedAddress,places.priceLevel",
    #         "X-Goog-Api-Key": API_KEY,
    #     }
    #     payload = {
    #         "textQuery": search_query
    #     }
    #
    #     response = requests.post(url, json=payload, headers=headers)
    #     response.raise_for_status()
    #     data = response.json()
    #
    #     with open('data.json', 'w', encoding='utf-8') as f:
    #         json.dump(data, f, ensure_ascii=False, indent=4)
    #     places = Place.objects.filter(name__icontains=search_query)
    #     return Response(PlaceListSerializer(places).data)
    def get(self, request):  # ✅ changed to GET, search_query from query params
        search_query = request.query_params.get('search_query', '')
        favourite_subquery = FavouritePlace.objects.filter(
            user_profile=request.user.profile,
            place_id=OuterRef('pk')
        )
        places = Place.objects.filter(
            name__icontains=search_query
        ).annotate(is_favourite=Exists(favourite_subquery))
        return Response(PlaceListSerializer(places, many=True, context={'request': request}).data)


class ListFavouritePlaces(APIView):
    permission_classes = [IsAuthenticated]  # ✅ added

    def get(self, request):
        favourite_subquery = FavouritePlace.objects.filter(
            user_profile=request.user.profile,
            place_id=OuterRef('pk')
        )
        places = Place.objects.filter(
            id__in=FavouritePlace.objects.filter(  # ✅ query Places not FavouritePlaces
                user_profile=request.user.profile
            ).values_list('place_id', flat=True)
        ).annotate(is_favourite=Exists(favourite_subquery))

        if not places.exists():  # ✅ fixed condition
            return Response({"message": "No favourites found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(PlaceListSerializer(places, many=True, context={'request': request}).data)


class PlaceToggleFavouriteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, place_id):
        try:
            place = Place.objects.get(id=place_id)
        except Place.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        favourite, created = FavouritePlace.objects.get_or_create(
            user_profile=request.user.profile,
            place_id=place
        )
        if not created:
            favourite.delete()
            return Response({'is_favourite': False}, status=status.HTTP_200_OK)
        return Response({'is_favourite': True}, status=status.HTTP_201_CREATED)

