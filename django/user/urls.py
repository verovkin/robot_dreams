from django.urls import path
from user.views import UserListView, UserDetailView, UserCreateView


urlpatterns = [
    path('', UserListView.as_view(), name='users-list'),
    path('<int:pk>', UserDetailView.as_view(), name='users-detail'),
    path('create', UserCreateView.as_view(), name='users-create'),
]
