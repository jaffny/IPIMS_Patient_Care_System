from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


#This class will also contain the list of names of the doctors who work for the hospital
class Doctor(models.Model):
	doctor_first_name = models.CharField(max_length=256, default="")
	doctor_last_name = models.CharField(max_length=256, default="")
	doctor_type = models.CharField(max_length=256, choices=[('Gynecologist', 'Gynecologist'), ('Neurologist', 'Neurologist'), ('Therapist', 'Therapist'), ('Allergist', 'Allergist'), ('Cardiologist', 'Cardiologist'), ('Dermatologist', 'Dermatologist'), ('Oncologist', 'Oncologist'), ('ENT', 'ENT'), ('Plastic Surgeon', 'Plastic Surgeon'), ('Psychiatrist', 'Psychiatrist'), ('Urologist','Urologist'), ('Podiatrist', 'Podiatrist')], default="Select Doctor Type") 
	
	def __unicode__(self):
		return "Dr. " + str(self.doctor_first_name.title()) + ' ' + str(self.doctor_last_name.title()) + ' - ' + str(self.doctor_type.title())

class PermissionsRole(models.Model):
	role = models.CharField(max_length=256, choices=[('admin', 'admin'), ('nurse', 'nurse'), ('staff', 'staff'), ('doctor', 'doctor'), ('patient', 'patient'), ('lab', 'lab')])
	user = models.OneToOneField(User, unique=True,  blank=True, default="")

	def __unicode__(self):
		return str(self.role)

#This is the mediator for the data that is submitted by the user to the HSP staff
#The data is stored and if the HSP staff approves the patient, then the data will be stored into a patient class
class TempPatientData(models.Model):

	user = models.OneToOneField(User,unique=True,null=True,default="")
	email_address = models.CharField(max_length=256, blank=False)
	first_name = models.CharField(max_length=256, default="")
	last_name = models.CharField(max_length=256, default="")
	age = models.IntegerField(default = 18, blank=False)
	gender = models.CharField(max_length=256, choices=[('male','Male'), ('female', 'Female'), ('other', 'Other'), ('prefer not to say', 'Prefer Not To Say')], default='Select a gender', blank = False)
	race = models.CharField(max_length=256, choices=[('white', 'White'), ('american_indian_alaskan_native', 'American Indian or Alaskan Native'),('hawaiian', 'Native Hawaiian or Other Pacific Islander'),('black', 'Black or African American'),('asian', 'Asian'), ('other', 'Other')], default="Other")
	phone_number = PhoneNumberField(blank = False, default="")
	DOB = models.DateField(auto_now=False, auto_now_add=False, default="")
	ssn = models.IntegerField(blank=False)
	allergies = models.CharField(max_length=256, default="")
	address = models.CharField(max_length=256, default="")
	medications = models.CharField(max_length=256, default="")
	insurance_provider =models.CharField(max_length=256, blank=False)
	insurance_policy_number = models.IntegerField(blank=False)
	data_sent = models.IntegerField(default=0)


	def __unicode__(self):
		return (str(self.first_name) + " " + str(self.last_name) + " " + str(self.email_address))



#This patient model will extend the user class so we can add the associated medical data for the user
class Patient(models.Model):

	fill_from_application = models.OneToOneField(TempPatientData,unique=True,null=True,default="")
	user = models.OneToOneField(User, unique=True,  blank=True, default="", null=True)
	approved = models.IntegerField(default=0, null=False)
	alertSent = models.IntegerField(default=0, null=False)

	def __unicode__(self):
		return str(self.user)

class PatientHealthConditions(models.Model):

	user = models.OneToOneField(Patient, unique=False, blank=True, default="")

	nausea_level = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(10)], default=0)
	hunger_level = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(10)], default=0)
	anxiety_level = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(10)], default=0)
	stomach_level = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(10)], default=0)
	body_ache_level = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(10)], default=0)
	chest_pain_level = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(10)], default=0)

	def __unicode__(self):
		return str(self.user.user.username)

#Class for the patients to schedule appointments for their associated doctor
class PatientAppt(models.Model):
	date = models.CharField(max_length=1000, unique=True)
	doctor = models.ForeignKey(Doctor, unique=False, default=-1)
	pain_level = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(10)], blank=False)
	medical_conditions = models.CharField(max_length=1000, default="None")
	allergies = models.CharField(max_length=1000, default="None")
	user = models.ForeignKey(Patient, unique=False, blank=True, default="")
	current_health_conditions = models.ForeignKey(PatientHealthConditions, unique=False, blank=True, default="", null=True)
	resolved = models.IntegerField(default=0, blank=True)

	def __unicode__(self):
		return str(self.doctor)


#Class that is responsible for housing all of the alerts that are submitted by the user
class Alert(models.Model):
	alert_level = models.IntegerField(default=0, null=False)
	alert_patient = models.OneToOneField(Patient, unique = True, null = True)
	alert_description = models.CharField(max_length=255, default="", null = True, unique=False)


