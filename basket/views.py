from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from .forms import OrderForm

def create_order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'order_form.html', context={'form': form, 'order': None})

def read_order_view(request):
    orders = Order.objects.all().order_by('-id')
    return render(request, 'order_list.html', context={'orders': orders})

def update_order_view(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'order_form.html', context={'form': form, 'order': order})

def delete_order_view(request, id):
    order = get_object_or_404(Order, id=id)
    order.delete()
    return redirect('order_list')
