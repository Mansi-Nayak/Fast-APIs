"""
FastAPI-based Patient Management System API.

This application provides endpoints to:
- Display a welcome message
- Provide an about message for the API
- Load and view patient records stored in a local JSON file (`patient.json`)
"""

from fastapi import FastAPI
import json

app = FastAPI()


def load_data():
    with open('patient.json', 'r') as f:
        data = json.load(f)
    return data


@app.get("/")
def hello():
    return {'message': 'Patient Management System API'}


@app.get('/about')
def about():
    return {'message': 'A fully functional API to manage your patient records'}


@app.get('/view')
def view():
    data = load_data()

    return data