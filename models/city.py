#!/usr/bin/python3
"""
City Class definition
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines the City model"""

    state_id = ""  # State ID associated with the city
    name = ""      # Name of the city

