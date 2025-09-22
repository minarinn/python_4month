from django.shortcuts import render
from clothes.models import Clothes

# все вещи
def all_clothes(request):
    if request.method == 'GET':
        clothes = Clothes.objects.all().order_by('-id')
        context = {
            'clothes': clothes,
        }
        return render(request, 'clothes/all_clothes.html', context=context)

# для детей
def kids_clothes(request):
    if request.method == 'GET':
        clothes = Clothes.objects.filter(tags__name='#для детей').order_by('-id')
        context = {
            'clothes': clothes,
        }
        return render(request, 'clothes/kids_clothes.html', context=context)

# для подростков
def teens_clothes(request):
    if request.method == 'GET':
        clothes = Clothes.objects.filter(tags__name='#для подростков').order_by('-id')
        context = {
            'clothes': clothes,
        }
        return render(request, 'clothes/teens_clothes.html', context=context)

# для взрослых
def adults_clothes(request):
    if request.method == 'GET':
        clothes = Clothes.objects.filter(tags__name='#для взрослых').order_by('-id')
        context = {
            'clothes': clothes,
        }
        return render(request, 'clothes/adults_clothes.html', context=context)
