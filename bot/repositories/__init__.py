from .gpt import GPT


class Repository:
	def __init__(self):
		self.gpt: GPT = GPT()
