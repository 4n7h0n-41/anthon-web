from fastapi import APIRouter, Depends
from pydantic import BaseModel

from repositories import salary_repository


class CreateSalaryDto(BaseModel):
    month: int
    year: int
    currency: str
    rate: float
    amount: float
    employer: str
    transferred_at: str
    user_id: str


router = APIRouter()


@router.post("/salary")
async def create_salary(create_salary_dto: CreateSalaryDto):
    dto = salary_repository.CreateDbSalaryDto(
        month=create_salary_dto.month,
        year=create_salary_dto.year,
        currency=create_salary_dto.currency,
        rate=create_salary_dto.rate,
        amount=create_salary_dto.amount,
        employer=create_salary_dto.employer,
        transferred_at=create_salary_dto.transferred_at,
        user_id=create_salary_dto.user_id,
    )

    new_salary_id = salary_repository.create_salary(
        dto
    )

    return {"data": new_salary_id}


@router.get("/salaries")
async def get_salaries():
    salaries = salary_repository.get_all_salaries()
    return {"data": salaries}
