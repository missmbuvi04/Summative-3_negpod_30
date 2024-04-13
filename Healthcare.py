from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import mysql.connector
from datetime import datetime

class HealthcareSystem:
    def __init__(self):
        self.conn = mysql.connector.connect(
            # host="localhost",
            # user="missmbuvi",
            # password="mypassword",
            # database="healthcare_system_db"
            host="localhost",
            user="missmbuvi",
            password="mypassword",
            database="healthcare_system_db"
        )
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                patient_id INT AUTO_INCREMENT ,
                name VARCHAR(255),
                gender ENUM('Male', 'Female', 'Other')
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                appointment_id INT AUTO_INCREMENT PRIMARY KEY,
                patient_id INT,
                doctor_name VARCHAR(255),
                appointment_date DATE,
                appointment_type VARCHAR(50),
                payment_method VARCHAR(50),
                FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
            )
        """)
        self.conn.commit()

    def prompt_patient_registration(self):
        patient_name = input("Enter patient name: ")
        gender = input("Enter patient gender (Male/Female/Other): ").capitalize()
        self.register_patient(patient_name, gender)

    def register_patient(self, name, gender):
        try:
            sql = "INSERT INTO patients (name, gender) VALUES (%s, %s)"
            val = (name, gender)
            self.cursor.execute(sql, val)
            self.conn.commit()
            print("Patient registered successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def book_appointment(self, patient_id, doctor_name, appointment_type):
        try:
            appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
            payment_method = input("Enter payment method: ")
            sql = "INSERT INTO appointments (patient_id, doctor_name, appointment_date, appointment_type, payment_method) VALUES (%s, %s, %s, %s, %s)"
            val = (patient_id, doctor_name, appointment_date, appointment_type, payment_method)
            self.cursor.execute(sql, val)
            self.conn.commit()
            print("Appointment booked successfully!")
            email_body = f"An appointment has been booked for {appointment_date} with Dr. {doctor_name}. Type: {appointment_type}. Payment method: {payment_method}."
            self.send_email("givenality@gmail.com", "Appointment Confirmation", email_body)
        except mysql.connector.Error as err:
            print(f"Error: {err}")

            
        

    def send_email(self, recipient, subject, body):
        try:
            s = smtplib.SMTP(host='mtabeapp.com', port=587)
            s.starttls()
            s.login('given@mtabeapp.com', 'C0mf1rM3DL8rBr0!')
            msg = MIMEMultipart()
            msg['From'] = 'gedward15@alustudent.com'
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            s.send_message(msg)
            s.quit()
            print("Email sent successfully!")
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")

# Create an instance of the HealthcareSystem class
healthcare_system = HealthcareSystem()

# Prompt patient registration
healthcare_system.prompt_patient_registration()

# Book an appointment
patient_id = int(input("Enter patient ID: "))  # Assuming patient ID is already available
doctor_name = input("Enter doctor's name: ")
appointment_type = input("Enter appointment type: ")
healthcare_system.book_appointment(patient_id, doctor_name, appointment_type)

