from fastapi import FastAPI
from api.routes import (
    eats
)


api = FastAPI(
    title="Eats API",
    description=""
)

routers = [
    eats.router
]

for router in routers:
    api.include_router(router=router)

