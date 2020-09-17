import traceback 

class Player:
	def __init__(self, name, symbol):
		self.name = name
		self.symbol = symbol

	def getUserInput(self, board, game):
		while True:
			try:
				position = int(input(self.name + ' (' + self.symbol + ') move: '))
				if position not in [1,2,3,4,5,6,7,8,9]:
					print("Invalid space. Enter a whole number from 1 to 9.")
					continue
				if game.legalMove(board, position):
					break
				else:
					continue
			except ValueError:
				print('Invalid input. Try again.')
				continue
			except Exception as err:
				print('You fucked up.')
				#print(type(err))
				#print(err)
				traceback.print_stack()
				continue
		return position

	def getMove(self, board, game):
		position = self.getUserInput(board, game)
		return position

	