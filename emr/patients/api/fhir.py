import requests
import datetime
from drf_spectacular.utils import extend_schema
from emr.utils.credentials import get_config
from rest_framework.views import APIView
from rest_framework.response import Response


class FhirPatientDetailApiView(APIView):
    @extend_schema(request=None, responses={})
    def get(self, request, **kwargs):
        set_config = get_config('demo')
        endpoint_url = f"{set_config['base_uri']}/api_fhir_r4/Patient/?identifier={kwargs.get('insuranceid')}"
        headers = {
            'remote-user': set_config['remote-user'],
            'Authorization': set_config['auth']
        }

        response = requests.get(endpoint_url, headers=headers)

        if response.status_code != 200:
            return f'Error making API request: {response.status_code}'

        data = response.json()
        return Response(data, 200)



class FhirCoverageApiView(APIView):
    @extend_schema(request=None, responses={})
    def get(self, request, **kwargs):
       
        today = datetime.date.today().isoformat()
        payload = {
            "resourceType": "CoverageEligibilityRequest",
            "patient": {
                "reference": f"Patient/{kwargs.get('insuranceid')}"
            },
            "extension": [
                {
                    "url": "visitDate",
                    "valueString": kwargs.get('visit_date')
                }
            ]
        }

        set_config = get_config('demo')
        headers = {
            'remote-user': set_config['remote-user'],
            'Content-Type': 'application/json',
            'Authorization': set_config['auth']
        }

        endpoint_url = f"{set_config['base_uri']}/api_fhir_r4/CoverageEligibilityRequest/"
        try:
            response = requests.post(endpoint_url, json=payload, headers=headers)
            response_data = response.json()
            return Response(response_data, 200)
        except requests.exceptions.RequestException as e:
            return f'Error: {e}'


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AttachmentUpload(APIView):
    def post(self, request):
        import requests
        import json

        # Ensure that set_config is defined before using it
        set_config = get_config('demo')

        url = f"{set_config['base_uri']}/api_fhir_r4/attachments"
        claim = request.data.get('claim')
        documents = request.data.get("documents")
        payload = json.dumps({
            "claim": claim,
            "documents": documents
        })

        headers = {
            'remote-user': set_config['remote-user'],
            'Content-Type': 'application/json',
            'Authorization': set_config['auth']
        }
        try:
            response = requests.post(url, headers=headers, data=payload)
            response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)

            # Request was successful
            return Response({'message': 'Upload successful'}, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            # Request encountered an error
            try:
                error_details = response.json().get('issue')[0].get('details', {}).get('text', str(e))
            except json.JSONDecodeError:
                error_details = str(e)

            return Response({'error': error_details}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



