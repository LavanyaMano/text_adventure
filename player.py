import os
import yaml
from datetime import datetime
import sys



class Player():
	"""docstring for Player"""
	def __init__(self):
		self.player_name=""
		self.player_age=""
		self.player_score = 0
		self.play_level = 0
		self.play_date = datetime.now()


	def get_player_details(self):
		self.player_name = input("Enter your name: ")
		self.player_age = input("Enter your age: ")


	def player_log(self):
		if not os.path.exists('./player'):
			os.makedirs('./player')

		filepath = "./player/{}.yml".format(self.player_name)
		if not os.path.exists(filepath):
			player_data = {"Name":self.player_name,
						"Age":self.player_age,
						"Date":self.play_date,
						"Level Completed":self.play_level,
						"Score":self.player_score}
			existing_data = player_data
			
		else:
			existing_data = {"\n"
							"Date":self.play_date,
							"Level Completed":self.play_level,
							"Score": self.player_score}
			# with open(filepath,'w+') as player_file:
			# 	existing_data =yaml.load(player_file)
			# existing_data.append(player_data)

		with open(filepath,'a') as player_file:
			yaml.dump(existing_data, player_file,default_flow_style=False)
