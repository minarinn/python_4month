from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from books.models import Book

def book_ru(request):
    if request.method == "GET":
        return HttpResponse("Добро пожаловать в библиотеку!")

def book_en(request):
    if request.method == "GET":
        return HttpResponse("Welcome to the library!")

def book_usa(request):
    if request.method == "GET":
        return HttpResponse("There are the USA books")

def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all().order_by('-id')
        paginator = Paginator(books, 2)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        context = {
            'books': page_obj
        }
        return render(request, 'book_list.html', context=context)

def book_detail(request, id):
    if request.method == 'GET':
        book = get_object_or_404(Book, id=id)
        context = {
            'book': book
        }
        return render(request, 'book_detail.html', context=context)

def search_books(request):
    query = request.GET.get('s', '')
    books = Book.objects.filter(title__icontains=query) if query else Book.objects.none()
    context = {
        'books': books,
        's': query,
    }
    return render(request, 'book_list.html', context=context)
