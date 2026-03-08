from django.contrib.auth import get_user_model
from .models import UserProfile
from rest_framework import serializers
User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('displayed_name', 'profile_picture')

class CustomUserSerializer(serializers.ModelSerializer):
    # This matches the 'related_name' in your OneToOneField
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        # We include the UUID 'id', 'email', and the nested 'profile'
        fields = ('id', 'email', 'username', 'profile')
        read_only_fields = ('id', 'email')