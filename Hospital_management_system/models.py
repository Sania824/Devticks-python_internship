"""models.py file code """

# models.py

class Patient:
    def __init__(self, patient_id, name, age, gender, phone, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.disease = disease

class Doctors:
    def __init__(self, doctor_id, name, age, gender, phone, email, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.email = email
        self.specialization = specialization

class Appointments:
    def __init__(self, apt_id, patient_id, doctor_id, apt_date, apt_time):
        self.apt_id = apt_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.apt_date= apt_date
        self.apt_time = apt_time

