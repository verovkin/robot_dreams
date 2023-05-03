from django.urls import path
from rest_framework.routers import SimpleRouter
from user.views import UserListView, UserDetailView, UserCreateView, UserViewSet


urlpatterns = [
    path('list', UserListView.as_view(), name='users-list'),
    path('<int:pk>', UserDetailView.as_view(), name='users-detail'),
    path('create', UserCreateView.as_view(), name='users-create'),
]

router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns += router.urls
