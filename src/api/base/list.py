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
from sqlmodel import SQLModel,Session,select
from .abstract import Router
from uuid import UUID,uuid4
from typing import TypeVar,Type
from pydantic import BaseModel
from src.models.db import UsersDB
from src.schemas.user import UserCreateSchema
from src.utils.db.session import get_session
SCHEMA = TypeVar("SCHEMA",bound='BaseModel')

DB = TypeVar("DB",bound="SQLModel")
class LIST(Router):
    """
    GET
    """

    def __init__(self, api_router: APIRouter, path: str, methods: List[str], name: str,table:Type[DB]) -> None:
        super().__init__(api_router, path, methods, name,table)


    def router(self,obj_schema:Type[SCHEMA]):

        def endpoint_router(db: Session = Depends(get_session)):
            @self.wrapper_log
            def list_items():
                items = db.exec(select(self._table)).all()
                return items
            return list_items()

        self._api_router.add_api_route(
            endpoint=endpoint_router,
            path= self._path,
            methods=self._methods,
            name=self._name, 
        )
        
