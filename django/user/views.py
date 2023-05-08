from django.views.generic import ListView, CreateView, DetailView
from user.forms import UserForm
from user.models import User

from rest_framework.viewsets import ModelViewSet
from user.serializers import UserSerializer


class UserListView(ListView):
    model = User


class UserDetailView(DetailView):
    queryset = User.objects.all()


class UserCreateView(CreateView):
    model = User
    form_class = UserForm


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
