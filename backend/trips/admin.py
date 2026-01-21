from django.contrib import admin

from trips.models import Trip


# Register your models here.
@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    pass