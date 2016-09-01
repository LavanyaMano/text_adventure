class Room():
	"""docstring for ClassName"""
	def __init__(self, level=1):
		self.level = level

	def maze_size(self):
		mazesize = []
		for i in range(level+1):
			a=["."]*level
			mazesize.append(a)
		print(mazesize.join(" "))

	def random_row(mazesize):
    	return randint(0, len(mazesize) - 1)

	def random_col(mazesize):
    	return randint(0, len(mazesize[0]) - 1)

	maze_row = random_row(mazesize)
	maze_col = random_col(mazesize)
	def monster(self):
		

