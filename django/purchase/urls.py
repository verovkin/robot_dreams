from django.urls import path
from rest_framework.routers import SimpleRouter
from purchase.views import PurchaseListView, PurchaseDetailView, PurchaseCreateView, PurchaseViewSet


urlpatterns = [
    path('list', PurchaseListView.as_view(), name='purchases-list'),
    path('<int:pk>', PurchaseDetailView.as_view(), name='purchases-detail'),
    path('create', PurchaseCreateView.as_view(), name='purchases-create'),
]

router = SimpleRouter()
router.register('', PurchaseViewSet)

urlpatterns += router.urls
