from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def menu_list(request):
    list = [
        {"name": "Espresso", "price": 3000},
        {"name": "Americano", "price": 3500},
        {"name": "Latte", "price": 4000},
    ]

    return JsonResponse(list, safe=False)