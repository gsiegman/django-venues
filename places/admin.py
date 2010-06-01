from django.contrib import admin
from places.models import Location, Place

class PlaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Place, PlaceAdmin)
admin.site.register(Location)