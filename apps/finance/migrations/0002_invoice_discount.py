# Generated by Django 4.1.7 on 2023-03-15 17:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finance", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="discount",
            field=models.IntegerField(default=0),
        ),
    ]
