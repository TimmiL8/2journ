from rest_framework import serializers
from .models import Trip

class TripSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Trip
        # fields = ["id", "title", "description", "start_date", "end_date"]
        fields = '__all__'