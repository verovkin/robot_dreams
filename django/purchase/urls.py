from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_purchases, name='index')
]
