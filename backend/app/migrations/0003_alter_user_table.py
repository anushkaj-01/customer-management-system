# Generated by Django 5.0.6 on 2024-05-20 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='auth_user',
        ),
    ]
