from django.contrib import admin

from places.models import Place, Trip

# Register your models here.
@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass
