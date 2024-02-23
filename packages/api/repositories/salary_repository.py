import uuid
from typing import List
from datetime import datetime

from pydantic import BaseModel

from database import run_query


class CreateDbSalaryDto(BaseModel):
    month: int
    year: int
    currency: str
    rate: float
    amount: float
    employer: str
    transferred_at: str
    user_id: str


class DbSalaryDto(BaseModel):
    id: str
    month: int
    year: int
    currency: str
    rate: float
    amount: float
    employer: str
    transferred_at: str
    user_id: str
    created_at: str


def create_salary(create_db_salary_dto: CreateDbSalaryDto) -> str:
    salary_id = uuid.uuid4()
    query = """
        INSERT INTO 
            salaries_log (id, month, year, currency, rate, amount, employer, transferred_at, user_id) 
        VALUES 
            (%s, %s, %s, %s, %s, %s, %s, %s, %s) 
        RETURNING id;
    """

    result = run_query(query, [
        str(salary_id),
        create_db_salary_dto.month,
        create_db_salary_dto.year,
        create_db_salary_dto.currency,
        create_db_salary_dto.rate,
        create_db_salary_dto.amount,
        create_db_salary_dto.employer,
        datetime.strptime(create_db_salary_dto.transferred_at,  '%d-%m-%Y'),
        create_db_salary_dto.user_id
    ])

    return result[0][0]


def get_all_salaries() -> List[DbSalaryDto]:
    query = """
        SELECT 
            id, month, year, currency, rate, amount, employer, created_at, transferred_at, user_id 
        FROM salaries_log
    """
    results = run_query(
        query
    )

    salaries = []

    for item in results:
        db_salary_dto = DbSalaryDto(
            id=item["id"],
            month=item["month"],
            year=item["year"],
            currency=item["currency"],
            rate=item["rate"],
            amount=item["amount"],
            employer=item["employer"],
            transferred_at=str(item["transferred_at"]),
            created_at=str(item["created_at"]),
            user_id=item["user_id"]
        )

        salaries.append(db_salary_dto)

    return salaries
