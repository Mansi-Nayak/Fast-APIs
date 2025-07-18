"""
This script defines a `Patient` data model using Pydantic for input validation.
It captures details like name, email, age, weight, height, marital status,
allergies, and contact information. It also includes a computed BMI field.
A function `update_patient_data` prints selected patient attributes and BMI.
The script creates a sample patient from a dictionary and passes it to the 
function.Pydantic ensures proper data type coercion and validation for the 
inputs.This structure supports easy and safe handling of patient health 
records.
"""

from typing import Dict, List

from pydantic import BaseModel, EmailStr, computed_field


class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float  # kg
    height: float  # mtr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2), 2)
        return bmi


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print("BMI", patient.bmi)
    print("updated")


patient_info = {
    "name": "nitish",
    "email": "abc@icici.com",
    "age": "65",
    "weight": 75.2,
    "height": 1.72,
    "married": True,
    "allergies": ["pollen", "dust"],
    "contact_details": {"phone": "2353462", "emergency": "235236"},
}

patient1 = Patient(**patient_info)

update_patient_data(patient1)
