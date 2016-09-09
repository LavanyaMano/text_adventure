

class Inventory():
	"""docstring for Inventory"""
	def __init__(self,keys=2,weapons=5,moves=20,life_line=3,score=0):
		self.keys= keys
		self.weapons= weapons
		self.moves = moves
		self.life_line= life_line
		self.score = score

	def add(self, arg):
		if arg == "keys":
			self.keys=self.keys+1
			return self.keys
		elif arg == "weapons":
			self.weapons=self.weapons+1
			return self.weapons
		elif arg == "moves":
			self.moves=self.moves+1
			return self.moves
		elif arg == "life_line":
			self.life_line=self.life_line+1
			return self.life_line
		elif arg == "score":
			self.score=self.score+1
			return self.score

	def remove(self, arg):
		if arg == "keys":
			self.keys=self.keys-1
			return self.keys
		elif arg == "weapons":
			self.weapons=self.weapons-1
			return self.weapons
		elif arg == "moves":
			self.moves=self.moves-1
			return self.moves
		elif arg == "life_line":
			self.life_line=self.life_line-1
			return self.life_line
		elif arg == "score":
			self.score=self.score-1
			return self.score
			
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
		print("Your inventory:")
		return("Key: {}, weapons: {}, moves: {}, life_line: {}.".format(self.keys,self.weapons,self.moves,self.life_line))

my_inventory=Inventory()
