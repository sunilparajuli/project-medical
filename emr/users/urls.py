from django.urls import path

from emr.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)
from emr.users.api.views import CustomTokenObtainPairView
from emr.users.api.views import UserListView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('list/', UserListView.as_view(), name='user-list'),
]
app_name = "users"
urlpatterns+= [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
