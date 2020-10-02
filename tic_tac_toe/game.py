from itertools import cycle
import numpy as np
import traceback

class Game:
	def __init__(self, board, players, n=3):
		self.ply = 0
		#self.winner = False

		self.board = board

		self.n = n
		
		self.players = players
		self.playerCycle = cycle(self.players)
		self.currentPlayer = next(self.playerCycle) # first call to next() gives first in cycle

		self.startMessage()

	def switchPlayer(self):
		self.currentPlayer = next(self.playerCycle)

	def startMessage(self):
		for player in self.players:
			print(player.name, 'is playing as', player.symbol)

	def endMessage(self):
		if self.winner():
			print(self.currentPlayer.name, 'wins after', self.ply, 'turns.') # should make this the winning player using the winner function or maybe change the game status
		else:
			print('The game is a tie after', self.ply, 'turns.')

	def legalMove(self, coordinate):
		if self.board.grid[coordinate] != '':
			raise Exception('Space already taken.')
			#print('Space already taken.')
			#return False
		else:
			return True

	def winner(self):
		
		def nextincol():
			coord[0] += 1

		def nextinrow():
			coord[1] += 1

		def nextindiag():
			coord[0] += 1
			coord[1] += 1

		def nextinanti():
			coord[0] += 1
			coord[1] -= 1

		directions = [nextincol, nextinrow, nextindiag, nextinanti]

		grid = self.board.grid
		for i, row in enumerate(grid):
			for j, _ in enumerate(row): # start from each square (in each row)
				#print('starting from square')
				#print(i,j)
				
				for nextsquare in directions: # try each direction
					c = 0 # for counting number of symbols found 'in a row'
					#print('testing wintype ' + nextsquare.__name__)
					coord = [i,j] # current square to check
					while 0 <= coord[0] < np.size(grid,0) and 0 <= coord[1] < np.size(grid,1): # if valid index
						# no negatives because that wraps around
						# using < since size is one more than final index because of index 0
						#print('now at coordinate')
						#print(coord)
						if grid[tuple(coord)] == self.currentPlayer.symbol:
							c += 1
							#print('count is now ' + str(c))
							#print('because we found a ' + self.currentPlayer.symbol)
							if c == self.n: # if count is target length
								#print('hit target length!!!')
								return True
							nextsquare() # go to next square
						else:
							#print('not the symbol')
							break # break out of while loop goes to check next direction
					#print('going to next win type')
				#print('going to next square in for loop')
		return False

	def getValidMove(self, game):
		while True:
			try:
				print(self.currentPlayer.name + ' (' + self.currentPlayer.symbol + ') move:', end=' ')
				coordinate = self.currentPlayer.getCoordinate(self)
				if self.legalMove(coordinate):
					break
				else:
					continue
			except Exception as err:
				#print('You fucked up.')
				#print(type(err))
				print(err)
				#traceback.print_stack()
				continue
		return coordinate

	def play(self):
		self.board.display()
		while self.board.squareLeft():
			coordinate = self.getValidMove(self)
			self.board.move(self.currentPlayer, coordinate)
			self.ply += 1
			self.board.display()
			if self.winner(): # just checks if current player has won
				break
			self.switchPlayer()
		self.endMessage()