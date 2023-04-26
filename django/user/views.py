from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import User
import json


def show_users(request):
    users = User.objects.all()
    users_json = serializers.serialize('json', users)
    return HttpResponse(users_json, content_type='application/json')
