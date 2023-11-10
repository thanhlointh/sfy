"""
App main
"""
import time
import importlib
from inspect import getmembers
from fastapi import FastAPI,Request
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.exceptions.exceptions import DataExceptions
from src.routers import __ROUTER_MODULE__ , __EXCLUDE_ROUTER_NAME__

app = FastAPI(
    debug=False,
    title="Large Project",
    summary="Summary Project",
    version="0.0.1"
)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def handle_request(request: Request, call_next):
    try:
        start_time = time.time()
        response = await call_next(request)
        return response
        return ORJSONResponse(status_code=200,content=response)        
    except DataExceptions as e:
        return ORJSONResponse(status_code=400,content="Not found item")
    except Exception as e:
        return ORJSONResponse(status_code=500,content="Server error, please check again!")

for module_name in __ROUTER_MODULE__:
    module = importlib.import_module(module_name)
    for memattr in getmembers(module):
        if memattr[0].endswith("_router") and memattr[0] not in __EXCLUDE_ROUTER_NAME__:
            app.include_router(memattr[1])


@app.get("/health")
async def health_check():
    """
    Check health
    """
    return True
