from django.shortcuts import render
from . import models
# from django.http.response import HttpResponse

# Create your views here.
def list_patients(request):
    all_patients = models.Patient.objects.all()
    context_list = {'patients' : all_patients}

    # return HttpResponse('patients list')
    return render(request, 'first_app/list.html', context=context_list)