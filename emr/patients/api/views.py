from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from emr.patients.models import Patient
from emr.patients.api.serializers import PatientSerializer
from emr.utils.response import success_response, created_response, error_response

class PatientView(APIView):
    def post(self, request):
        serializer = PatientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()  # Create a new patient
            return created_response(data=serializer.data, message='Patient created successfully')
        else:
            return error_response(data=serializer.errors)

    def put(self, request, pk):
        try:
            patient = Patient.objects.get(pk=pk)
            serializer = PatientSerializer(patient, data=request.data)

            if serializer.is_valid():
                serializer.save()  # Update the existing patient
                return success_response(data=serializer.data, message='Patient updated successfully')

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Patient.DoesNotExist:
            return error_response(message='Patient not found', status_code=status.HTTP_404_NOT_FOUND)
