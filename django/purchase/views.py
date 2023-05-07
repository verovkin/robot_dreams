import django_filters
from rest_framework import filters
from django.views.generic import ListView, CreateView, DetailView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from purchase.models import Purchase
from purchase.serializers import PurchaseSerializer


class PurchaseListView(ListView):
    model = Purchase


class PurchaseDetailView(DetailView):
    queryset = Purchase.objects.all()


class PurchaseCreateView(CreateView):
    model = Purchase
    fields = ('book_id', 'user_id',)


# Filter
class PurchaseFilter(django_filters.FilterSet):
    class Meta:
        model = Purchase
        fields = {
            'book_id': ['exact'],
            'user_id': ['exact'],
            'purchase_date': ['gte', 'lte', 'gt', 'lt', 'exact']
        }


class CustomPaginator(PageNumberPagination):
    page_size_query_param = 'page_size'


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    filterset_class = PurchaseFilter
    search_fields = ['book_id', 'user_id']
    ordering_fields = ['purchase_date',]
    pagination_class = CustomPaginator

    max_page_size = 10
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
    ]

