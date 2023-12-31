import uvicorn
from fastapi import FastAPI

from src.auth.base_config import auth_backend, fastapi_users
from src.auth.schemas import UserRead, UserCreate

from src.operations.router import router as router_operations


app = FastAPI()


app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


app.include_router(router_operations)


if __name__ == "__main__":
    uvicorn.run("main:app", log_level="info", reload=True)
