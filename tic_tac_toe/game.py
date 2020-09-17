from itertools import cycle

class Game:
	def __init__(self, board, players):
		self.ply = 0

		self.board = board
		
		self.players = players
		self.playerCycle = cycle(self.players)
		self.currentPlayer = next(self.playerCycle)

		self.startMessage()

	def switchPlayer(self):
		self.currentPlayer = next(self.playerCycle)

	def startMessage(self):
		for player in self.players:
			print(player.name, 'is playing as', player.symbol)

	def endMessage(self):
		if self.winner():
			print(self.currentPlayer.name, 'wins after', self.ply, 'turns.')
		else:
			print('The game is a tie after', self.ply, 'turns.')

	def legalMove(self, position):
		coordinate = self.board.parseInput(position)
		if self.board.grid[coordinate] != '':
			print('Space already taken.')
			return False
		else:
			return True

	def winner(self):
		for i in range(self.board.rows):
			if self.board.grid[i,0] == self.board.grid[i,1] == self.board.grid[i,2] != '':
				winner = self.board.grid[i,0]
				return winner
		for i in range(self.board.cols):
			if self.board.grid[0,i] == self.board.grid[1,i] == self.board.grid[2,i] != '':
				winner = self.board.grid[0,i]
				return winner
		if self.board.grid[0,0] == self.board.grid[1,1] == self.board.grid[2,2] != '':
			winner = self.board.grid[0,0]
			return winner
		if self.board.grid[0,2] == self.board.grid[1,1] == self.board.grid[2,0] != '':
			winner = self.board.grid[0,2]
			return winner
		else:
			return False

	def play(self):
		self.board.display()
		while self.board.squareLeft():
			position = self.currentPlayer.getMove(self)
			self.board.move(self.currentPlayer, position)
			self.ply += 1
			self.board.display()
			if self.winner():
				break
			self.switchPlayer()
		self.endMessage()