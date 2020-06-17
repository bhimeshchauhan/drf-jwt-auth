from django.urls import path
from main.user.api.views import (
	registration_view,
	login_view
)

app_name = 'account'

urlpatterns = [
	path('register', registration_view, name="register"),
	path('login', login_view, name="login"),
]
