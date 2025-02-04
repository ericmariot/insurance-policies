from policies.models import Policy
from django.utils.timezone import now
from rest_framework import serializers


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = ["policy_id", "customer_name", "policy_type", "expiry_date"]

    def validate_expiry_date(self, value):
        if value <= now().date():
            raise serializers.ValidationError("Expiry date has to be in the future.")
        return value
