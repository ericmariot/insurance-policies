from django.db import models


class Policy(models.Model):
    policy_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    policy_type = models.CharField(
        max_length=50, choices=[("auto", "Auto"), ("home", "Home")]
    )
    expiry_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name}; {self.policy_type}; {self.expiry_date}"
