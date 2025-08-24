from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from books import books
import random

# Create your views here.
@api_view(['GET'])
def recommend(request):
    filtered_books = [book for book in books if book['rating'] >= 6.0]
    recommend_book = random.choice(filtered_books)
    return JsonResponse(recommend_book)