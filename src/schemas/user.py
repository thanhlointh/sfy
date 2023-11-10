"""
Schema user
"""

from pydantic import BaseModel,EmailStr

class UserCreateSchema(BaseModel):
    nick_name : str | None = None
    first_name : str | None = None
    last_name : str | None = None
    phone_number : str | None = None
    email : EmailStr
    address : str | None = None
    descriptions: str | None = None


class UserReadSchema(UserCreateSchema):
    pass

class UserUpdateSchema(UserReadSchema):
    pass

class UserDeleteSchema(BaseModel):
    pass