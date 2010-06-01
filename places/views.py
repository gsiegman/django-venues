from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from places.models import Place

def place_detail(request, slug, **kwargs):
	"""
	The detail view of a place.
	
	Templates(default): ``places/place_detail.html``
	Context:
		place:
			the ``place`` (:model:`places.Place`) to be detailed
	"""
	template_name = kwargs.get("template_name", "places/place_detail.html")
	
	place = get_object_or_404(Place, slug=slug)
	
	return render_to_response(template_name, {
		"place": place,
	}, context_instance=RequestContext(request))
