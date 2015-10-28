from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from datetime import datetime
from ipcms.models import TempPatientData, Doctor, Patient, PatientHealthConditions, PatientAppt, Alert
from pprint import pprint

# class PatientHealthTest(TestCase):
# 	def testHealthCondition(self):

# 		HC = PatientHealthConditions.objects.create()
# 		HC.user = 1
# 		HC.nausea_level = 5
# 		HC.hunger_level = 7
# 		HC.anxiety_level = 3
# 		HC.stomach_level = 1
# 		HC.body_ache_level = 4
# 		HC.chest_pain_level = 9

# 		self.assertEqual(HC.user, 1)
# 		self.assertEqual(HC.nausea_level, 5)
# 		self.assertEqual(HC.hunger_level, 7)
# 		self.assertEqual(HC.anxiety_level, 3)
# 		self.assertEqual(HC.stomach_level, 1)
# 		self.assertEqual(HC.body_ache_level, 4)
# 		self.assertEqual(HC.chest_pain_level, 9)


class TestingPatientApointment(TestCase):

	#Globally references patient object
	def testPatientAppt(self):

		temp_patient_object = TempPatientData.objects.create()
		#Create the user to append into the model
		temp_patient_object.user = User.objects.create(username="user", email="user@user.com", password="newuser")

		# #Assign the attributes that are associated wi+th the user
		temp_patient_object.first_name = "Po-Kai"
		temp_patient_object.last_name = "Huang"
		temp_patient_object.age = 23
		# temp_patient_object.phone_number = "+114804460455"
		temp_patient_object.DOB = "1990-11-20"
		temp_patient_object.ssn = 123456789
		temp_patient_object.allergies = "peanut"
		temp_patient_object.address = "1349 E Spence Ave"
		temp_patient_object.medications = "NONE"
		temp_patient_object.insurance_provider = "School"
		temp_patient_object.insurance_policy_number = 19938343434
		temp_patient_object.email_address = "user@user.com"
		temp_patient_object.data_sent = 1

		# #Save user into the test database
		temp_patient_object.save()

		self.assertEqual(temp_patient_object.first_name, "Po-Kai")
		self.assertEqual(temp_patient_object.last_name, "Huang")
		self.assertEqual(temp_patient_object.age, 23)
		# self.assertEqual(temp_patient_object.phone_number, "+114804460455")
		self.assertEqual(temp_patient_object.DOB, "1990-11-20")
		self.assertEqual(temp_patient_object.ssn, 123456789)
		self.assertEqual(temp_patient_object.allergies, "peanut")
		self.assertEqual(temp_patient_object.address, "1349 E Spence Ave")
		self.assertEqual(temp_patient_object.medications, "NONE")
		self.assertEqual(temp_patient_object.insurance_provider, "School")
		self.assertEqual(temp_patient_object.insurance_policy_number, 19938343434)
		self.assertEqual(temp_patient_object.email_address, "user@user.com")
		self.assertEqual(temp_patient_object.data_sent, 1)


		patient_object = Patient.objects.create()

		patient_object.fill_from_application = temp_patient_object
		patient_object.user = temp_patient_object.user
		patient_object.approved  = 1
		patient_object.alertSent = 1
		
		self.assertEqual(patient_object.alertSent,1)
		self.assertEqual(patient_object.approved, 1)
		self.assertEqual(patient_object.user.username, 'user')

		patient_object.save()
		
		TestPatientAppt_object = PatientAppt.objects.create()
		TestPatientAppt_object.date = "2015-10-29"
		TestPatientAppt_object.doctor = 1
		TestPatientAppt_object.pain_level = 4
		TestPatientAppt_object.medical_conditions = "none"
		TestPatientAppt_object.allergies = "peanut"
		TestPatientAppt_object.user = patient_object
		TestPatientAppt_object.current_health_conditions = ""
		TestPatientAppt_object.resolved = ""

		TestPatientAppt_object.save()

		self.assertEqual(TestPatientAppt_object.date, "2015-10-29")
		self.assertEqual(TestPatientAppt_object.doctor, 1)
		self.assertEqual(TestPatientAppt_object.pain_level, 3)
		self.assertEqual(TestPatientAppt_object.medical_conditions, "none")
		self.assertEqual(TestPatientAppt_object.allergies, "peanut")
		self.assertEqual(TestPatientAppt_object.user, patient_object)
		self.assertEqual(TestPatientAppt_object.current_health_conditions, "")
		self.assertEqual(TestPatientAppt_object.resolved, "")
		

		pprint(TestPatientAppt_object)

		print ('\n\n\nTestPatientAppt FOR THE USER HAS BEEN SUCCESSFULLY CREATED!\n\n\n')

