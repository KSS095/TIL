from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_get_or_create),
    path('<int:posts_pk>/', views.posts_update_or_delete),
]