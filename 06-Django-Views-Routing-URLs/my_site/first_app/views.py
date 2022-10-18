from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def simple_view(request):
    return HttpResponse('SAMPLE VIEWS ~~~~') # template HTML > JINJA

articles = {
    'sports':'Sport page~',
    'finance':'Finance page~',
    'politics':'Politics page~',
}    

def sports_view(request):
    return HttpResponse(articles['sports'])

def finance_view(request):
    return HttpResponse(articles['finance'])

def news_view(request, topic):
    return HttpResponse(articles[topic])

def add_view(request, num1, num2):
    # domain.com/first_app/num1/num2 --> num1+num2
    result = f'{num1} + {num2} = {num1+num2}'
    return HttpResponse(str(result))

