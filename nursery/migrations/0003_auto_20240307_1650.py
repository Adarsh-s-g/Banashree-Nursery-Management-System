# Generated by Django 3.1.4 on 2024-03-07 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nursery', '0002_auto_20240307_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchagemaster',
            name='purchage_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
