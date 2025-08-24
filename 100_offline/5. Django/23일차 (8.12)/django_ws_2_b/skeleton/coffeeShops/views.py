from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import CoffeeShop
from .serializers import CoffeeShopSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def create_and_list(request):
    if request.method == 'GET':
        # coffeeshop = get_object_or_404(CoffeeShop)
        coffeeshop = CoffeeShop.objects.all()

        if not coffeeshop: return JsonResponse({'detail': 'No Coffee Shops found.'}, status=404)

        serializer = CoffeeShopSerializer(coffeeshop, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CoffeeShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)