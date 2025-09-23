from django.views import generic
from tours.models import Tour

class TourListView(generic.ListView):
    model = Tour
    template_name = 'tour_list.html'
    context_object_name = 'tours'
    ordering = ['-id']