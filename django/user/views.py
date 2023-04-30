from django.views.generic import ListView, CreateView, DetailView
from user.models import User
from user.forms import UserForm

class UserListView(ListView):
    model = User


class UserDetailView(DetailView):
    queryset = User.objects.all()


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    # fields = ('first_name', 'last_name', 'age',)

