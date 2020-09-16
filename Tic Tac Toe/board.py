import numpy as np

class Board:
	def __init__(self):
		self.rows = 3
		self.cols = 3
		self.grid = np.empty((self.rows, self.cols), dtype=str)

	def display(self):
		print(self.grid)

	def move(self, playerid, position):
			coordinate = self.parseInput(position)
			self.grid[coordinate] = playerid #coordinate is (row, col)

	def parseInput(self, position):
		if position == 1:
			return (0,0)
		if position == 2:
			return (0,1)
		if position == 3:
			return (0,2)
		if position == 4:
			return (1,0)
		if position == 5:
			return (1,1)
		if position == 6:
			return (1,2)
		if position == 7:
			return (2,0)
		if position == 8:
			return (2,1)
		if position == 9:
			return (2,2)
		else:
			return False

	def squareLeft(self):
		for row in self.grid:
			for square in row:
				if square == '':
					return True