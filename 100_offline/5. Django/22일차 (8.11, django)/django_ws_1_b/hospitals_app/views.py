from django.http import JsonResponse
from django.shortcuts import render
from hospitals import hospitals
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def hospital_list(request):
    return JsonResponse(hospitals, safe=False)