# Cell 3: BloodBank Class
class BloodBank:
    @staticmethod
    def donor_details(name, age, gender, blood_type, weight, disease):
        db_query("""
            INSERT INTO donor (donor_name, donor_age, donor_gender, donor_blood_type, donor_weight, donor_disease)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, age, gender, blood_type, weight, disease))

    @staticmethod
    def request_blood(hospital_name, patient_name, patient_age, patient_gender, patient_blood_type,
                      patient_weight, patient_disease, donor_name, donor_age, donor_gender, donor_blood_type):
        db_query("""
            INSERT INTO request (hospital_name, patient_name, patient_age, patient_gender,
                                 patient_blood_type, patient_weight, patient_disease,
                                 donor_name, donor_age, donor_gender, donor_blood_type)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (hospital_name, patient_name, patient_age, patient_gender, patient_blood_type,
              patient_weight, patient_disease, donor_name, donor_age, donor_gender, donor_blood_type))

        BloodBank.donor_details(donor_name, donor_age, donor_gender, donor_blood_type, patient_weight, patient_disease)
        Inventory.add_blood(donor_blood_type)
        Inventory.deduct_blood(patient_blood_type)
