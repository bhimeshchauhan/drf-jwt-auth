# Generated by Django 3.0.7 on 2020-06-15 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200613_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
