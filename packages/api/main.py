from fastapi import FastAPI

from controllers import user_controller, salary_controller, taxes_log_controller

app = FastAPI()

app.include_router(user_controller.router)
app.include_router(salary_controller.router)
app.include_router(taxes_log_controller.router)
