from rest_framework import serializers
from main.cars.models import Car


class TruckSerializer(serializers.ModelSerializer):
	class Meta:
		model = Car
		fields = [
			'make',
			'model',
			'year',
			'length',
			'width',
			'hin',
			'current_hours',
			'service_interval',
			'next_service',
		]