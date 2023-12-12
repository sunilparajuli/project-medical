from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListAPIView
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.pagination import PageNumberPagination
from .filters import UserFilter
from django_filters.rest_framework import DjangoFilterBackend

User = get_user_model()


# class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     lookup_field = "username"

#     def get_queryset(self, *args, **kwargs):
#         assert isinstance(self.request.user.id, int)
#         return self.queryset.filter(id=self.request.user.id)

#     @action(detail=False)
#     def me(self, request):
#         serializer = UserSerializer(request.user, context={"request": request})
#         return Response(status=status.HTTP_200_OK, data=serializer.data)


# views.py


# from django.contrib.auth.models import User


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            User = get_user_model()
            username = request.data["username"]
            user = User.objects.get(username=username)
            refresh = response.data["refresh"]
            access = response.data["access"]
            return Response(
                {
                    "access_token": access,
                    "refresh_token": refresh,
                    "username": username,
                },
                status=status.HTTP_200_OK,
            )
        return response


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    paginate_by = 10  # Set the number of items per page
    paginate_by_param = "page_size"  # Customize the query parameter for page size
    max_paginate_by = 100  # Limit the maximum page size


from rest_framework import views


class LogoutView(views.APIView):
    def post(self, request):
        try:
            token = RefreshToken(request.data.get("refresh_token"))
            token.blacklist()
            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10  # Number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 100
class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        # queryset = self.get_queryset()
        paginator = CustomPageNumberPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = UserSerializer(result_page, many=True, context= {"request": request})        
        # serializer = UserSerializer(result_page, many=True)
        response_data = {
            'page_size' : 10,
            'count': paginator.page.paginator.count,
            'count_per_page': paginator.page_size,
            'results': serializer.data,
            'max_page_size' : 30,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link()
        }

        return Response(response_data)
    
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
