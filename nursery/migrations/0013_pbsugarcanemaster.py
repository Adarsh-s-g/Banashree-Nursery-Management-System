# Generated by Django 5.0.3 on 2024-03-22 06:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nursery", "0012_pbledgermaster"),
    ]

    operations = [
        migrations.CreateModel(
            name="PbsugarcaneMaster",
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
                ("farmer_name", models.CharField(max_length=200, null=True)),
                ("nurser_date", models.CharField(max_length=200, null=True)),
                ("address", models.CharField(max_length=200, null=True)),
                ("mobile_num", models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
