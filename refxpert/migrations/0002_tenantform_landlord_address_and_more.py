# Generated by Django 4.2.7 on 2023-11-19 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("refxpert", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tenantform",
            name="landlord_address",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="tenantform",
            name="landlord_email",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="tenantform",
            name="landlord_name",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="tenantform",
            name="landlord_phone",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
