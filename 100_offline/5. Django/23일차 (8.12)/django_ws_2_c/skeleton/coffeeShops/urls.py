from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_create_coffee_shops),
    path('<int:pk>/', views.coffee_shops_detail),
]