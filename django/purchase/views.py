from django.views.generic import ListView, DetailView, CreateView
from purchase.models import Purchase
from rest_framework.viewsets import ModelViewSet
from purchase.serializers import PurchaseSerializer


class PurchaseListView(ListView):
    model = Purchase


class PurchaseDetailView(DetailView):
    queryset = Purchase.objects.all()


class PurchaseCreateView(CreateView):
    model = Purchase
    fields = ('book_id', 'user_id',)


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

