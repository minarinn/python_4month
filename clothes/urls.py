from django.urls import path
from .views import (
    AllClothesListView, KidsClothesListView,
    TeensClothesListView, AdultsClothesListView
)

urlpatterns = [
    path('all_clothes/', AllClothesListView.as_view(), name='all_clothes'),
    path('kids_clothes/', KidsClothesListView.as_view(), name='kids_clothes'),
    path('teens_clothes/', TeensClothesListView.as_view(), name='teens_clothes'),
    path('adults_clothes/', AdultsClothesListView.as_view(), name='adults_clothes'),
]