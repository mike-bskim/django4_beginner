from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def simple_view(request):
    return HttpResponse('SAMPLE VIEWS ~~~~') # template HTML > JINJA

def sports_view(request):
    return HttpResponse('sports Page ~~~~')

def finance_view(request):
    return HttpResponse('Finance Page ~~~~')

