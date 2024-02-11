#!/usr/bin/python3
"""
Review Class definition
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines the Review model"""

    place_id = ""  # ID of the place associated with the review
    user_id = ""   # ID of the user who created the review
    text = ""      # Text content of the review

