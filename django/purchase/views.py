from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Purchase


# Create your views here.
def show_purchases(request):
    purchases = Purchase.objects.all()
    purchases_json = serializers.serialize('json', purchases)
    return HttpResponse(purchases_json, content_type='application/json')
