from django.views.generic import ListView, DetailView, CreateView
from purchase.models import Purchase


class PurchaseListView(ListView):
    model = Purchase
#

class PurchaseDetailView(DetailView):
    queryset = Purchase.objects.all()


class PurchaseCreateView(CreateView):
    model = Purchase
    fields = ('book_id', 'user_id',)
