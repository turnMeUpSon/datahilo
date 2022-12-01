from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
    path('search/', searchbar, name='search'),
    path('treasury_y10_minus_y2', get_treasury_y_10_minus_y2, name='treasury_y10_minus_y2'),
    path('motor_vehicle_retail_sales', get_motor_vehicle_retail_sales, name='motor_vehicle_retail_sales'),
]
