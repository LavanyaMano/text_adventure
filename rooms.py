import math
from random import shuffle

class Room():
	"""docstring for ClassName"""
	def __init__(self, level=1):
		self.level = level

	def maze_size(self):
		mazesize = []
		for i in range(self.level):
			a=["o"]*self.level
			mazesize.append(a)
		print("Maze : ",mazesize.join(" "))
		
    def enter(self):
    	return mazesize[0][0]="p"

	def monster(self):
		if (self.level>2):
			monster_numbers = level
		elif(self.level == 2):
			monster_numbers =1
		else:
			monster_numbers=0
		for i in range(monster_numbers+1):
			mazesize[0][i]="m"
		return mazesize

	def display_maze(self):
		print ("Your playing maze is: ")
		shuffle(mazesize)
		for i in mazesize:
        	print (" ".join(i))	


	def move_up(self):
		return mazesize[a-1][b]
	def move_down(self):
		return mazesize[a+1][b]
	def move_left(self):
		return mazesize[a][b-1]
	def move_right(self):
		return mazesize[a][b+1]

	def call_genie(self):
		







