"""
Abstract router
"""

import time
from typing import List
from fastapi import APIRouter
from functools import partial
from src.schemas.user import UserCreateSchema
class Router():
    def __init__(self,api_router:APIRouter,path:str,methods:List[str],name: str,table:any) -> None:
        self._api_router = api_router
        self._methods = methods
        self._path = path
        self._name = name
        self._table = table

    def wrapper_log(self,func):
        #TODO: write log
        # 
        def wrap(*args,**kwargs):
            start_time = time.time()
            result = func(*args,**kwargs)  
            print(result)
            print(f"Time execute: {time.time()-start_time} s")
            return result
        return wrap
    
    def endpoint_router(self):
        return "Response Empty"

    def router(self):
        self._api_router.add_api_route(
            endpoint=self.endpoint_router,
            path= self._path,
            methods=self._methods,
            name=self._name, 
        )

