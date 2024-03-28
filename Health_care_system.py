#!/usr/bin/python3

class HealthcareSystem:
    def __init__(self):
        self.patients = {}
        self.queue = []
        self.resources = {}

    def prompt_patient_registration(self):
        patient_name = input("Enter patient name: ")
        patient_id = input("Enter patient ID: ")
        patient_info = {"name": patient_name}
        self.register_and_check_in_patient(patient_id, patient_info)

    def register_and_check_in_patient(self, patient_id, patient_info):
        if patient_id in self.patients:
            print(f"Patient {patient_id} is already registered.")
        else:
            self.patients[patient_id] = patient_info
            print(f"Patient {patient_id} has been registered and checked in.")

# Create an instance of the HealthcareSystem class
healthcare_system = HealthcareSystem()

# Call the prompt_patient_registration method to prompt the user for patient information
healthcare_system.prompt_patient_registration()
