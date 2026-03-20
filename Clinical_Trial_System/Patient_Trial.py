class TrialSubject:

    def __init__(self, first, last, age, blood_type):
        self.first = first
        self.last = last
        self.age = age
        self.blood_type = blood_type

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def patient_id(self):
        return f'{self.first[0]}{self.last}{self.age}'

    @classmethod
    def from_csv_string(cls, subject_str):
        first, last, age, blood_type = subject_str.split('-')
        return cls(first, last, age, blood_type)

    def __str__(self):
        return f'Subject: {self.fullname()} {self.age} '

    def __repr__(self):
        return "TrialSubject('{}', '{}', '{}', '{}')".format(self.first, self.last, self.age, self.blood_type)


class PlaceboGroup(TrialSubject):

    def __init__(self, first, last, age, blood_type):
        super().__init__(first, last, age, blood_type)
        self.treatment_status = "Placebo (Sugar Pill)"


class ActiveGroup(TrialSubject):

    def __init__(self, first, last, age, blood_type, dosage_mg):
        super().__init__(first, last, age, blood_type)
        self.dosage_mg = dosage_mg

    def adjust_dose(self, amount):
        self.dosage_mg += amount
        return f'ALERT: {self.fullname()} dosage adjusted to {self.dosage_mg}mg'


if __name__ == '__main__':
    # --- FINAL SYSTEM TEST ---

    # 1. Spawn the Patients
    patient_1 = PlaceboGroup("Arthur", "Morgan", 35, "O-")
    patient_2 = ActiveGroup("Eren", "Yeager", 19, "A+", 50)

    # 2. Test the Placebo Automation
    print(f"Patient 1 ID: {patient_1.patient_id}")
    print(f"Status: {patient_1.treatment_status}")
    print("-" * 30)

    # 3. Test the Active Group Math
    print(f"Patient 2 ID: {patient_2.patient_id}")
    print(f"Starting Dose: {patient_2.dosage_mg}mg")
    print(patient_2.adjust_dose(25))
