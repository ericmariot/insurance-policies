import factory
import factory.fuzzy

from policies.models import Policy, POLICIES_TYPES


class PolicyFactory(factory.django.DjangoModelFactory):
    customer_name = factory.fuzzy.FuzzyChoice(
        ["Eric", "Rafa", "Renato", "Luiz Mauricio"]
    )
    policy_type = factory.fuzzy.FuzzyChoice(POLICIES_TYPES)
    expiry_date = factory.Faker("date_between", start_date="+30d", end_date="+365d")

    class Meta:
        model = Policy
