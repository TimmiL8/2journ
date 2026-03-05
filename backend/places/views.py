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
import requests
import os


import json
# Create your views here.

class PlacesListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        favourite_subquery = FavouritePlace.objects.filter(
            user_profile=request.user.profile,
            place_id = OuterRef('pk')
        )
        places = Place.objects.annotate(is_favourite=Exists(favourite_subquery))
        serializer = PlaceListSerializer(places, many=True, context={'request': request})
        return Response(serializer.data)

class PlaceDetailView(APIView):
    def get(self, request, pk):
        try:
            favourite_subquery = FavouritePlace.objects.filter(
                user_profile=request.user.profile,
                place_id=OuterRef('pk')
            )
            place = Place.objects.annotate(
                is_favourite=Exists(favourite_subquery)
            ).get(pk=pk)
        except Place.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PlaceDetailSerializer(place, context={'request': request})
        return Response(serializer.data)

class PlaceSearchList(APIView):
    def post(self, request, search_query):
        # load_dotenv()
        # API_KEY = os.getenv("GOOGLE_PLACES_API")
        #

        # if not search_query:
        #     return Response({"error": "searchQuery is required"}, status=status.HTTP_400_BAD_REQUEST)
        #
        # url = "https://places.googleapis.com/v1/places:searchText"
        # headers = {
        #     "Content-Type":"application/json",
        #     "X-Goog-FieldMask":"places.displayName,places.formattedAddress,places.priceLevel",
        #     "X-Goog-Api-Key": API_KEY,
        # }
        # payload = {
        #     "textQuery": search_query
        # }
        #
        # response = requests.post(url, json=payload, headers=headers)
        # response.raise_for_status()
        # data = response.json()
        #
        # with open('data.json', 'w', encoding='utf-8') as f:
        #     json.dump(data, f, ensure_ascii=False, indent=4)
        places = Place.objects.filter(name__icontains=search_query)
        return Response(list(places.values()))
class ListFavouritePlaces(APIView):
    # Add appropriate auth classes

    def get(self, request):
        current_user = request.user
        favourites = FavouritePlace.objects.filter(user=current_user)
        if favourites:
            return JsonResponse("No favourites found", safe=False)
        return JsonResponse(favourites)

class PlaceToggleFavouriteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            place = Place.objects.get(pk=pk)
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

