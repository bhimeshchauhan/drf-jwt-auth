from django.urls import path
from main.cars.api.views import (
	retrieve_cars,
	create_car,
	pk_operate_car,
)


app_name = 'account'

urlpatterns = [
	path('cars/', retrieve_cars, name="listall"),
	path('cars/<str:pk>/', pk_operate_car, name="listone"),
	path('cars', create_car, name="create"),
	path('cars/<str:pk>', pk_operate_car, name="update"),
	path('cars/<str:pk>', pk_operate_car, name="delete"),
]
