from django.shortcuts import render
# from django.http.response import HttpResponse

# Create your views here.
def list_patients(request):
    # return HttpResponse('patients list')
    return render(request, 'first_app/list.html')