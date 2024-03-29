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
    
    def book_appointment(self, patient_id, doctor_type="General"):
        if patient_id not in self.patients:
            print(f"Patient {patient_id} is not registered.")
        else:
            print(f"Appointment booked for patient {patient_id} with {doctor_type} Doctor.") 
    
    def place_in_queue(self, patient_id):
        if patient_id not in self.patients:
            print(f"Patient {patient_id} is not registered.")
        elif patient_id in self.queue:
            print(f"Patient {patient_id} is already in the queue.")
        else:
            self.queue.append(patient_id)
            print(f"Patient {patient_id} has been placed in the queue.")
   
    def send_notification(self, patient_id):
        if patient_id in self.queue:
            queue_status = self.queue.index(patient_id) + 1
            print(f"Notification sent to patient {patient_id}. Queue status: {queue_status}")
        else:
            print(f"Patient {patient_id} is not in the queue.")

    def track_queue_and_allocate_resources(self):
        if not self.queue:
            print("The queue is empty.")
        else:
            for i, patient_id in enumerate(self.queue):
                self.resources[patient_id] = "Resource Allocated"
                print(f"Tracking Queue: Patient {patient_id} is number {i+1} in the queue.")
    
    def ask_payment_method(self, patient_id):
        payment_method = input(f"Enter payment method for patient {patient_id}: ")
        print(f"Payment method {payment_method} recorded for patient {patient_id}.")

# Create an instance of the HealthcareSystem class
healthcare_system = HealthcareSystem()

# Call the prompt_patient_registration method to prompt the user for patient information
healthcare_system.prompt_patient_registration()

# Call the book_appointment method to book an appointment for the registered patient
patient_id = input("Enter patient ID to book appointment: ")
healthcare_system.book_appointment(patient_id)

# Call the place_in_queue method to place the registered patient in the queue
patient_id_queue = input("Enter patient ID to place in the queue: ")
healthcare_system.place_in_queue(patient_id_queue)

# Call the send_notification method to send a notification to a patient in the queue
patient_id_notification = input("Enter patient ID to send notification: ")
healthcare_system.send_notification(patient_id_notification)

# Call the track_queue_and_allocate_resources method to track the queue and allocate resources
healthcare_system.track_queue_and_allocate_resources()

