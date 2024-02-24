from fastapi import APIRouter, FastAPI

# from .middlewares import APIMiddleware

from .users import UsersHandler

from services import Service


class Handler:
    def __init__(self, service: Service):
        # APIMiddleware.auth_service = service.auth

        self.users = UsersHandler(service)
 
    def register(self, app: FastAPI) -> list[APIRouter]:
        self.users_router = APIRouter(prefix="/v1", tags=["v1"])

        self.users_router.add_api_route("/login/{tg_id}", endpoint=self.users.login, methods=["GET"])

        self.users_router.add_api_route("/registration/{tg_id}", endpoint=self.users.registration, methods=["POST"])

        app.include_router(self.users_router)