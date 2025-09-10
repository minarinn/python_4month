from django.shortcuts import render
from django.http import HttpResponse

def book_ru(request):
    if request.method == "GET":
        return HttpResponse("Добро пожаловать в библиотеку!")

def book_en(request):
    if request.method == "GET":
        return HttpResponse("Welcome to the library!")

def book_usa(request):
    if request.method == "GET":
        return HttpResponse("There are the USA books")

