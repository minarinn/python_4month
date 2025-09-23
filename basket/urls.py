from django.urls import path
from .views import (
    OrderListView, OrderCreateView,
    OrderUpdateView, OrderDeleteView
)

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/create/', OrderCreateView.as_view(), name='create_order'),
    path('orders/update/<int:id>/', OrderUpdateView.as_view(), name='order_update'),
    path('orders/delete/<int:id>/', OrderDeleteView.as_view(), name='order_delete'),
]