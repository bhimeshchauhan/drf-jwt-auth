from django.urls import path
from main.trucks.api.views import (
	retrieve_trucks,
	create_truck,
	pk_operate_truck,
)


app_name = 'account'

urlpatterns = [
	path('trucks/', retrieve_trucks, name="listall"),
	path('trucks/<str:pk>/', pk_operate_truck, name="listone"),
	path('trucks', create_truck, name="create"),
	path('trucks/<str:pk>', pk_operate_truck, name="update"),
	path('trucks/<str:pk>', pk_operate_truck, name="delete"),
]
