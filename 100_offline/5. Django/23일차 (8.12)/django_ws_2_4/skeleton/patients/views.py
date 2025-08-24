from .models import Patient
from .serializers import PatientSerializer, PatientListSerializer, PatientDetailSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(["POST"])
def patient_create(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)


@api_view(['GET'])
def patient_list(request):
    patients = Patient.objects.all()
    serializer = PatientListSerializer(patients, many=True)
    return Response(serializer.data)


@api_view(["GET", "DELETE"])
def patient_detail(request, patient_id):
    if request.method == "GET":
        patient = get_object_or_404(Patient, pk=patient_id)
        serializer = PatientDetailSerializer(patient)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        patient = Patient.objects.get(pk=patient_id)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["PATCH"])
def patient_update(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    serializer = PatientSerializer(patient, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)