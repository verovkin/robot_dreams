from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Book



def show_books(request):
    books = Book.objects.all()
    books_json = serializers.serialize('json', books)
    return HttpResponse(books_json, content_type='application/json')
