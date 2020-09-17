from itertools import cycle

class Game:
	def __init__(self, players):
		self.ply = 0
		
		self.players = players
		self.playerCycle = cycle(self.players)
		self.currentPlayer = next(self.playerCycle)

		self.startMessage()

	def switchPlayer(self):
		self.currentPlayer = next(self.playerCycle)

	def startMessage(self):
		for player in self.players:
			print(player.name, 'is playing as', player.symbol)

	def endMessage(self, board):
		if self.winner(board):
			print(self.currentPlayer.name, 'wins after', self.ply, 'turns.')
		else:
			print('The game is a tie after', self.ply, 'turns.')

	def legalMove(self, board, position):
		coordinate = board.parseInput(position)
		if board.grid[coordinate] != '':
			print('Space already taken.')
			return False
		else:
			return True

	def winner(self, board):
		for i in range(board.rows):
			if board.grid[i,0] == board.grid[i,1] == board.grid[i,2] != '':
				winner = board.grid[i,0]
				return winner
		for i in range(board.cols):
			if board.grid[0,i] == board.grid[1,i] == board.grid[2,i] != '':
				winner = board.grid[0,i]
				return winner
		if board.grid[0,0] == board.grid[1,1] == board.grid[2,2] != '':
			winner = board.grid[0,0]
			return winner
		if board.grid[0,2] == board.grid[1,1] == board.grid[2,0] != '':
			winner = board.grid[0,2]
			return winner
		else:
			return False