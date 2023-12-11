"""
Models
Module that contains the Picture model for storage in the database.
"""


class Picture:
    """
    Picture class representing a Picture stored in the database.
    Attributes:
        picture_id (uuid): The id of the picture
        url (str): The url of the picture
        event_country (str): The country of the event where the picture was taken
        event_state (str): The state of the event where the picture was taken
        event_city (str): The city of the event where the picture was taken
        event_date (str): format: "mm/dd/yyyy" The date when the picture was taken
    """

    def __init__(self, picture_id: uuid.UUID, url: str, event_country: str, event_state: str, event_city: str,
                 event_date: str):
        self.picture_id = picture_id
        self.url = url
        self.event_country = event_country
        self.event_state = event_state
        self.event_city = event_city
        self.event_date = event_date
