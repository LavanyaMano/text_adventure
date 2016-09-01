class Inventory():
	"""docstring for Inventory"""
	def __init__(self, arg, keys=1, weapons=2, food=10):
		self.keys= keys
		self.weapons=weapons
		self.food=food
		self.arg=arg

	def add(self, arg):
		return self.arg+1

	def remove(self, arg):
		return self.arg-1

	def initialize(self):
		return self.keys,self.weapons,self.food
