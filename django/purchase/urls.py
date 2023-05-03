from django.urls import path
from purchase.views import PurchaseListView, PurchaseDetailView, PurchaseCreateView


urlpatterns = [
    path('', PurchaseListView.as_view(), name='purchases-list'),
    path('<int:pk>', PurchaseDetailView.as_view(), name='purchases-detail'),
    path('create', PurchaseCreateView.as_view(), name='purchases-create'),
]
