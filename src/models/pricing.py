"""
Model pricing
"""
from sqlmodel import Field
from src.models.base import BaseDBModel

class PricingDB(BaseDBModel,table=True):
    price : int = Field(default=0) 