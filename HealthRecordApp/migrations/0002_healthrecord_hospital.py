# Generated by Django 4.2.5 on 2024-03-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthRecordApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthrecord',
            name='Hospital',
            field=models.CharField(default='hospital A', max_length=20),
        ),
    ]