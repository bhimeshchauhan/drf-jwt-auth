from rest_framework import serializers
from django.contrib.auth import authenticate

from main.user.models import UserAccount


class LoginSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserAccount
		fields = ['email', 'password']

		extra_kwargs = {'password': {'write_only': True}}

	def validate(self, data):
		password = data.get('password')
		email = data.get('email')
		if email is None:
			raise serializers.ValidationError(
				'An email address is required to log in.'
			)
		
		if password is None:
			raise serializers.ValidationError(
				'A password is required to log in.'
			)

		user = authenticate(username=email, password=password)
		
		if user is None:
			raise serializers.ValidationError(
				'A user with this email and password was not found.'
			)
		
		if not user.is_active:
			raise serializers.ValidationError(
				'This user has been deactivated.'
			)

		return {
			'email': user.email,
			'username': user.username,
			'token': user.token
		}


class RegistrationSerializer(serializers.ModelSerializer):
	password2 = serializers.CharField(
		style={'input_type': 'password'},
		write_only=True
	)
	# token = serializers.CharField(max_length=255, read_only=True)
	
	class Meta:
		model = UserAccount
		fields = ['email', 'username', 'password', 'password2']
		extra_kwargs = {
			'password': {'write_only': True},
		}
	
	def save(self):
		account = UserAccount(
			email=self.validated_data['email'],
			username=self.validated_data['username']
		)
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		account.set_password(password)
		account.save()
		return account
