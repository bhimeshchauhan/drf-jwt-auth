from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from main.user.backends import JWTAuthentication

from .serializers import CarSerializer
from main.cars.models import Car
from main.user.models import UserAccount


@api_view(['GET', ])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def retrieve_cars(request):
	try:
		cars = Car.objects.all()
	except Car.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	
	if request.method == 'GET':
		serializer = CarSerializer(cars, many=True)
		return Response(serializer.data)


@api_view(['DELETE', 'GET', 'PUT', ])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def pk_operate_car(request, pk):
	try:
		cars = Car.objects.get(id=pk)
	except Car.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = CarSerializer(cars, many=False)
		return Response(serializer.data)
	elif request.method == 'DELETE':
		delete_ops = cars.delete()
		data = {}
		if delete_ops:
			data["success"] = "delete successful"
		else:
			data["failure"] = "delete failed"
		return Response(data=data)
	elif request.method == 'PUT':
		serializer = CarSerializer(cars, data=request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data["success"] = "update successful"
			return Response(data=data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_car(request):
	user = UserAccount.objects.get(id=1)
	car = Car(user_id=user)
	
	if request.method == 'POST':
		serializer = CarSerializer(car, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
