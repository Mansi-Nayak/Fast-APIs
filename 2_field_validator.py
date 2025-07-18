"""
This script defines a `Patient` model using Pydantic with custom field 
validations.It ensures the email belongs to specific domains and transforms 
the name to uppercase.It also validates that age is between 1 and 99.  
Validated patient data is then printed using the `update_patient_data` 
function.
"""

from typing import Dict, List

from pydantic import BaseModel, EmailStr, field_validator


class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator("email")
    @classmethod
    def email_validator(cls, value):

        valid_domains = ["hdfc.com", "icici.com"]
        # abc@gmail.com
        domain_name = value.split("@")[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")

        return value

    @field_validator("name")
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator("age", mode="after")
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Age should be in between 0 and 100")


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print("updated")


patient_info = {
    "name": "nitish",
    "email": "abc@icici.com",
    "age": "30",
    "weight": 75.2,
    "married": True,
    "allergies": ["pollen", "dust"],
    "contact_details": {"phone": "2353462"},
}

patient1 = Patient(**patient_info)  # validation -> type coercion

update_patient_data(patient1)