# #This will be used to prepare the creation of the users within the system
# class TestingDifferentUserCreations(TestCase):

# 	#Globally references patient object
# 	def testSubmitApplicationToHSPStaff(self):
# 		temp_patient_object = TempPatientData.objects.create()
# 		#Create the user to append into the model
# 		temp_patient_object.user = User.objects.create(username="johnson", email="johnson@johnson.com", password="johnson")
# 		print ('Temporary Patient Created Successfully!')

# 		#Assign the attributes that are associated with the user
# 		temp_patient_object.first_name = "Ryan"
# 		temp_patient_object.last_name = "Schachte"
# 		temp_patient_object.DOB = "1995-02-20"
# 		temp_patient_object.ssn	 = "600489139"
# 		temp_patient_object.allergies = "NONE"
# 		temp_patient_object.address = "2463 E. Mallory Dr. Tempe, AZ 85281"
# 		temp_patient_object.phone_number = "+14804460455"
# 		temp_patient_object.medications = "NONE"
# 		temp_patient_object.insurance_provider = "Allstate"
# 		temp_patient_object.insurance_policy_number = "19938343434"
# 		temp_patient_object.email_address = "johnson@johnson.com"
# 		temp_patient_object.data_sent = "1"

# 		#Save user into the test database
# 		temp_patient_object.save()

# 		self.assertEqual(temp_patient_object.first_name, "Ryan")
# 		self.assertEqual(temp_patient_object.last_name, "Schachte")
# 		self.assertEqual(temp_patient_object.DOB, "1995-02-20")
# 		self.assertEqual(temp_patient_object.ssn, "600489139")
# 		self.assertEqual(temp_patient_object.phone_number,"+14804460455")
# 		self.assertEqual(temp_patient_object.allergies, "NONE")
# 		self.assertEqual(temp_patient_object.address, "2463 E. Mallory Dr. Tempe, AZ 85281")
# 		self.assertEqual(temp_patient_object.medications, "NONE")
# 		self.assertEqual(temp_patient_object.insurance_provider, "Allstate")
# 		self.assertEqual(temp_patient_object.insurance_policy_number, "19938343434")
# 		self.assertEqual(temp_patient_object.email_address, "johnson@johnson.com")
# 		self.assertEqual(temp_patient_object.data_sent, "1")

# 		pprint (vars(temp_patient_object))

