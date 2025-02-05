import uuid
from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError


class PolicyType(models.TextChoices):
    AUTO = ("auto", "Auto")
    HOME = ("home", "Home")
    LIFE = ("life", "Life")
    TRAVEL = ("travel", "Travel")


class Policy(models.Model):
    policy_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_name = models.CharField(max_length=256)
    policy_type = models.CharField(max_length=64, choices=PolicyType)
    expiry_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.expiry_date < now().date():
            raise ValidationError({"expiry_date": "Expiry date cannot be in the past."})
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer_name}; {self.policy_type}; {self.expiry_date}"
