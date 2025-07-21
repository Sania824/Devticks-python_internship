import streamlit as st
from database import *
from models import Patient, Doctors, Appointments
from auth import login, register, logout

init_db()

# Initialize session state
if 'show_login' not in st.session_state:
    st.session_state.show_login = False  # Start with registration

# Show appropriate page
if not st.session_state.get('logged_in'):
    if st.session_state.show_login:
        login()
    else:
        register()
        st.markdown("Already have an account?")
        if st.button("Login instead"):
            st.session_state.show_login = True
            st.rerun()
    st.stop()  # Stop if not logged in

st.title("🏥 Hospital Management System")

menu = st.sidebar.selectbox(
    "Navigate", ["Patients", "Doctors", "Appointments"]
)

if menu == "Patients":
    option = st.radio("Select Option", ["➕ Add Patient", '✅ View Patient', '🔍 Search Patients', '👀 View Patient Appointment','❌ Delete Patient'])
    if option == '➕ Add Patient':
       st.header("Patient Management")
       with st.form('patient_form'):
         st.subheader('Add new patient')
         patient_id = st.text_input('Patient ID')
         name = st.text_input('Name')
         age = st.text_input('Age')
         gender = st.text_input('Gender')
         phone = st.text_input('Phone')
         disease = st.text_input('Disease')

         if st.form_submit_button("Save Patient"):
             add_patients(patient_id, name, age, gender, phone, disease)
             st.success('Patient Added Successfully')

    elif option == '✅ View Patient':
        st.subheader("All Patients")
        patients = get_patients()
        if patients:
           for p in patients:
               st.write(f"""
                    - ID: {p[0]}
                      - Name: {p[1]}
                      - Age: {p[2]}
                      - Gender: {p[3]}
                      - Phone: {p[3]}
                      - Disease: {p[4]}
                    """)
        else:
            st.info("No Patients Found")
    
    elif option == '🔍 Search Patients':
        st.header("🔍 Search Patient by ID")
        search_id = st.text_input("Enter Patient ID")

        if st.button("Search Patient"):
            patient = search_patient(search_id)

            if patient:
                st.success(f"""
                    Patient Found:
                    - ID: {patient[0]}
                    - Name: {patient[1]}
                    - Age: {patient[2]}
                    - Gender: {patient[3]}
                    - Phone: {patient[3]}
                    - Disease: {patient[4]}
                    """)
            else:
                st.error("Patient Not Found")

    # elif option == 'Delete Patient':
    #     st.header("Delete patient by ID")
    #     search_id = st.text_input("Enter Patient ID to delete")
    #
    #     if st.button('Delete Patient'):
    #         if not search_id:
    #             st.warning("Enter an ID")
    #         else:
    #             patient = search_patient(search_id)
    #             if patient:
    #                 st.write("This action can't be undone once implemented")
    #                 if st.button("Confirm Deletion"):
    #                     if delete_patient(search_id):
    #                         st.success("Patient Deleted Successfully")
    #                         st.rerun()
    #                     else:
    #                         st.error("Deletion Failed!")
    #             else:
    #                 st.error("Patient Not Found")

    # elif option == 'Delete Patient':
    #     st.header("Delete Patient by ID")
    #     search_id = st.text_input("Enter Patient ID to Delete")
    #
    #     if st.button('Delete Patient'):
    #         if not search_id:
    #             st.warning("Please enter a Patient ID")
    #         else:
    #             # First show confirmation
    #             patient = search_patient(search_id)
    #             if patient:
    #                 st.warning(f"""You are about to delete:
    #                 - Name: {patient[1]}
    #                 - Age: {patient[2]}
    #                 This action cannot be undone!""")
    #
    #                 if st.button("Confirm Deletion"):
    #                     if delete_patient(search_id):
    #                         st.success("Patient deleted successfully!")
    #                         st.rerun()  # Refresh the view
    #                     else:
    #                         st.error("Deletion failed")
    #             else:
    #                 st.error("No patient found with this ID")

    elif option == '❌ Delete Patient':
        st.header("Delete Patient")
        search_id = st.text_input("Enter Patient ID to Delete", key="delete_input")

        if st.button('Delete Patient', type="primary", key="delete_btn"):
            if not search_id.strip():
                st.warning("Please enter a valid Patient ID")
            else:
                patient = search_patient(search_id)
                if patient:
                    st.warning(f"""You are about to delete this patient:

                    **ID**: {patient[0]}  
                    **Name**: {patient[1]}  
                    **Age**: {patient[2]}  
                    **Gender**: {patient[3]}

                    *This action cannot be undone!*""")

                    # Confirmation step - this needs to be a separate button
                    if st.button("CONFIRM DELETION", type="secondary", key="confirm_delete"):
                        if delete_patient(search_id):
                            st.success("Patient deleted successfully!")
                            st.balloons()
                            st.experimental_rerun()  # Refresh the view
                        else:
                            st.error("Failed to delete patient")
                else:
                    st.error(f"No patient found with ID: {search_id}")

    elif option == '👀 View Patient Appointment':
        st.header("View Your Appointments")
        search_id = st.text_input("Enter the patient's ID")

        if st.button("View Appointment"):
            patient = get_patient_appointment(search_id)
            if patient:
                st.success(f"""
                 Appointment Found
                  - Appointment ID: {patient[0]}
""")
            else:
                st.info("No Appointments Found")

            # patient = delete_patient(search_id)
            #
            # if patient:
            #     st.success("Patient Deleted Successfully")
            # elif patient == None:
            #     st.info("No patient with the given ID")

