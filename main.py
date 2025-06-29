"""
FastAPI app that exposes a simple root endpoint returning a greeting message.
GET /
    Returns a simple greeting message as a JSON response.

    Returns:
        dict: A dictionary containing a welcome message.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message': 'Hello World'}