# 		print ('\n\n\nALERT FOR THE USER HAS BEEN SUCCESSFULLY CREATED!\n\n\n')


	# #Test the creation of a patient
	# def testPatientCreation(self):

	# 	temp_patient_object = TempPatientData.objects.create()

	# 	#Create the user to append into the model
	# 	temp_patient_object.user = User.objects.create(username="johnson", email="johnson@johnson.com", password="johnson")
	# 	print ('Temporary Patient Created Successfully!')

	# 	#Assign the attributes that are associated with the user
	# 	temp_patient_object.first_name = "Ryan"
	# 	temp_patient_object.last_name = "Schachte"
	# 	temp_patient_object.DOB = "2201995"
	# 	temp_patient_object.ssn = "600489139"
	# 	temp_patient_object.allergies = "NONE"
	# 	temp_patient_object.address = "2463 E. Mallory Dr. Tempe, AZ 85281"
	# 	temp_patient_object.medications = "NONE"
	# 	temp_patient_object.insurance_provider = "Allstate"
	# 	temp_patient_object.insurance_policy_number = "19938343434"
	# 	temp_patient_object.email_address = "johnson@johnson.com"
	# 	temp_patient_object.data_sent = "1"

	# 	#Save user into the test database
	# 	temp_patient_object.save()

	# 	print ('Application Submitted, now testing creation of an approved patient by HSP staff')

	# 	approved_patient = Patient.objects.create()
	# 	approved_patient.user = temp_patient_object.user
	# 	approved_patient.fill_from_application = temp_patient_object
	# 	approved_patient.approved = 1
	# 	approval = approved_patient.approved

	# 	#Testing to ensure the object data from temp patient filtered down into the approved patient
	# 	self.assertEqual(approved_patient.user.username, temp_patient_object.user.username)
	# 	self.assertEqual(approved_patient.fill_from_application.DOB, "2201995")
	# 	self.assertEqual(approval, 1)

	# 	approved_patient.save()

	# 	print ('\n\n\nThe patient has been approved succesfully!\n\n\n')


	# # #Test the update of health condition
	# def testUpdateHealthConditions(self):


	# 	temp_patient_object = TempPatientData.objects.create()

	# 	#Create the user to append into the model
	# 	temp_patient_object.user = User.objects.create(username="johnson1", email="johnson1@johnson.com", password="johnson1")
	# 	print ('Temporary Patient Created Successfully!')

	# 	#Assign the attributes that are associated with the user
	# 	temp_patient_object.first_name = "Ryewfan"
	# 	temp_patient_object.last_name = "Schawefchte"
	# 	temp_patient_object.DOB = "220195"
	# 	temp_patient_object.ssn = "6009139"
	# 	temp_patient_object.allergies = "fNONE"
	# 	temp_patient_object.address = "24f63 E. Mallory Dr. Tempe, AZ 85281"
	# 	temp_patient_object.medications = "NONE"
	# 	temp_patient_object.insurance_provider = "Allstaefte"
	# 	temp_patient_object.insurance_policy_number = "19938343434"
	# 	temp_patient_object.email_address = "johnsofn@johnsown.com"
	# 	temp_patient_object.data_sent = "1"

	# 	# #Save user into the test database
	# 	temp_patient_object.save()

	# 	print ('Application Submitted, now testing creation of an approved patient by HSP staff')

	# 	approved_patient = Patient.objects.create()
	# 	approved_patient.user = temp_patient_object.user
	# 	approved_patient.fill_from_application = temp_patient_object
	# 	approved_patient.approved = 1
	# 	approval = approved_patient.approved

	# 	#Testing to ensure the object data from temp patient filtered down into the approved patient
	# 	self.assertEqual(approved_patient.user.username, temp_patient_object.user.username)
	# 	self.assertEqual(approved_patient.fill_from_application.DOB, "220195")
	# 	self.assertEqual(approval, 1)
	# 	approved_patient.save()

		# ---------------------------------------------------------------------#
		# temp_doctor_object = Doctor.objects.create()
		# #Assign the attributes to the doctor object 
		# temp_doctor_object.doctor_first_name = 	"test"
		# temp_doctor_object.doctor_last_name = "Doctor1"
		# temp_doctor_object.doctor_type = "Gynecologist"

		# temp_doctor_object.save()

		# self.assertEqual(temp_patient_object.doctor_first_name, "test")
		# self.assertEqual(temp_patient_object.doctor_last_name, "Doctor1")
		# self.assertEqual(temp_patient_object.doctor_type, "Gynecologist")
		

	# # 	# user is now created, we want to update the health conditions of the patient
	# 	patient_health_conditions = PatientHealthConditions.objects.create()
	# 	patient_health_conditions.nausea_level = 5
	# 	patient_health_conditions.hunger_level = 7
	# 	patient_health_conditions.anxiety_level = 3
	# 	patient_health_conditions.stomach_level = 1
	# 	patient_health_conditions.body_ache_level = 4
	# 	patient_health_conditions.chest_pain_level = 9

	# 	self.assertEqual(patient_health_conditions.nausea_level, 5)
	# 	self.assertEqual(patient_health_conditions.hunger_level, 7)
	# 	self.assertEqual(patient_health_conditions.anxiety_level, 3)
	# 	self.assertEqual(patient_health_conditions.stomach_level, 1)
	# 	self.assertEqual(patient_health_conditions.body_ache_level, 4)
	# 	self.assertEqual(patient_health_conditions.body_ache_level, 4)
	# 	self.assertEqual(patient_health_conditions.chest_pain_level, 9)

	# 	print ('\n\n\nAPPT. SCHEDULED SUCCESSFULLY!!!\n\n\n')


	# # #Test the creation of a an appointment
	# def testPatientAppoitmentSchedule(self):
	# 	appt_obj = PatientAppt.objects.create()

	# 	appt_obj.date = '2000-02-20'
	# 	# appt_obj.doctor = Doctor_Obj()
	# 	appt_obj.pain_level = 5
	# 	appt_obj.medical_conditions = "None"
	# 	# appt_obj.user = patient_user()
	# 	appt_obj.allergies = "None"
	# 	# appt_obj.current_health_conditions = health_conditions()

	# 	# self.assertEqual(appt_obj.doctor.name, Doctor_Obj.name)
	# 	self.assertEqual(appt_obj.pain_level, 5)
	# 	self.assertEqual(appt_obj.medical_conditions, "None")

	# 	print ('Appt. Created Successfully!')



	# date = models.CharField(max_length=1000, unique=True)
	# doctor = models.ForeignKey(Doctor, unique=False, blank=False, default=-1)
	# pain_level = models.IntegerField(validators=[MinValueValidator(0),
 #                                       MaxValueValidator(10)], default=0)
	# medical_conditions = models.CharField(max_length=1000, default="None")
	# allergies = models.CharField(max_length=1000, default="None")
	# user = models.ForeignKey(Patient, unique=False, blank=True, default="")
	# current_health_conditions = models.ForeignKey(PatientHealthConditions, unique=False, blank=True, default="", null=True)


