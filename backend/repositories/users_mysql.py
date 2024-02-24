from sqlalchemy.orm import Session
from sqlalchemy import Engine

from .mysql import User as MysqlUser
from schemas import CreateUser 


class UsersMYSQL:
    def __init__(self, mysql: Engine):
        self.mysql: Engine = mysql

    def create(self, tg_id: str, login: str, password: str) -> None:
        with Session(self.mysql) as session:
            user = MysqlUser(id = tg_id, login = login, password = password)
            session.add(user)
            session.commit()

    def get_by_id(self, tg_id: int) -> MysqlUser|None:
        with Session(self.mysql) as session:
            return session.query(MysqlUser).get(tg_id)
        
    def get_all(self) -> list[CreateUser|None]:
        with Session(self.mysql) as session:
            return session.query(MysqlUser).all()
        
    def update(self, user_id: int, **kwargs):
        with Session(self.mysql) as session:
            session.query(MysqlUser).filter_by(id=user_id).update(kwargs)
            session.commit()