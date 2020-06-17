from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from main.user.backends import JWTAuthentication

from .serializers import TruckSerializer
from main.trucks.models import Truck
from main.user.models import UserAccount


@api_view(['GET', ])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def retrieve_trucks(request):
	try:
		trucks = Truck.objects.all()
	except Truck.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	if request.method == 'GET':
		serializer = TruckSerializer(trucks, many=True)
		return Response(serializer.data)


@api_view(['DELETE', 'GET', 'PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def pk_operate_truck(request, pk):
	try:
		trucks = Truck.objects.get(id=pk)
	except Truck.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	if request.method == 'GET':
		serializer = TruckSerializer(trucks, many=False)
		return Response(serializer.data)
	elif request.method == 'DELETE':
		delete_ops = trucks.delete()
		data = {}
		if delete_ops:
			data["success"] = "delete successful"
		else:
			data["failure"] = "delete failed"
		return Response(data=data)
	elif request.method == 'PUT':
		serializer = TruckSerializer(trucks, data=request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data["success"] = "update successful"
			return Response(data=data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_truck(request):
	user = UserAccount.objects.get(pk=1)
	truck = Truck(user_id=user)
	
	if request.method == 'POST':
		serializer = TruckSerializer(truck, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
