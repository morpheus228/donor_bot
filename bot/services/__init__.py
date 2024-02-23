from repositories import Repository

class Service:
	def __init__(self, repository: Repository):
		self.repository: Repository = repository

		self.users: Users = Users(self.repository)