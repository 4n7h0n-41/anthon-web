import uuid
from typing import List
from datetime import datetime

from pydantic import BaseModel

from database import run_query

class CreateDbTaxesLogDto(BaseModel):
    month: int
    year: int
    amount: float
    transferred_at: str
    user_id: str
    tax_type: str


class DbTaxesLogDto(BaseModel):
    id: str
    month: int
    year: int
    amount: float
    transferred_at: str
    created_at: str
    user_id: str
    tax_type: str


def create_taxes_log(create_db_taxes_log_dto: CreateDbTaxesLogDto) -> str:
    taxes_log_id = uuid.uuid4()
    query = """
        INSERT INTO 
            taxes_log (id, month, year, amount, transferred_at, tax_type, user_id) 
        VALUES 
            (%s, %s, %s, %s, %s, %s, %s) 
        RETURNING id;
    """

    result = run_query(query, [
        str(taxes_log_id),
        create_db_taxes_log_dto.month,
        create_db_taxes_log_dto.year,
        create_db_taxes_log_dto.amount,
        datetime.strptime(create_db_taxes_log_dto.transferred_at, '%d-%m-%Y'),
        create_db_taxes_log_dto.tax_type,
        create_db_taxes_log_dto.user_id,
    ])

    return result[0][0]


def get_all_taxes_logs() -> List[DbTaxesLogDto]:
    query = """
        SELECT 
            id, month, year, amount, created_at, transferred_at, tax_type, user_id 
        FROM taxes_log
    """
    results = run_query(
        query
    )

    taxes_logs = []

    for item in results:
        db_taxes_log = DbTaxesLogDto(
            id=item["id"],
            month=item["month"],
            year=item["year"],
            amount=item["amount"],
            tax_type=item["tax_type"],
            transferred_at=str(item["transferred_at"]),
            created_at=str(item["created_at"]),
            user_id=item["user_id"]
        )

        taxes_logs.append(db_taxes_log)

    return taxes_logs
