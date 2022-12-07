from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
    path('search/', searchbar, name='search'),
    path('treasury_y10_minus_y2', get_treasury_y_10_minus_y2, name='treasury_y10_minus_y2'),
    path('motor_vehicle_retail_sales', get_motor_vehicle_retail_sales, name='motor_vehicle_retail_sales'),
    path('unemployment_rate', get_unemployment_rate, name='unemployment_rate'),
    path('federal_funds_effective_rate_and_cpi_usa', get_federal_funds_effective_rate_and_cpi_usa,
         name='federal_funds_effective_rate_and_cpi_usa'),
    path('treasury_y10_minus_m3', get_treasury_y10_minus_m3, name='treasury_y10_minus_m3'),
    path('global_price_of_food_index', get_global_price_of_food_index, name='global_price_of_food_index'),
    path('natural_gas_liquid_composite_price_usa', get_natural_gas_liquid_composite_price_usa,
         name='natural_gas_liquid_composite_price_usa'),
    path('real_gross_domestic_product', get_real_gross_domestic_product, name='real_gross_domestic_product'),
    path('industrial_production_and_capacity_utilization', get_industrial_production_and_capacity_utilization,
         name='industrial_production_and_capacity_utilization'),
    path('initial_claims', get_initial_claims, name='initial_claims'),
    path('real_personal_consumption_expenditures', get_real_personal_consumption_expenditures,
         name='real_personal_consumption_expenditures'),
    path('advance_retail_sales_retail_trade', get_advance_retail_sales_retail_trade, name='advance_retail_sales_retail_trade'),
    path('merchant_wholesalers_sales', get_merchant_wholesalers_sales, name='merchant_wholesalers_sales'),
    path('total_business_inventories', get_total_business_inventories, name='total_business_inventories'),
    path('total_consumer_credit_outstanding_usa', get_total_consumer_credit_outstanding_usa,
         name='total_consumer_credit_outstanding_usa'),
]
