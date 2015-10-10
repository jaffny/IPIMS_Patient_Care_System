from django.contrib import admin
from .forms import *
from .models import Patient, PatientAppt, PermissionsRole, Doctor


#Add custom columns to appear inside of the database for the user
class PatientApptAdmin(admin.ModelAdmin):
	list_display = ('user', 'doctor', 'date')

class PermissionsRoleAdmin(admin.ModelAdmin):
	list_display = ('user', 'role')

class DoctorAdmin(admin.ModelAdmin):
	list_display = ('doctor_first_name', 'doctor_last_name')


admin.site.register(Patient)
admin.site.register(PatientAppt, PatientApptAdmin)
admin.site.register(PermissionsRole, PermissionsRoleAdmin)
admin.site.register(Doctor, DoctorAdmin)