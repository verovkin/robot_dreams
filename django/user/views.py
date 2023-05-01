from django.views.generic import ListView, CreateView, DetailView
from user.forms import UserForm
from user.models import User


class UserListView(ListView):
    model = User


class UserDetailView(DetailView):
    queryset = User.objects.all()


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
