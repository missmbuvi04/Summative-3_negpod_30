#!/usr/bin/python3

class HealthcareSystem:
    def init(self):
        self.patients = {}
        self.queue = []
        self.resources = {}

    # 1. Lungile's function
    def register_and_check_in_patient(self, patient_id, patient_info):
        if patient_id in self.patients:
            print(f"Patient {patient_id} is already registered.")
        else:
            self.patients[patient_id] = patient_info
            print(f"Patient {patient_id} has been registered and checked in.")

    # 2. Alice's function
    def book_appointment(self, patient_id, doctor_type="General"):
        if patient_id not in self.patients:
            print(f"Patient {patient_id} is not registered.")
        else:
            print(f"Appointment booked for patient {patient_id} with {doctor_type} Doctor.")

    # 3. Tashinga's function
    def place_in_queue(self, patient_id):
        if patient_id not in self.patients:
            print(f"Patient {patient_id} is not registered.")
        elif patient_id in self.queue:
            print(f"Patient {patient_id} is already in the queue.")
        else:
            self.queue.append(patient_id)
            print(f"Patient {patient_id} has been placed in the queue.")

    # 4. David's function
    def send_notification(self, patient_id):
        if patient_id not in self.queue:
            print(f"Patient {patient_id} is not in the queue.")
        else:
            queue_status = self.queue.index(patient_id) + 1
            print(f"Notification sent to patient {patient_id}. Queue status: {queue_status}")

    # 5. Maureen's function
    def track_queue_and_allocate_resources(self):
        if not self.queue:
            print("The queue is empty.")
        else:
            for i, patient_id in enumerate(self.queue):
                self.resources[patient_id] = "Resource Allocated"
                print(f"Tracking Queue: Patient {patient_id} is number {i+1} in the queue.")

    # 6. Given's function
    def ask_payment_method(self):
        payment_method = input("Please enter your preferred payment method (card, insurance, cash): ")
        if payment_method not in ["card", "insurance", "cash"]:
            print("Invalid payment method. Please enter either 'card', 'insurance', or 'cash'.")
        else:
            print(f"You have selected {payment_method} as your payment method.")
