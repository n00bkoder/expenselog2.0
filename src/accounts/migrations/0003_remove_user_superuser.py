# Generated by Django 3.0.8 on 2020-07-20 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_superuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='superuser',
        ),
    ]
