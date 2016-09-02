from datetime import datetime

class Player():
	"""docstring for Player"""
	def __init__(self, player):
		self.player = []
		self.player.trophy = ""

	def get_player_details():
		self.player.name = input("Enter your name: ")
		self.player.age = input("Enter your age: ")

	filepath = "./player/{}.yml".format(datetime.now())
	with open(filepath,'w') as order_file:
		yaml.dump(player, player_file)




	


