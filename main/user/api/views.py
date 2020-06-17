from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.conf import settings
from django.contrib import auth
import jwt

from main.user.api.serializers import RegistrationSerializer, LoginSerializer


@api_view(['POST', ])
def registration_view(request):
	if request.method == 'POST':
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			account = serializer.save()
			data['response'] = 'successfully registered new user.'
			data['email'] = account.email
			data['username'] = account.username
			status_code = status.HTTP_200_OK
		else:
			data = serializer.errors
			status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
		return Response(data, status=status_code)


# user = request.data.get('user', {})
#
# serializer = RegistrationSerializer(data=user)
# serializer.is_valid(raise_exception=True)
# serializer.save()
#
# return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST', ])
def login_view(request):
	if request.method == 'POST':
		data = request.data
		email = data.get('email', '')
		password = data.get('password', '')
		user = auth.authenticate(email=email, password=password)
		
		if user:
			auth_token = jwt.encode({'email': user.email}, settings.JWT_SECRET_KEY)
			serializer = LoginSerializer(user)
			data = {
				'user': serializer.data,
				'token': auth_token
			}
			return Response(data, status=status.HTTP_200_OK)
		
		return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
	
	# serializer = LoginSerializer(data={'email': email, 'password': password})
	# if serializer.is_valid():
	# 	serializer.is_valid(raise_exception=True)
	# 	return Response(serializer.data, status=status.HTTP_200_OK)
	# else:
	# 	return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# 	serializer = LoginSerializer(data=request.data)
# 	if serializer.is_valid():
# 		print(serializer.data)
# 		return Response(serializer.data, status=status.HTTP_200_OK)
# 	else:
# 		print('err',serializer.data)
# 		return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
