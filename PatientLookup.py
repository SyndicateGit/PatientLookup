"""
This program keep track of patient history and searches patients based on MRN, name, DOB on an Excel file.
"""

# Installed openpyxl library for read/write Excel 2010 files
# https://openpyxl.readthedocs.io/en/stable/ Documentation for openpyxl
from datetime import datetime

current_year = datetime.now().year
current_month = datetime.now().month
current_day = datetime.now().day

print(f"Today is {current_day}-{current_month}-{current_year}")


class Patient:  # Patient class
    """
    Patient should have first and last name, mrn, dob, and optional medical history
    dob type: string; format: dd-mm-yyyy
    mrn type: int
    first name type: string
    last name type: string
    history type: string
    """

    def __init__(self, mrn, last_name, first_name, dob, history=None):
        self.last_name = last_name
        self.first_name = first_name
        self.mrn = mrn
        self.dob = dob
        self.history = history

    def calculate_age(self):  # This function calculates patient's age based on dob (dd-mm-yyyy) and current date
        dob_day, dob_month, dob_year = self.dob.split("-")
        age = current_year - int(dob_year) - ((current_month, current_day) < (int(dob_month), int(dob_day)))
        # If current,month date < dob month,date subtract 1 from age^
        if age < 0:
            return "Error: Age out of bound"
        return age




