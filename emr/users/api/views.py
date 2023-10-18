from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListAPIView
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


# views.py

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth.models import User


 

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            User = get_user_model()
            username = request.data['username']
            user = User.objects.get(username=username)
            refresh = response.data['refresh']
            access = response.data['access']
            return Response({
                'access_token': access,
                'refresh_token': refresh,
                'username': username,
            }, status=status.HTTP_200_OK)
        return response


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    paginate_by = 10  # Set the number of items per page
    paginate_by_param = 'page_size'  # Customize the query parameter for page size
    max_paginate_by = 100  # Limit the maximum page size