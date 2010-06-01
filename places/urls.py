from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^(?P<place_id>[\d]+)/$',
			'places.views.place_detail',
			name='places_place_detail'
	),
)