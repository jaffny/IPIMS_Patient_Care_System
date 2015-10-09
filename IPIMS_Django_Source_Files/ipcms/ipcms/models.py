from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

#This class will define all the permissions for the doc
#This class will also contain the list of names of the doctors who work for the hospital
class Doctor(models.Model):
	# doctor_name = models.CharField(max_length=256, choices=[('Dr. Schachte', 'Dr. Schachte'), ('Dr. Schachte', 'Dr. Huffy')], default="DEFAULT")
	doctor_first_name = models.CharField(max_length=256, default="")
	doctor_last_name = models.CharField(max_length=256, default="")
	doctor_type = models.CharField(max_length=256, choices=[('Gynecologist', 'Gynecologist'), ('Neuro', 'Neuro')], default="Select Doctor Type") 
	
	def __unicode__(self):
		return "Dr. " + str(self.doctor_last_name)

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

#Class for the patients to schedule appointments for their associated doctor
class PatientAppt(models.Model):
	date = models.DateTimeField(auto_now=False, auto_now_add=False, unique=True)
	doctor = models.ForeignKey(Doctor, unique=False, blank=True, default="")
	pain_level = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(10)], default=0)
	user = models.ForeignKey(Patient, unique=False, blank=True, default="")

	def __unicode__(self):
		return str(self.doctor)