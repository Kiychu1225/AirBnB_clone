#!/usr/bin/python3
"""
Place Class definition
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Defines the Place model"""

    city_id = ""           # City ID associated with the place
    user_id = ""           # User ID associated with the place
    name = ""              # Name of the place
    description = ""       # Description of the place
    number_rooms = int(0)  # Number of rooms in the place
    number_bathrooms = int(0)  # Number of bathrooms in the place
    max_guest = int(0)     # Maximum number of guests allowed
    price_by_night = int(0)  # Price per night for the place
    latitude = float(0.0)  # Latitude coordinate of the place
    longitude = float(0.0)  # Longitude coordinate of the place
    amenity_ids = [""]     # List of amenity IDs associated with the place

