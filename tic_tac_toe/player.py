import traceback 
import numpy as np

# base class. every child class must have a getMove(self, game)
class Player:
	def __init__(self, name, symbol):
		self.name = name
		self.symbol = symbol

	def getValidMove(self, game):
		while True:
			try:
				print(self.name + ' (' + self.symbol + ') move:', end=' ')
				position = self.getPosition(game)
				if position not in [1,2,3,4,5,6,7,8,9]:
					print("Invalid space. Enter a whole number from 1 to 9.")
					continue
				if game.legalMove(position):
					break
				else:
					continue
			except ValueError:
				print('Invalid input. Try again.')
				continue
			except Exception as err:
				print('You fucked up.')
				print(type(err))
				print(err)
				traceback.print_stack()
				continue
		return position

# human players get input from a keyboard
class HumanPlayer(Player):
	def getPosition(self, game):
		position = int(input())#self.name + ' (' + self.symbol + ') move: '))
		return position

#random player will select a random space
class StupidRandomPlayer(Player):
	def getPosition(self,game):
		position = np.random.random_integers(1, 10) #low inclusive, high exclusive
		print(position)
		return position
