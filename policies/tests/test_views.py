import pytest
from django.urls import reverse
from rest_framework import status
from datetime import date, timedelta

from policies.models import Policy, PolicyType
from policies.tests.factories import PolicyFactory


@pytest.mark.django_db
class TestPolicyViewSet:
    def test_get_policies_list(self, client):
        url = reverse("policies:policy-list")
        response = client.get(url)

        # 3 policies from initial migration
        assert len(response.data) == 3
        assert response.status_code == status.HTTP_200_OK

    def test_get_policy_detail(self, client):
        p = PolicyFactory()
        url = reverse("policies:policy-detail", args=[p.policy_id])
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.data, dict)
        assert response.data["customer_name"] == p.customer_name
        assert response.data["policy_type"] == p.policy_type
        assert response.data["expiry_date"] == str(p.expiry_date)

    def test_create_policy(self, client):
        url = reverse("policies:policy-list")
        data = {
            "customer_name": "Eric",
            "policy_type": PolicyType.LIFE,
            "expiry_date": (date.today() + timedelta(days=365)).isoformat(),
        }
        response = client.post(url, data, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["customer_name"] == data["customer_name"]
        assert response.data["policy_type"] == data["policy_type"]
        assert response.data["expiry_date"] == data["expiry_date"]

    def test_put_policy(self, client):
        p = PolicyFactory()
        url = reverse("policies:policy-detail", args=[p.policy_id])
        data = {
            "customer_name": "Updated Eric",
            "policy_type": p.policy_type,
            "expiry_date": str(p.expiry_date),
        }

        response = client.put(url, data, content_type="application/json")

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["customer_name"] == "Updated Eric"

    def test_patch_policy(self, client):
        p = PolicyFactory()
        url = reverse("policies:policy-detail", args=[p.policy_id])
        data = {
            "customer_name": "Partially Updated Eric",
        }

        response = client.patch(url, data, content_type="application/json")

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["customer_name"] == "Partially Updated Eric"

    def test_delete_policy(self, client):
        p = PolicyFactory()
        url = reverse("policies:policy-detail", args=[p.policy_id])

        response = client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Policy.objects.filter(policy_id=p.policy_id).exists()

    def test_throw_error_invalid_expiry_date(self, client):
        url = reverse("policies:policy-list")
        data = {
            "customer_name": "Eric",
            "policy_type": PolicyType.AUTO,
            "expiry_date": (date.today() - timedelta(days=365)).isoformat(),
        }
        response = client.post(url, data, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["expiry_date"] == ["Expiry date has to be in the future."]
