"""
Generate auto crud endpoint:
    -GET: get data with uuid
    -POST: create new data
    -LIST: list all data with pagnations
    -DELETE: delete data wit uuid
    -Search: search data
"""
from typing import List
from fastapi import APIRouter
from sqlmodel import SQLModel
from pydantic import BaseModel
from .get import GET_ONE
from .post import CREATE
from .list import LIST
from typing import TypeVar, Type, Generic
from src.schemas.user import UserCreateSchema

DB = TypeVar("DB", bound="SQLModel")
SCHEMA = TypeVar("SCHEMA", bound="BaseModel")


class CRUD:
    def __init__(
        self,
        api_router: APIRouter,
        table: Type[DB],
        create: Type[SCHEMA],
        read: Type[SCHEMA],
        update: Type[SCHEMA],
        delete: Type[SCHEMA],
    ) -> None:
        self._api_router = api_router
        self._create = create
        self._read = read
        self._update = update
        self._delete = delete
        self._table = table

    def generate_crud(self):
        GET_ONE(api_router=self._api_router,
            path="/{uuid}",
            methods=["GET"],
            name="GET",
            table=self._table).router(None)
        CREATE(
            api_router=self._api_router,
            path="/",
            methods=["POST"],
            name="POST",
            table=self._table
        ).router(obj_schema=self._create)
        LIST(
            api_router=self._api_router,
            path="/",
            methods=["GET"],
            name="GET",
            table=self._table
        ).router(obj_schema=self._create)
