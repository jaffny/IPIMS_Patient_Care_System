from django.test import TestCase
from .models import Patient,TempPatientData
#create a patient (we need this in order to get to information registration stage)
class PatientRegisterTestCase(TestCase):
    def test_setup(self):
        patient = Patient.objects.create(
        phone_number=4805555555,
        email_address="email@example.com",
        #user=
        approved=1,
        )
        patient.save()
class PatientDataTestCase(TestCase):
    def test_create_setup(
        self,
        first_name = "bob",
        last_name="saget",
        phone_number=1234567890,
        DOB=11171992,
        ssn=123125678,
        allergies="peanuts",
        address="123 S. Fake St.",
        medications="none",
        insurance_provider="Aetna",
        #insurance_policy_number=258,
        ):
        temp = TempPatientData.objects.create(
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        DOB=DOB,
        ssn=ssn,
        allergies=allergies,
        address=address,
        medications=medications,
        insurance_provider=insurance_provider,
        #insurance_policy_number=insurance_policy_number
        )
        temp.save()
    def test_obj_exist(self):
        w = self.test_create_setup()
        self.assertTrue(isinstance(w, TempPatientData))
'''
# registration test, the entry is test. assert equal is used to see if the database and inserted attribute values match
    def test_data_entry(self):
        firstname = TempPatientData.objects.filter(first_name="bob")
        self.assertEqual(firstname,"bob")
        lastname = TempPatientData.objects.filter(last_name="saget")
        self.assertEqual(lastname,"saget")
        phone = TempPatientData.objects.filter(phone_number=1234567890)
        self.assertEqual(phone,1234567890)
        dateofbirth = TempPatientData.objects.filter(DOB=11171992)
        self.assertEqual(dateofbirth,11171992)
        socialsecuritynumber = TempPatientData.objects.filter(ssn=123125678)
        self.assertEqual(socialsecuritynumber,123125678)
        address = TempPatientData.objects.filter(address="123 S. Fake St.")
        self.assertEqual(address,"123 S. Fake St.")
        medications = TempPatientData.objects.filter(medications="none")
        self.assertEqual(medications,"none")
        insuranceProvider = TempPatientData.objects.filter(insurance_provider="Aetna")
        self.assertEqual(insuranceProvider,"Aetna")
        policynumber = TempPatientData.objects.filter(insurance_policy_number=258)
        self.assertEqual(policynumber,258)'''
