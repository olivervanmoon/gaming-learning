import numpy as np
import random

# base class. every child class must have a getMove(self, game)
class Player:
	def __init__(self, name, symbol):
		self.name = name
		self.symbol = symbol

# human players get input from a keyboard
class HumanPlayer(Player):
	def getCoordinate(self, game):
		#coordinate = HumanPlayer.parseInput(input()) # for inputs with numbers 1-9
		coordinate = tuple(int(x.strip()) for x in input('input: ').split(',')) # strip removes spaces # let me input coordinates in "computer mode"
		return coordinate

	@staticmethod
	def parseInput(position):
		try:
			position = int(position)
		except Exception:
			raise Exception('Invalid input. Enter a whole number form 1 to 9.')
		if position not in [1,2,3,4,5,6,7,8,9]:
			#print("Invalid space. Enter a whole number from 1 to 9.")
			raise Exception("Invalid space. Enter a whole number from 1 to 9.")
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

class RandomPlayer(Player): # will select a random empty space
	def getCoordinate(self, game):
		grid = game.board.grid
		possibilities = []
		for row_ind, row in enumerate(grid):
			for col_ind, square in enumerate(row):
				if square == '':
					possibilities.append((row_ind, col_ind))
		coordinate = random.choice(possibilities)
		print(coordinate)
		return coordinate


