from django.urls import include, path
from rest_framework import routers

from policies.views import PolicyViewSet

app_name = "policies"

router = routers.SimpleRouter()
router.register(r"policies", PolicyViewSet, basename="policy")

urlpatterns = [path("", include(router.urls))]
