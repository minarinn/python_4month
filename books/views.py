from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views import generic
from django.core.paginator import Paginator
from .models import Book

class BookRuView(generic.View):
    def get(self, request):
        return HttpResponse("Добро пожаловать в библиотеку!")

class BookEnView(generic.View):
    def get(self, request):
        return HttpResponse("Welcome to the library!")
    
class BookUsaView(generic.View):
    def get(self, request):
        return HttpResponse("There are the USA books")


class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
    ordering = ['-id']
    paginate_by = 2

    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(generic.DetailView):
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

    def get_object(self, *args, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(Book, id=book_id)


class SearchBooksView(generic.ListView):
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('s', '')
        if query:
            return Book.objects.filter(title__icontains=query)
        return Book.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s', '')
        return context
