"""Maze Craze Game"""
Implementation plan:

1. Create classes for 1. Maze, 2.Player, 3.Inventory, 4. Game Plot.
2. Class Maze : * create maze/rooms as multidimensional array depends on level.
				* Assigining exit and monsters randomly.
				* Displaying the maze 
3. Class Player: * Getting player details(name&age)
				* (storing player log with the achievements.)
4.Inventory: * Item list (keys,weapons,food for lives, lifelines)
			* lifeline calls genie which access random list of puzzles.
5.Actions; * enter
			* exit
			* attack(use weapon)
			* take(add the gift if any)
			* ask (life line)