from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 함수기반의 view
def index(request):
    return HttpResponse('HELLO THIS A VIEW INSODE MY_APP')