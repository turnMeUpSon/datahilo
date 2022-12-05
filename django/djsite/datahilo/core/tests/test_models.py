from django.test import TestCase

from core.models import Indicators


class IndicatorsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Indicators.objects.create(title='Crypto Total Market Cap', symbol='TOTAL')

    def test_title(self):
        indicator = Indicators.objects.get(id=1)
        field_title = indicator._meta.get_field('title').verbose_name
        self.assertEqual(field_title, 'title')

    def test_title_max_length(self):
        indicator = Indicators.objects.get(id=1)
        max_length = indicator._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_symbol(self):
        indicator = Indicators.objects.get(id=1)
        field_symbol = indicator._meta.get_field('symbol').verbose_name
        self.assertEqual(field_symbol, 'symbol')

    def test_symbol_max_length(self):
        indicator = Indicators.objects.get(id=1)
        max_lenght = indicator._meta.get_field('symbol').max_length
        self.assertEqual(max_lenght, 30)
