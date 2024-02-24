from fastapi.responses import JSONResponse
from services import Service
# from handlers.middlewares import APIMiddleware
from schemas import CreateUser, User
from fastapi import HTTPException
from fastapi import Query, Request
from fastapi import Response
import requests

class UsersHandler:
    def __init__(self, service: Service):
        self.service: Service = service

    async def login(self, tg_id: int) -> User:
        user = self.service.users.get(tg_id)
        return JSONResponse(content={"login": user.login, "password": user.password, "tg_id": user.id, }, status_code= 200)

    async def registration(self, tg_id: int, request: Request,  logPass: str = Query(...)):
        # todo отправить на проверку в api
        # todo записывать в базу данных

        Login, Password = decodeLogPass(logPass)
        url = "https://hackaton.donorsearch.org/api/auth/login/"
        response = send_post_request(url,     {"username": Login,     "password": Password})
        if response.status_code == 400 :
            return Response(status_code=400)

        user = self.service.users.create(tg_id,   Login, Password)

        return JSONResponse(content={"telegram_id": tg_id, "Token": response.headers["Token"]})


def send_post_request(url, body):
    try:
        response = requests.post(url, json=body)
        return response
    except Exception as e:
        print(f"Ошибка при отправке POST-запроса: {e}")
        return None


def decodeLogPass (logPass):
    parts = logPass.split(":")
    if len(parts) == 2:
        return parts[0], parts[1]
    else:
        raise HTTPException(status_code=404, detail="Not valid login or password")