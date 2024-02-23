from fastapi.responses import JSONResponse
from services import Service
# from handlers.middlewares import APIMiddleware
from schemas import CreateUser, UserUpdate, User
from fastapi import Query, Request
from fastapi import Response


class UsersHandler:
    def __init__(self, service: Service):
        self.service: Service = service

    async def login(self, tg_id: int) -> User:
        user = self.service.users.get(tg_id)



        #todo проверить наличие в базе данных.
        # tg_id -> login, password, user_id, email
        #если  есть - 200 JSONResponse(content={"login":user.login, "password": user.password, "user_id":user.user_id, "email":user.email}, status_code=200 )
        #если нет - 204  Response(status_code=204)



        print(tg_id)
        return JSONResponse(content=tg_id, status_code=200 )

    async def registration(self, request: Request, telegram_id: str = Query(...), logPass: str = Query(...)):
        # todo отправить на проверку в api


        #todo записывать в базу данных


        return JSONResponse(content={"telegram_id": telegram_id, "logPass": logPass})


