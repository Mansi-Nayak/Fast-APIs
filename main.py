"""
FastAPI-based Patient Management System API.

This application provides endpoints to:
- Display welcome and about messages
- View all patient records stored in a JSON file
- View details of a specific patient using a path parameter
- Sort patient records based on fields like height, weight, or BMI using query 
  parameters

Data is loaded from a local JSON file `patient.json`.
"""

import json

from fastapi import FastAPI, HTTPException, Path, Query

app = FastAPI()


def load_data():
    with open("patient.json", "r") as f:
        data = json.load(f)
    return data


# Home


@app.get("/")
def hello():
    return {"message": "Patient Management System API"}


# About


@app.get("/about")
def about():
    return {"message": "A fully functional API to manage your patient records"}


# View


@app.get("/view")
def view():
    data = load_data()

    return data


# view specific patient


# @app.get('/patient/{patient_id}')
# def view_patient(patient_id: str):
#     # load all the patients
#     data = load_data()

#     if patient_id in data:
#         return data[patient_id]
#     return {'error': 'patient not found'}

# Path Parameter

# @app.get('/patient/{patient_id}')
# def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')):
#     # load all the patients
#     data = load_data()

#     if patient_id in data:
#         return data[patient_id]
#     return {'error': 'patient not found'}


@app.get("/patient/{patient_id}")
def view_patient(
    patient_id: str = Path(
        ..., description="ID of the patient in the DB", example="P001"
    )
):
    # load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")


# Sort using Query


@app.get("/sort")
def sort_patients(
    sort_by: str = Query(
        ..., description="Sort on the basis of " "height, weight or bmi"
    ),
    order: str = Query("asc", description="sort in asc or desc order"),
):

    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400, detail=f"Invalid field select from {valid_fields}"
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400, detail="Invalid order select between asc and desc"
        )

    data = load_data()

    sort_order = True if order == "desc" else False

    sorted_data = sorted(
        data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order
    )

    return sorted_data
