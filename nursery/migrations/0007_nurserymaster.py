# Generated by Django 5.0.3 on 2024-03-18 06:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nursery", "0006_customer_alter_purchagemaster_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Nurserymaster",
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
                ("farmer_name", models.CharField(max_length=200, null=True)),
                ("description", models.CharField(max_length=200, null=True)),
                ("advance", models.CharField(max_length=200, null=True)),
                ("total_price", models.IntegerField(blank=True, null=True)),
                ("price", models.IntegerField(blank=True, null=True)),
                ("address", models.CharField(max_length=200, null=True)),
                ("tray_no", models.IntegerField(blank=True, null=True)),
                ("nursery_date", models.CharField(max_length=200, null=True)),
                ("swoing_date", models.CharField(max_length=200, null=True)),
                ("lot_no", models.IntegerField(blank=True, null=True)),
                ("mobile_num", models.IntegerField(blank=True, null=True)),
                ("packet_no", models.IntegerField(blank=True, null=True)),
                ("packet_name", models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
