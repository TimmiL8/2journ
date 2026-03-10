from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomUser, UserProfile

admin.site.register(CustomUser)
admin.site.register(UserProfile)
