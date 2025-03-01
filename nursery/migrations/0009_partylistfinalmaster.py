# Generated by Django 5.0.3 on 2024-03-20 07:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nursery", "0008_partylistmaster"),
    ]

    operations = [
        migrations.CreateModel(
            name="PartylistfinalMaster",
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
                ("bill_no", models.CharField(max_length=200, null=True)),
                ("customer_name", models.CharField(max_length=200, null=True)),
                ("date", models.CharField(max_length=200, null=True)),
                ("address", models.CharField(max_length=200, null=True)),
                ("mobile_num", models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
