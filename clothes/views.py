from django.views.generic import ListView
from .models import Clothes

# все вещи
class AllClothesListView(ListView):
    model = Clothes
    template_name = 'clothes/all_clothes.html'
    context_object_name = 'clothes'
    ordering = ['-id']

# для детей
class KidsClothesListView(ListView):
    model = Clothes
    template_name = 'clothes/kids_clothes.html'
    context_object_name = 'clothes'

    def get_queryset(self):
        return Clothes.objects.filter(tags__name='#для детей').order_by('-id')

# для подростков
class TeensClothesListView(ListView):
    model = Clothes
    template_name = 'clothes/teens_clothes.html'
    context_object_name = 'clothes'

    def get_queryset(self):
        return Clothes.objects.filter(tags__name='#для подростков').order_by('-id')

# для взрослых
class AdultsClothesListView(ListView):
    model = Clothes
    template_name = 'clothes/adults_clothes.html'
    context_object_name = 'clothes'

    def get_queryset(self):
        return Clothes.objects.filter(tags__name='#для взрослых').order_by('-id')