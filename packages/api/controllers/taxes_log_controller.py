from fastapi import APIRouter, Depends
from pydantic import BaseModel

from repositories import taxes_log_repository


class CreateTaxesLogDto(BaseModel):
    month: int
    year: int
    amount: float
    transferred_at: str
    user_id: str
    tax_type: str


router = APIRouter()


@router.post("/taxes_log")
async def create_taxes_log(create_taxes_log_dto: CreateTaxesLogDto):
    dto = taxes_log_repository.CreateDbTaxesLogDto(
        month=create_taxes_log_dto.month,
        year=create_taxes_log_dto.year,
        amount=create_taxes_log_dto.amount,
        tax_type=create_taxes_log_dto.tax_type,
        transferred_at=create_taxes_log_dto.transferred_at,
        user_id=create_taxes_log_dto.user_id,
    )

    new_taxes_log_id = taxes_log_repository.create_taxes_log(
        dto
    )

    return {"data": new_taxes_log_id}


@router.get("/taxes_logs")
async def get_taxes_logs():
    taxes_logs = taxes_log_repository.get_all_taxes_logs()
    return {"data": taxes_logs}
