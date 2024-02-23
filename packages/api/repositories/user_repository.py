import uuid
from typing import List

from pydantic import BaseModel

from database import run_query


class CreateDbUserDto(BaseModel):
    email: str
    password: str


class DbUserDto(BaseModel):
    id: str
    email: str
    created_at: str
    updated_at: str


def create_user(create_db_user_dto: CreateDbUserDto) -> str:
    user_id = uuid.uuid4()
    query = "INSERT INTO users (id, email, password) VALUES (%s, %s, %s) RETURNING id;"
    result = run_query(query, [str(user_id), create_db_user_dto.email, create_db_user_dto.password])
    return result[0][0]


def get_all_users() -> List[DbUserDto]:
    query = "SELECT id, email, created_at, updated_at FROM users"
    results = run_query(
        query
    )

    users = []

    for item in results:
        db_user_dto = DbUserDto(
            id=item["id"],
            email=item["email"],
            created_at=str(item["created_at"]),
            updated_at=str(item["updated_at"])
        )

        users.append(db_user_dto)

    return users
