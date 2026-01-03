import re 
medical_records=[
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 20,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304'
    }
]

def invalid_records(patient_id,age,gender,diagnosis,medications,last_visit_id):
    conditions={
        "patient_id":isinstance(patient_id,str) and re.fullmatch("p\\d+",patient_id,re.IGNORECASE),
        "age":isinstance(age,int) and age>18,
        "gender": isinstance(gender,str) and gender.lower() in ("male","female"),
        "diagnosis":isinstance(diagnosis,str) or diagnosis is None,
        "medications":isinstance(medications,list) and all([isinstance(i,str) for i in medications]),
        "last_visit_id": isinstance(last_visit_id,str) and re.fullmatch("v\\d+",last_visit_id,re.IGNORECASE)
    }
    return [key for key,value in conditions.items() if not value]

def validation(records):
    is_invalid=False
    if not isinstance(records,(list,tuple)):
        print ("Invalid format: expected a list or tuple.")
        is_invalid=True
        return False
    
    key_sets=set(["patient_id","age","gender","diagnosis","medications","last_visit_id"])

    for idx,patients in enumerate(records):
        if not isinstance(patients,dict):
            print(f"Invalid format: expected a dictionary at index {idx}:{patients}")
            is_invalid=True
            return False

        if set(patients.keys())!=key_sets:
            print(f"Invalid format: {patients} at position {idx} has missing and/or invalid keys.")
            is_invalid=True
            return False
        
        invalid=invalid_records(**patients)
        for key in invalid:
            val=patients[key]
            print(f"Unexpected format '{key}:{val}' at position {idx}")
            is_invalid=True
            return False
        
    if is_invalid is False:
        print("Records are Valid.")
        return True
        

validation(medical_records)