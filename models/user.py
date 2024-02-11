#!/usr/bin/python3
"""
User Class definition
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines the User model"""

    email = ""       # Email address of the user
    password = ""    # Password of the user
    first_name = ""  # First name of the user
    last_name = ""   # Last name of the user

