# Generated by Django 4.2.4 on 2023-11-20 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("refxpert", "0003_blogpost"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Tenancy", "Tenancy"),
                    ("Legal", "Legal"),
                    ("Landlords", "Landlords"),
                ],
                max_length=200,
                null=True,
            ),
        ),
    ]
