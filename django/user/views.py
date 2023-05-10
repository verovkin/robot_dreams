import django_filters
from rest_framework import filters
from django.views.generic import ListView, CreateView, DetailView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from user.forms import UserForm
from user.models import User
from user.serializers import UserSerializer
from user.tasks import my_task_list, my_task_retrieve, my_task_user_create


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

    # This one works!
    def perform_create(self, serializer):
        my_task_user_create.delay()
        serializer.save()

    # why this one does not work?
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        my_task_list.delay()  # calling a task
        print("yo")
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        my_task_retrieve.delay(instance.id)
        print("popo")
        return Response(serializer.data)
