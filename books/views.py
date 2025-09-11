from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
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
        context = {
            'books': books
        }
        return render(request, 'book_list.html', context=context)

def book_detail(request, id):
    if request.method == 'GET':
        book = get_object_or_404(Book, id=id)
        context = {
            'book': book
        }
        return render(request, 'book_detail.html', context=context)
