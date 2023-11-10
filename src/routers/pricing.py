"""
Router pricing
"""

from fastapi import APIRouter
from fastapi.routing import APIRoute
from src.api.base.crud import CRUD
from src.models.users import UsersDB
from src.schemas.user import UserCreateSchema,UserReadSchema,UserUpdateSchema,UserDeleteSchema

pricing_router = APIRouter(prefix="/pricing", tags=["Pricing product"])

######################
# GET POST LIST DELETE
######################d
CRUD(
    api_router=pricing_router,
    table=UsersDB,
    create=UserCreateSchema,
    read=UserReadSchema,
    update=UserUpdateSchema,
    delete=UserDeleteSchema,
).generate_crud()

# async def example_endpoint():
#     return {"message": "This is an example"}

# pricing_router.add_api_route(
#             endpoint=example_endpoint,
#             path="/path",
#             methods=["GET"],
#             name="Get list",
#         )
