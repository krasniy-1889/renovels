from dataclasses import dataclass
import random

from fastapi import FastAPI

from src.auth import schemas
from src.auth.services.user import UserService
from src.utils.dependencies import UOWDep
from src.auth.router import auth_router

app = FastAPI(debug=True, title="Renovels")


@app.get("/users", response_model=list[schemas.UserReadDTO])
async def get_users(uow: UOWDep):
    users = await UserService().get_users(uow)
    return users


app.include_router(auth_router)
