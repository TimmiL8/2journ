from rest_framework.serializers import ModelSerializer
from places.models import Place
class PlaceListSerializer(ModelSerializer):
    """
    Serializer for place list
    Includes:
        - Descriptive fields: id, name
        - Sorting fields: popularity, price, rating
        - Category fields: category, country, region
    """
    class Meta:
        model = Place
        fields = ('id', 'name', 'short_name', 'category', 'popularity', 'price', 'rating', 'country', 'region')


class PlaceDetailSerializer(ModelSerializer):
    """
        Serializer for place details
        Includes:
            - Descriptive fields: id, name, short_name, description, pictures, website
            - Sorting fields: popularity, price, rating
            - Category fields: category, country, region
        """
    class Meta:
        model = Place
        fields = ('id', 'name', 'description', 'short_name', 'category', 'popularity', 'price', 'rating', 'country',
                  'region', 'pictures', 'website')

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
