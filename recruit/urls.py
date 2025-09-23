from django.urls import path
from .views import RegisterView, LoginView, UserListView, LogoutView

app_name = 'recruit'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('logout/', LogoutView.as_view(), name='logout'),
]