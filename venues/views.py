from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from venues.models import Venue

def venue_detail(request, slug):
    """
    The detail view of a venue.
	
    Templates(default): ``venues/venue_detail.html``
    Context:
	    venue:
		    the ``venue`` (:model:`venues.Venue`) to be detailed
    """
    venue = get_object_or_404(Venue, slug=slug)
    venue_app = venue.venue_model_type.split('.')[0]
    venue_model_label = venue.venue_model_type.split('.')[1]

    venue_of_type = get_object_or_404(ContentType.objects.get(app_label=venue_app,
                        model=venue_model_label).model_class(), slug=slug)

    template_name = "%s/%s_detail.html" % (venue_app, venue_model_label)
	
    return render_to_response(template_name, {
        "venue": venue_of_type,
    }, context_instance=RequestContext(request))
