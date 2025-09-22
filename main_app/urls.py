"""
URL configuration for main_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from books.views import book_ru, book_en, book_usa, book_list, book_detail, search_books
from tours.views import tour_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book_ru/', book_ru, name='book_ru'),
    path('book_en/', book_en, name='book_en'),
    path('book_usa/', book_usa, name='book_usa'),
    path('books/', book_list, name='book_list'),
    path('books/<int:id>/', book_detail, name='book_detail'),
    path('search_books/', search_books, name='search_books'),
    path('tours/', tour_list, name='tour_list'),
    path('basket/', include('basket.urls')),
    path('recruit/', include('recruit.urls', namespace='recruit')),
    path('captcha/', include('captcha.urls')),
    path('', include('clothes.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
