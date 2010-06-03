from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from venues.models import Venue

def venue_detail(request, slug, **kwargs):
	"""
	The detail view of a venue.
	
	Templates(default): ``venues/venue_detail.html``
	Context:
		venue:
			the ``venue`` (:model:`venues.Venue`) to be detailed
	"""
	template_name = kwargs.get("template_name", "venues/venue_detail.html")
	
	venue = get_object_or_404(Venue, slug=slug)
	
	return render_to_response(template_name, {
		"venue": venue,
	}, context_instance=RequestContext(request))
