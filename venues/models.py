from django.db import models
from django.contrib.localflavor.us.models import USStateField, PhoneNumberField

class Location(models.Model):
    """
    A geographic location.
    """
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = USStateField(blank=True)
    zip_code = models.CharField(max_length=5, blank=True)
   
    def __unicode__(self):
        return u'%s %s, %s %s at %s, %s' % (self.address, self.city, self.state,
                                                self.zip_code, self.latitude, self.longitude)                                        
    @property
    def full_address(self):
        return '%s %s, %s %s' % (self.address, self.city, self.state, self.zip_code)
    
class Venue(models.Model):
    """
    A place where something occurs.
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    phone = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    location = models.ForeignKey(Location)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("venues_venue_detail", 
                kwargs={"id": self.id}
        )