# class TestingPatientAlertSystem(TestCase):

# 	#Globally references patient object
# 	def testAlertSystem(self):
# 		temp_patient_object = TempPatientData.objects.create()
# 		#Create the user to append into the model
# 		temp_patient_object.user = User.objects.create(username="johnson", email="johnson@johnson.com", password="johnson")
# 		print ('Temporary Patient Created Successfully!')

# 		#Assign the attributes that are associated with the user
# 		temp_patient_object.first_name = "Ryan"
# 		temp_patient_object.last_name = "Schachte"
# 		temp_patient_object.DOB = "1990-12-11"
# 		temp_patient_object.ssn = "600-48-9139"
# 		temp_patient_object.allergies = "NONE"
# 		temp_patient_object.address = "2463 E. Mallory Dr. Tempe, AZ 85281"
# 		temp_patient_object.medications = "NONE"
# 		temp_patient_object.insurance_provider = "Allstate"
# 		temp_patient_object.insurance_policy_number = "19938343434"
# 		temp_patient_object.email_address = "johnson@johnson.com"
# 		temp_patient_object.data_sent = "1"

# 		#Save user into the test database
# 		temp_patient_object.save()

# 		self.assertEqual(temp_patient_object.first_name, "Ryan")
# 		self.assertEqual(temp_patient_object.last_name, "Schachte")
# 		self.assertEqual(temp_patient_object.DOB, "1990-12-11")
# 		self.assertEqual(temp_patient_object.ssn, "600-48-9139")
# 		self.assertEqual(temp_patient_object.allergies, "NONE")
# 		self.assertEqual(temp_patient_object.address, "2463 E. Mallory Dr. Tempe, AZ 85281")
# 		self.assertEqual(temp_patient_object.medications, "NONE")
# 		self.assertEqual(temp_patient_object.insurance_provider, "Allstate")
# 		self.assertEqual(temp_patient_object.insurance_policy_number, "19938343434")
# 		self.assertEqual(temp_patient_object.email_address, "johnson@johnson.com")
# 		self.assertEqual(temp_patient_object.data_sent, "1")

# 		patient_object = Patient.objects.create()

# 		patient_object.fill_from_application = temp_patient_object
# 		patient_object.user = temp_patient_object.user
# 		patient_object.approved = 1
# 		patient_object.alertSent = 1

# 		self.assertEqual(patient_object.alertSent,1)
# 		self.assertEqual(patient_object.approved, 1)
# 		self.assertEqual(patient_object.user.username, 'johnson')

# 		patient_object.save()

		
# 		alert_object = Alert.objects.create()
# 		alert_object.alert_level = 40
# 		alert_object.alert_patient = patient_object
# 		alert_object.alert_description = 'Hello, this is the description for alerts'
# 		alert_object.save()

# 		self.assertEqual(alert_object.alert_level, 40)
# 		self.assertEqual(alert_object.alert_patient, patient_object)
# 		alert_object.alert_description, 'Hello, this is the description for alerts'

# 		pprint(alert_object)

# 		print ('\n\n\nALERT FOR THE USER HAS BEEN SUCCESSFULLY CREATED!\n\n\n')

