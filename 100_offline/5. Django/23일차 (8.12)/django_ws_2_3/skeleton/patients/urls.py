from django.urls import path
from . import views
urlpatterns = [
    path("new/", views.patient_create),
    path("", views.patient_list),
    path("<int:pk>/", views.patient_info),
]