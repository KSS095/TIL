from django.http import JsonResponse
from django.shortcuts import render
from hospitals import hospitals
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def hospital_list(request):
    return JsonResponse(hospitals, safe=False)

@api_view(['GET'])
def hospitals_detail(request, pk):
    for hospital in hospitals:
        if hospital['pk'] == pk:
            return JsonResponse(hospital)
        
    return JsonResponse({"error": "해당 병원을 찾을 수 없습니다."}, status=404)