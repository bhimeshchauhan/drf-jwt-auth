from django.db import models
from main.user.models import UserAccount


class Car(models.Model):
	id = models.IntegerField(primary_key=True)
	make = models.CharField(max_length=50)
	model = models.CharField(max_length=50)
	year = models.IntegerField()
	seats = models.IntegerField()
	color = models.CharField(max_length=50)
	vin = models.CharField(max_length=50)
	current_mileage = models.IntegerField()
	service_interval = models.DurationField()
	next_service = models.DateTimeField()
	user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.model