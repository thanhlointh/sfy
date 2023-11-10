"""
Generic get endpoint
Class GET:
include:
    - log
    - log database
    -
"""
from typing import List
from fastapi import APIRouter,Depends
from sqlmodel import SQLModel,Session
from .abstract import Router
from uuid import UUID,uuid4
from typing import TypeVar,Type
from pydantic import BaseModel
from src.models.db import UsersDB
from src.schemas.user import UserCreateSchema
from src.utils.db.session import get_session
SCHEMA = TypeVar("SCHEMA",bound='BaseModel')

DB = TypeVar("DB",bound="SQLModel")
class CREATE(Router):
    """
    GET
    """

    def __init__(self, api_router: APIRouter, path: str, methods: List[str], name: str,table:Type[DB]) -> None:
        super().__init__(api_router, path, methods, name,table)


    def router(self,obj_schema:Type[SCHEMA]):

        def endpoint_router(item: obj_schema, db: Session = Depends(get_session)):
            @self.wrapper_log
            def create():
                db_data = self._table.from_orm(item)
                db.add(db_data)
                db.commit()
                return item
            return create()

        self._api_router.add_api_route(
            endpoint=endpoint_router,
            path= self._path,
            methods=self._methods,
            name=self._name, 
        )
        
