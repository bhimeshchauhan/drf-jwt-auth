# Generated by Django 3.0.7 on 2020-06-15 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20200614_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='is_deleted',
        ),
    ]
