from django.urls import path
from . import views

urlpatterns = [
    path('recommend/', views.recommend_books),
    path('', views.show_pages, {'page': 1}),
    path('<int:page>/', views.show_pages),
]