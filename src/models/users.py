"""
Model user
"""
from sqlmodel import Field
from src.models.base import BaseDBModel

class UsersDB(BaseDBModel,table=True):
    """
    User Model
    """
    nick_name : str  = Field(default="Anonymous",unique=True,description=" Nick name of user")
    first_name : str = Field(nullable=False, description="First name of user")
    last_name : str= Field(nullable=False, description="Last name of customer")
    phone_number : str | None = Field(default=None, nullable=True, description="Phone number of user")
    email : str  = Field(nullable=False,unique=True,description="Email of user")
    address : str | None = Field(nullable=True,default=None,description="Address of User")
    descriptions: str | None = Field(default=None ,description="Description of user")


