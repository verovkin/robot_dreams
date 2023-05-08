import django_filters
from rest_framework import filters
from django.views.generic import ListView, CreateView, DetailView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from user.forms import UserForm
from user.models import User
from user.serializers import UserSerializer


class UserListView(ListView):
    model = User


class UserDetailView(DetailView):
    queryset = User.objects.all()


class UserCreateView(CreateView):
    model = User
    form_class = UserForm

# Filter
class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'first_name': ['contains'],
            'last_name': ['contains'],
            'age': ['gte', 'lte', 'gt', 'lt', 'exact']
        }


class CustomPaginator(PageNumberPagination):
    page_size_query_param = 'page_size'


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filterset_class = UserFilter
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['last_name', 'age']
    pagination_class = CustomPaginator

    max_page_size = 10
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
    ]
