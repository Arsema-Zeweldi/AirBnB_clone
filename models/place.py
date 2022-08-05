#!/usr/bin/python3
""" Place Class """


from models.base_model import BaseModel


class Place(BaseModel):
    """ inherits BaseModel"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_of_rooms = 0
    number_of_bathrooms = 0
    max_no_guests = 0
    price_per_night = 0
    lat = 0.0
    lon = 0.0
    amenity_ids = []
