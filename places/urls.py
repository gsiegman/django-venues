from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^(?P<slug>[-\w]+)/$',
			'places.views.place_detail',
			name='places_place_detail'
	),
)