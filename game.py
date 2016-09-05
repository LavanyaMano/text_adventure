import os
import sys
import copy
import yaml 
# from player import get_player_details
from rooms import Room

def play_game():
	print("You can decide the level you want to play. Default level is 0")
	p_level=int(input("Enter the level you want: "))
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
		p_room.display_maze(p_step)
		while True:
			print("Moves :\nr - right\nl - left\nu - up\nd - down\nk - keys\nw -weapons\ng -lifeline\n x - exit")
			p_input = input("> ")
			if p_input == "r":
				p_step=p_room.move_right(p_step)
				p_room.display_maze(p_step)
			elif p_input == "l":
				p_step=p_room.move_left(p_step)
				p_room.display_maze(p_step)
			elif p_input == "u":
				p_step=p_room.move_up(p_step)
				p_room.display_maze(p_step)
			elif p_input == "d":
				p_step=p_room.move_down(p_step)
				p_room.display_maze(p_step)
			elif p_input == "x":
				sys.exit()
			else:
				print("Give correct choice")




def main():

	"""Game description"""
	""" This is multi level maze game. Each level has its 
	own challenges. Find exit at each level and win trophy/credit.
	You have got lives, keys, weapons to handle monsters.
	You have life lines to get genie to help."""
	print("Welcome to the Maze Craze game")
	print("Would you like to play this game: Y/N")
	choice = (input("> ")).lower()


	if choice == "y":
		play_game()
	else:
		print("Exiting the Maze Craze game!")
		sys.exit(0)





if __name__=="__main__":
	main()