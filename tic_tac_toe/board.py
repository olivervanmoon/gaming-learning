import numpy as np

class Board:
	def __init__(self, rows=3, cols=3):
		self.rows = rows
		self.cols = cols
		self.grid = np.full((self.rows, self.cols), '', dtype=object)

	def display(self):
		print(self.grid)
		
	def move(self, player, coordinate):
			self.grid[coordinate] = player.symbol #coordinate is (row, col)

	def squareLeft(self):
		for row in self.grid:
			for square in row:
				if square == '':
					return True