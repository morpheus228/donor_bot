from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import Engine

from repositories import Repository
from repositories.mysql import User
from schemas.user import  User


class Users:
    def __init__(self, repository: Repository):
        self.repository: Repository = repository

    def get(self, tg_id: int) -> User:
        mysql_user = self.repository.users.get_by_id(tg_id)

        if mysql_user is None:
            raise HTTPException(status_code=404, detail="The user with the specified ID was not found")

        return User(
            login = mysql_user["login"],
            password =mysql_user["password"] ,
            # user_id = mysql_user["id"],
            # email = mysql_user["email"],
            username =  mysql_user["username"] if mysql_user.get("username") else None,
            id = mysql_user["tg_id"]
        )

    def create(self, tg_id: int, login: str, password: str) -> int:
        mysql_user = self.repository.users.get_by_id(tg_id)
        if mysql_user is None:
            self.repository.users.create(tg_id, login, password)


        return 200