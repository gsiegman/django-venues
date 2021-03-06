from django.contrib import admin
from venues.models import Location, Venue, VenueImage

class VenueAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Venue, VenueAdmin)
admin.site.register(Location)
admin.site.register(VenueImage)
