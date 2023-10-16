from django.urls import path

from emr.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)
from emr.users.api.views import CustomTokenObtainPairView


urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
app_name = "users"
urlpatterns+= [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
