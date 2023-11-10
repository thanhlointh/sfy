import os

PARENT_DIR = (
    os.path.dirname(os.path.realpath(__file__)).replace(os.getcwd() + "/", "").replace("/", ".")
)
# Add the router module name to import
MODULE_NAMES = [
    "pricing",
]

__EXCLUDE_ROUTER_NAME__ = ["create_crud_router"]

__ROUTER_MODULE__ = [f"{PARENT_DIR}.{r}" for r in MODULE_NAMES]
