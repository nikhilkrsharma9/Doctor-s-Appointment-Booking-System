# Generated by Django 5.0.6 on 2024-06-12 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dproject1', '0012_alter_appointment_doctor_pwd'),
    ]

    operations = [
        migrations.CreateModel(
            name='doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('pwd', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'doc',
            },
        ),
    ]
