# Generated by Django 5.0.6 on 2024-06-11 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dproject1', '0010_remove_doctor_mozakkir_slot_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doctor_pwd',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
