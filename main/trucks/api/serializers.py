from rest_framework import serializers
from main.trucks.models import Truck


class TruckSerializer(serializers.ModelSerializer):
	class Meta:
		model = Truck
		fields = [
			'make',
			'model',
			'year',
			'seats',
			'bed_length',
			'color',
			'vin',
			'current_mileage',
			'service_interval',
			'next_service',
		]