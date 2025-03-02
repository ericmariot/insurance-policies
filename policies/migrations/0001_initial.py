# Generated by Django 5.1.5 on 2025-02-05 21:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Policy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "policy_id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("customer_name", models.CharField(max_length=256)),
                (
                    "policy_type",
                    models.CharField(
                        choices=[
                            ("auto", "Auto"),
                            ("home", "Home"),
                            ("life", "Life"),
                            ("travel", "Travel"),
                        ],
                        max_length=64,
                    ),
                ),
                ("expiry_date", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
