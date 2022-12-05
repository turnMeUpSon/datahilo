from django.urls import reverse, resolve


class TestUrls:

    def test_index_URL(self):
        path = reverse('index')
        assert resolve(path).view_name == 'index'

    def test_dashboard_URL(self):
        path = reverse('dashboard')
        assert resolve(path).view_name == 'dashboard'

    def test_search_URL(self):
        path = reverse('search')
        assert resolve(path).view_name == 'search'

    def test_treasury_y10_minus_y2_URL(self):
        path = reverse('treasury_y10_minus_y2')
        assert resolve(path).view_name == 'treasury_y10_minus_y2'

    def test_motor_vehicle_retail_sales_URL(self):
        path = reverse('motor_vehicle_retail_sales')
        assert resolve(path).view_name == 'motor_vehicle_retail_sales'

    def test_unemployment_rate_URL(self):
        path = reverse('unemployment_rate')
        assert resolve(path).view_name == 'unemployment_rate'

    def test_federal_funds_effective_rate_and_cpi_usa_URL(self):
        path = reverse('federal_funds_effective_rate_and_cpi_usa')
        assert resolve(path).view_name == 'federal_funds_effective_rate_and_cpi_usa'

    def test_treasury_y10_minus_m3_URL(self):
        path = reverse('treasury_y10_minus_m3')
        assert resolve(path).view_name == 'treasury_y10_minus_m3'

    def test_global_price_of_food_index_URL(self):
        path = reverse('global_price_of_food_index')
        assert resolve(path).view_name == 'global_price_of_food_index'

    def test_natural_gas_liquid_composite_price_usa_URL(self):
        path = reverse('natural_gas_liquid_composite_price_usa')
        assert resolve(path).view_name == 'natural_gas_liquid_composite_price_usa'

    def test_real_gross_domestic_product_URL(self):
        path = reverse('real_gross_domestic_product')
        assert resolve(path).view_name == 'real_gross_domestic_product'

    def test_industrial_production_and_capacity_utilization_URL(self):
        path = reverse('industrial_production_and_capacity_utilization')
        assert resolve(path).view_name == 'industrial_production_and_capacity_utilization'

    def test_initial_claims_URL(self):
        path = reverse('initial_claims')
        assert resolve(path).view_name == 'initial_claims'

    def test_real_personal_consumption_expenditures_URL(self):
        path = reverse('real_personal_consumption_expenditures')
        assert resolve(path).view_name == 'real_personal_consumption_expenditures'

    def test_advance_retail_sales_retail_trade_URL(self):
        path = reverse('advance_retail_sales_retail_trade')
        assert resolve(path).view_name == 'advance_retail_sales_retail_trade'

    def test_merchant_wholesalers_sales_URL(self):
        path = reverse('merchant_wholesalers_sales')
        assert resolve(path).view_name == 'merchant_wholesalers_sales'

    def test_total_business_inventories_URL(self):
        path = reverse('total_business_inventories')
        assert resolve(path).view_name == 'total_business_inventories'

    def test_total_consumer_credit_outstanding_usa_URL(self):
        path = reverse('total_consumer_credit_outstanding_usa')
        assert resolve(path).view_name == 'total_consumer_credit_outstanding_usa'
