from django.urls import path
from book.views import BookListView, BookDetailView, BookCreateView

urlpatterns = [
    path('', BookListView.as_view(), name='books-list'),
    path('<int:pk>', BookDetailView.as_view(), name='books-detail'),
    path('create', BookCreateView.as_view(), name='books-create')
]
