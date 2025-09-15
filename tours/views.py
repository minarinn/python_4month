from django.shortcuts import render
from tours.models import Person, Tour

def tour_list(request):
    tours = Tour.objects.all()
    context = {
        'tours': tours
    }
    return render(request, 'tour_list.html', context=context)
