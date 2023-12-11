"""
Pictures Server
Module with the handlers for the basic CRUD operations.
"""
import uuid

from models import Picture


def get_all_pictures():
    """
    Function that returns the list of all pictures available in the database.
    returns - list with all the pictures stored
    """
    pass


def get_picture_by_id(picture_id: uuid.UUID):
    """
    Function that obtains the information of a picture from the database given its id.
    If the picture doesn't exist it will raise an error.
    returns - picture with the given id
    """
    pass


def create_picture(picture: Picture):
    """
    Function that creates a new picture and stores it into the database.
    param - picture - The picture to be stored in the database
    """
    pass


def update_picture(picture_id: uuid.UUID, picture: Picture):
    """
    Function that updates a picture that already exists in the database. If no picture exists
    It will raise an error.
    """
    pass


def delete_picture(picture_id):
    """
    Function that deletes a picture from the database. If the picture does not exist it will raise an error.
    """
    pass
