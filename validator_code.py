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
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]

def invalid_records(patient_id,age,gender,diagnosis,medications,last_visit_id):
    conditions={
        "patient_id":isinstance(patient_id,str) and re.fullmatch("p\d+",patient_id,re.IGNORECASE),
        "age":isinstance(age,int) and age>18,
        "gender": isinstance(gender,str) and gender.lower()==("male","female"),
        "diagnosis":isinstance(diagnosis,str) or diagnosis is None,
        "medications":isinstance(medications,list) and all[(isinstance(i,str) for i in medications)],
        "last_visit_id": isinstance(last_visit_id,str) and re.fullmatch("v\d+",last_visit_id,re.IGNORECASE)
    }
    return [key for key,value in conditions.items() if not value]
