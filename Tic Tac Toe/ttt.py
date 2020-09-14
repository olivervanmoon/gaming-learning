# tic tac toe

import numpy as np

def parseInput(position):
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

class Board:
	def __init__(self):
		self.rows = 3
		self.cols = 3
		self.grid = np.empty((self.rows, self.cols), dtype=str)
		
		self.turn = 'x'
		self.ply = 0

	def display(self):
		print(self.grid)

	def legalMove(self, position):
		coordinate = parseInput(position)
		if self.grid[coordinate] != '':
			print('Space already taken.')
			return False
		else:
			return True

	def move(self, player, position):
		coordinate = parseInput(position)
		self.grid[coordinate] = player #coordinate is (row, col)

	def getValidInput(self):
		while True:
			try:
				position = int(input(self.turn + ' move: '))
				if position not in [1,2,3,4,5,6,7,8,9]:
					print("Invalid space. Enter a whole number from 1 to 9.")
					continue
				if self.legalMove(position):
					break
				else:
					continue
			except ValueError:
				print('Whoops. Not a number.')
				continue
			except Exception as e:
				print('You fucked up.')
				print(type(e))
				print(e)
				continue
		return position

	def winner(self):
		for i in range(self.rows):
			if self.grid[i,0] == self.grid[i,1] == self.grid[i,2] != '':
				winner = self.grid[i,0]
				return winner
		for i in range(self.cols):
			if self.grid[0,i] == self.grid[1,i] == self.grid[2,i] != '':
				winner = self.grid[0,i]
				return winner
		if self.grid[0,0] == self.grid[1,1] == self.grid[2,2] != '':
			winner = self.grid[0,0]
			return winner
		if self.grid[0,2] == self.grid[1,1] == self.grid[2,0] != '':
			winner = self.grid[0,2]
			return winner
		else:
			return False

	def squareLeft(self):
		for row in self.grid:
			for square in row:
				if square == '':
					return True
		
	def switchPlayers(self):
		if self.turn == 'x':
			self.turn = 'o'
		elif self.turn == 'o':
			self.turn = 'x'

	def endseq(self):
		if self.winner():
			print(board.winner(), ' wins after ', board.ply, ' turns.')
		else:
			print('The game is a tie after ', self.ply, ' turns.')

class Player:
	def __init__(self, name, id):
		self.name = name
		self.id = id
		pass

	def chooseMove(self, grid):
		position = board.getValidInput()
		return position



board = Board()

player1 = Player('Oliver', 'x')
player2 = Player('Niko', 'o')

players = [player1, player2]

board.display()
while not board.winner() and board.squareLeft():
	position = board.getValidInput()
	board.move(board.turn, position)
	board.display()
	board.switchPlayers()
	board.ply += 1
board.endseq()

	