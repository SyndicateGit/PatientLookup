"""
Unit Testing for MedicalFiles.
"""
import unittest
import PatientLookup  # Module we want to test
from datetime import datetime
current_year = datetime.now().year
current_month = datetime.now().month
current_day = datetime.now().day
class TestMedicalFiles(unittest.TestCase):
    """
    TestCase class provides assert methods to check for and report failures.
    https://docs.python.org/3/library/unittest.html doc for unnit test framework
    https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug doc for assert methods

    """

    def test_calculate_age(self):  # Tests calculate_age function in MedicalFiles, needs test_ in name to run as test
        result = PatientLookup.calculate_age("01-01-1998")  # Calls calculate age function from PatientLookup
        result2 = PatientLookup.calculate_age("31-12-1998")
        age = current_year - 1998 - ((current_month, current_day) < (1,1))
        age2 = current_year - 1998 - ((current_month, current_day) < (31,12))
        self.assertEqual(result, age)
        self.assertEqual(result2, age2)


if __name__ == '__main__':  # This makes it so it's only run if you're running this file specifically.
    unittest.main()