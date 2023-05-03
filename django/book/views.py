from django.views.generic import ListView, DetailView, CreateView
from .models import Book
from rest_framework.viewsets import ModelViewSet
from book.serializers import BookSerializer


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    queryset = Book.objects.all()


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'year', 'price']


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
