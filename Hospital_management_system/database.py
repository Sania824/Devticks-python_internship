import sqlite3
from sqlite3 import Error

# from Hospital_management_system.main import search_id


def init_db():
    conn = None
    try:
        conn = sqlite3.connect("hospital.db")
        cursor = conn.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS patients(
            patient_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INT,
            gender TEXT,
            phone TEXT,
            disease TEXT
            )"""
        )

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS doctors(
           doctor_id TEXT PRIMARY KEY,
           name TEXT NOT NULL,
           age INT,
           gender TEXT,
           phone TEXT,
           email TEXT,
           specialization TEXT
           )"""
        )

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS appointments(
            apt_id TEXT PRIMARY KEY,
            patient_id TEXT,
            doctor_id TEXT,
            apt_date TEXT,
            apt_time TEXT,
            FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
            FOREIGN KEY(doctor_id) REFERENCES doctors(doctor_id))"""
        )

        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users(
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
        )"""
        )

        # cursor.execute('''
        #     INSERT OR IGNORE INTO users VALUES ('admin', 'admin123', 'admin')
        #     ''')

        conn.commit()
    except Error as e:
        print(f"Database Error: {e}")
    finally:
        if conn:
            conn.close()


def add_patients(patient_id, name, age, gender, phone, disease):
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO patients(patient_id, name, age, gender, phone, disease)
    VALUES(?,?,?,?,?,?)""", (patient_id, name, age, gender, phone, disease))
    conn.commit()
    conn.close()

def get_patients():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM patients""")
    patients = cursor.fetchall()
    conn.close()
    return patients

def search_patient(patient_id):
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * from patients WHERE patient_id = ?""", (patient_id,))
    patient = cursor.fetchone()
    conn.close()
    return patient

def delete_patient(patient_id):
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM patients WHERE patient_id = ?""", (patient_id,))
    patient = cursor.fetchone()
    if not patient:
        conn.close()
        return False

    cursor.execute("""DELETE from patients WHERE patient_id = ?""", (patient_id,))
    cursor.execute("""DELETE FROM appointments WHERE patient_id = ?""", (patient_id,))
    conn.commit()
    conn.close()
    return True
# def delete_patient(patient_id):
#     conn = sqlite3.connect('hospital.db')
#     cursor = conn.cursor()
#
#     # First check if patient exists
#     cursor.execute("SELECT * FROM patients WHERE patient_id = ?", (patient_id,))
#     patient = cursor.fetchone()
#
#     if not patient:
#         conn.close()
#         return False  # Patient doesn't exist
#
#     # Delete the patient
#     cursor.execute("DELETE FROM patients WHERE patient_id = ?", (patient_id,))
#
#     # Also delete related appointments (to maintain referential integrity)
#     cursor.execute("DELETE FROM appointments WHERE patient_id = ?", (patient_id,))
#
#     conn.commit()
#     conn.close()
#     return True  # Successfully deleted


    return True

def add_doctors(doctor_id, name, age, gender, phone, email, specialization):
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO doctors(doctor_id, name, age, gender, phone, email, specialization)
    VALUES(?,?,?,?,?,?,?)""", (doctor_id, name, age, gender, phone, email, specialization))
    conn.commit()
    conn.close()

def get_doctors():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM doctors""")
    doctors = cursor.fetchall()
    conn.close()
    return doctors

def search_doctor(doctor_id):
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * from doctors WHERE doctor_id = ?""", (doctor_id,))
    doctor = cursor.fetchone()
    conn.close()
    return doctor

def add_appointments(apt_id, patient_id, doctor_id, apt_date, apt_time):
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO appointments(apt_id, patient_id, doctor_id, apt_date, apt_time)
    VALUES(?,?,?,?,?)""", (apt_id, patient_id, doctor_id, apt_date, apt_time))
    conn.commit()
    conn.close()

def get_appointments():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM appointments""")
    appointments = cursor.fetchall()
    conn.close()
    return appointments

def get_patient_appointment(patient_id):
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM appointments WHERE patient_id = ?""", (patient_id,))
    apts = cursor.fetchall()
    conn.close()
    return apts

def search_appointment(apt_id):
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * from appointments WHERE apt_id = ?""", (apt_id,))
    apts = cursor.fetchone()
    conn.close()
    return apts

def check_user(username, password):
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM users WHERE username=? AND password=?""", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user  # Returns (username, password, role) if valid

def add_user(username, password):
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO users (username, password) VALUES (?,?)""", (username, password))
    conn.commit()
    conn.close()
    # return user  # Returns (username, password, role) if valid