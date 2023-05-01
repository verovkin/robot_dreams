from django.views.generic import ListView, DetailView, CreateView
from .models import Book


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    queryset = Book.objects.all()


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'year', 'price']