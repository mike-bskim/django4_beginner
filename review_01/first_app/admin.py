from django.contrib import admin
from first_app.models import Patient

# Register your models here.
# admin.site.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    # fields = ['heartrate', 'last_name','first_name', 'age']
    fieldsets = [
        ('USER NAME', {'fields':['first_name','last_name']}),
        ('HEALTH CONDITIONS', {'fields':['age','heartrate']}),

    ]

admin.site.register(Patient, PatientAdmin)
