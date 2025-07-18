"""
This script defines two Pydantic models: Address and Patient.
It demonstrates how to nest one model (Address) within another (Patient).
The models validate and serialize structured data using type annotations.
An Address instance is created using a dictionary of values.
A Patient instance is then created using that Address object.
Finally, it accesses and prints the type of the model's dump method.
"""

from pydantic import BaseModel


class Address(BaseModel):

    city: str
    state: str
    pin: str


class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address


address_dict = {"city": "gurgaon", "state": "haryana", "pin": "122001"}

address1 = Address(**address_dict)

patient_dict = {"name": "nitish", "gender": "male", "age": 35, "address": address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump

print(type(temp))


# Better organization of related data (e.g., vitals, address, insurance)

# Reusability: Use Vitals in multiple models (e.g., Patient, MedicalRecord)

# Readability: Easier for developers and API consumers to understand

# Validation: Nested models are validated automatically—no extra work needed
