from django.contrib import admin

from .models import Patient, PatientAppt, PermissionsRole


#Add custom columns to appear inside of the database for the user
class PatientApptAdmin(admin.ModelAdmin):
	list_display = ('user', 'doctor', 'date')

class PermissionsRoleAdmin(admin.ModelAdmin):
	list_display = ('user', 'role')


admin.site.register(Patient)
admin.site.register(PatientAppt, PatientApptAdmin)
admin.site.register(PermissionsRole, PermissionsRoleAdmin)