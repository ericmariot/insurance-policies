from django.db import models


class POLICIES_TYPES(models.TextChoices):
    AUTO = (
        "auto",
        "Auto",
    )
    HOME = (
        "home",
        "Home",
    )
    LIFE = (
        "life",
        "Life",
    )
    TRAVEL = (
        "travel",
        "Travel",
    )


class Policy(models.Model):
    policy_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=256)
    policy_type = models.CharField(max_length=64, choices=POLICIES_TYPES)
    expiry_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name}; {self.policy_type}; {self.expiry_date}"
