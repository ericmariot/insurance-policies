from rest_framework import viewsets

from policies.models import Policy
from policies.serializers import PolicySerializer


class PolicyViewSet(viewsets.ModelViewSet):
    queryset = Policy.objects.all().order_by("expiry_date")
    serializer_class = PolicySerializer
    lookup_field = "policy_id"
