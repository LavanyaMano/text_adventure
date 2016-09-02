class Inventory():
	"""docstring for Inventory"""
	def __init__(self, arg, keys=2, weapons=2, food=10, life_line=3):
		self.keys= keys
		self.weapons=weapons
		self.food=food
		self.arg=arg
		self.life_line=life_line

	def add(self, arg):
		return self.arg+1

	def remove(self, arg):
		return self.arg-1

	def __str__(self):
		print("Your inventory \n")
		print("Key: {} weapons: {} food: {} life_line: {}".format(self.keys,self.weapons,self.food,self.life_line))
