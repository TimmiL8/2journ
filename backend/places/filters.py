from django_filters import rest_framework as filters
from places.models import Place, Category


class PlacesFilter(filters.FilterSet):
    RATING_CHOICES = [(float(i)/2, str(i/2)) for i in range(2, 11)]
    PRICE_CHOICES = [(i, str(i)) for i in range(5)]

    # Change lookup_expr if needed
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    region = filters.CharFilter(field_name='region', lookup_expr='iexact')
    country = filters.CharFilter(field_name='country', lookup_expr='icontains')
    category = filters.ModelChoiceFilter(queryset=Category.objects.all())

    rating = filters.MultipleChoiceFilter(
        choices = RATING_CHOICES,
        field_name='rating',
        lookup_expr='exact',
    )

    price = filters.MultipleChoiceFilter(
        choices = PRICE_CHOICES,
        field_name='price',
        lookup_expr='exact',
    )
    class Meta:
        model = Place
        fields = ['rating', 'price', 'name', 'region', 'country', 'category']