"""City model that inherits the base model"""

from models.base_model import BaseModel


class City(BaseModel):
    """creates new city model"""
    state_id = ""
    name = ""
