from django.shortcuts import render
from .models import *
from django.db.models import Q


def index(request):
    indicator1 = Indicators.objects.get(pk=1)
    indicator2 = Indicators.objects.get(pk=2)
    indicator3 = Indicators.objects.get(pk=3)
    indicator4 = Indicators.objects.get(pk=4)
    indicator5 = Indicators.objects.get(pk=5)
    indicator6 = Indicators.objects.get(pk=6)
    indicator7 = Indicators.objects.get(pk=7)
    indicator8 = Indicators.objects.get(pk=8)
    indicator9 = Indicators.objects.get(pk=9)
    indicator10 = Indicators.objects.get(pk=10)
    indicator11 = Indicators.objects.get(pk=11)
    indicator12 = Indicators.objects.get(pk=12)
    indicator13 = Indicators.objects.get(pk=13)
    indicator14 = Indicators.objects.get(pk=14)
    indicator15 = Indicators.objects.get(pk=15)

    return render(request, 'core/index.html', {
        'indicator1': indicator1, 'indicator2': indicator2, 'indicator3': indicator3,
        'indicator4': indicator4, 'indicator5': indicator5, 'indicator6': indicator6,
        'indicator7': indicator7, 'indicator8': indicator8, 'indicator9': indicator9,
        'indicator10': indicator10, 'indicator11': indicator11, 'indicator12': indicator12,
        'indicator13': indicator13, 'indicator14': indicator14, 'indicator15': indicator15
    })


def test(request):
    return render(request, 'core/test.html')


def searchbar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            indicators = Indicators.objects.filter(title__icontains=query)
            return render(request, 'core/searchbar.html', {'indicators': indicators})
        else:
            print("No results")
            return render(request, 'core/searchbar.html', {})
