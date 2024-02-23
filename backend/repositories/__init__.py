from sqlalchemy import Engine

from .mysql import get_mysql

from .users_mysql import UsersMYSQL


class Repository:
	def __init__(self):
		# self.mysql: Engine = get_mysql()
		self.mysql: Engine =  None

		self.users: UsersMYSQL = UsersMYSQL(self.mysql)
