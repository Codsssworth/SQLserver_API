from . import app
from flask import request,make_response
from .models import Person
import jwt
from datetime import datetime

@app.get("/")
def home():
    return "hello world"