import os
import yaml
from datetime import date
from inventory import Inventory
inv = Inventory()
class Player():
	"""docstring for Player"""

	def get_player_details(self):
		self.player_name = input("Enter your name: ")
		self.player_age = input("Enter your age: ")
		self.player_score = inv.score
		player_data = {"Name":self.player_name,
						"Age":self.player_age,
						"Score":self.player_score}
		if not os.path.exists('./player'):
			os.makedirs('./player')
		filepath = "./player/{}.yml".format(date.today())
		with open(filepath,'w') as player_file:
			yaml.dump(player_data, player_file)

