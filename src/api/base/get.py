"""
Generic get endpoint
Class GET:
include:
    - log
    - log database
    -
"""
from typing import List,TypeVar,Type
from pydantic import BaseModel

from sqlmodel import SQLModel,Session,select
from fastapi import APIRouter,Depends
from src.utils.db.session import get_session
from .abstract import Router
from uuid import UUID

SCHEMA = TypeVar("SCHEMA",bound='BaseModel')

DB = TypeVar("DB",bound="SQLModel")

class GET_ONE(Router):
    """
    GET
    """

    def __init__(self, api_router: APIRouter, path: str, methods: List[str], name: str,table) -> None:
        super().__init__(api_router, path, methods, name,table)


    def router(self,obj_schema:Type[SCHEMA]):

        def endpoint_router(uuid: UUID, db: Session = Depends(get_session)):
            @self.wrapper_log
            def create():
                item = db.exec(select(self._table).where(self._table.id==uuid.hex)).first()
                return item
            return create()

        self._api_router.add_api_route(
            endpoint=endpoint_router,
            path= self._path,
            methods=self._methods,
            name=self._name, 
        )
        
