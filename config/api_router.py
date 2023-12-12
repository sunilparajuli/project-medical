from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from emr.users.api.views import  UsersViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

#router.register("users", UserViewSet)
router.register("emr-users", UsersViewSet, basename="emrusers")


app_name = "api"
urlpatterns = router.urls
