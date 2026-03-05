from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from places.models import Place
from profiles.models import FavouritePlace
class PlaceListSerializer(ModelSerializer):
    """
    Serializer for place list
    Includes:
        - Descriptive fields: id, name
        - Sorting fields: popularity, price, rating
        - Category fields: category, country, region
    """

    is_favourite = serializers.SerializerMethodField()
    class Meta:
        model = Place
        fields = ('id', 'name', 'short_name', 'category', 'popularity', 'price', 'rating', 'country', 'region', "is_favourite")

    def get_is_favourite(self, obj):
        return getattr(obj, 'is_favourite', False)

class PlaceDetailSerializer(ModelSerializer):
    """
        Serializer for place details
        Includes:
            - Descriptive fields: id, name, short_name, description, pictures, website
            - Sorting fields: popularity, price, rating
            - Category fields: category, country, region
        """
    is_favourite = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = ('id', 'name', 'description', 'short_name', 'category', 'popularity', 'price', 'rating', 'country',
                  'region', 'pictures', 'website')

    def get_is_favourite(self, obj):
        return getattr(obj, 'is_favourite', False)
class PlaceUpdateSerializer(ModelSerializer):
    """
        Serializer for place update
        Includes:
            - Descriptive fields: id, name, short_name, description, pictures, website
            - Sorting fields: popularity, price, rating
            - Category fields: category, country, region
        """
    class Meta:
        model = Place
        fields = ('id', 'name', 'description', 'short_name', 'category', 'popularity', 'price', 'rating', 'country',
                  'region', 'pictures', 'website')

class FavouritePlaceListSerializer(ModelSerializer):
    class Meta:
        model = FavouritePlace
        fields = ('id', 'place_id', 'created_at')