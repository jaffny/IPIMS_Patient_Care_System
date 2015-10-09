from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class PermissionsRole(models.Model):
	role = models.CharField(max_length=256, choices=[('admin', 'admin'), ('nurse', 'nurse'), ('staff', 'staff'), ('doctor', 'doctor'), ('patient', 'patient'), ('lab', 'lab')])
	user = models.OneToOneField(User, unique=True,  blank=True, default="")

	def __unicode__(self):
		return str(self.role)

#This patient model will extend the user class so we can add the associated medical data for the user
class Patient(models.Model):
	phone_number = PhoneNumberField(blank = True)
	email_address = models.EmailField(blank = True, max_length=254)
	user = models.OneToOneField(User, unique=True,  blank=True, default="")

	def __unicode__(self):
		return str(self.user)

class PatientAppt(models.Model):
	date = models.DateTimeField(auto_now=False, auto_now_add=False)
	doctor = models.CharField(max_length=80)
	user = models.ForeignKey(Patient, unique=False, blank=True, default="")

	def __unicode__(self):
		return str(self.doctor)