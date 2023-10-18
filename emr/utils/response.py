from rest_framework.response import Response
from rest_framework import status

def success_response(data=None, message=None):
    response_data = {
        'status': status.HTTP_200_OK,
        'message': message or 'Success',
        'data': data,
    }
    return Response(response_data, status=status.HTTP_200_OK)

def created_response(data=None, message=None):
    response_data = {
        'status': status.HTTP_201_CREATED,
        'message': message or 'Created',
        'data': data,
    }
    return Response(response_data, status=status.HTTP_201_CREATED)

def error_response(data=None, message=None, status_code=status.HTTP_400_BAD_REQUEST):
    response_data = {
        'status': status_code,
        'message': message or 'Bad Request',
        'data': data,
    }
    return Response(response_data, status=status_code)
