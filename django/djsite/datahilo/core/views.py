from django.shortcuts import render
from .models import *


def index(request):
    treasury_y10__minus_y2 = Indicators.objects.get(pk=1)
    motor_vehicle_retail_sales_heavy_weight_trucks = Indicators.objects.get(
        pk=2)
    unemployment_rate = Indicators.objects.get(pk=3)
    federal_funds_effective_rate_and_cpi_usa = Indicators.objects.get(pk=4)
    treasury_y10_minus_m3 = Indicators.objects.get(pk=5)
    global_price_of_food_index = Indicators.objects.get(pk=6)
    natural_gas_liquid_composite_price_usa = Indicators.objects.get(pk=7)
    real_gross_domestic_product = Indicators.objects.get(pk=8)
    industrial_production_and_capacity_utilization = Indicators.objects.get(
        pk=9)
    initial_claims = Indicators.objects.get(pk=10)
    real_personal_consumption_expenditures = Indicators.objects.get(pk=11)
    advance_retail_sales_retail_trade = Indicators.objects.get(pk=12)
    merchant_wholesalers_sales = Indicators.objects.get(pk=13)
    total_business_inventories = Indicators.objects.get(pk=14)
    total_consumer_credit_outstanding_usa = Indicators.objects.get(pk=15)

    return render(request, 'core/index.html', {
        'treasury_y10__minus_y2': treasury_y10__minus_y2, 'motor_vehicle_retail_sales_heavy_weight_trucks': motor_vehicle_retail_sales_heavy_weight_trucks, 'unemployment_rate': unemployment_rate,
        'federal_funds_effective_rate_and_cpi_usa': federal_funds_effective_rate_and_cpi_usa, 'treasury_y10_minus_m3': treasury_y10_minus_m3, 'global_price_of_food_index': global_price_of_food_index,
        'natural_gas_liquid_composite_price_usa': natural_gas_liquid_composite_price_usa, 'real_gross_domestic_product': real_gross_domestic_product, 'industrial_production_and_capacity_utilization': industrial_production_and_capacity_utilization,
        'initial_claims': initial_claims, 'real_personal_consumption_expenditures': real_personal_consumption_expenditures, 'advance_retail_sales_retail_trade': advance_retail_sales_retail_trade,
        'merchant_wholesalers_sales': merchant_wholesalers_sales, 'total_business_inventories': total_business_inventories, 'total_consumer_credit_outstanding_usa': total_consumer_credit_outstanding_usa
    })


def dashboard(request):
    return render(request, 'core/dashboard.html')


def searchbar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            indicators = Indicators.objects.filter(title__icontains=query)
            return render(request, 'core/searchbar.html', {'indicators': indicators})
        else:
            print("No results")
            return render(request, 'core/searchbar.html', {})


def get_treasury_y_10_minus_y2(request):
    treasury_y10__minus_y2 = Indicators.objects.get(pk=1)
    return render(request, 'core/treasury_y10_minus_y2.html', {'treasury_y10__minus_y2': treasury_y10__minus_y2})


def get_motor_vehicle_retail_sales(request):
    motor_vehicle_retail_sales_heavy_weight_trucks = Indicators.objects.get(pk=2)
    return render(request, 'core/motor_vehicle_retail_sales.html', {'motor_vehicle_retail_sales_heavy_weight_trucks': motor_vehicle_retail_sales_heavy_weight_trucks})
