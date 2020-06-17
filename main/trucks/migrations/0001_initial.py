# Generated by Django 3.0.7 on 2020-06-15 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_auto_20200613_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('bed_length', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('vin', models.CharField(max_length=50)),
                ('current_mileage', models.IntegerField()),
                ('service_interval', models.DurationField()),
                ('next_service', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserAccount')),
            ],
        ),
    ]
