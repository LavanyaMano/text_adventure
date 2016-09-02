import os
import sys
import copy
import yaml 
from player import get_player_details
from rooms import maze_size






def main():

	"""Game description"""
	""" This is multi level maze game. Each level has its 
	own challenges. Find exit at each level and win trophy/credit.
	You have got lives, keys, weapons to handle monsters.
	You have life lines to get genie to help."""
	print("Welcome to the Maze Craze game")
	print("Would you like to play this game: Y/N")
	choice = lower(input("> "))

	try:
		if choice == "Y":
			play = Game()
		else:
		print("Exiting the Maze Craze game!")
		sys.exit(0)

	except FileNotFoundError:
		print("WARNING: Could not find premade file, no premade pizzas")

class Game(object):
	"""docstring for Game"""
	print("You can decide the level you want to play. Default level is 0")
	p_level=input("Enter the level you want: ")
	if p_level.isdigit():
		p_room = Room(p_level)
	else:
		print("Taking you to level 1")
		p_room = Room()
		

	if (choice=="Y"):
		print("Entering the Maze....")

		#####Initializing an instance of class Inventory
		####This will initialize the keys, weapons and the 
		#####Food values
		inv1 = Inventory(10)

		#####Calling the initialize value function
		keys, weapons, food = inv1.initialize()
		print('You have ->'+str(keys)+' keys,'+str(weapons)+' weapons and '+str(food)+' meals')
		
		#####Creating the instance of the Room class
		room1 = Room(number="1")


		monster_value = room1.check_in()
	#	food = inv1.remove(food)
		if (monster_value == "monster"):
			weapons = inv1.remove(weapons)
		
		print('Now you have ->'+str(keys)+' keys,'+str(weapons)+' weapons and '+str(food)+' meals')


if __name__=="__main__":
	main()