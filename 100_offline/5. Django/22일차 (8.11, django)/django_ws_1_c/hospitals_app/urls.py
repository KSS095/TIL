from django.urls import path
from . import views

urlpatterns = [
    path('', views.hospital_list),
    path('<int:pk>', views.hospitals_detail),
]
