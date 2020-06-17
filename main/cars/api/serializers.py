from rest_framework import serializers
from main.cars.models import Car


class CarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Car
		fields = [
			'make',
			'model',
			'year',
			'seats',
			'color',
			'vin',
			'current_mileage',
			'service_interval',
			'next_service',
		]