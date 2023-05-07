import django_filters
from rest_framework import filters
from django.views.generic import ListView, CreateView, DetailView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from book.models import Book
from book.serializers import BookSerializer


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    queryset = Book.objects.all()


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'year', 'price']


# Filter
class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['contains'],
            'author': ['contains'],
            'price': ['gte', 'lte', 'gt', 'lt', 'exact']
        }


class CustomPaginator(PageNumberPagination):
    page_size_query_param = 'page_size'


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['price', 'title']
    pagination_class = CustomPaginator

    max_page_size = 10
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
    ]