elif menu == "Doctors":
    option = st.radio("Select Option", ["➕ Add Doctor", '✅ View Doctors', '🔍 Search Doctor'])
    if option == '➕ Add Doctor':
        st.header("Doctor Management")
        with st.form('doctor_form'):
            st.subheader('Add new doctor')
            doctor_id = st.text_input('Doctor ID')
            name = st.text_input('Name')
            age = st.text_input('Age')
            gender = st.text_input('Gender')
            phone = st.text_input('Phone')
            email = st.text_input('Email')
            specialization = st.text_input('Specialization')

            if st.form_submit_button("Save Doctor"):
                add_doctors(doctor_id, name, age, gender, phone, email, specialization)
                st.success('Doctor Added Successfully')

    elif option == '✅ View Doctors':
        st.subheader("All Doctors")
        doctors = get_doctors()
        if doctors:
            for p in doctors:
                st.write(f"""
                        - ID: {p[0]}
                          - Name: {p[1]}
                          - Age: {p[2]}
                          - Gender: {p[3]}
                          - Phone: {p[4]}
                          - Email: {p[5]}
                          - Specialization {p[6]}
                        """)
        else:
            st.info("No Doctors Found")

    elif option == '🔍 Search Doctor':
        st.header("🔍 Search Doctor by ID")
        search_id = st.text_input("Enter Doctor ID")

        if st.button("Search Doctor"):
            doctor = search_doctor(search_id)

            if doctor:
                st.success(f"""
                        Doctor Found:
                        - ID: {doctor[0]}
                        - Name: {doctor[1]}
                        - Age: {doctor[2]}
                        - Gender: {doctor[3]}
                        - Phone: {doctor[4]}
                        - Email: {doctor[5]}
                        - Specialization: {doctor[6]}
                        """)
            else:
                st.error("Doctor Not Found")

elif menu == 'Appointments':
    option = st.radio("Select Option", ["➕ Add Appointment", '✅ View Appointment', '🔍 Search Appointment'])
    if option == '➕ Add Appointment':
        st.header("Appointment Management")
        with st.form('apt_form'):
            st.subheader('Add new appointment')
            apt_id = st.text_input('Appointment ID')
            patient_id = st.text_input('Patient ID')
            doctor_id = st.text_input('Doctor ID')
            apt_date = st.date_input('Appointment Date')
            apt_time = st.text_input('Appointment Time')

            if st.form_submit_button("Save Appointment"):
                add_appointments(apt_id, patient_id, doctor_id, apt_date, apt_time)
                st.success('Appointment Added Successfully')

    elif option == '✅ View Appointment':
        st.subheader("All Appointment")
        apt = get_appointments()
        if apt:
            for p in apt:
                st.write(f"""
                            - Appointment ID: {p[0]}
                              - Patient ID: {p[1]}
                              - Doctor ID: {p[2]}
                              - Appointment Date: {p[3]}
                              - Appointment TIme: {p[4]}
                            """)
        else:
            st.info("No Appointments Found")

    elif option == '🔍 Search Appointment':
        st.header("🔍 Search Appointment by ID")
        search_id = st.text_input("Enter Appointment ID")

        if st.button("Search Appointment"):
            apt = search_appointment(search_id)

            if apt:
                st.success(f"""
                            Appointment Found:
                            - Appointment ID: {apt[0]}
                            - Patient ID: {apt[1]}
                            - Doctor ID: {apt[2]}
                            - Appointment Date: {apt[3]}
                            - Appointment Time: {apt[4]}
                            """)
            else:
                st.error("Appointment Not Found")

st.sidebar.button("Logout", on_click=logout)

# menu = st.sidebar.selectbox("Menu", ["Add Patient", "View Patients", "Search Patient"])
#
# # patients = load_patients()
#
# if menu == "Add Patient":
#     st.header("➕ Add New Patient")
#
#     patient_id = st.text_input("Patient ID")
#     name = st.text_input("Name")
#     age = st.number_input("Age", min_value=0, step=1)
#     disease = st.text_input("Disease")
#
#     if st.button("Save Patient"):
#         new_patient = Patient(patient_id, name, age, disease)
#         patients.append(new_patient)
#         save_patients(patients)
#         st.success("Patient added successfully!")
#
# elif menu == "View Patients":
#     st.header("📋 All Patients")
#
#     if not patients:
#         st.info("No patients found.")
#     else:
#         for p in patients:
#             st.write(f"🧑 ID: {p.patient_id}, Name: {p.name}, Age: {p.age}, Disease: {p.disease}")
#
# elif menu == "Search Patient":
#     st.header("🔍 Search Patient by ID")
#
#     search_id = st.text_input("Enter Patient ID")
#
#     if st.button("Search"):
#         found = next((p for p in patients if p.patient_id == search_id), None)
#         if found:
#             st.success(f"Patient Found: {found.name}, Age: {found.age}, Disease: {found.disease}")
#         else:
#             st.error("Patient not found.")