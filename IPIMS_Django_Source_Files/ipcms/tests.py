from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from ipcms.models import TempPatientData, Doctor, Patient
from pprint import pprint

#This will be used to prepare the creation of the users within the system
class TestingDifferentUserCreations(TestCase):

	#Globally references patient object
	def testSubmitApplicationToHSPStaff(self):
		temp_patient_object = TempPatientData.objects.create()
		#Create the user to append into the model
		temp_patient_object.user = User.objects.create(username="johnson", email="johnson@johnson.com", password="johnson")
		print 'Temporary Patient Created Successfully!'

		#Assign the attributes that are associated with the user
		temp_patient_object.first_name = "Ryan"
		temp_patient_object.last_name = "Schachte"
		temp_patient_object.DOB = "2201995"
		temp_patient_object.ssn = "600489139"
		temp_patient_object.allergies = "NONE"
		temp_patient_object.address = "2463 E. Mallory Dr. Tempe, AZ 85281"
		temp_patient_object.medications = "NONE"
		temp_patient_object.insurance_provider = "Allstate"
		temp_patient_object.insurance_policy_number = "19938343434"
		temp_patient_object.email_address = "johnson@johnson.com"
		temp_patient_object.data_sent = "1"

		#Save user into the test database
		temp_patient_object.save()

		self.assertEqual(temp_patient_object.first_name, "Ryan")
		self.assertEqual(temp_patient_object.last_name, "Schachte")
		self.assertEqual(temp_patient_object.DOB, "2201995")
		self.assertEqual(temp_patient_object.ssn, "600489139")
		self.assertEqual(temp_patient_object.allergies, "NONE")
		self.assertEqual(temp_patient_object.address, "2463 E. Mallory Dr. Tempe, AZ 85281")
		self.assertEqual(temp_patient_object.medications, "NONE")
		self.assertEqual(temp_patient_object.insurance_provider, "Allstate")
		self.assertEqual(temp_patient_object.insurance_policy_number, "19938343434")
		self.assertEqual(temp_patient_object.email_address, "johnson@johnson.com")
		self.assertEqual(temp_patient_object.data_sent, "1")

		pprint (vars(temp_patient_object))

		print '\n\n\nUSER APPLICATION HAS BEEN CREATED AND SENT SUCCESSFULLY\n\n\n'

	#Create a doctor object that will be used for the patient to schedule an appt. within the system
	def testDoctorCreation(self):

		#Create the doctor object
		temp_doctor_object = Doctor.objects.create()
		print 'The doctor object has been successfully created'

		#Assign the attributes to the doctor object 
		temp_doctor_object.doctor_first_name = "Katelyn"
		temp_doctor_object.doctor_last_name = "Duffy"
		temp_doctor_object.doctor_type = "Gynecologist"

		pprint (vars(temp_doctor_object))

		print '\n\n\nDOCTOR HAS BEEN CREATED AND SENT SUCCESSFULLY\n\n\n'

		return temp_doctor_object

	#Test the creation of a patient
	def testPatientCreation(self):

		temp_patient_object = TempPatientData.objects.create()

		#Create the user to append into the model
		temp_patient_object.user = User.objects.create(username="johnson", email="johnson@johnson.com", password="johnson")
		print 'Temporary Patient Created Successfully!'

		#Assign the attributes that are associated with the user
		temp_patient_object.first_name = "Ryan"
		temp_patient_object.last_name = "Schachte"
		temp_patient_object.DOB = "2201995"
		temp_patient_object.ssn = "600489139"
		temp_patient_object.allergies = "NONE"
		temp_patient_object.address = "2463 E. Mallory Dr. Tempe, AZ 85281"
		temp_patient_object.medications = "NONE"
		temp_patient_object.insurance_provider = "Allstate"
		temp_patient_object.insurance_policy_number = "19938343434"
		temp_patient_object.email_address = "johnson@johnson.com"
		temp_patient_object.data_sent = "1"

		#Save user into the test database
		temp_patient_object.save()

		print 'Application Submitted, now testing creation of an approved patient by HSP staff'

		approved_patient = Patient.objects.create()
		approved_patient.user = temp_patient_object.user
		approved_patient.fill_from_application = temp_patient_object
		approved_patient.approval = 1
		approval = approved_patient.approval

		#Testing to ensure the object data from temp patient filtered down into the approved patient
		self.assertEqual(approved_patient.user.username, temp_patient_object.user.username)
		self.assertEqual(approved_patient.fill_from_application.DOB, "2201995")
		self.assertEqual(approval, 1)

		print '\n\n\nThe patient has been approved succesfully!\n\n\n'


	# #Test the update of health condition
	# def testUpdateHealthConditions(self):





	# #Test the creation of a an appointment
	# def testPatientAppoitmentSchedule(self):






# #This class will also contain the list of names of the doctors who work for the hospital
# class Doctor(models.Model):
# 	# doctor_name = models.CharField(max_length=256, choices=[('Dr. Schachte', 'Dr. Schachte'), ('Dr. Schachte', 'Dr. Huffy')], default="DEFAULT")
# 	doctor_first_name = models.CharField(max_length=256, default="")
# 	doctor_last_name = models.CharField(max_length=256, default="")
# 	doctor_type = models.CharField(max_length=256, choices=[('Gynecologist', 'Gynecologist'), ('Neuro', 'Neuro')], default="Select Doctor Type") 
	
# 	def __unicode__(self):
# 		return "Dr. " + str(self.doctor_last_name)


