"""
This script defines Address and Patient models using Pydantic.
The Patient model includes a default gender value ('Male').
It creates Address and Patient instances using dictionary unpacking.
Nested model validation is handled automatically by Pydantic.
The model_dump method is used to extract only explicitly set fields.
Finally, it prints the dumped data and its type.
"""

from pydantic import BaseModel


class Address(BaseModel):

    city: str
    state: str
    pin: str


class Patient(BaseModel):

    name: str
    gender: str = "Male"
    age: int
    address: Address


address_dict = {"city": "gurgaon", "state": "haryana", "pin": "122001"}

address1 = Address(**address_dict)

patient_dict = {"name": "nitish", "age": 35, "address": address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(exclude_unset=True)

print(temp)
print(type(temp))
