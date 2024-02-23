from fastapi import APIRouter, Depends
from pydantic import BaseModel

from repositories import user_repository


class CreateUserDto(BaseModel):
    email: str
    password: str


router = APIRouter()


@router.post("/user")
async def create_user(create_user_dto: CreateUserDto):
    dto = user_repository.CreateDbUserDto(
        email=create_user_dto.email,
        password=create_user_dto.password
    )

    new_user_id = user_repository.create_user(
        dto
    )

    return {"data": new_user_id}


@router.get("/users")
async def get_users():
    users = user_repository.get_all_users()
    return {"data": users}
