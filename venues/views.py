from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from venues.models import Venue

def venue_detail(request, slug, venue_type=None, 
        venue_model="venues.venue", extra_context=None, **kwargs):
    """
    The detail view of a venue.
	
    Templates(default): ``venues/venue_detail.html``
    Context:
	    venue:
		    the ``venue`` (:model:`venues.Venue`) to be detailed
	    venue_type:
		    a venue type typically provided by models that inherit
		    from ``venue`` (:model:`venues.Venue`)
    """
    template_name = kwargs.get("template_name", "venues/venue_detail.html")

    c = RequestContext(request, {'venue_type': venue_type})

    if extra_context is None:
        extra_context = {}
    else:
        for k, v in extra_context.items():
            c[k] = v

    venue_model_type = ContentType.objects.get(app_label=venue_model.split()[0],
                                    model=venue_model.split()[1])
    venue = get_object_or_404(venue_model_type.model_class(), slug=slug)
	
    return render_to_response(template_name, {
        "venue": venue,
    }, context_instance=c)
