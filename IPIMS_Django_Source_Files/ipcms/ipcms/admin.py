from django.contrib import admin
from .forms import *
from .models import Patient, PatientAppt, PermissionsRole, Doctor, PatientHealthConditions, TempPatientData


#Add custom columns to appear inside of the database for the user
class PatientApptAdmin(admin.ModelAdmin):
	list_display = ('user', 'doctor', 'date')
	form = PatientApptForm

class PermissionsRoleAdmin(admin.ModelAdmin):
	list_display = ('user', 'role')

class DoctorAdmin(admin.ModelAdmin):
	list_display = ('doctor_first_name', 'doctor_last_name')

class PatientHealthConditionsAdmin(admin.ModelAdmin):
	form = PatientHealthConditionsForm

class TempPatientDataAdmin(admin.ModelAdmin):
	list_display=('first_name','last_name')

admin.site.register(TempPatientData,TempPatientDataAdmin)
admin.site.register(PatientHealthConditions, PatientHealthConditionsAdmin)
admin.site.register(Patient)
admin.site.register(PatientAppt, PatientApptAdmin)
admin.site.register(PermissionsRole, PermissionsRoleAdmin)
admin.site.register(Doctor, DoctorAdmin)