from django.urls import path
from rest_framework.routers import SimpleRouter
from book.views import BookListView, BookDetailView, BookCreateView, BookViewSet

urlpatterns = [
    path('list', BookListView.as_view(), name='books-list'),
    path('<int:pk>', BookDetailView.as_view(), name='books-detail'),
    path('create', BookCreateView.as_view(), name='books-create')
]

router = SimpleRouter()
router.register('', BookViewSet)

urlpatterns += router.urls

