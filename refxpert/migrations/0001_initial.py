# Generated by Django 4.2.7 on 2023-11-19 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("phone", models.CharField(blank=True, max_length=200, null=True)),
                ("email", models.CharField(blank=True, max_length=200, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="TenantForm",
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
                ("first_name", models.CharField(max_length=200, null=True)),
                ("last_name", models.CharField(max_length=200, null=True)),
                ("property_name", models.CharField(max_length=200, null=True)),
                (
                    "country",
                    django_countries.fields.CountryField(max_length=2, null=True),
                ),
                ("phone", models.CharField(max_length=200, null=True)),
                ("email", models.CharField(max_length=200, null=True)),
                ("confirm_email", models.CharField(max_length=200, null=True)),
                ("email_tenant", models.BooleanField(default=False)),
                ("guarantor_details", models.BooleanField(default=False)),
                ("address", models.CharField(max_length=200, null=True)),
                (
                    "employment",
                    models.CharField(
                        choices=[
                            ("employed", "Employed"),
                            ("self_employed", "Self Employed"),
                            ("unemployed", "Unemployed"),
                            ("retired", "Retired"),
                            ("student", "Student"),
                            ("other", "Other"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
                ("annual_income", models.CharField(max_length=200, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")],
                        max_length=200,
                        null=True,
                    ),
                ),
                ("date_of_birth", models.DateField(null=True)),
                ("smoking", models.BooleanField(default=False)),
                ("pets", models.BooleanField(default=False)),
                ("children", models.BooleanField(default=False)),
                ("next_of_kin", models.CharField(max_length=200, null=True)),
                ("next_of_kin_phone", models.CharField(max_length=200, null=True)),
                ("next_of_kin_address", models.CharField(max_length=200, null=True)),
                (
                    "next_of_kin_relationship",
                    models.CharField(max_length=200, null=True),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                ("permission", models.BooleanField(default=False)),
                ("marketing", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PropertyManagement",
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
                ("Property", models.CharField(max_length=200, null=True)),
                ("PropertyType", models.CharField(max_length=200, null=True)),
                ("PropertyAddress", models.CharField(max_length=200, null=True)),
                ("PropertyCity", models.CharField(max_length=200, null=True)),
                ("NumberOfUnits", models.CharField(max_length=200, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "Rent",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Rent Collected", "Rent Collected"),
                            ("Rent Due", "Rent Due"),
                            ("Rent Overdue", "Rent Overdue"),
                            ("Total Rent", "Total Rent"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
                ("RentCollectedDate", models.CharField(max_length=200, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LegalService",
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
                    "service_type",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("property", models.CharField(blank=True, max_length=200, null=True)),
                ("location", models.CharField(blank=True, max_length=200, null=True)),
                ("price", models.FloatField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("In Progress", "In Progress"),
                            ("Completed", "Completed"),
                            ("Review", "Review"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "customer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="refxpert.customer",
                    ),
                ),
                ("tag", models.ManyToManyField(to="refxpert.tag")),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HouseApplication",
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
                ("house_type", models.CharField(blank=True, max_length=200, null=True)),
                ("location", models.CharField(blank=True, max_length=200, null=True)),
                ("price", models.FloatField(null=True)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Pending", "Pending"),
                            ("Approved", "Approved"),
                            ("Rejected", "Rejected"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "customer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="refxpert.customer",
                    ),
                ),
                ("tag", models.ManyToManyField(to="refxpert.tag")),
            ],
        ),
    ]
