from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^(?P<slug>[-\w]+)/$',
			'venues.views.venue_detail',
			name='venues_venue_detail'
	),
)
