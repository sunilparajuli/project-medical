from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from emr.patients.models import Patient
from emr.patients.api.serializers import PatientSerializer
from emr.utils.response import success_response, created_response, error_response,success_response_pagination
import datetime
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import RetrieveAPIView


class PatientView(APIView, PageNumberPagination):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
    def post(self, request):
        print(request.data)
        req_data = request.data.copy()
        now = datetime.datetime.now()
        formatted_datetime = now.strftime('%Y%m%d%H%M') + str(now.second * 1000)
        keys_to_map = {
            'identifier' : formatted_datetime,
            'first_name': 'firstName',
            'middle_name': 'middleName',
            'last_name': 'lastName',
            'birthdate': 'dateOfBirth',
            'gender': 'gender',
            'email': 'email',
            'phone': 'contactNumber',
            'country': 'country',
            'province': 'province',
            'district': 'district',  # Assuming this should be mapped to the same key
            'municipality': 'city'    # Assuming this should be mapped to the 'city' key
        }
        dict_to_map = {key: req_data.get(value) for key, value in keys_to_map.items()}
        serializer = PatientSerializer(data=dict_to_map)

        if serializer.is_valid():
            serializer.save()  # Create a new patient
            return created_response(data=serializer.data, message='Patient created successfully')
        else:
            return error_response(data=serializer.errors)
    
    def get(self, request):
        # Create an instance of PageNumberPagination
        paginator = PageNumberPagination()
        paginator.page_size = int(request.query_params.get('page_size', 10))  # Set the page size

        patients = Patient.objects.all()
        
        # Paginate the queryset
        patients_page = paginator.paginate_queryset(patients, request, view=self)

        # Serialize the paginated data
        serializer = PatientSerializer(patients_page, many=True)

        # Call the success_response function with the paginated data and pagination metadata
        return success_response_pagination(
            serializer.data,
            paginator.page.paginator.count,  # Count of total items
            paginator.get_next_link(),  # Next page URL
            paginator.get_previous_link()  # Previous page URL
        )

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



class PatientDetailView(RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer