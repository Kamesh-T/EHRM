# Generated by Django 4.2.5 on 2024-05-10 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthRecordApp', '0002_healthrecord_hospital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthrecord',
            name='Hospital',
            field=models.CharField(max_length=20),
        ),
    ]