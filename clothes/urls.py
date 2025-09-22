from django.urls import path
from . import views

urlpatterns = [
    path('all_clothes/', views.all_clothes, name='all_clothes'),
    path('kids_clothes/', views.kids_clothes, name='kids_clothes'),
    path('teens_clothes/', views.teens_clothes, name='teens_clothes'),
    path('adults_clothes/', views.adults_clothes, name='adults_clothes'),
]
