import jwt

from datetime import datetime, timedelta
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')
		
		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)
		
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, email, password):
		if password is None:
			raise TypeError('Superusers must have a password.')

		user = self.create_user(username, email, password)
		user.is_superuser = True
		user.is_staff = True
		user.save(using=self._db)
		return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(verbose_name="email", max_length=60, unique=True)
	username = models.CharField(max_length=30, unique=False)
	date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']
	
	objects = UserManager()
	
	def __str__(self):
		return self.email
	
	@property
	def token(self):
		return self._generate_jwt_token()

	def get_full_name(self):
		return self.username

	def get_short_name(self):
		return self.username

	def _generate_jwt_token(self):
		'''
		Generates a JSON Web Token that stores this user's ID and
		expires 60 days into the future.
		'''
		dt = datetime.now() + timedelta(days=60)

		token = jwt.encode({
			'id': self.pk,
			'exp': int(dt.strftime('%s'))
		}, settings.SECRET_KEY, algorithm='HS256')

		return token.decode('utf-8')
