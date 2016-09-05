
class Inventory():
	"""docstring for Inventory"""
	def __init__(self, keys=2, weapons=2, moves=10, life_line=3):
		self.keys= keys
		self.weapons=weapons
		self.moves =moves
		self.life_line=life_line

	def add(self, arg):
		if arg == "keys":
			return self.keys+1
		elif arg == "weapons":
			return self.weapons+1
		elif arg == "moves":
			return self.moves+1
		elif arg == "life_line":
			return self.life_line+1

	def remove(self, arg):
		if arg == "keys":
			return self.keys-1
		elif arg == "weapons":
			return self.weapons-1
		elif arg == "moves":
			return self.moves-1
		elif arg == "life_line":
			return self.life_line-1
			
	def check(self,arg):
		if arg == "keys":
			return self.keys>0
		elif arg == "weapons":
			return self.weapons>0
		elif arg == "moves":
			return self.moves>0
		elif arg == "life_line":
			return self.life_line>0

	def __str__(self):
		print("Your inventory \n")
		print("Key: {} weapons: {} moves: {} life_line: {}".format(self.keys,self.weapons,self.moves,self.life_line))

# inv1 = Inventory()
# var = inv1.add("weapons")
# print(var)

