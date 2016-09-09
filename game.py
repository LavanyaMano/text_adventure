import os
import sys
import copy
import yaml
import curses
from player import Player
from rooms import Room
from inventory import my_inventory

player1 = Player()

def play_game(p_level):
	p_room = Room(p_level)
	print("You are about to play in maze craze level - {}".format(p_level))
	maze_disp = p_room.maze_size()
	for i in maze_disp:
		print("\t".join(i))
	print ("Press e for entering the maze")
	print ("Press i for checking the inventory")
	print("Press x for exiting the game")
	
	while my_inventory.moves>0:
		user = input(" >  ")
		if user == "e":
			p_step= p_room.maze_setup()
			p_room.display_maze(p_step)
			print("`"*50)
			while True:
				print("\033[3;32;40m Your score is {} \033[m".format(my_inventory.score))
				print("."*80)
				print("Moves :r - right\tl - left\tu - up\td - down \t x - exit")
				print("."*80)
				p_input = input("> ")
				if p_input == "r" or p_input == "l" or p_input == "u" or p_input == "d":
					p_step,p_stage=p_room.move(p_step,p_input)
					if p_stage:
						os.system("clear")
						print("\033[3;30;43m Level up.\033[m")
						player1.play_level = p_level
						player1.player_score = my_inventory.score
						player1.player_log()
						p_level=p_level+1
						play_game(p_level)
					else:
						p_room.display_maze(p_step)
				elif p_input == "x":
					sys.exit(0)
				elif p_input == "i":
					print(my_inventory)
				else:
					print("Give correct choice")
		elif user == "i":
			print(my_inventory)
		elif user == "x":
			print("Exiting the game.")
			sys.exit()
		else:
			print("\033[3;32;46m Please enter the right choice.\033[m")

	os.system("clear")
	print("\033[3;32;47m Sorry you dont have moves.\033[m")
	sys.exit()


def main():

	"""Game description"""
	""" This is multi level maze game. Each level has its 
	own challenges. Find exit at each level and win trophy/credit.
	You have got lives, keys, weapons to handle monsters.
	You have life lines to get genie to help."""
	print("Welcome to the Maze Craze game")
	print("\033[3;32;40m Maze-Craze Game \033[m\n")

	player1.get_player_details()
	player1.player_log()
	print("Would you like to play this game: Y/N")
	choice = (input("> ")).lower()

	if choice == "y":
		print("You can decide the level you want to play.(Any number above 0)")
		p_level=int(input("Enter the level you want: "))
		play_game(p_level)
	else:
		print("Exiting the Maze Craze game!")
		sys.exit(0)





if __name__=="__main__":
	main()