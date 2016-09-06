import os
import sys
import copy
import yaml
from player import Player
from rooms import Room
from inventory import Inventory
inv1=Inventory()
def play_game(p_level):
	p_room = Room(p_level)

	print("You are about to play in maze craze level - {}".format(p_level))
	maze_disp = p_room.maze_size()
	for i in maze_disp:
		print("\t".join(i))
	print ("Press e for entering the maze")
	print ("Press i for checking the inventory")
	print("Press x for exiting the game")
	user = input(" >  ")

	if user == "e":
		p_step= p_room.maze_setup()
		print("Result maze")
		p_room.result_maze(p_step)
		print("*"*50)
		p_room.display_maze(p_step)
		print("Result maze")
		p_room.result_maze(p_step)
		print("*"*50)
		while True:
			print("Moves :r - right\tl - left\tu - up\t\td - down\nk - keys\tw -weapons\tg -lifeline\n x - exit")
			p_input = input("> ")
			if p_input == "r" or p_input == "l" or p_input == "u" or p_input == "d":
				p_stage=p_room.move(p_step,p_input)
				p_room.display_maze(p_stage[0])
				if p_stage[1]:
					print("Level up.")
					play_game(p_level+1)
				else:
					p_room.display_maze(p_step)
			elif p_input == "x":
				sys.exit(0)
			elif p_input == "i":
				print(inv1)
			else:
				print("Give correct choice")
	elif user == "i":
		print(inv1)
	elif user == "x":
		print("Exiting the game.")
		sys.exit()
	else:
		print("Please enter the right choice.")


def main():

	"""Game description"""
	""" This is multi level maze game. Each level has its 
	own challenges. Find exit at each level and win trophy/credit.
	You have got lives, keys, weapons to handle monsters.
	You have life lines to get genie to help."""
	print("Welcome to the Maze Craze game")
	player1 = Player()
	player1.get_player_details()

	print("Would you like to play this game: Y/N")
	choice = (input("> ")).lower()

	if choice == "y":
		print("You can decide the level you want to play. Default level is 1")
		p_level=int(input("Enter the level you want: "))
		play_game(p_level)
	else:
		print("Exiting the Maze Craze game!")
		sys.exit(0)





if __name__=="__main__":
	main()