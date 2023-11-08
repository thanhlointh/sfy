"""
Base model
"""
import re
from functools import partial
from uuid import UUID,uuid4
from typing import Annotated
from sqlalchemy.orm import declared_attr
from sqlmodel import Field, SQLModel

_snake_1 = partial(re.compile(r"(.)((?<![^A-Za-z])[A-Z][a-z]+)").sub, r"\1_\2")
_snake_2 = partial(re.compile(r"([a-z0-9])([A-Z])").sub, r"\1_\2")


def snake_case(string: str) -> str:
    """
    snake_case Snake casing

    Transform camel case to snake case

    Arguments:
        string -- camel case string

    Returns:
        snake case string
    """
    return _snake_2(_snake_1(string)).casefold()

class BaseDBModel(SQLModel):
    
    @declared_attr  # type: ignore
    def __tablename__(cls) -> str:
        return snake_case(cls.__name__.replace("DB", ""))
    
    id : UUID | None = Field(default_factory=uuid4,primary_key=True)

    
