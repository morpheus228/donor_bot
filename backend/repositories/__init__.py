from sqlalchemy import Engine
from typing import Dict
from .mysql import get_mysql

from .users_mysql import UsersMYSQL
from schemas import User

class Repository:
	def __init__(self):
		#self.mysql: Engine = get_mysql()
		self.mysql: Engine =  None
		self.map: Dict[str, User]
		self.users: UsersMYSQL = UsersMYSQL(self.mysql)
