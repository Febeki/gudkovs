# Generated by Django 4.2 on 2023-04-06 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_remove_user_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
    ]