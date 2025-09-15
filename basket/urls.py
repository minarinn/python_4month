from django.urls import path
from . import views

urlpatterns = [
    path('', views.read_order_view, name='order_list'),  # теперь /basket/ покажет список заказов
    path('orders/create/', views.create_order_view, name='create_order'),
    path('orders/update/<int:id>/', views.update_order_view, name='update_order'),
    path('orders/delete/<int:id>/', views.delete_order_view, name='delete_order'),
]