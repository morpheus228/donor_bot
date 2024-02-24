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
        return JSONResponse(content={"login":user.login, "password": user.password, "user_id":user.user_id, "email":user.email}, status_code=200 )

    async def registration(self, tg_id: int, request: Request,  logPass: str = Query(...)):
        # todo отправить на проверку в api
        Login, Password = decodeLogPass(logPass)

        url = "https://hackaton.donorsearch.org/api/auth/login/"
        response = send_post_request(url, {"username": "0ec95cc3-3501-489e-b2ae-8d6b22fc0f9b", "password": Password})

        if response is not None:
            print("Статус код:", response.status_code)
            print("Текст ответа:", response.text)
        else:
            print("Ошибка при выполнении запроса.")

        user = self.service.users.create(tg_id,   Login, Password)


        print({"telegram_id": tg_id, "logPass": logPass})
        #todo записывать в базу данных
        return JSONResponse(content={"telegram_id": tg_id, "logPass": logPass})






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