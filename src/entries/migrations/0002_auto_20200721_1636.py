# Generated by Django 3.0.8 on 2020-07-21 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-timestamp']},
        ),
    ]
