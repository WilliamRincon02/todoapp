# Generated by Django 5.0.4 on 2024-06-06 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="jwt_token",
            field=models.TextField(blank=True, null=True),
        ),
    ]
