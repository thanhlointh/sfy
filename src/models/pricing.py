"""
Model pricing
"""
from typing import Union
from sqlmodel import Field
from src.models.base import BaseDBModel

class PricingModel(BaseDBModel,table=True):
    price : int = Field(default=0) 