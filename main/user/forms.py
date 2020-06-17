from django.contrib.auth.forms import UserCreationForm
from main.user.models import UserAccount
from django import forms


class CreateUserForm(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')
	
	class Meta:
		model = UserAccount
		fields = ('email', 'username', 'password', 'password2',)
