from django.db import models
from django.contrib.localflavor.us.models import USStateField, PhoneNumberField

class Location(models.Model):
    """
    A geographic location.
    """
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = USStateField(blank=True)
    zip_code = models.CharField(max_length=5, blank=True)
   
    def __unicode__(self):
        return u'%s %s, %s %s at %s, %s' % (self.address, self.city, self.state,
                                                self.zip_code, self.latitude, self.longitude)                                        
    @property
    def full_address(self):
        return '%s %s, %s %s' % (self.address, self.city, self.state, self.zip_code)
    
class Place(models.Model):
    """
    A place (with a name).
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    phone = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    location = models.ForeignKey(Location)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("places_place_detail", 
                kwargs={"id": self.id}
        )
