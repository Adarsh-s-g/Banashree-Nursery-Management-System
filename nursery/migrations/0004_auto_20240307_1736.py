# Generated by Django 3.1.4 on 2024-03-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nursery', '0003_auto_20240307_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchagemaster',
            name='purchage_date',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
