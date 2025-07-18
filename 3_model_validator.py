"""
This code defines a `Patient` model using Pydantic with strict field typing 
and validation.It includes fields like name, email, age, weight, marital 
status, allergies, and contact details.A custom `model_validator` ensures 
patients over 60 have an emergency contact listed.The validator runs after the 
full model is initialized.Type coercion is applied when instantiating the 
model using dictionary data.If validation passes, patient data is printed via 
`update_patient_data`.This ensures both field-level and model-level data 
integrity.
"""

from typing import Dict, List

from pydantic import BaseModel, EmailStr, model_validator


class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode="after")
    def validate_emergency_contact(cls, model):
        if model.age > 60 and "emergency" not in model.contact_details:
            raise ValueError("Patients older than 60 must have an emergency contact")
        return model


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print("updated")


patient_info = {
    "name": "nitish",
    "email": "abc@icici.com",
    "age": "65",
    "weight": 75.2,
    "married": True,
    "allergies": ["pollen", "dust"],
    "contact_details": {"phone": "2353462", "emergency": "235236"},
}

patient1 = Patient(**patient_info)

update_patient_data(patient1)
