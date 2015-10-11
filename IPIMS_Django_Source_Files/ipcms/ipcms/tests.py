#to execute test, use 'python tests.py'

import unittest


class RegistrationInfoTest(unittest.TestCase):
    #registration information functionality
    def test_one_plus_one(self):
        assert 1 + 1 == 2

class ScheduleAppointmentTest(unittest.TestCase):
    #registration information functionality
    def test_one_plus_one(self):
        assert 1+1==2

class updateHealthcareConditionsTest(unittest.TestCase):
    #update healthcare conditions functionality
    def test_one_plus_one(self):
        assert 1+1==2

if __name__ == '__main__':
    unittest.main()
