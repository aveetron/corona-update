from django.shortcuts import render
import bangla
import corona_info as corona
import requests
import json


# Create your views here.
def dashboard(request):
    coronaSummaryResult = requests.get('https://corona.lmao.ninja/all').json()
    countryWiseSummary = requests.get('https://corona.lmao.ninja/countries').json()
    context = {
        'cases': bangla.convert_english_digit_to_bangla_digit(int(coronaSummaryResult['cases'])),
        'deaths': bangla.convert_english_digit_to_bangla_digit(int(coronaSummaryResult['deaths'])),
        'recovered': bangla.convert_english_digit_to_bangla_digit(int(coronaSummaryResult['recovered'])),
        'countryWiseSummary': countryWiseSummary
    }
    return render(request, 'index.html', context)